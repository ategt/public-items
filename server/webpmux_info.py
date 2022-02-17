# coding: utf-8

import subprocess
import json
import os
import re

HEADER_PATTERN = re.compile(r"canvas\s+size:\s+(?P<width>\d+)\s+x\s+(?P<height>\d+)\nfeatures\s+present:\s+(?P<features>[\w\s]+)\nbackground\s+color\s+:\s+(?P<bgColor>[\d\w]+)\s+loop\s+count\s+:\s+(?P<loopCount>\d+)\nnumber\s+of\s+frames:\s+(?P<numberOfFrames>\d+)", re.IGNORECASE|re.DOTALL|re.MULTILINE)

FRAME_NUMBER_PATTERN = re.compile(r"\A\d+\:\Z")
NUMBER_PATTERN = re.compile(r"\A\d+\Z")
BOOL_PATTERN = re.compile(r"\A(?:yes|no)\Z", re.IGNORECASE)

# libwebp_directory = r"C:\Users\ATeg\Downloads\libwebp-1.2.2-windows-x64"
# webpmuxPath = os.path.join(libwebp_directory, "bin", "webpmux.exe")
# sourceFile = r"C:\Users\ATeg\Pictures\Saved Pictures\Gasket\gasket-1.webp"

class WebpInfo(object):
    """
        Wrapper for webpmux.exe to generate info for webp files.
    """
    def __init__(self, webpmuxPath):
        super(WebpInfo, self).__init__()
        self.webpmuxPath = webpmuxPath
    
    def getInfo(self, webpPath):
        lines = self._callWebpmux(webpPath)
        metaInfo = self._parseMetaHeader(lines)
        metaInfo['frames'] = self._parseFrameInfo(lines)

        return metaInfo

    def _callWebpmux(self, webpPath):    
        command = [self.webpmuxPath, "-info", webpPath]
        resultOutput = subprocess.check_output(command, encoding='UTF-8')

        lines = [value.strip() for value in resultOutput.strip().split("\n")]

        return lines

    def _parseMetaHeader(self, lines):
        match = HEADER_PATTERN.search("\n".join(lines[:4]))
        headerInfo = match.groupdict()

        for key, value in headerInfo.items():
            if NUMBER_PATTERN.match(value):
                headerInfo[key] = int(value)
        
        return headerInfo                

    def _parseFrameInfo(self, lines):
        frameHeader = self._parseFrameHeader(lines[4])

        return [self._parseFrame(line, frameHeader) for line in lines[5:]]

    def _parseFrameHeader(self, frameHeaderLine):
        frameAttrs = frameHeaderLine.split()

        if frameAttrs[0] == 'No.:':
            frameAttrs[0] = 'No'

        return frameAttrs

    def _parseFrame(self, line, columns):
        items = line.split()

        try:   
            if FRAME_NUMBER_PATTERN.match(items[0]):
                items[0] = items[0].replace(":","")
                
            for index, cell in enumerate(items):
                if NUMBER_PATTERN.match(cell):
                    items[index] = int(cell)

                if BOOL_PATTERN.match(cell):
                    items[index] = cell == "yes"
                    
            return dict(zip(columns, items))
        except IndexError:
            print(line)
            raise