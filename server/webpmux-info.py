# coding: utf-8

import webptools
webptools.webplib
help(webptools.webplib)
webptools.webpbin
webptools.webpbin.getcwebp()
help(webptools.webpbin.getcwebp)
help(webptools.webplib)
import subprocess
import json
import os
libwebp_directory = r"C:\Users\ATeg\Downloads\libwebp-1.2.2-windows-x64\bin"
webpmuxPath = os.path.join(libwebp_directory, "bin", "webpmux.exe")
sourceFile = r"C:\Users\ATeg\Pictures\Saved Pictures\Gasket\gasket-1.webp"

with open(os.devnull, 'w') as FNULL, open("webp-tools.log", 'w') as logfile:
    command = [webpmuxPath, "-info", sourceFile]
    print("Running Command", command)
    result_proc = subprocess.call(command, stdout=logfile, stderr=subprocess.STDOUT)  # Ignore output
libwebp_directory = r"C:\Users\ATeg\Downloads\libwebp-1.2.2-windows-x64"
webpmuxPath = os.path.join(libwebp_directory, "bin", "webpmux.exe")
sourceFile = r"C:\Users\ATeg\Pictures\Saved Pictures\Gasket\gasket-1.webp"

with open(os.devnull, 'w') as FNULL, open("webp-tools.log", 'w') as logfile:
    command = [webpmuxPath, "-info", sourceFile]
    print("Running Command", command)
    result_proc = subprocess.call(command, stdout=logfile, stderr=subprocess.STDOUT)  # Ignore output
with open("webp-tools.log","r") as handle:
    handle.read()
    
with open("webp-tools.log","r") as handle:
    print(handle.read())
    
    
with open("webp-tools.log","r") as handle, open(os.devnull, 'w') as fnull:
    fnull.write(handle.read())
    
    
    
with open(os.devnull,"r") as handle:
    print(handle.read())
    
    

# Importing the StringIO module.
from io import StringIO 
standardOutput = StringIO()
libwebp_directory = r"C:\Users\ATeg\Downloads\libwebp-1.2.2-windows-x64"
webpmuxPath = os.path.join(libwebp_directory, "bin", "webpmux.exe")
sourceFile = r"C:\Users\ATeg\Pictures\Saved Pictures\Gasket\gasket-1.webp"

with open(os.devnull, 'w') as FNULL, open("webp-tools.log", 'w') as logfile:
    command = [webpmuxPath, "-info", sourceFile]
    print("Running Command", command)
    result_proc = subprocess.call(command, stdout=standardOutput, stderr=subprocess.STDOUT)  # Ignore output
libwebp_directory = r"C:\Users\ATeg\Downloads\libwebp-1.2.2-windows-x64"
webpmuxPath = os.path.join(libwebp_directory, "bin", "webpmux.exe")
sourceFile = r"C:\Users\ATeg\Pictures\Saved Pictures\Gasket\gasket-1.webp"

stdout = ""

command = [webpmuxPath, "-info", sourceFile]
print("Running Command", command)

result_proc = subprocess.call(command, stdout=stdout, stderr=subprocess.STDOUT)  # Ignore output
from io import FileIO
standardOutput = FileIO()
libwebp_directory = r"C:\Users\ATeg\Downloads\libwebp-1.2.2-windows-x64"
webpmuxPath = os.path.join(libwebp_directory, "bin", "webpmux.exe")
sourceFile = r"C:\Users\ATeg\Pictures\Saved Pictures\Gasket\gasket-1.webp"

stdout = ""

command = [webpmuxPath, "-info", sourceFile]
print("Running Command", command)

result_proc = subprocess.run(command, capture_output=True)
from io import FileIO

libwebp_directory = r"C:\Users\ATeg\Downloads\libwebp-1.2.2-windows-x64"
webpmuxPath = os.path.join(libwebp_directory, "bin", "webpmux.exe")
sourceFile = r"C:\Users\ATeg\Pictures\Saved Pictures\Gasket\gasket-1.webp"

stdout = FileIO()

command = [webpmuxPath, "-info", sourceFile]
print("Running Command", command)

result_proc = subprocess.call(command, stdout=stdout, stderr=subprocess.STDOUT)  # Ignore output
from io import BytesIO

libwebp_directory = r"C:\Users\ATeg\Downloads\libwebp-1.2.2-windows-x64"
webpmuxPath = os.path.join(libwebp_directory, "bin", "webpmux.exe")
sourceFile = r"C:\Users\ATeg\Pictures\Saved Pictures\Gasket\gasket-1.webp"

stdout = BytesIO()

command = [webpmuxPath, "-info", sourceFile]
print("Running Command", command)

result_proc = subprocess.call(command, stdout=stdout, stderr=subprocess.STDOUT)  # Ignore output
subprocess.check_output(command)
from io import BytesIO

libwebp_directory = r"C:\Users\ATeg\Downloads\libwebp-1.2.2-windows-x64"
webpmuxPath = os.path.join(libwebp_directory, "bin", "webpmux.exe")
sourceFile = r"C:\Users\ATeg\Pictures\Saved Pictures\Gasket\gasket-1.webp"

stdout = BytesIO()

command = [webpmuxPath, "-info", sourceFile]
print("Running Command", command)

#result_proc = subprocess.call(command, stdout=stdout, stderr=subprocess.STDOUT)  # Ignore output
result_output = subprocess.check_output('wc --lines /var/log/syslog', encoding='UTF-8')
from io import BytesIO

libwebp_directory = r"C:\Users\ATeg\Downloads\libwebp-1.2.2-windows-x64"
webpmuxPath = os.path.join(libwebp_directory, "bin", "webpmux.exe")
sourceFile = r"C:\Users\ATeg\Pictures\Saved Pictures\Gasket\gasket-1.webp"

stdout = BytesIO()

command = [webpmuxPath, "-info", sourceFile]
print("Running Command", command)

#result_proc = subprocess.call(command, stdout=stdout, stderr=subprocess.STDOUT)  # Ignore output
result_output = subprocess.check_output(command, encoding='UTF-8')
from io import BytesIO

libwebp_directory = r"C:\Users\ATeg\Downloads\libwebp-1.2.2-windows-x64"
webpmuxPath = os.path.join(libwebp_directory, "bin", "webpmux.exe")
sourceFile = r"C:\Users\ATeg\Pictures\Saved Pictures\Gasket\gasket-1.webp"

stdout = BytesIO()

command = [webpmuxPath, "-info", sourceFile]
print("Running Command", command)

#result_proc = subprocess.call(command, stdout=stdout, stderr=subprocess.STDOUT)  # Ignore output
result_output = subprocess.check_output(command, encoding='UTF-8')
result_proc = subprocess.check_call(command)
result_proc
from io import BytesIO

libwebp_directory = r"C:\Users\ATeg\Downloads\libwebp-1.2.2-windows-x64"
webpmuxPath = os.path.join(libwebp_directory, "bin", "webpmux.exe")
sourceFile = r"C:\Users\ATeg\Pictures\Saved Pictures\Gasket\gasket-1.webp"

stdout = BytesIO()

command = [webpmuxPath, "-info", sourceFile]
print("Running Command", command)

#result_proc = subprocess.call(command, stdout=stdout, stderr=subprocess.STDOUT)  # Ignore output
result_output = subprocess.check_output(command, encoding='UTF-8')
#result_proc = subprocess.check_call(command)
result_output
print(result_output)
import re
CANVAS_SIZE_PATTERN = re.compile(r"canvas\s+size:\s+(\d+)\s+x\s+(\d+)", re.IGNORECASE)
FEATURES_PRESENT_PATTERN = re.compile(r"features\s+present:\s+(\w+)")
BG_COLOR_LOOP_COUNT_PATTERN = re.compile(r"background\s+color\s+:\s+([\d\w]+)\s+loop\s+count\s+:\s+(\d+)")
NUMBER_OF_FRAMES = re.compile(r"number\s+of\s+frames:\s+(\d+)")
import re
CANVAS_SIZE_PATTERN = re.compile(r"canvas\s+size:\s+(\d+)\s+x\s+(\d+)", re.IGNORECASE)
FEATURES_PRESENT_PATTERN = re.compile(r"features\s+present:\s+(\w+)", re.IGNORECASE)
BG_COLOR_LOOP_COUNT_PATTERN = re.compile(r"background\s+color\s+:\s+([\d\w]+)\s+loop\s+count\s+:\s+(\d+)", re.IGNORECASE)
NUMBER_OF_FRAMES = re.compile(r"number\s+of\s+frames:\s+(\d+)", re.IGNORECASE)
result_output.split("\r\n")
for value in result_output.split("\r\n"):
    txt = value.strip()
    canvasSize = CANVAS_SIZE_PATTERN.match(txt)
    featuresPresent = FEATURES_PRESENT_PATTERN.match(txt)
    bgColorAndLoopCount = BG_COLOR_LOOP_COUNT_PATTERN.match(txt)
    numberOfFrames = NUMBER_OF_FRAMES.match(txt)
    
info = dict()

for value in result_output.split("\r\n"):
    txt = value.strip()
    canvasSize = CANVAS_SIZE_PATTERN.match(txt)
    featuresPresent = FEATURES_PRESENT_PATTERN.match(txt)
    bgColorAndLoopCount = BG_COLOR_LOOP_COUNT_PATTERN.match(txt)
    numberOfFrames = NUMBER_OF_FRAMES.match(txt)
    
info = dict()

for value in result_output.split("\r\n"):
    txt = value.strip()
    canvasSize = CANVAS_SIZE_PATTERN.match(txt)
    featuresPresent = FEATURES_PRESENT_PATTERN.match(txt)
    bgColorAndLoopCount = BG_COLOR_LOOP_COUNT_PATTERN.match(txt)
    numberOfFrames = NUMBER_OF_FRAMES.match(txt)
    
    if canvasSize:
         info['width'] = int(canvasSize[1])
         info['height'] = int(canvasSize[2])
         
    if featuresPresent:
         print("Features:", featuresPresent)
         
         
         
info = dict()

for value in result_output.split("\r\n"):
    txt = value.strip()
    print(txt)
    canvasSize = CANVAS_SIZE_PATTERN.match(txt)
    featuresPresent = FEATURES_PRESENT_PATTERN.match(txt)
    bgColorAndLoopCount = BG_COLOR_LOOP_COUNT_PATTERN.match(txt)
    numberOfFrames = NUMBER_OF_FRAMES.match(txt)
    
    if canvasSize:
         info['width'] = int(canvasSize[1])
         info['height'] = int(canvasSize[2])
         
    if featuresPresent:
         print("Features:", featuresPresent)
         
         
         
txts = [value.strip() for value in result_output.split("\r\n")]
txts[0]
txts = [value.strip() for value in result_output.split("\n")]
txts[0]
CANVAS_SIZE_PATTERN.fullmatch(txts[0])
match_full = CANVAS_SIZE_PATTERN.fullmatch(txts[0])
match_match = CANVAS_SIZE_PATTERN.match(txts[0])
match_match
match_search = CANVAS_SIZE_PATTERN.search(txts[0])
match_search
match_search.groups()
import re
CANVAS_SIZE_PATTERN = re.compile(r"canvas\s+size:\s+(?P<width>\d+)\s+x\s+(?P<height>\d+)", re.IGNORECASE)
FEATURES_PRESENT_PATTERN = re.compile(r"features\s+present:\s+(?P<features>\w+)", re.IGNORECASE)
BG_COLOR_LOOP_COUNT_PATTERN = re.compile(r"background\s+color\s+:\s+(?P<bgColor>[\d\w]+)\s+loop\s+count\s+:\s+(?P<loopCount>\d+)", re.IGNORECASE)
NUMBER_OF_FRAMES = re.compile(r"number\s+of\s+frames:\s+(?P<numberOfFrames>\d+)", re.IGNORECASE)
HEADER_PATTERN = re.compile(r"canvas\s+size:\s+(?P<width>\d+)\s+x\s+(?P<height>\d+).features\s+present:\s+(?P<features>\w+).background\s+color\s+:\s+(?P<bgColor>[\d\w]+)\s+loop\s+count\s+:\s+(?P<loopCount>\d+).number\s+of\s+frames:\s+(?P<numberOfFrames>\d+)", re.IGNORECASE|re.DOTALL)
HEADER_PATTERN.search(result_output)
txts[:4]
CANVAS_SIZE_PATTERN.match(txts[0])
FEATURES_PRESENT_PATTERN.match(txts[1])
BG_COLOR_LOOP_COUNT_PATTERN.match(txts[2])
NUMBER_OF_FRAMES.match(txts[3])
HEADER_PATTERN = re.compile(r"canvas\s+size:\s+(?P<width>\d+)\s+x\s+(?P<height>\d+).features\s+present:\s+(?P<features>\w+).background\s+color\s+:\s+(?P<bgColor>[\d\w]+)\s+loop\s+count\s+:\s+(?P<loopCount>\d+).number\s+of\s+frames:\s+(?P<numberOfFrames>\d+)", re.IGNORECASE|re.DOTALL|re.MULTILINE)
HEADER_PATTERN.search(result_output)
HEADER_PATTERN.match(result_output)
HEADER_PATTERN = re.compile(r"canvas\s+size:\s+(?P<width>\d+)\s+x\s+(?P<height>\d+)\\nfeatures\s+present:\s+(?P<features>\w+).background\s+color\s+:\s+(?P<bgColor>[\d\w]+)\s+loop\s+count\s+:\s+(?P<loopCount>\d+).number\s+of\s+frames:\s+(?P<numberOfFrames>\d+)", re.IGNORECASE|re.DOTALL|re.MULTILINE)
HEADER_PATTERN = re.compile(r"canvas\s+size:\s+(?P<width>\d+)\s+x\s+(?P<height>\d+)\nfeatures\s+present:\s+(?P<features>\w+)\nbackground\s+color\s+:\s+(?P<bgColor>[\d\w]+)\s+loop\s+count\s+:\s+(?P<loopCount>\d+)\nnumber\s+of\s+frames:\s+(?P<numberOfFrames>\d+)", re.IGNORECASE|re.DOTALL|re.MULTILINE)
HEADER_PATTERN.match(result_output)
HEADER_PATTERN.search(result_output)
HEADER_PATTERN.match("\n".join(txts[:4]))
"\n".join(txts[:4])
HEADER_PATTERN = re.compile(r"canvas\s+size:\s+(?P<width>\d+)\s+x\s+(?P<height>\d+)\nfeatures\s+present:\s+(?P<features>\w+)\nbackground\s+color\s+:\s+(?P<bgColor>[\d\w]+)\s+loop\s+count\s+:\s+(?P<loopCount>\d+)\nnumber\s+of\s+frames:\s+(?P<numberOfFrames>\d+)", re.IGNORECASE|re.DOTALL|re.MULTILINE)
HEADER_PATTERN = re.compile(r"canvas\s+size:\s+(?P<width>\d+)\s+x\s+(?P<height>\d+)\nfeatures\s+present:\s+(?P<features>\w+)\nbackground\s+color\s+:\s+", re.IGNORECASE|re.DOTALL|re.MULTILINE)
HEADER_PATTERN.match("\n".join(txts[:4]))
HEADER_PATTERN.search("\n".join(txts[:4]))
HEADER_PATTERN = re.compile(r"canvas\s+size:\s+(?P<width>\d+)\s+x\s+(?P<height>\d+)\nfeatures\s+present:\s+", re.IGNORECASE|re.DOTALL|re.MULTILINE)
HEADER_PATTERN.search("\n".join(txts[:4]))
HEADER_PATTERN = re.compile(r"canvas\s+size:\s+(?P<width>\d+)\s+x\s+(?P<height>\d+)\nfeatures\s+present:\s+(?P<features>\w+)\nbackground\s+color\s+:\s+", re.IGNORECASE|re.DOTALL|re.MULTILINE)
HEADER_PATTERN.search("\n".join(txts[:4]))
HEADER_PATTERN = re.compile(r"canvas\s+size:\s+(?P<width>\d+)\s+x\s+(?P<height>\d+)\nfeatures\s+present:\s+(?P<features>[\w\s]+)\nbackground\s+color\s+:\s+", re.IGNORECASE|re.DOTALL|re.MULTILINE)
HEADER_PATTERN.search("\n".join(txts[:4]))
HEADER_PATTERN = re.compile(r"canvas\s+size:\s+(?P<width>\d+)\s+x\s+(?P<height>\d+)\nfeatures\s+present:\s+(?P<features>[\w\s]+)\nbackground\s+color\s+:\s+(?P<bgColor>[\d\w]+)\s+loop\s+count\s+:\s+(?P<loopCount>\d+)", re.IGNORECASE|re.DOTALL|re.MULTILINE)
HEADER_PATTERN.search("\n".join(txts[:4]))
HEADER_PATTERN = re.compile(r"canvas\s+size:\s+(?P<width>\d+)\s+x\s+(?P<height>\d+)\nfeatures\s+present:\s+(?P<features>\w+)\nbackground\s+color\s+:\s+(?P<bgColor>[\d\w]+)\s+loop\s+count\s+:\s+(?P<loopCount>\d+)\nnumber\s+of\s+frames:\s+(?P<numberOfFrames>\d+)", re.IGNORECASE|re.DOTALL|re.MULTILINE)
HEADER_PATTERN = re.compile(r"canvas\s+size:\s+(?P<width>\d+)\s+x\s+(?P<height>\d+)\nfeatures\s+present:\s+(?P<features>[\w\s]+)\nbackground\s+color\s+:\s+(?P<bgColor>[\d\w]+)\s+loop\s+count\s+:\s+(?P<loopCount>\d+)\nnumber\s+of\s+frames:\s+(?P<numberOfFrames>\d+)", re.IGNORECASE|re.DOTALL|re.MULTILINE)
HEADER_PATTERN.search("\n".join(txts[:4]))
match = HEADER_PATTERN.search("\n".join(txts[:4]))
match.groupdict()
"\n".join(txts[4:])
print("\n".join(txts[4:]))
txts[4]
help(txts[4].split)
txts[4].split()
frameAttrs = txts[4].split()
if frames[0] == 'No.:':
    frameAttrs[0] = 'No'
    
if frameAttrs[0] == 'No.:':
    frameAttrs[0] = 'No'
    
frameAttrs
txts[7]
txts[4:]
txts[7].split()
FRAME_NUMBER_PATTERN = re.compile(r"\d+\:")
NUMBER_PATTERN = re.compile(r"\d+")

def parseFrame(line, columns):
    items = line.split()
    
    if FRAME_NUMBER_PATTERN.match(items[0]):
        items[0] = items[0].replace(":","")
        
    for index, cell in enumerate(items):
        if NUMBER_PATTERN.match(cell):
            items[index] = int(cell)
            
    return dict(zip(columns, items))
frameAttrs
parseFrame(txts[7], frameAttrs)
FRAME_NUMBER_PATTERN = re.compile(r"\d+\:")
NUMBER_PATTERN = re.compile(r"\d+")
BOOL_PATTERN = re.compile(r"yes|no")

def parseFrame(line, columns):
    items = line.split()
    
    if FRAME_NUMBER_PATTERN.match(items[0]):
        items[0] = items[0].replace(":","")
        
    for index, cell in enumerate(items):
        if NUMBER_PATTERN.match(cell):
            items[index] = int(cell)

        if BOOL_PATTERN.match(cell):
            items[index] = bool(cell)
            
    return dict(zip(columns, items))
parseFrame(txts[7], frameAttrs)
FRAME_NUMBER_PATTERN = re.compile(r"\d+\:")
NUMBER_PATTERN = re.compile(r"\d+")
BOOL_PATTERN = re.compile(r"(?:yes|no)")

def parseFrame(line, columns):
    items = line.split()
    
    if FRAME_NUMBER_PATTERN.match(items[0]):
        items[0] = items[0].replace(":","")
        
    for index, cell in enumerate(items):
        if NUMBER_PATTERN.match(cell):
            items[index] = int(cell)

        if BOOL_PATTERN.match(cell):
            items[index] = bool(cell)
            
    return dict(zip(columns, items))
parseFrame(txts[7], frameAttrs)
txts[7]
FRAME_NUMBER_PATTERN = re.compile(r"\d+\:")
NUMBER_PATTERN = re.compile(r"\d+")
BOOL_PATTERN = re.compile(r"(?:yes|no)")

def parseFrame(line, columns):
    items = line.split()
    
    if FRAME_NUMBER_PATTERN.match(items[0]):
        items[0] = items[0].replace(":","")
        
    for index, cell in enumerate(items):
        if NUMBER_PATTERN.match(cell):
            items[index] = int(cell)

        if BOOL_PATTERN.match(cell):
            items[index] = cell == "yes"
            
    return dict(zip(columns, items))
parseFrame(txts[7], frameAttrs)
txts[7]
txts[4]
BOOL_PATTERN.match("none")
FRAME_NUMBER_PATTERN = re.compile(r"\d+\:")
NUMBER_PATTERN = re.compile(r"\d+")
BOOL_PATTERN = re.compile(r"(?:yes|no)", re.TEMPLATE)

def parseFrame(line, columns):
    items = line.split()
    
    if FRAME_NUMBER_PATTERN.match(items[0]):
        items[0] = items[0].replace(":","")
        
    for index, cell in enumerate(items):
        if NUMBER_PATTERN.match(cell):
            items[index] = int(cell)

        if BOOL_PATTERN.match(cell):
            items[index] = cell == "yes"
            
    return dict(zip(columns, items))
BOOL_PATTERN.match("none")
FRAME_NUMBER_PATTERN = re.compile(r"\d+\:")
NUMBER_PATTERN = re.compile(r"\d+")
BOOL_PATTERN = re.compile(r"(?:yes|no)\Z",)

def parseFrame(line, columns):
    items = line.split()
    
    if FRAME_NUMBER_PATTERN.match(items[0]):
        items[0] = items[0].replace(":","")
        
    for index, cell in enumerate(items):
        if NUMBER_PATTERN.match(cell):
            items[index] = int(cell)

        if BOOL_PATTERN.match(cell):
            items[index] = cell == "yes"
            
    return dict(zip(columns, items))
BOOL_PATTERN.match("none")
parseFrame(txts[7], frameAttrs)
get_ipython().run_line_magic('save', '"webpmux-info" 0-115')
