import os
import smtplib
from email.message import EmailMessage
from segredos import senha

#
EMAIL_ENVIO = 'marcioluizm@gmail.com'
EMAIL_PASSWORD = senha

# Criar um email
msg = EmailMessage()
msg['subject']="Carga chegou ao porto"
msg['From']='marcioluizm@gmail.com'
msg['To']='marcioluizm@yahoo.com.br'
msg.set_content('Favor buscar a carga nro xyz que acaba de chegar ao porto')

# Enviar 
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ENVIO,EMAIL_PASSWORD)
    smtp.send_message(msg)



