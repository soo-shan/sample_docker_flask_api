#%%
import io
import requests

from pathlib import Path
from base64 import decodebytes
#%%

filename = Path("test_pdf1.pdf")
folder_out = Path(filename.stem)

if not folder_out.exists():
    folder_out.mkdir()


assert filename.exists()
with open(filename, "rb") as f:
    filebinary = f.read()


url = "http://127.0.0.1:5001/app/pdfconverter"

response = requests.post(url, data={"id":1000, "doc_name":filename.stem}, files={"binary_pdf":filebinary})
# %%
if response.status_code == 200:
    list_images = response.json()["imgs"]

for i,image in enumerate(list_images):
    filename_out = f"{folder_out.stem}_{i}.png"
    with open(folder_out/filename_out,"wb") as f:
        f.write(decodebytes(image.encode("ascii")))
# %%
