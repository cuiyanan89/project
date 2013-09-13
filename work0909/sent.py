#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import time
import MySQLdb
import smtplib
import os.path
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def check():
    date_now = time.strftime("%Y%m%d",time.localtime())
    letter_list = []
    try:
        conn = MySQLdb.connect(host="localhost",user="root",passwd="rongrong",db="future",charset="utf8")
        cursor = conn.cursor()
        cursor.execute("select id,deliverdate from future_letter where maturity = 0")
        letter_list = cursor.fetchall()
    except:
        pass
    finally:
        cursor.close()
        conn.close()
    date_now = '20130917'
    send_list = []
    for letter in letter_list:
        if letter[1].strftime("%Y%m%d") == date_now:
            send_list.append(letter[0])
    return send_list

def message(letter):
    sender = letter[0]
    receiver = letter[1]
    subject = letter[2]
    text = letter[3]
    picture = letter[4]
    currentdate = letter[5]

    msg = MIMEText(text,_subtype="plain",_charset='gb2312')
    image = MIMEImage(open())
    msg['Subject'] = Header(subject)
    smtp = smtplib.SMTP("smtp.qq.com")
    smtp.ehlo()
    conn_off = True
    while conn_off:
        try:
            smtp.close()
            smtp.connect('smtp.qq.com')
            smtp.helo()
            conn_off = False
        except:
            smtp.close()
    smtp.login('332761705@qq.com','cuiyanan891227')
    receiver = 'cuiyanan@outlook.com'
    try:
        smtp.sendmail('332761705@qq.com',receiver,msg.as_string())
        return True
    except:
        return False

def send(send_list):
    letters = []
    conn = MySQLdb.connect(host="localhost",user="root",passwd="rongrong",db="future",charset="utf8")
    cursor = conn.cursor()
    for id in send_list:
        cursor.execute("select future_user.email,future_letter.email,future_letter.subject,future_letter.text,future_letter.picture,future_letter.currentdate from future_user,future_letter where future_user.id=future_letter.user_id and future_letter.id=%d"%id)
        letters.append(cursor.fetchone())
#        cursor.execute("update future_letter set maturity = 1 where id=%d"%id)
#        conn.commit()
    cursor.close()
    conn.close()
    return letters


def main():
    send_list = check()
    print send_list
    if len(send_list) != 0:
        letters = send(send_list)
        for i in range(len(letters)):
            print message(letters[i])

if __name__=="__main__":
    main()
