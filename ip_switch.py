import smtplib

from email.mime.text import MIMEText
import time

class send_mail():
    def __init__(self):
        self.mail_host="smtp.gmail.com"
        self.mail_user="ipswitcher001"
        self.mail_passwd="wjzpwwjzpw"
        self.postfix="gmail.com"
        self.mailto=['xxshutong@gmail.com']
    def send_mail(self,sub,content):
        gmail_user=self.mail_user+"@"+self.postfix
        msg=MIMEText(content)
        msg['Subject']=sub
        msg['From']='Me'
        msg['To']=';'.join(self.mailto)

        s=smtplib.SMTP('smtp.gmail.com',587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(self.mail_user,self.mail_passwd)
        s.sendmail(gmail_user,self.mailto,msg.as_string())
        s.close()

def get_current_ip():
    import socket
    # 1: Use the gethostname method

    ipaddr = socket.gethostbyname(socket.gethostname())
    if not( ipaddr.startswith('127') ) :
        print('Can use Method 1: ' + ipaddr)
        return ipaddr

    # 2: Use outside connection
    '''
    Source:
    http://commandline.org.uk/python/how-to-find-out-ip-address-in-python/
    '''

    ipaddr=''
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('google.com', 0))
        ipaddr=s.getsockname()[0]
        print('Can used Method 2: ' + ipaddr)
        return ipaddr
    except:
        pass


    # 3: Use OS specific command
    import subprocess , platform
    ipaddr=''
    os_str=platform.system().upper()

    if os_str=='LINUX' :

        # Linux:
        arg='ip route list'
        p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
        data = p.communicate()
        sdata = data[0].split()
        ipaddr = sdata[ sdata.index('src')+1 ]
        #netdev = sdata[ sdata.index('dev')+1 ]
        print('Can used Method 3: ' + ipaddr)
        return ipaddr

    elif os_str=='WINDOWS' :

        # Windows:
        arg='route print 0.0.0.0'
        p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
        data = p.communicate()
        strdata=data[0].decode()
        sdata = strdata.split()

        while len(sdata)>0:
            if sdata.pop(0)=='Netmask' :
                if sdata[0]=='Gateway' and sdata[1]=='Interface' :
                    ipaddr=sdata[6]
                    break
        print('Can used Method 4: ' + ipaddr)
        return ipaddr

if __name__ == "__main__":
    previous_ip = get_current_ip()
    print previous_ip
    send_mail().send_mail('New IP address From leon', 'Current address: http://%s:5000' % previous_ip)
    while True:
        try:
            current_ip = get_current_ip()
        except:
            continue

        if previous_ip != current_ip:
            send_mail().send_mail('New IP address From leon', 'Current address: http://%s:5000' % current_ip)
        time.sleep(60)

