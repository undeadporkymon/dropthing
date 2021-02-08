import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        
        
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'access token here'
    transferData = TransferData(access_token)

    file_from = 'wow.txt'
    file_to = '/wow/wow.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)


main()
