import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

inbox = outlook.GetDefaultFolder(6) # "6" refers to the index of a folder - in this case,
                                    # the inbox. You can change that number to reference
                                    # any other folder

searchname=outlook.CreateRecipient("anil.ye@ltts.com")
objFolder = outlook.GetSharedDefaultFolder(searchname, 6)
strFilter = "@SQL=" + "urn:schemas:httpmail:subject" + " like '%Acting / Additional%'"
reslut=objFolder.Items.Restrict(strFilter)
for item in reslut:
    print(result)
#messages = inbox.Items
#message = messages.GetLast()
#body_content = message.body
#print (body_content)


