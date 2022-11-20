import schedule
import subprocess
import sys
import time
import signal
import os
import smtplib
import email
from email.mime.image import MIMEImage
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



pid = os.fork()

def job():
    subprocess.Popen([sys.executable, 'RunForAllPairs.py'])

def takeScreenshot():
    
    os.system("""
    powershell.exe \"
        Add-Type -AssemblyName System.Windows.Forms
        [Windows.Forms.Sendkeys]::SendWait('+{Prtsc}')
        \$img = [Windows.Forms.Clipboard]::GetImage()
        \$img.Save(\\\"/home/portsz/Projects/volumeTradeBot/screenshots/screenshot.jpg\\\", [Drawing.Imaging.ImageFormat]::Jpeg)\" """)
    print("Screenshot Taken\n")

    email_addr = 'mining.portsz@gmail.com'
    email_passw = 'ehfdmlrsadqhdkjk'

    msg=MIMEMultipart()
    msg['From']='mining.portsz@gmail.com'
    msg['To']='jp.portsz@gmail.com'
    msg['Subject']='Volume Spike Alert Bot'

    file_location = "./screenshots/screenshot.jpg"

    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb").read()
    image = MIMEImage(attachment,'jpg', name=filename)
    msg.attach(image)


    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(email_addr, email_passw)

        
        

        smtp.sendmail(email_addr, 'jp.portsz@gmail.com', msg.as_string())
        smtp.sendmail(email_addr, 'marcosfaeh@hotmail.com', msg.as_string())
        print("-> Email sent!\n")

def sendEmail():

    email_addr = 'mining.portsz@gmail.com'
    email_passw = 'ehfdmlrsadqhdkjk'

    msg=MIMEMultipart()
    msg['From']='mining.portsz@gmail.com'
    msg['To']='jp.portsz@gmail.com'
    msg['Subject']='Volume Spike Alert Bot'

    file_location = "./screenshots/screenshot.jpg"

    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb").read()
    image = MIMEImage(attachment,'jpg', name=filename)
    msg.attach(image)


    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(email_addr, email_passw)

        
        

        smtp.sendmail(email_addr, 'jp.portsz@gmail.com', msg.as_string())
        smtp.sendmail(email_addr, 'marcosfaeh@hotmail.com', msg.as_string())
        print("-> Email sent!\n")

def close():
    os.kill(pid, signal.SIGINT)

schedule.every().day.at("20:57").do(job)
schedule.every().day.at("21:02").do(takeScreenshot)
schedule.every().day.at("21:03").do(sendEmail)
schedule.every().day.at("21:04").do(close)


while 1:
    schedule.run_pending()
    time.sleep(1)        