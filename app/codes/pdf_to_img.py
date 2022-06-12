#%%
import os
import fitz

from base64 import encodebytes

#%%
import logging

#%%
loglevel = os.environ.get("LOGLEVEL","INFO")
numeric_level = getattr(logging, loglevel.upper(), None) 
if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % loglevel)
logging.basicConfig(level=numeric_level)

def pdf2img(fname):

    logging.info("Calling pdf2img function") 

    binary_images = []
    doc = fitz.open("pdf",fname.read())  # open document
    for page in doc:  # iterate through the pages
        pix = page.get_pixmap(dpi=300)  # render page to an image
        binary_image = pix.tobytes(output="png")  # store image as a bytes memory object in PNG
        encoded_img = encodebytes(binary_image).decode('ascii')
        binary_images.append(encoded_img)
    return {"imgs":binary_images,"status":"Success"}, 200

