import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

inbox = outlook.GetDefaultFolder(6) # "6" refers to the index of a folder - in this case,
                                    # the inbox. You can change that number to reference
                                    # any other folder

#searchname=outlook.CreateRecipient("anil.ye@ltts.com")
#objFolder = outlook.GetDefaultFolder(6)
#strFilter = "[From]"='anil.ye@ltts.com'
resluts=inbox.Items.Restrict("[From]='anil.ye@ltts.com'")
for reslut in results:
    print(result)
#messages = inbox.Items
#message = messages.GetLast()
#body_content = message.body
#print (body_content)


