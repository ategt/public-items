from archive_extractor import ArchiveExtractor
import sys

def main():
    if len(sys.argv) == 3:
        ar = ArchiveExtractor(baseDirectory = sys.argv[2])
        count = ar.reconstitute(archiveFileName = sys.argv[1])
        print(count, "files processed.")
    else:
        print("Usage: python archive_extractor_runner.py Archive.zip baseDirectory")

if __name__ == "__main__":
    main()