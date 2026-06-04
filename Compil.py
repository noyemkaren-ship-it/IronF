import os
body = False
css_err = False
from Compl.base import baseCSS, create_directories, appendf, create_basic_html, css_logic, create_js_clasic
from Compl.util import *

create_directories()
create_js_clasic()

with open("main.html", "r") as err:
    for line in err:
        if (line.startswith("endhtml")):
            body = True
        elif (line.startswith("css")):
            css_err = True

with open("main.html", "r") as file:
    if (body == False):
        print("НАШЕЛ ОШИБКИ В КОДЕ НЕТУ endlhtml")
        exit()
    elif (css_err == False):
        print("НАШЕЛ ОШИБКУ, НЕТ css НУ ХОТЯБЫ ДОБАВЬТЕ css и далее basic")
        exit()
    
    del body
    del css_err

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
            create_basic_html(name)
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
            with open(line[7:], "r") as imp:
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

            
