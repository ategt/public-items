# coding: utf-8

from webpmux_info import WebpInfo
import subprocess
import uuid
import sys
import re
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

def cleanupOutput(line):
    return line.decode("UTF-8").replace("\n","-").replace("\r","")

def saveImage(path, data):
    with open(path, 'wb') as handle:
        handle.write(data)

SAVED_FILE_PATTERN = re.compile(r"Saved\s+file\s+\-\s+\((?P<bytes>\d+)\s+bytes\)", re.IGNORECASE)
DECOMPRESSOR_PATTERN = re.compile(r"Decoded\s+\-\.\s+Dimensions\:\s+(?P<width>\d+)\s+x\s+(?P<height>\d+)\s+\.\s+Format\:\s+(?P<format>\w+)\.\s+Now\s+saving\.\.\.\-Saved\s+to\s+stdout", re.IGNORECASE)

for frame in frames:
    frameNumber = frame['No']

    webpImageData, demux_info = demux(frameNumber)
    pngImageData, decompress_info = decompress(webpImageData)

    demux_screen = cleanupOutput(demux_info)
    decompress_screen = cleanupOutput(decompress_info)

    bytes_saved = int(SAVED_FILE_PATTERN.match(demux_screen).groupdict()['bytes'])
    decompressor_data = DECOMPRESSOR_PATTERN.match(decompress_screen).groupdict()

    print("\r", f"Working on Frame {frameNumber} - {bytes_saved} bytes\t Dimensions: {decompressor_data['width']} x {decompressor_data['height']}\t Format: {decompressor_data['format']}", end="")
    
    output_png_path = os.path.join(temp_directory,f"frame-{frameNumber}.png")
    saveImage(output_png_path, pngImageData)
    pngs.append(output_png_path)

input_png_files = os.path.join(temp_directory, "frame-*.png")
gifski_command = [gifski_path, input_png_files, "--fps", "20", "--quality", "90", "--output", "-"]

print("\nGenerating GIF...", end="\r")

gifski_output = subprocess.check_output(gifski_command)

print("Saving GIF", end="\r")

with open(output_gif_path, 'wb') as handle:
    handle.write(gifski_output)

print("Cleaning up", end="\r")

for file in pngs:
    os.remove(file)

os.rmdir(temp_directory)

print("Done!")