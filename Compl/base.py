import os
from Compl.util import base_css

def baseCSS():
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

def css_logic(eline):
    if (eline.startswith("talign: ")):
        appendf("src/css/style.css", f"    text-align: {eline[8:].strip()}")
    elif (eline.startswith("fsize: ")):
        appendf("src/css/style.css", f"    font-size: {eline[7:].strip()};")
    else:
        appendf("src/css/style.css", eline)

def create_js_clasic():
    with open("src/scripts/main.js", "w") as i:
        i.write("// IronF Simplified JavaScript\n")
        i.write("// Эти функции доступны сразу, ничего подключать не нужно!\n\n")
        i.write("function put(text) {\n")
        i.write("    console.log(text);\n")
        i.write("}\n\n")
        i.write("function print(text) {\n")
        i.write("    alert(text);\n")
        i.write("}\n\n")
        i.write("function getElement(id) {\n")
        i.write("    return document.getElementById(id);\n")
        i.write("}\n\n")
        i.write("function setText(id, text) {\n")
        i.write("    document.getElementById(id).innerText = text;\n")
        i.write("}\n\n")
        i.write("// Приветствие при загрузке\n")
        i.write("put('Проект создан на IronF Framework');\n")
        i.write("print('Добро пожаловать в IronF!');\n")