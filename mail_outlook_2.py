import win32com.client
from win32com.client import Dispatch, constants

const=win32com.client.constants
olMailItem = 0x0
obj = win32com.client.Dispatch("Outlook.Application")
newMail = obj.CreateItem(olMailItem)
newMail.Subject = "I AM SUBJECT!!"
# newMail.Body = "I AM\nTHE BODY MESSAGE!"
newMail.BodyFormat = 2 # olFormatHTML https://msdn.microsoft.com/en-us/library/office/aa219371(v=office.11).aspx
newMail.HTMLBody = "<HTML><BODY>Enter the <span style='color:red'>message</span> text here.</BODY></HTML>"
newMail.To = ""
attachment1 = r"C:\Users\Public\Pictures\Sample Pictures\Jellyfish.jpg"
newMail.Attachments.Add(Source=attachment1)
newMail.display()
#newMail.send()
