# Util Methods
def saveEmailAttachement(email_text, attachment_text, filePath):
    file_path = "./data/emails/"+filePath
    file = open(file_path, 'w', encoding='UTF-8')
    file.write(email_text+" " + attachment_text)
    file.close()