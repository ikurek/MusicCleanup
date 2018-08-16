#!/usr/local/bin/python3
import sys
import os

scannedFiles = 0
removedFiles = 0
scannedFolders = 0
removedFolders = 0

def removeFileIfBad(file):
    global scannedFiles, removedFiles
    scannedFiles += 1
    if file.lower().endswith(('.png', '.jpg', '.jpeg', '.txt', '.nfo', '.info', '.m3u', '.pls', '.svg', '.torrent', '.part', '.ini', '.ds_store')):
        removedFiles += 1
        os.remove(file)
        print("            ==> Removed file {}".format(file))
    return

def removeFolderIfEmpty(folder):
    global scannedFolders, removedFolders
    scannedFolders += 1
    if os.path.isdir and os.listdir(os.path.abspath(folder)) == []:
        removedFolders += 1
        os.rmdir(folder)
        print("            ==> Removed folder {}".format(os.path.basename(folder)))
    return 

# Check arguments
if len(sys.argv) != 2:
    print("==> Please specify root as an argument!")
    print("==> Exiting...")
    exit()

# Continue if arg is okay
else:
    startingDir = os.path.abspath(sys.argv[1])
    print("==> Script running in {}".format(startingDir))

    # Find all subdirectories in given folder
    dirs = [d for d in os.listdir(startingDir) if os.path.isdir(os.path.join(startingDir, d))]
    if len(dirs) == 0:
        print("==> No directories found, exiting...")
        exit()
    else:
        print("==> {} directories found".format(len(dirs)))

    # Iterate over all artists
    for artistDir in dirs:
        print("    ==> {}:".format(artistDir))

        # Walk trough every file inside artist
        for albumDir in os.listdir(os.path.join(startingDir, artistDir)):
            
            # If file is found inside album folder, validate it
            if os.path.isfile(os.path.join(startingDir, artistDir, albumDir)):
                removeFileIfBad(os.path.join(startingDir, artistDir, albumDir))
            
            # If directory is found, check it for files
            else:
                for root, dirs, files in os.walk(os.path.join(startingDir, artistDir, albumDir)):
                    print("        ==> {}:".format(os.path.basename(root)))
                    
                    # Validate all files found inside subdirs
                    for file in files:
                        removeFileIfBad(os.path.join(root, file))

                    # Validate if current folder is empty
                    removeFolderIfEmpty(root)
    
    
    print("==> Cleanup finished!")
    print("==> Scanned {} files, {} removed".format(scannedFiles, removedFiles))
    print("==> Scanned {} folders, {} removed".format(scannedFolders, removedFolders))
