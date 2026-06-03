from Compl.base import baseCSS, create_directories, appendf, create_html_start, css_logic

create_directories()

css = False
html = False
script = False
meta = False
body = False
css_err = False
name = ""

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

    for line in file:
        if (line.startswith("html")):
            html = True
            css = False
            continue
        if (line.startswith("jscript")):
            script = True
            html = False
            css = False
            continue
        if (line.startswith("endhtml")):
            html = False
            appendf('src/index.html', "</body>\n")
            appendf('src/index.html', "</html>\n")
            continue
        elif (line.startswith("meta ")):
            name = line[5:]
            create_html_start()
            appendf("src/index.html", f"    <title>{line.strip()}</title>\n")
            appendf('src/index.html', '<script src="scripts/main.js"></script>\n')
            appendf('src/index.html', "</head>\n")
            appendf('src/index.html', "<body>")
            meta = True
            continue
        if (line.startswith("css")):
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

            
