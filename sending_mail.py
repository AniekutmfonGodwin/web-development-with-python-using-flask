import smtplib
from settings import EMAIL,PASSWORD



mailer = smtplib.SMTP_SSL("smtp.gmail.com",465)

mailer.login(EMAIL,PASSWORD)
mailer.send_message("hello ",EMAIL,to_addrs="example@gmail.com")
mailer.quit()


