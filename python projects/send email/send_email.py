import smtplib as s

ob = s.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()
ob.login('joelroy8140@gmail.com', 'djan wnxj izbo hvqe')
subject = "testing python"
body = "Hey there"
message = "subject:{}\n\n{}".format(subject,body)
listadd= ['jj848451@gmail.com',
           "jroy87819@gmail.com"]
ob.sendmail('joelroy8140@gmail.com', listadd,message)
print("sent mail")
ob.quit()