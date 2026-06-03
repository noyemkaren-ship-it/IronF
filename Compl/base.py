import os
from util import base_css

def baseCSS():
    global base_css
    with open("src/css/style.css", "w") as file:
        file.write(base_css)

def create_html_start():
    with open("src/index.html", "w") as file:
        file.write('<!DOCTYPE html>\n')
        file.write('<html lang="ru">\n')
        file.write("<head>\n")
        file.write('    <meta charset="UTF-8">\n')
        file.write('    <link rel="stylesheet" href="css/style.css">\n')
        file.write('    <meta name="viewport" content="width=device-width, initial-scale=1.0">')

def create_directories():
    os.makedirs("src", exist_ok=True)
    os.makedirs("src/css", exist_ok=True)
    os.makedirs("src/scripts", exist_ok=True)

def appendf(filename: str, line: str):
    with open(filename, "a") as file:
        file.write(line + "\n")