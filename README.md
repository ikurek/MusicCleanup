# MusicCleanup

## Why?
Ever copied an album to a phone and had to deal with cover arts being added to gallery, old playlists being registered inside music player, etc? Arw You annoyed by random *.txt files being added to Your music? I was, so I fixed it.

## How does it work?
This script runs through You music collection and removes all unnecesary files, empty directories and all the useless stuff. Currently, deleted file formats are:
```
# Random text files
*.nfo
*.txt
*.info

# Covers and graphics
*.jpg
*.jpeg
*.png
*.svg

# I have my own playlists, i don't need this
*.m3u
*.pls

# Remember, piracy is a theft
*.torrent
*.part

# System stuff
.ini
.DS_Store
```

## Folder structure
This script assumes that music is stored inside folders this way:
```
Root:
    ==> Artist 1:
        ==> Album 1:
            ==> Track 1 / Subfolder 1
            ==> Track 2 / Subfolder 2
            .
            ==> Track N / Subfolder N
        ==> Album 2
        .
        ==> Album N
    ==> Artist 2
    .
    ==> Artist N
```

## Usage
Simply run:
```
python3 musicCleanup.py <root directory>
```