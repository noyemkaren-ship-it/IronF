import os
from Compl.base import baseCSS, create_directories, appendf, create_basic_html, css_logic, create_js_clasic
from Compl.util import *
create_directories()
create_js_clasic()
body = False
css_err = False
html_err = False
print("\033[32mСтарт компилятора\033[0m")

with open("main.html", "r") as err:
    for line in err:
        if (line.startswith("endhtml")):
            body = True
        elif (line.startswith("css")):
            css_err = True
        elif (line.startswith("html")):
            html_err = True
    if (body == False):
        print("\033[33m НАШЕЛ ОШИБКИ В КОДЕ НЕТУ endlhtml\033[0m")
        exit()
    elif (css_err == False):
        print("\033[33m НАШЕЛ ОШИБКУ, НЕТ css НУ ХОТЯБЫ ДОБАВЬТЕ css и далее basic\033[0m")
        exit()
    elif (html_err == False):
        print("\033[33m ПОЧЕМУ НЕТУ html В ФАЙЛЕ\033[0m")

with open("main.html", "r") as file:
    del body
    del css_err
    del html_err

    for line in file:
        if (line.startswith("Imkdir ")):
            os.makedirs(line[7:])
            continue
        elif (line.startswith("html")):
            html = True
            css = False
            meta = False
            continue
        elif (line.startswith("jscript")):
            script = True
            html = False
            css = False
            meta = False
            continue
        elif (line.startswith("endhtml")):
            html = False
            appendf('src/index.html', "</body>\n")
            appendf('src/index.html', "</html>\n")
            continue
        elif (line.startswith("meta ")):
            name = line[5:]
            create_basic_html(name.strip())
            meta = True
            continue
        elif (line.startswith("css")):
            css = True
            continue
        elif (line.startswith("basic")) and css == True:
            css = False
            baseCSS()
            continue
        elif (line.startswith("import ")) and css == True:
            with open(line[7:].strip(), "r") as imp:
                css = False
                for eline in imp:
                    css_logic(eline)
        elif (css == True):
            css_logic(line)
            continue
        elif (html == True) and (meta == True):
            appendf("src/index.html", line)
            continue
        elif (script == True):
            appendf("src/scripts/main.js", line)
            continue

print("\033[32mВсе прошло хорошо\033[0m")

