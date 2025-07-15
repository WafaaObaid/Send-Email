
import smtplib
sender = "ali@psut.edu.jo"
receivers = ["ahmad@pust.edu.jo"]
message = "I would like to invite you to python course"
try:
  smtpObj = smtplib.SMTP('www.psut.edu.jo')
  smtpObj.sendmail(sender, receivers, message)
  print("Succefully sent email")
except:
  print("Error: Unable to send email")   
