# coding: utf-8

from webpmux_info import WebpInfo
import subprocess
import uuid
import sys
import os

if len(sys.argv) < 3 or {"-h", r"/?", "--help"} & set(sys.argv):
    print("Usage: script.py input.webp output.gif [libwebp_directory]")
    quit()

sourceFile = sys.argv[1]
output_gif_path = sys.argv[2]

if os.path.exists(output_gif_path):
    print("The output path specified already exists.")
    quit()

libwebp_directory = r"C:\Users\ATeg\Downloads\libwebp-1.2.2-windows-x64" if len(sys.argv) < 4 else sys.argv[3]
webpmuxPath = os.path.join(libwebp_directory, "bin", "webpmux.exe")
dwebpPath = os.path.join(libwebp_directory, "bin", "dwebp.exe")
gifski_path = os.path.join("..", "gifski.exe")

temp_directory = f"temp-directory-{uuid.uuid4().hex}"

webpInfo = WebpInfo(webpmuxPath)
info = webpInfo.getInfo(sourceFile)
frames = info['frames']

os.mkdir(temp_directory)

pngs = list()

def decompress(webpImageData):
    webp_to_png_command = [dwebpPath, "-o", "-", "--", "-"]
    proc = subprocess.Popen(webp_to_png_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate(webpImageData)

    return stdout, stderr

def demux(frameNumber):
    animationFrame_to_image__command = [webpmuxPath, "-get", "frame", str(frameNumber), sourceFile, "-o", "-"]
    #webpImageData = subprocess.check_output(animationFrame_to_image__command)
    proc = subprocess.Popen(animationFrame_to_image__command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()

    return stdout, stderr

def saveImage(path, data):
    with open(path, 'wb') as handle:
        handle.write(data)

for frame in frames:
    frameNumber = frame['No']

    webpImageData, stderr1 = demux(frameNumber)
    pngImageData, stderr2 = decompress(webpImageData)

    print("\r", stderr1.decode("UTF-8").replace("\n","-").replace("\r",""),"\t=2=", stderr2.decode("UTF-8").replace("\n", "-").replace("\r",""), end="")
    
    output_png_path = os.path.join(temp_directory,f"frame-{frameNumber}.png")
    saveImage(output_png_path, pngImageData)
    pngs.append(output_png_path)

input_png_files = os.path.join(temp_directory, "frame-*.png")
gifski_command = [gifski_path, input_png_files, "--fps", "20", "--quality", "90", "--output", "-"]

print("\nGenerating GIF...")

gifski_output = subprocess.check_output(gifski_command)

with open(output_gif_path, 'wb') as handle:
    handle.write(gifski_output)

for file in pngs:
    os.remove(file)

os.rmdir(temp_directory)