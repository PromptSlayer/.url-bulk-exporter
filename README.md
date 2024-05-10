# .url-bulk-exporter

A Python program that converts .url files in a directory into an importable HTML file for potential use in a web browser context.
This is essentially a script that takes a path and writes target files metadata into a valid, importable HTML format.
It is a basic utility made for personal use, thus Windows-only.

## Use of the Utility

1. Make sure to download and install latest version of Python3
2. Clone the repository:
```bash
   git clone https://github.com/PromptSlayer/.url-bulk-exporter
```
3. Open a Terminal with administrative privileges (Powershell, CMD).
4. Go to the Script's location of SFE.py
Example;
```bash
   cd C:\Windows\SFE\Main
```
5. Run the script using python 
```bash
   python sfe.py
```
``bash
   python .\sfe.py
```
6. Enter valid prompted path and file name for the target .url files location.
Path example;
```bash
   C:\Windows\your-shortcuts-folder
```
7. Enjoy your generated file!


## Additional Info

The script can take in any sort of path, it will write all directories and .url files if any. When encountering unsupported file types or file extensions, it will simply ignore them. 
While a folder dedicated solely for Shortcut storing purposes is the most convenient, above statement means it will also export urls in a folder that may contain files of unrelated types.
