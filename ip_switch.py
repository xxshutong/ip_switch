import smtplib

from email.mime.text import MIMEText

class send_mail():
    def __init__(self):
        self.mail_host="smtp.gmail.com"
        self.mail_user="ipswitcher001"
        self.mail_passwd="wjzpwwjzpw"
        self.postfix="gmail.com"
        self.mailto="262238056@qq.com"
    def send_mail(self,sub,content):
        gmail_user=self.mail_user+"@"+self.postfix
        msg=MIMEText(content)
        msg['Subject']=sub
        msg['From']='Me'
        msg['To']=self.mailto
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(self.mail_user,self.mail_passwd)
        s.sendmail(gmail_user,self.mailto,msg.as_string())
        s.close()

if __name__ == "__main__":
    print 3
    send_mail().send_mail('Subject', 'haha')