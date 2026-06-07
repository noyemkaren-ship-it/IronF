base_css = """
/* === Сброс и база === */
body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    line-height: 1.7;
    max-width: 800px;
    margin: 0 auto;
    padding: 40px 20px;
    text-align: center;
    color: #2c3e50;
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
}

/* === Карточка-контейнер (чтобы всё было на подложке) === */
/* Если хочешь обернуть форму в div.container — добавь этот класс в HTML */
.container {
    background: rgba(255, 255, 255, 0.8);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-radius: 24px;
    padding: 40px;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.08), 0 0 0 1px rgba(255, 255, 255, 0.5);
    width: 100%;
    box-sizing: border-box;
}

img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 30px auto;
    border-radius: 16px;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
    transition: transform 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.bigimg {
    max-width: 300%;
}

img:hover {
    transform: scale(1.02);
}

/* === Стили для полей ввода === */
input[type="text"], 
input[type="email"], 
input[type="password"], 
input[type="number"], 
textarea {
    width: 100%;
    max-width: 450px;
    box-sizing: border-box;
    padding: 14px 20px;
    margin: 12px auto;
    display: block;
    background: rgba(255, 255, 255, 0.7);
    backdrop-filter: blur(5px);
    -webkit-backdrop-filter: blur(5px);
    border: 1.5px solid rgba(0, 0, 0, 0.08);
    border-radius: 14px;
    font-size: 16px;
    color: #2c3e50;
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.02);
}

/* Эффект при наведении на поле */
input[type="text"]:hover, 
input[type="email"]:hover, 
input[type="password"]:hover, 
input[type="number"]:hover, 
textarea:hover {
    border-color: rgba(0, 118, 255, 0.3);
    box-shadow: 0 8px 25px rgba(0, 118, 255, 0.08);
}

/* Эффект при клике (фокус) */
input[type="text"]:focus, 
input[type="email"]:focus, 
input[type="password"]:focus, 
input[type="number"]:focus, 
textarea:focus {
    outline: none;
    border-color: #0076ff;
    background: white;
    box-shadow: 0 0 0 4px rgba(0, 118, 255, 0.15), 0 10px 30px rgba(0, 118, 255, 0.1);
}

/* Стили для плейсхолдера */
::placeholder {
    color: #a0aec0;
    font-weight: 300;
    transition: color 0.3s ease;
}

input:focus::placeholder,
textarea:focus::placeholder {
    color: #cbd5e0;
}

/* === Стили для кнопок === */
button, 
input[type="submit"] {
    background: linear-gradient(135deg, #0076ff 0%, #0056b3 100%);
    color: white;
    padding: 14px 32px;
    font-size: 16px;
    font-weight: 600;
    letter-spacing: 0.3px;
    border: none;
    border-radius: 14px;
    cursor: pointer;
    margin: 20px auto;
    display: block;
    transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    box-shadow: 0 8px 25px rgba(0, 118, 255, 0.3);
    position: relative;
    overflow: hidden;
}

/* Блик на кнопке */
button::after,
input[type="submit"]::after {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
    transition: left 0.5s ease;
}

button:hover::after,
input[type="submit"]:hover::after {
    left: 100%;
}

/* Эффект при наведении */
button:hover, 
input[type="submit"]:hover {
    transform: translateY(-3px);
    box-shadow: 0 15px 35px rgba(0, 118, 255, 0.4);
    background: linear-gradient(135deg, #1a82ff 0%, #0062cc 100%);
}

/* Эффект при нажатии */
button:active, 
input[type="submit"]:active {
    transform: translateY(1px) scale(0.98);
    box-shadow: 0 5px 15px rgba(0, 118, 255, 0.3);
    transition: all 0.1s ease;
}

/* === Адаптивность === */
@media (max-width: 600px) {
    body {
        padding: 20px 15px;
    }
    
    .container {
        padding: 25px 20px;
        border-radius: 20px;
    }

    input[type="text"], 
    input[type="email"], 
    input[type="password"], 
    input[type="number"], 
    textarea {
        max-width: 100%;
        padding: 12px 16px;
    }

    button, 
    input[type="submit"] {
        width: 100%;
        max-width: 300px;
        padding: 16px 24px;
    }
}

/* === Небольшая анимация появления === */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.container, form {
    animation: fadeInUp 0.6s ease forwards;
}
"""
css = False
html = False
script = False
meta = False
name = ""
