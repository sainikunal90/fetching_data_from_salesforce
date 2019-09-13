
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import datetime
from simple_salesforce import Salesforce
import pandas as pd

cur_date = datetime.datetime.now().strftime ("%Y-%m-%d")

sf = Salesforce(username='kunal.saini@gmail.com', password='', security_token='')
query1 = sf.query("SELECT Lead_Created_Date__c , PT_Lead_Stage__c, PT_Lead_ID__c FROM Account WHERE CreatedDate >= LAST_N_DAYS:14 AND FulFillment_id__c IN ('0',NULL) AND Fulfillment_Service_Id_For_Digital_Merch__c IN ('0', NULL) AND Agent_Code__c LIKE '%sym%'")

df1 = pd.DataFrame(query1)

result = pd.concat(frames, ignore_index=True)
i = len(result.index)
s = str(i)

msg = MIMEMultipart()
msg['From'] = "kunal.saini@gmail.com"
To = ["kunal.saini@gmail.com"]
password = "App password"
msg['Subject'] = "O2O Onboarding Score : " + cur_date
body = """\
<html>
<head>
<style>
#myHeader {
    background-color: lightblue;
    color: black;
    padding: 40px;
    text-align: center;
} 
</style>
</head>
<body>

<h1 id="myHeader">O2O Onboarding Yesterday Score""" + ' = ' + s +"""
</h1> 
<h2>Above numbers are fetched from SalesForce API, and numbers consist for New and Duplicate MIDs </h2>
<p> </p>
<p>Downloading Attachment capabilites is under work</p>

</body>
</html>
""" 
print(s)
msg.attach(MIMEText(body, 'html'))

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("sainikunal90@gmail.com", password)
server.sendmail(msg['From'],To,msg.as_string())
server.quit()
