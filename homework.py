import dropbox
accesstoken = 'sl.BDz9TWkfYZ2IFM3zOoH-CjBdASdRLqMR1wEJWcIH25n16uFHRQhYmwhnyeynBzzAfbiAc2qIrduF0tvFP-cnEDCQR4AqtlSp7cmURgi99vd5smzPUZjkEZnzsa5cFQHSSALTJZPS7zQ'
def uploadtoCloud():
    dbx = dropbox.Dropbox(accesstoken)
    f = open('soie chinoise.jpg', 'rb')
    dbx.files_upload(f.read(), "/Yena BYJU'S/soie chinoise.jpg")
uploadtoCloud()