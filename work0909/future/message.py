#!/usr/bin/env python
#_*_coding: utf-8 _*_
import time
import threading
import MySQLdb
import smtplib
import os.path
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def singleton(cls,*args,**kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args,**kw)
        return instances[cls]
    return _singleton

class CheckAndSend(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            date_now = time.strftime("%Y%m%d",time.localtime())
            letter_list = []
            try:
                conn = MySQLdb.connect(host="localhost",user="root",passwd="rongrong",db="future",charset="utf8")
                cursor = conn.cursor()
                cursor.execute("select id,deliverdate from future_letter where maturity = 0")
                letter_list = cursor.fetchall()
            except:
                pass
#            date_now = '20130917'
            send_list = []
            for letter in letter_list:
                if letter[1].strftime('%Y%m%d') == date_now:
                    send_list.append(letter[0])
            print send_list
#            x = raw_input()
            if len(send_list) != 0:
                for id in send_list:
                    cursor.execute("select future_user.email,future_letter.email,future_letter.subject,future_letter.text,future_letter.picture,future_letter.currentdate from future_user,future_letter where future_user.id=future_letter.user_id and future_letter.id=%d"%id)
                letter = cursor.fetchone()
                sender = letter[0]
                receiver = letter[1]
                subject = letter[2]
                text = letter[3]
                picture = letter[4]
                currentdate = letter[5]
                msg = MIMEText(sender+' wrote to you at:'+currentdate.strftime('%Y/%m/%d')+'\n'+text+'\nsend by tofuture me...',_subtype="plain",_charset="gb2312")
                msg['Subject'] = Header(subject)
#                if picture != '':
#                    path_img = os.path.join(os.path.abspath(os.path.curdir)+'/static/upload/image/',picture)
#                    image = MIMEImage(open(path_img,'rb').read())
#                    image.add_header('Content-ID','<image1>')
#                    msg.attach(image)
#                if picture != '':
#                    path_img = os.path.join(os.path.abspath(os.path.curdir)+'/static/upload/image/',picture)
#                    image = MIMEImage(open(path_img,'rb').read())
#                    image.add_header('Content-Disposition','attachment',filename=picture)
#                    msg.attach(image)
                    
                smtp = smtplib.SMTP("smtp.gmail.com",587)
                conn_off = True
                send_ok = False
                while conn_off:
                    try:
                       # smtp.close()
                        print smtp.ehlo()
                        print smtp.starttls()
                        #print smtp.connect('smtp.qq.com')
                        #print smtp.helo()
                        conn_off = False
                    except:
                    #    time.sleep(10)
                        smtp.close()
                #print smtp.login('332761705@qq.com','cuiyanan891227')
                print smtp.login('hi.cuiyanan@gmail.com','cuiyanan15122175532')
                try:
                    receiver = 'cuiyanan@outlook.com'
                    #print smtp.sendmail('332761705@qq.com',receiver,msg.as_string())
                    print smtp.sendmail('hi.cuiyanan@gmail.com',receiver,msg.as_string())

                    send_ok = True
                except:
                    send_ok = False

                if send_ok:
                    cursor.execute("update future_letter set maturity = 1 where id=%d"%id)
                    conn.commit()
            cursor.close()
            conn.close()
            time.sleep(900)
#            time.sleep(86000)
