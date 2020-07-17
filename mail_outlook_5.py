import win32com.client as win32

outlook = win32.Dispatch("Outlook.Application").GetNamespace("MAPI")

outbox = outlook.GetDefaultFolder(5) 

messages = outbox.Items.restrict("[SentOn] > '9/23/2019 08:00 AM'")

for message in messages:
    NewMsg = message.Forward()
    NewMsg.Body = message.Body
    NewMsg.Subject = message.Subject
    NewMsg.display()
    
