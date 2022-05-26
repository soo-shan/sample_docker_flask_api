#%%
import io
import fitz

from base64 import encodebytes
#%%

def pdf2img(fname):
    
    binary_images = []
    doc = fitz.open("pdf",fname.read())  # open document
    for page in doc:  # iterate through the pages
        pix = page.get_pixmap(dpi=300)  # render page to an image
        binary_image = pix.tobytes(output="png")  # store image as a bytes memory object in PNG
        encoded_img = encodebytes(binary_image).decode('ascii')
        binary_images.append(encoded_img)
    return {"imgs":binary_images,"status":"Success"}, 200

