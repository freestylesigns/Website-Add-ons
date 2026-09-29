#!/usr/bin/env python3
import json, os, smtplib
from email.message import EmailMessage
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

ROOT=Path(__file__).resolve().parent
OUTBOX=ROOT/"outbox"
MAX_BODY=10*1024*1024
TO_EMAIL=os.environ.get("SMTP_TO","sales@freestyle-signs.co.uk")
FROM_EMAIL=os.environ.get("SMTP_FROM",TO_EMAIL)
ALLOWED_ORIGIN=os.environ.get("ALLOWED_ORIGIN","http://localhost:8000")

class Handler(SimpleHTTPRequestHandler):
    def _cors(self):
        origin=self.headers.get("Origin","")
        if origin and origin in {x.strip() for x in ALLOWED_ORIGIN.split(",") if x.strip()}:
            self.send_header("Access-Control-Allow-Origin",origin)
            self.send_header("Vary","Origin")
            return True
        return not origin
    def end_headers(self):
        self._cors()
        super().end_headers()
    def do_OPTIONS(self):
        if urlparse(self.path).path!="/api/inquiry":
            self.send_error(404);return
        if not self._cors():
            self.send_error(403);return
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin",self.headers.get("Origin",""))
        self.send_header("Access-Control-Allow-Methods","POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers","Content-Type")
        self.end_headers()
    def do_POST(self):
        if urlparse(self.path).path!="/api/inquiry":
            self.send_error(404);return
        if not self._cors():
            self.send_error(403);return
        try:
            length=int(self.headers.get("Content-Length","0"))
            if length<=0 or length>MAX_BODY: raise ValueError("Submission too large")
            p=json.loads(self.rfile.read(length).decode("utf-8"))
            name=str(p.get("name","")).strip(); company=str(p.get("company","")).strip()
            email=str(p.get("email","")).strip(); phone=str(p.get("phone","")).strip()
            message=str(p.get("message","")).strip(); summary=str(p.get("design_summary","")).strip()
            svg=str(p.get("design_svg","")).strip()
            if not name or not email or not svg.startswith("<svg"): raise ValueError("Missing required enquiry or design data")
            if len(svg.encode("utf-8"))>8*1024*1024: raise ValueError("Artwork is too large")
            body="New Marker Plates website enquiry\n\nName: %s\nCompany: %s\nEmail: %s\nTelephone: %s\n\nMessage:\n%s\n\n%s\n"%(name,company,email,phone,message,summary)
            msg=EmailMessage()
            msg["Subject"]="Website enquiry — Marker Plates"
            msg["From"]=FROM_EMAIL; msg["To"]=TO_EMAIL; msg["Reply-To"]=email
            msg.set_content(body)
            msg.add_attachment(svg.encode("utf-8"),maintype="image",subtype="svg+xml",filename="marker-plate-design.svg")
            send_or_queue(msg,p)
            self.send_response(200); self.send_header("Content-Type","application/json"); self.end_headers(); self.wfile.write(b'{"ok":true}')
        except Exception as exc:
            self.send_response(400); self.send_header("Content-Type","application/json"); self.end_headers()
            self.wfile.write(json.dumps({"ok":False,"error":str(exc)}).encode("utf-8"))

def send_or_queue(msg,p):
    host=os.environ.get("SMTP_HOST")
    if not host:
        OUTBOX.mkdir(exist_ok=True)
        import datetime
        stamp=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        (OUTBOX/f"{stamp}-inquiry.json").write_text(json.dumps({k:v for k,v in p.items() if k!="design_svg"},ensure_ascii=False),encoding="utf-8")
        (OUTBOX/f"{stamp}-design.svg").write_text(p["design_svg"],encoding="utf-8")
        return
    port=int(os.environ.get("SMTP_PORT","587")); user=os.environ.get("SMTP_USER"); password=os.environ.get("SMTP_PASSWORD")
    secure=os.environ.get("SMTP_SECURE","false").lower()=="true"; starttls=os.environ.get("SMTP_STARTTLS","true").lower()=="true"
    smtp=smtplib.SMTP_SSL(host,port,timeout=30) if secure else smtplib.SMTP(host,port,timeout=30)
    try:
        smtp.ehlo()
        if not secure and starttls: smtp.starttls(); smtp.ehlo()
        if user and password: smtp.login(user,password)
        smtp.send_message(msg)
    finally: smtp.quit()

if __name__=="__main__":
    os.chdir(ROOT)
    ThreadingHTTPServer(("0.0.0.0",int(os.environ.get("PORT","8000"))),Handler).serve_forever()
