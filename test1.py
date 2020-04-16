#libraries
import smtplib
from   email.message import EmailMessage
import itertools
import pandas as pd 

#user input and display information
usr_mail=input("Enter mail id:")
usr_pwd=input("Enter password:")
#path=input("Enter path of csv file:")

#readinf csv converting df----->list

#df=pd.read_csv(path)
df=pd.read_csv('record.csv')
#lists
names_list=df['name'].values.tolist()
mail_list=df['mail'].values.tolist()
subject_list=df['subject'].values.tolist()
m_essage_list=df['msg'].values.tolist()


'''
send attachment(image)

with open('name.jpg','rb') as f:
    file_data=f.read()
    file_type = imghdr.what(f.name)
    file_name=f.name

msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)
'''

for(a,b,c,d) in zip(names_list,mail_list,subject_list,m_essage_list):
    msg= EmailMessage()
    msg['From']=usr_mail
    msg['To']=b
    msg['Subject']=c
    msg.set_content(d)


    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(usr_mail,usr_pwd)
        smtp.send_message(msg)
    






