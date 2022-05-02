

from wand.image import Image
import os
import argparse

parser = argparse.ArgumentParser("QRs to PDF")
parser.add_argument("qrdir", help="Directory who store QRs in PNG format", type=str)
args = parser.parse_args()
directory = args.qrdir
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        print(f)
        filecon = os.path.splitext(filename)[0]  + '.pdf'
        ny = Image(filename = f)
        ny_convert = ny.convert('pdf')
        ny_convert.save(filename = os.path.join(directory, filecon))
