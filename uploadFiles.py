import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        
        dbx = dropbox.Dropbox(self.access_token)
        for rootdir,folders,files in os.walk(file_from):
            for fileNames in files:
                localPath = os.path.join(rootdir,fileNames)
                relativePath=os.path.relpath(localPath,file_from)
                dropboxPath=os.path.join(file_to,relativePath)
                with open(localPath, 'rb') as f:
                    dbx.files_upload(f.read(), dropboxPath)

def main():
    access_token = 'DMlKVe2pvEoAAAAAAAAAAbTblB2azdnHYYlakrGYm42FjkVURIP8U-T923qLOMOp'
    transferData = TransferData(access_token)

    file_from = input('Enter The File To Transfer')
    file_to = input('Enter The Path To Upload')
    transferData.upload_file(file_from, file_to)
    print("The Files Has Been Moved")

main()