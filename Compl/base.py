import os
from Compl.util import base_css, base_css1, base_css2

def baseCSS():
    with open("src/css/style.css", "w") as file:
        file.write(base_css)

def photoBaseCSS(photoName: str):
    with open("/src/css/style.css", "w") as file:
        file.write(base_css2)
        file.write(f"   background-image: url('{photoBaseCSS}');\n")
        file.write(base_css1)

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

def yprint(text):
    print("\033[33mWARNING\033[0m")
    print(f"\033[33m{text}\033[0m")
    print("\033[33mWARNING\033[0m")

def create_button(text: str, fun: str):
    # Убираем скобки если они есть в имени функции
    clean_fun = fun.strip().rstrip('()')
    appendf("src/index.html", f'<button onclick={clean_fun}()>{text}</button>')

def create_js_clasic():
    with open("src/scripts/main.js", "w") as i:
        i.write('"use strict";\n')
        i.write('function put(...a){console.log("[IronF]",...a)}\n')
        i.write('function print(t){alert(String(t))}\n')
        i.write('function ask(t,d=""){return prompt(String(t),d)}\n')
        i.write('function gid(id){return document.getElementById(id)}\n')
        i.write('function gq(s){return document.querySelector(s)}\n')
        i.write('function gqa(s){return document.querySelectorAll(s)}\n')
        i.write('function txt(id,v){let e=gid(id);if(e)e.innerText=v}\n')
        i.write('function html(id,v){let e=gid(id);if(e)e.innerHTML=v}\n')
        i.write('function val(id,v){let e=gid(id);if(e){if(v!==undefined)e.value=v;return e.value}}\n')
        i.write('function addC(id,c){let e=gid(id);if(e)e.classList.add(c)}\n')
        i.write('function remC(id,c){let e=gid(id);if(e)e.classList.remove(c)}\n')
        i.write('function togC(id,c){let e=gid(id);if(e)e.classList.toggle(c)}\n')
        i.write('function hide(id){let e=gid(id);if(e)e.style.display="none"}\n')
        i.write('function show(id,d="block"){let e=gid(id);if(e)e.style.display=d}\n')
        i.write('function el(tag,a={},t=""){let e=document.createElement(tag);for(let[k,v]of Object.entries(a)){if(k=="class")e.className=v;else if(k=="style"&&typeof v=="object")Object.assign(e.style,v);else e.setAttribute(k,v)}if(t)e.innerText=t;return e}\n')
        i.write('function app(parent,child){let p=typeof parent=="string"?gid(parent):parent;if(p)p.appendChild(child)}\n')
        i.write('function r(url,m,body=null,h={}){let o={method:m,headers:{"Content-Type":"application/json",...h}};if(body&&m!="GET")o.body=typeof body=="string"?body:JSON.stringify(body);return fetch(url,o).then(r=>r.json().then(d=>({ok:r.ok,status:r.status,data:d})).catch(()=>({ok:r.ok,status:r.status,data:null}))).catch(e=>({ok:false,status:0,data:null,error:e.message}))}\n')
        i.write('function rget(url,h={}){return r(url,"GET",null,h)}\n')
        i.write('function rpost(url,body,h={}){return r(url,"POST",body,h)}\n')
        i.write('function rput(url,body,h={}){return r(url,"PUT",body,h)}\n')
        i.write('function rdel(url,h={}){return r(url,"DELETE",null,h)}\n')
        i.write('function store(k,v){if(v!==undefined){try{localStorage.setItem(k,typeof v=="object"?JSON.stringify(v):v)}catch(e){}}else{let d=localStorage.getItem(k);try{return JSON.parse(d)}catch{return d}}}\n')
        i.write('function storeDel(k){localStorage.removeItem(k)}\n')
        i.write('function storeClear(){localStorage.clear()}\n')
        i.write('function wait(ms){return new Promise(r=>setTimeout(r,ms))}\n')
        i.write('function rand(min,max){return Math.floor(Math.random()*(max-min+1))+min}\n')
        i.write('function isEmpty(v){return v===null||v===undefined||(typeof v=="string"&&v.trim()==="")||(Array.isArray(v)&&v.length===0)||(typeof v=="object"&&Object.keys(v).length===0)}\n')
        i.write('function onReady(fn){document.readyState=="loading"?document.addEventListener("DOMContentLoaded",fn):fn()}\n')
        i.write('function onClick(id,fn){let e=gid(id);if(e)e.addEventListener("click",fn)}\n')
        i.write('function setCSS(id,s){let e=gid(id);if(e)Object.assign(e.style,s)}\n')
        i.write('function getAttr(id,a){let e=gid(id);return e?e.getAttribute(a):null}\n')
        i.write('function setAttr(id,a,v){let e=gid(id);if(e)e.setAttribute(a,v)}\n')
        i.write('function remAttr(id,a){let e=gid(id);if(e)e.removeAttribute(a)}\n')
        i.write('put("IronF loaded")\n')
        i.write("put('Проект создан на IronF Framework');\n")

def create_basic_html(line):
    create_html_start()
    appendf("src/index.html", f"    <title>{line.strip()}</title>\n")
    appendf('src/index.html', '<script src="scripts/main.js"></script>\n')
    appendf('src/index.html', "</head>\n")
    appendf('src/index.html', "<body>")