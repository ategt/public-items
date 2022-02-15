# coding: utf-8

import subprocess
import requests
import json
import os

class ArchiveExtractor(object):
    """
        Reconstitutes a file directory sturcture from a saveUrls archive.
        @arg baseDirectory - The directory that ArchiveExtractor expects to find archives in.
        @arg extractorPath - Path to 7zip executable.

        Example:
        >>> # Creates a "NxnnUIy" folder in Downloads from "NxnnUIy.zip" archive.
        >>> ar = ArchiveExtractor(baseDirectory = "C:\\Users\\ATeg\\Downloads")
        >>> ar.reconstitute(archiveName = "NxnnUIy.zip")
    """
    def __init__(self, baseDirectory, extractorPath = "C:\\Program Files\\7-Zip\\7z.exe", defaultExtension = 'jpg'):
        super(ArchiveExtractor, self).__init__()
        self.baseDirectory = baseDirectory
        self.extractorPath = extractorPath
        self.logPath = 'logfile.log'
        self.defaultExtension = defaultExtension

    def setDefaultExtension(self, extension):
        self.defaultExtension = extension

    def extract(self, archiveFileName, destinationDirectory = None):
        """
            Creates a directory and extracts archive into it.
                Will raise an exception if extration fails.
            @param {str} archiveFileName - probably something like "archive.zip"
                expects the extension to be included, only supports zip at the moment
            @param {str} [destinationDirectory] - Directory to create, will be infered from archive name if empty.
            @returns {str} - Directory that was created by this method.
        """
        if not destinationDirectory:
            destinationDirectory = os.path.join(self.baseDirectory, archiveFileName.replace(".zip", ""))

        if os.path.exists(destinationDirectory):
            raise Exception(f"Destination Directory already exists - {destinationDirectory}")

        with open(os.devnull, 'w') as FNULL, open(self.logPath, 'w') as logfile:  # log to here for output ignoring
            command = [self.extractorPath, 'x', os.path.join(self.baseDirectory, archiveFileName), f'-o{destinationDirectory}', "*"]
            print("Running Command", command)
            result_proc = subprocess.call(command, stdout=logfile, stderr=subprocess.STDOUT)  # Ignore output

        if result_proc:
            raise Exception("Archive Extraction Failed - See Log For Details")
        else:
            print('Archive Extraction Succeeded')

        return destinationDirectory

    def printLog(self):
        """ Calls print on the contents of the extraction log file. """
        with open(self.logPath,"r") as handle:
            print(handle.read())

    def restoreNames(self, directory):
        """
            Expects directory to contain a file called sources.json, which is stringifyed
                json of a list of dicts containing 'url' and 'uuid' keys.  
            @returns {int} - Number of files processed.
        """
        files = os.listdir(directory)

        with open(os.path.join(directory, "sources.json"), 'r') as handle:
            sourceData = json.load(handle)

        for sourceDatum in sourceData:
            uuid = sourceDatum['uuid']
            url = sourceDatum['url']
            name = url.split("/")[-1]

            fullDestinationPath = os.path.join(directory, name)

            if not os.path.exists(fullDestinationPath):
                os.rename(os.path.join(directory, uuid), fullDestinationPath)
            else:
                os.rename(os.path.join(directory, uuid), os.path.join(directory, f"{uuid}.{self.defaultExtension}"))

        return len(sourceData)

    def reconstitute(self, archiveFileName, destinationDirectory = None):
        """
            Runs extraction and then restoreNames methods.
            See those methods for more detailed help.
        """
        directory = self.extract(archiveFileName = archiveFileName, destinationDirectory = destinationDirectory)
        return self.restoreNames(directory)