import smtplib


email_addr = 'mining.portsz@gmail.com'
email_passw = 'ehfdmlrsadqhdkjk'



def send_email(pair, candle_open, candle_close, volume, last_candle_open, last_candle_close, last_volume):
    print("pair -> " + pair + "<- Email sent!\n")
    # with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    #     smtp.ehlo()
    #     smtp.starttls()
    #     smtp.ehlo()

    #     smtp.login(email_addr, email_passw)

    #     volume_change = 0
        
    #     # if volume != 0 and last_volume != 0:
    #     #     volume_change = (float(volume)-float(last_volume))/float(last_volume)
    #     #     volume_change = 100*volume_change
        
    #     subject = f"Volume Spike Alert {pair}"
    #     body = (f'''
        
    #     Volume spike alert on {pair} \n\n 
    #     Open Last: {last_candle_open}\tOpen: {candle_open}\n
    #     Close Last: {last_candle_close}\tClose: {candle_close}\n
    #     Volume Last: {last_volume}\tVolume: {volume}\n

    #     \nThis candle had an increase in volume by {volume_change}%
        
    #     ''')
    #     msg = f'Subject: {subject} \n\n {body}'

    #     # smtp.sendmail(email_addr, 'jp.portsz@gmail.com', msg)
    #     print("pair -> " + pair + "<- Email sent!\n")