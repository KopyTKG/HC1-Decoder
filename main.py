import base45
import zlib
import flynn
import os
import json
import webbrowser
from PIL import Image
from datetime import datetime
from flynn import data
from pyzbar import pyzbar
from inc import annotate


path = "./out/Decode.txt"

# Write into file
with open(path, "w") as File:

    # Try load QRcode img
    try:
        qr_code = Image.open("./src/QR_CODE.png")
        code = pyzbar.decode(qr_code)[0].data
    # If dont exist load file
    except:
        code = open("./Code.txt", "r").read()

    # decode base45
    unBase45 = base45.b45decode(code[4:])
    
    # decompress
    uncompressed = zlib.decompress(unBase45)

    # COSE decode
    (_, (headers1, headers2, cbor_data, signature)) = flynn.decoder.loads(uncompressed)
    
    # CBOR decode
    data = flynn.decoder.loads(cbor_data)

    # Time preset
    date = lambda ts: datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    # Write timestamps in QRcode
    File.write("QR Code Issuer :" + data[1] + "\n")
    File.write("QR Code Expiry :" + date(data[4]) + "\n")
    File.write("QR Code Generated :" + date(data[6]) + "\n")


    # load Schema for output
    sch = open("./inc/Schema.json", "r")
    # parse to json
    glb_schema = json.load(sch)

    # run Annotate function 
    annotate(data[-260][1], glb_schema['properties'],File)
    # return status
    print(f"""
    Decode Done
    
    all information has been save to {path} file at
    - {os.path.abspath(path)}""")

# open output file in browser
webbrowser.open(path)