🚀 IronF Framework

Пиши сайты на человеческом языке

IronF — это микро-фреймворк для тех, кто устал от трех файлов, сложного CSS и вечной возни с подключениями. Один файл. Понятные команды. Красивый результат.

📦 Установка

bash
git clone https://github.com/noyemkaren-ship-it/IronF.git
cd IronF
Убедись, что у тебя установлен Python 3.6+:

bash
python --version
🎮 Быстрый старт за 30 секунд

1. Создай файл main.html:

text
css
basic

html
meta МойПервыйСайт
<h1>Привет, мир!</h1>
<p>IronF рулит!</p>
<button id="myBtn">Нажми меня</button>
endhtml

jscript
onClick("myBtn", function() {
    print("Сайт готов!");
});
2. Запусти компилятор:

bash
python compil.py
3. Открой src/index.html в браузере и радуйся! 🎉

📝 Синтаксис

Структура файла

Файл main.html состоит из трех секций строго по порядку:

text
css      ← стили
html     ← структура
jscript  ← логика
📌 Секция CSS

Вариант А — готовый дизайн (для ленивых и новичков):

text
css
basic
Одна команда basic дает:

Адаптивные шрифты
Красивые кнопки и поля ввода
Центрирование и отступы
Плавные анимации
Вариант Б — свой CSS:

text
css
a {
    color: red;
    text-align: center;
}
Вариант В — сокращения IronF (еще проще):

text
css
talign: center;
fsize: 24px;
color: blue;
Сокращение	Что заменяет
talign:	text-align:
fsize:	font-size:
Вариант Г — импорт CSS из другого файла:

text
css
import styles/theme.css
import common/buttons.css
💡 Можно смешивать: basic, свой CSS, сокращения и import — всё в одной секции!
📌 Секция HTML

Команда meta — обязательна! Она создает заголовок страницы и всю служебную структуру:

text
html
meta МояКрутаяСтраница
<h1>Заголовок</h1>
<p>Текст...</p>
endhtml
⚠️ endhtml обязателен. Забудешь — компилятор поругается!
📌 Секция JScript

## 🎯 Упрощённый JavaScript (фишка IronF!)

IronF автоматически добавляет 28 встроенных функций, чтобы тебе не приходилось писать скучный код.

### 🪟 Окна и консоль

| Функция | Что делает | Пример |
|---------|-----------|--------|
| `print(text)` | Всплывающее окно | `print("Привет!")` |
| `put(...args)` | Вывод в консоль | `put("Клик:", count)` |
| `ask(text, default)` | Окно ввода текста | `let name = ask("Имя?", "Гость")` |
| `confirm(text)` | Окно Да/Нет | `if(confirm("Удалить?")){...}` |

### 🔍 Поиск элементов

| Функция | Что делает | Пример |
|---------|-----------|--------|
| `gid(id)` | Найти по ID | `gid("myBtn")` |
| `gq(selector)` | Найти по CSS селектору | `gq(".btn")` |
| `gqa(selector)` | Найти все по селектору | `gqa("p")` |

### ✏️ Работа с содержимым

| Функция | Что делает | Пример |
|---------|-----------|--------|
| `txt(id, text)` | Установить текст | `txt("title", "Привет")` |
| `html(id, html)` | Установить HTML | `html("list", "<li>1</li>")` |
| `val(id, value)` | Получить/установить значение поля | `val("input", "Иван")` |

### 🎨 CSS классы и стили

| Функция | Что делает | Пример |
|---------|-----------|--------|
| `addC(id, class)` | Добавить класс | `addC("btn", "active")` |
| `remC(id, class)` | Убрать класс | `remC("btn", "active")` |
| `togC(id, class)` | Переключить класс | `togC("btn", "hidden")` |
| `hide(id)` | Скрыть элемент | `hide("loader")` |
| `show(id, display)` | Показать элемент | `show("loader", "flex")` |
| `setCSS(id, styles)` | Установить стили | `setCSS("box", {color:"red"})` |

### 🏗️ Создание элементов

| Функция | Что делает | Пример |
|---------|-----------|--------|
| `el(tag, attrs, text)` | Создать элемент | `el("div", {class:"box"}, "Текст")` |
| `app(parent, child)` | Добавить в родителя | `app("list", item)` |

### 🌐 HTTP запросы

| Функция | Что делает | Пример |
|---------|-----------|--------|
| `rget(url)` | GET запрос | `let users = await rget("/api/users")` |
| `rpost(url, body)` | POST запрос | `await rpost("/api/user", {name:"Иван"})` |
| `rput(url, body)` | PUT запрос | `await rput("/api/user/1", data)` |
| `rdel(url)` | DELETE запрос | `await rdel("/api/user/1")` |

### 💾 Хранилище

| Функция | Что делает | Пример |
|---------|-----------|--------|
| `store(key, value)` | Сохранить/загрузить | `store("theme", "dark")` |
| `storeDel(key)` | Удалить запись | `storeDel("theme")` |
| `storeClear()` | Очистить всё | `storeClear()` |

### 🛠️ Утилиты

| Функция | Что делает | Пример |
|---------|-----------|--------|
| `wait(ms)` | Пауза в мс | `await wait(1000)` |
| `rand(min, max)` | Случайное число | `rand(1, 100)` |
| `isEmpty(v)` | Проверка на пустоту | `if(isEmpty(name)){...}` |
| `onReady(fn)` | После загрузки DOM | `onReady(() => {...})` |
| `onClick(id, fn)` | Обработчик клика | `onClick("btn", () => {...})` |

### Полный пример с новыми функциями:

jscript
let count = 0;

onClick("myBtn", async function() {
    count++;
    txt("counter", count);
    put("Нажатий: " + count);
    
    let data = await rget("/api/stats");
    if(data.ok) {
        put("Ответ сервера:", data.data);
    }
    
    store("clicks", count);
    print("Успешно!");
});

onReady(function() {
    let saved = store("clicks") || 0;
    txt("counter", saved);
});
🛠️ Полный пример

text
css
basic
import my-styles.css

html
meta МойБлог

<h1>Добро пожаловать в мой блог</h1> <p id="counter">Кликов: 0</p> <input type="text" id="name" placeholder="Твое имя"> <button id="subBtn">Подписаться</button> endhtml
jscript
let clicks = store("clicks") || 0;
txt("counter", "Кликов: " + clicks);

onClick("subBtn", async function() {
let name = val("name");

if(isEmpty(name)) {
print("Введи имя!");
return;
}

clicks++;
txt("counter", "Кликов: " + clicks);
store("clicks", clicks);

let result = await rpost("/api/subscribe", {name: name});
if(result.ok) {
print(name + ", ты подписан!");
hide("subBtn");
txt("counter", "Готово!");
}
});

text

📂 Что получается на выходе

После компиляции появляется папка src/:

text
src/
├── index.html
├── css/
│   └── style.css
└── scripts/
    └── main.js
Можешь закинуть src/ на любой хостинг — всё работает.

🚨 Ошибки и их решение

Ошибка	Что делать
НЕТУ endlhtml	Добавь endhtml в конце секции html
НЕТ css	Добавь секцию css в самое начало файла
файл не найден (при import)	Проверь, что путь к CSS-файлу правильный
🤔 Для кого IronF?

✅ Идеально подходит	❌ Не подходит
Новички в веб-разработке	Профессионалы
Быстрое прототипирование	Крупные коммерческие проекты
Обучение детей	Те, кто хочет изучить настоящий HTML/CSS
Пет-проекты и демки	
⚠️ Важно: IronF — это тренажер и ускоритель. Для серьезной разработки учи чистый HTML/CSS/JS. Но начать свой путь — самое то!
🧪 Запуск тестового примера

В папке с IronF создай main.html, скопируй пример выше и выполни:

bash
python compil.py
Если всё ок — в папке src появится готовый сайт.

📜 Лицензия

MIT — делай что хочешь, но автора упомяни.

🙏 Автор

IronEagle Company
GitHub: @noyemkaren-ship-it

Сделано с ❤️ для тех, кто начинает свой путь в вебе