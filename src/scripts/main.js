"use strict";
function put(...a){console.log("[IronF]",...a)}
function print(t){alert(String(t))}
function ask(t,d=""){return prompt(String(t),d)}
function gid(id){return document.getElementById(id)}
function gq(s){return document.querySelector(s)}
function gqa(s){return document.querySelectorAll(s)}
function txt(id,v){let e=gid(id);if(e)e.innerText=v}
function html(id,v){let e=gid(id);if(e)e.innerHTML=v}
function val(id,v){let e=gid(id);if(e){if(v!==undefined)e.value=v;return e.value}}
function addC(id,c){let e=gid(id);if(e)e.classList.add(c)}
function remC(id,c){let e=gid(id);if(e)e.classList.remove(c)}
function togC(id,c){let e=gid(id);if(e)e.classList.toggle(c)}
function hide(id){let e=gid(id);if(e)e.style.display="none"}
function show(id,d="block"){let e=gid(id);if(e)e.style.display=d}
function el(tag,a={},t=""){let e=document.createElement(tag);for(let[k,v]of Object.entries(a)){if(k=="class")e.className=v;else if(k=="style"&&typeof v=="object")Object.assign(e.style,v);else e.setAttribute(k,v)}if(t)e.innerText=t;return e}
function app(parent,child){let p=typeof parent=="string"?gid(parent):parent;if(p)p.appendChild(child)}
function r(url,m,body=null,h={}){let o={method:m,headers:{"Content-Type":"application/json",...h}};if(body&&m!="GET")o.body=typeof body=="string"?body:JSON.stringify(body);return fetch(url,o).then(r=>r.json().then(d=>({ok:r.ok,status:r.status,data:d})).catch(()=>({ok:r.ok,status:r.status,data:null}))).catch(e=>({ok:false,status:0,data:null,error:e.message}))}
function rget(url,h={}){return r(url,"GET",null,h)}
function rpost(url,body,h={}){return r(url,"POST",body,h)}
function rput(url,body,h={}){return r(url,"PUT",body,h)}
function rdel(url,h={}){return r(url,"DELETE",null,h)}
function store(k,v){if(v!==undefined){try{localStorage.setItem(k,typeof v=="object"?JSON.stringify(v):v)}catch(e){}}else{let d=localStorage.getItem(k);try{return JSON.parse(d)}catch{return d}}}
function storeDel(k){localStorage.removeItem(k)}
function storeClear(){localStorage.clear()}
function wait(ms){return new Promise(r=>setTimeout(r,ms))}
function rand(min,max){return Math.floor(Math.random()*(max-min+1))+min}
function isEmpty(v){return v===null||v===undefined||(typeof v=="string"&&v.trim()==="")||(Array.isArray(v)&&v.length===0)||(typeof v=="object"&&Object.keys(v).length===0)}
function onReady(fn){document.readyState=="loading"?document.addEventListener("DOMContentLoaded",fn):fn()}
function onClick(id,fn){let e=gid(id);if(e)e.addEventListener("click",fn)}
function setCSS(id,s){let e=gid(id);if(e)Object.assign(e.style,s)}
function getAttr(id,a){let e=gid(id);return e?e.getAttribute(a):null}
function setAttr(id,a,v){let e=gid(id);if(e)e.setAttribute(a,v)}
function remAttr(id,a){let e=gid(id);if(e)e.removeAttribute(a)}
put("IronF loaded")
put('Проект создан на IronF Framework');
