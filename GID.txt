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
<button>Нажми меня</button>
endhtml

jscript
alert("Сайт готов!");
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

Обычный JavaScript. Без упрощений, без магии:

text
jscript
console.log("Сайт загружен");

document.querySelector("button").onclick = function() {
    alert("Кнопка нажата!");
};
🛠️ Полный пример

text
css
basic
import my-styles.css

html
meta МойБлог
<h1>Добро пожаловать в мой блог</h1>
<p>Здесь будет интересный текст</p>
<input type="text" placeholder="Твое имя">
<button>Подписаться</button>
endhtml

jscript
let count = 0;
document.querySelector("button").onclick = () => {
    alert("Спасибо за подписку!");
};
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

Karen Gevorgyan
GitHub: @noyemkaren-ship-it

Сделано с ❤️ для тех, кто начинает свой путь в вебе

