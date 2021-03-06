# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from comm import Comm


class MailSender:
    @staticmethod
    def send_mail(subject, content):
        "发送邮件"
        # 获取用户邮箱配置信息
        cp = Comm.get_config()
        user = cp.get("mail", "user")
        pwd = cp.get("mail", "pwd")
        server = cp.get("mail", "server")
        port = cp.getint("mail", "port")
        to = cp.get("mail", "to")
        sender = cp.get("mail", "sender")

        msg = MIMEText(content, "html", "utf-8")
        msg["From"] = Header(sender, "utf-8")
        msg["To"] = Header(to, "utf-8")
        msg["Subject"] = Header(subject, "utf-8")
        try:
            mail = smtplib.SMTP()
            mail.connect(server, port)
            mail.login(user, pwd)
            mail.sendmail(user, to, msg.as_string())
            mail.quit()
            print("邮件发送成功！")
        except Exception as error:
            print("邮件发送失败：" + str(error))
