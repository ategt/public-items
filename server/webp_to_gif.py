# coding: utf-8

from webpmux_info import WebpInfo
import os

libwebp_directory = r"C:\Users\ATeg\Downloads\libwebp-1.2.2-windows-x64"
webpmuxPath = os.path.join(libwebp_directory, "bin", "webpmux.exe")

webpInfo = WebpInfo(webpmuxPath)

info = webpInfo.getInfo(r"C:\Users\ATeg\Pictures\Saved Pictures\Gasket\gasket-1.webp")
info['duration']
info
info['numberOfFrames']
import subprocess
command = [webpmuxPath, "-get", "frame", frameNumber, sourceFile, "-o", "-", "|", "bin\dwebp.exe", "-o", "-", "--", "-"]
frames = info['frames']
import os

sourceFile = r"C:\Users\ATeg\Pictures\Saved Pictures\Gasket\gasket-1.webp"

libwebp_directory = r"C:\Users\ATeg\Downloads\libwebp-1.2.2-windows-x64"
webpmuxPath = os.path.join(libwebp_directory, "bin", "webpmux.exe")
dwebpPath = os.path.join(libwebp_directory, "bin", "dwebp.exe")

webpInfo = WebpInfo(webpmuxPath)

info = webpInfo.getInfo(sourceFile)
os.mkdir("temp-directory")

for frame in frames:
    frameNumber = frame['No']
    command = [webpmuxPath, "-get", "frame", frameNumber, sourceFile, "-o", "-", "|", dwebpPath, "-o", "-", "--", "-"]
    pngData = subprocess.check_output(command, encoding='UTF-8')
    
    with open(os.path.join("temp-directory",f"frame-{frameNumber}.png"), 'wb') as handle:
        handle.write(pngdata)
os.mkdir("temp-directory")

for frame in frames:
    frameNumber = frame['No']
    command = [webpmuxPath, "-get", "frame", frameNumber, sourceFile, "-o", "-", "|", dwebpPath, "-o", "-", "--", "-"]
    pngData = subprocess.check_output(command)
    
    with open(os.path.join("temp-directory",f"frame-{frameNumber}.png"), 'wb') as handle:
        handle.write(pngdata)
#os.mkdir("temp-directory")

for frame in frames:
    frameNumber = frame['No']
    command = [webpmuxPath, "-get", "frame", frameNumber, sourceFile, "-o", "-", "|", dwebpPath, "-o", "-", "--", "-"]
    pngData = subprocess.check_output(command)
    
    with open(os.path.join("temp-directory",f"frame-{frameNumber}.png"), 'wb') as handle:
        handle.write(pngdata)
#os.mkdir("temp-directory")

for frame in frames:
    frameNumber = frame['No']
    command = [webpmuxPath, "-get", "frame", str(frameNumber), sourceFile, "-o", "-", "|", dwebpPath, "-o", "-", "--", "-"]
    pngData = subprocess.check_output(command)
    
    with open(os.path.join("temp-directory",f"frame-{frameNumber}.png"), 'wb') as handle:
        handle.write(pngdata)
dx = ['C:\\Users\\ATeg\\Downloads\\libwebp-1.2.2-windows-x64\\bin\\webpmux.exe', '-get', 'frame', '1', 'C:\\Users\\ATeg\\Pictures\\Saved Pictures\\Gasket\\gasket-1.webp', '-o', '-', '|', 'C:\\Users\\ATeg\\Downloads\\libwebp-1.2.2-windows-x64\\bin\\dwebp.exe', '-o', '-', '--', '-']
"".join(dx)
" ".join(dx)
" ".join(dx).replace("\\\\", "\\")
" ".join(dx).replace(r"\\", r"\")
" ".join(dx).replace(r"\\\\", r"\\")
#os.mkdir("temp-directory")

for frame in frames:
    frameNumber = frame['No']
    command = [webpmuxPath, "-get", "frame", str(frameNumber), f"'{sourceFile}'", "-o", "-", "|", dwebpPath, "-o", "-", "--", "-"]
    pngData = subprocess.check_output(command)
    
    with open(os.path.join("temp-directory",f"frame-{frameNumber}.png"), 'wb') as handle:
        handle.write(pngdata)
dx = ['C:\\Users\\ATeg\\Downloads\\libwebp-1.2.2-windows-x64\\bin\\webpmux.exe', '-get', 'frame', '1', "'C:\\Users\\ATeg\\Pictures\\Saved Pictures\\Gasket\\gasket-1.webp'", '-o', '-', '|', 'C:\\Users\\ATeg\\Downloads\\libwebp-1.2.2-windows-x64\\bin\\dwebp.exe', '-o', '-', '--', '-']
" ".join(dx)
#os.mkdir("temp-directory")

for frame in frames:
    frameNumber = frame['No']
    command = [webpmuxPath, "-get", "frame", str(frameNumber), f"\"{sourceFile}\"", "-o", "-", "|", dwebpPath, "-o", "-", "--", "-"]
    pngData = subprocess.check_output(command)
    
    with open(os.path.join("temp-directory",f"frame-{frameNumber}.png"), 'wb') as handle:
        handle.write(pngdata)
dx = ['C:\\Users\\ATeg\\Downloads\\libwebp-1.2.2-windows-x64\\bin\\webpmux.exe', '-get', 'frame', '1', '"C:\\Users\\ATeg\\Pictures\\Saved Pictures\\Gasket\\gasket-1.webp"', '-o', '-', '|', 'C:\\Users\\ATeg\\Downloads\\libwebp-1.2.2-windows-x64\\bin\\dwebp.exe', '-o', '-', '--', '-']
print(" ".join(dx))
#os.mkdir("temp-directory")

for frame in frames:
    frameNumber = frame['No']
    command = [webpmuxPath, "-get", "frame", str(frameNumber), f"\"{sourceFile}\"", "-o", "-", "|", dwebpPath, "-o", "-", "--", "-"]
    pngData = subprocess.check_output(command)
    
    with open(os.path.join("temp-directory",f"frame-{frameNumber}.png"), 'wb') as handle:
        handle.write(pngdata)
#os.mkdir("temp-directory")

for frame in frames:
    frameNumber = frame['No']
    command = [webpmuxPath, "-get", "frame", str(frameNumber), f"\"{sourceFile}\"", "-o", "-"]
    pngData = subprocess.check_output(command)
    
    with open(os.path.join("temp-directory",f"frame-{frameNumber}.png"), 'wb') as handle:
        handle.write(pngdata)
#os.mkdir("temp-directory")

for frame in frames:
    frameNumber = frame['No']
    command = [webpmuxPath, "-get", "frame", str(frameNumber), sourceFile, "-o", "-"]
    pngData = subprocess.check_output(command)
    
    with open(os.path.join("temp-directory",f"frame-{frameNumber}.png"), 'wb') as handle:
        handle.write(pngdata)
#os.mkdir("temp-directory")

for frame in frames:
    frameNumber = frame['No']
    command = [webpmuxPath, "-get", "frame", str(frameNumber), sourceFile, "-o", "-"]
    pngData = subprocess.check_output(command)
    
    with open(os.path.join("temp-directory",f"frame-{frameNumber}.png"), 'wb') as handle:
        handle.write(pngData)
#os.mkdir("temp-directory")

for frame in frames:
    frameNumber = frame['No']
    animationFrame_to_image__command = [webpmuxPath, "-get", "frame", str(frameNumber), sourceFile, "-o", "-"]    
    webpImageData = subprocess.check_output(command)
    
    webp_to_png_command = [dwebpPath, "-o", "-", "--", "-"]
    proc = subprocess.Popen(command, stdin=subprocess.PIPE)
    stdout, stderr = proc.communicate(webpImageData)

    print("DWebp-", stderr)
    
    with open(os.path.join("temp-directory",f"frame-{frameNumber}.png"), 'wb') as handle:
        handle.write(stdout)
#os.mkdir("temp-directory")

for frame in frames:
    frameNumber = frame['No']
    animationFrame_to_image__command = [webpmuxPath, "-get", "frame", str(frameNumber), sourceFile, "-o", "-"]    
    webpImageData = subprocess.check_output(command)
    
    webp_to_png_command = [dwebpPath, "-o", "-", "--", "-"]
    proc = subprocess.Popen(webp_to_png_command, stdin=subprocess.PIPE)
    stdout, stderr = proc.communicate(webpImageData)

    print("DWebp-", stderr)
    
    with open(os.path.join("temp-directory",f"frame-{frameNumber}.png"), 'wb') as handle:
        handle.write(stdout)
#os.mkdir("temp-directory")

for frame in frames:
    frameNumber = frame['No']
    animationFrame_to_image__command = [webpmuxPath, "-get", "frame", str(frameNumber), sourceFile, "-o", "-"]    
    webpImageData = subprocess.check_output(command)
    
    outputPngPath = os.path.join("temp-directory",f"frame-{frameNumber}.png")
    
    webp_to_png_command = [dwebpPath, "-o", outputPngPath, "--", "-"]
    proc = subprocess.Popen(webp_to_png_command, stdin=subprocess.PIPE)
    stdout, stderr = proc.communicate(webpImageData)

    print("DWebp-", stderr)
    
#os.mkdir("temp-directory")

for frame in frames:
    frameNumber = frame['No']
    animationFrame_to_image__command = [webpmuxPath, "-get", "frame", str(frameNumber), sourceFile, "-o", "-"]    
    webpImageData = subprocess.check_output(command)
    
    outputWebpPath = os.path.join("temp-directory",f"frame-{frameNumber}.webp")

    with open(outputWebpPath, 'wb') as handle:
        handle.write(webpImageData)
        
#os.mkdir("temp-directory")

for frame in frames:
    frameNumber = frame['No']
    print(frameNumber)
    continue
    animationFrame_to_image__command = [webpmuxPath, "-get", "frame", str(frameNumber), sourceFile, "-o", "-"]    
    webpImageData = subprocess.check_output(command)
    
    outputWebpPath = os.path.join("temp-directory",f"frame-{frameNumber}.webp")

    with open(outputWebpPath, 'wb') as handle:
        handle.write(webpImageData)
        
    
    
    
#os.mkdir("temp-directory")

for frame in frames:
    frameNumber = frame['No']
    animationFrame_to_image__command = [webpmuxPath, "-get", "frame", str(frameNumber), sourceFile, "-o", "-"]    
    webpImageData = subprocess.check_output(animationFrame_to_image__command)
    
    outputWebpPath = os.path.join("temp-directory",f"frame-{frameNumber}.webp")

    with open(outputWebpPath, 'wb') as handle:
        handle.write(webpImageData)
        
    
    
    
#os.mkdir("temp-directory")

for frame in frames:
    frameNumber = frame['No']
    animationFrame_to_image__command = [webpmuxPath, "-get", "frame", str(frameNumber), sourceFile, "-o", "-"]    
    webpImageData = subprocess.check_output(animationFrame_to_image__command)
    
    webp_to_png_command = [dwebpPath, "-o", "-", "--", "-"]
    proc = subprocess.Popen(command, stdin=subprocess.PIPE)
    stdout, stderr = proc.communicate(webpImageData)

    print("DWebp-", stderr)
    
    with open(os.path.join("temp-directory",f"frame-{frameNumber}.png"), 'wb') as handle:
        handle.write(stdout)
#os.mkdir("temp-directory")

for frame in frames:
    frameNumber = frame['No']
    animationFrame_to_image__command = [webpmuxPath, "-get", "frame", str(frameNumber), sourceFile, "-o", "-"]    
    webpImageData = subprocess.check_output(animationFrame_to_image__command)
    
    webp_to_png_command = [dwebpPath, "-o", "-", "--", "-"]
    proc = subprocess.Popen(webp_to_png_command, stdin=subprocess.PIPE)
    stdout, stderr = proc.communicate(webpImageData)

    print("DWebp-", stderr)
    
    with open(os.path.join("temp-directory",f"frame-{frameNumber}.png"), 'wb') as handle:
        handle.write(stdout)
#os.mkdir("temp-directory")

for frame in frames:
    frameNumber = frame['No']
    animationFrame_to_image__command = [webpmuxPath, "-get", "frame", str(frameNumber), sourceFile, "-o", "-"]    
    webpImageData = subprocess.check_output(animationFrame_to_image__command)
    
    webp_to_png_command = [dwebpPath, "-o", "-", "--", "-"]
    proc = subprocess.Popen(webp_to_png_command, stdin=subprocess.PIPE)
    stdout, stderr = proc.communicate(webpImageData)

    print("ERR:DWebp-", stderr)
    print("STD:DWebp-", stdout)
#os.mkdir("temp-directory")

for frame in frames:
    frameNumber = frame['No']
    animationFrame_to_image__command = [webpmuxPath, "-get", "frame", str(frameNumber), sourceFile, "-o", "-"]    
    webpImageData = subprocess.check_output(animationFrame_to_image__command)
    
    webp_to_png_command = [dwebpPath, "-o", "-", "--", "-"]
    proc = subprocess.Popen(webp_to_png_command, stdin=subprocess.PIPE)
    stdout, stderr = proc.communicate(webpImageData)

    print("ERR:DWebp-", stderr)
    print("STD:DWebp-", stdout)
    break
#os.mkdir("temp-directory")

for frame in frames:
    frameNumber = frame['No']
    animationFrame_to_image__command = [webpmuxPath, "-get", "frame", str(frameNumber), sourceFile, "-o", "-"]    
    webpImageData = subprocess.check_output(animationFrame_to_image__command)
    
    webp_to_png_command = [dwebpPath, "-o", "-", "--", "-"]
    proc = subprocess.Popen(webp_to_png_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout, stderr = proc.communicate(webpImageData)

    print("ERR:DWebp-", stderr)
    print("STD:DWebp-", stdout)
    break
#os.mkdir("temp-directory")

for frame in frames:
    frameNumber = frame['No']
    animationFrame_to_image__command = [webpmuxPath, "-get", "frame", str(frameNumber), sourceFile, "-o", "-"]    
    webpImageData = subprocess.check_output(animationFrame_to_image__command)
    
    webp_to_png_command = [dwebpPath, "-o", "-", "--", "-"]
    proc = subprocess.Popen(webp_to_png_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout, stderr = proc.communicate(webpImageData)

    print("DWebp-", stderr)
    
    with open(os.path.join("temp-directory",f"frame-{frameNumber}.png"), 'wb') as handle:
        handle.write(stdout)
#os.mkdir("temp-directory")

for frame in frames:
    frameNumber = frame['No']
    animationFrame_to_image__command = [webpmuxPath, "-get", "frame", str(frameNumber), sourceFile, "-o", "-"]    
    webpImageData = subprocess.check_output(animationFrame_to_image__command)
    
    webp_to_png_command = [dwebpPath, "-o", "-", "--", "-"]
    proc = subprocess.Popen(webp_to_png_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout, _stderr = proc.communicate(webpImageData)
    
    with open(os.path.join("temp-directory",f"frame-{frameNumber}.png"), 'wb') as handle:
        handle.write(stdout)
gifski_command = [gifski_path, "
gifski_path = os.path.join("..", "gifski.exe") #--fps 20 --quality 90 --output
input_png_files = os.path.join("temp-directory", "frame-*.png")
gifski_command = [gifski_path, input_png_files, "--fps", "20", "--quality", "90", "--output", "-"]

gifski_output = subprocess.check_output(gifski_command)
with open("gasket-1.gif", 'wb') as handle:
    handle.write(gifski_output)
    
get_ipython().run_line_magic('save', '"webp_to_gif" 0-46')
