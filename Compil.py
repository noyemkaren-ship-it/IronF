import os
from Compl.base import *
from Compl.util import *
create_directories()
create_js_clasic()
body = False
css_err = False
html_err = False
btn = False
is_fun_name = False
btn_text = ""
fun_name = ""
game = False
two = False
print("\033[32mСтарт компилятора\033[0m")


with open("main.html", "r") as err:
    for line in err:
        if (line.startswith("endhtml")):
            body = True
        elif (line.stript().startswith("function")):
            if ( "(" in line):
                pass 
            else:
                yprint("ТАК КАЖЕТСЯ ИЛИ ВЫ В function ЗАБЫЛИ СКОБКИ")
        elif ("<h1>" in line) and ("</h1>" in line):
            bprinte("ЭТО НЕ ОШИБКА, НО ЛУЧШЕ ВМЕСТО <h1> текст </h1> писать:")
            bprinte("<h1>")
            bprinte("   Текст")
            bprinte("</h1>")
        elif (line.startswith("css")):
            css_err = True
        elif (line.startswith("meta")):
            mata_err = True
        elif (line.startswith("html")):
            html_err = True
        elif ('"' in line) and ("'" in line):
            bprinte("Вижу кавычки надеюсь что вы не забыли закрыть их ''")
        elif (line.startswith("<P")):
            yprint("Найдена ошибка в html почему то написано <P> а не <p>")
            exit()
        elif (line.strip().startswith("put(")):
            if (line.strip().endswith(";")):
                pass
            else:
                yprint("КАЖЕТСЯ Я НАШЕЛ ОШИБКУ В put В КОНЦЕ НЕТУ ;, НО БЛОКИРОВАТЬ НЕ БУДУ ВОЗМОЖНО Я, ЧТО ТО НЕ ТАК ПОНЯЛ")
        elif (line.strip().startswith("let")) or (line.strip().startswith("var")):
            if (line.strip().endswith(";")):
                pass 
            else:
                yprint("Кажется вы забили ; в обьявлении переменных используя var или let я их не различаю, простите:)")
        elif (line.startswith("jscripts")):
            yprint("Пишется jscript, а не jscripts")
            exit()
        elif (line.startswith("<H1")):
            yprint("Найдена ошибка в html написано <H1> вместо <h1>")
            exit()
        elif (line.startswith("<Big")):
            yprint("Найдена ошибка в html написано <Big вместо <big")
            exit()
        elif (line.strip().startswith("pipint")):
            yprint("Найдине КРИТИЧЕСКАЯ ОШИБКА пишется print а не pipint")
            exit()
        elif (line.startswith("fanction")):
            yprint("КРИТИЧЕСКАЯ ОШИБКА, НАПИСАНО fanction, а не function")
            exit()
        elif (line.startswith("console.log")):
            yprint("Ошибка не критичная, но лучше вместо console.log используй более простой put")
        elif (line.startswith("alert")):
            yprint("Ошибка не критическая, но лучше вместо alert используй print потому что так принято, НО сайт все равно заработает")
        elif (line.startswith("<p>")) and (line.strip().endswith("/p>")):
            bprinte("Найдена не желательная строчка это не ошибка ,но дело в том что в коде для красоты кода нужно писать так <p> и остальные теги")
            bprinte("<p>")
            bprinte("   текст")
            bprinte("</p>")
            bprinte("Надеюсь вы запомнили!")
        elif (line.strip().startswith("print(")) or ("print(" in line.strip()):
            if (line.strip().endswith(");")):
                pass
            else:
                yprint("ВНИМАНИЯ У print В КОНЦЕ ОТСУСТВОЕТ ;")
                exit()
        elif (line.startswith("<h1 >")):
            bprinte("Не ошипка НО почему у теюя <h1 > почему тут пусто скорее всегораньше был какой то параметр у h1 но влюбом случае снизу написал как исправить")
            bprinte("<h1 > -> <h1>")
    if (body == False):
        yprint("НАШЕЛ ОШИБКИ В КОДЕ НЕТУ endhtml")
        exit()
    elif (css_err == False):
        print("НАШЕЛ ОШИБКУ, НЕТ css НУ ХОТЯБЫ ДОБАВЬТЕ css и далее basic")
        exit()
    elif (html_err == False):
        yprint("ПОЧЕМУ НЕТУ html В ФАЙЛЕ")
    elif (mata_err == False):
        yprint("Отсуствует meta !!")

with open("main.html", "r") as file:
    del body, css_err, html_err, mata_err
    for line in file:
        if line.startswith("game"):
            print("НАЙДЕНА ПЕРВАЯ СТРОКА game ПЕРЕКЛОЮЧАЮ В РЕЖИМ СОЗДАНИЯ ИГР")
            game = True
            break
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
        elif (line.startswith("Pbasic ")) and css == True:
            css = False
            line = line[7:]
            photoBaseCSS(line)
            continue
        elif (line.startswith("import ")) and css == True:
            with open(line[7:].strip(), "r") as imp:
                css = False
                for eline in imp:
                    css_logic(eline)
        elif (css == True):
            css_logic(line)
            continue
        elif (line.startswith("btn ")):
            btn_text = line[4:].strip()
            is_fun_name = True
            continue
        elif (is_fun_name == True):
            fun_name = line.strip()
            create_button(btn_text, fun_name)
            is_fun_name = False
            continue
        elif (html == True) and (meta == True):
            appendf("src/index.html", line)
            continue
        elif (script == True):
            appendf("src/scripts/main.js", line)
            continue


if game:
    print("\033[32mПроцесс начался, важно не забывайте все картинки и sprite перекидывать в папку static\033[0m")
    with open("main.html", "r") as file:
        if (line.startswith("csss")):
            print("Начинию скан CSS")
    

print("\033[32mВсе прошло хорошо\033[0m")