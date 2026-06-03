base_css = """
body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    line-height: 1.6;
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    text-align: center;
    color: #333;
}

img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 20px auto;
    border-radius: 8px;
}

/* Стили для полей ввода и текстовых областей */
input[type="text"], 
input[type="email"], 
input[type="password"], 
input[type="number"], 
textarea {
    width: 100%;
    max-width: 400px; /* Чтобы поля не были слишком широкими */
    box-sizing: border-box; /* Учитывает padding в общей ширине */
    padding: 10px 15px;
    margin: 10px auto;
    display: block;
    border: 1px solid #ccc;
    border-radius: 6px;
    font-size: 16px; /* Защищает от автозума на смартфонах */
    transition: border-color 0.2s ease;
}

/* Эффект при клике на поле ввода */
input:focus, 
textarea:focus {
    border-color: #0076ff;
    outline: none; /* Убирает стандартную синюю рамку браузера */
}

/* Стили для кнопок */
button, 
input[type="submit"] {
    background-color: #0076ff;
    color: white;
    padding: 12px 24px;
    font-size: 16px;
    font-weight: 500;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    margin: 15px auto;
    display: block;
    transition: background-color 0.2s ease, transform 0.1s ease;
}

/* Эффект при наведении на кнопку */
button:hover, 
input[type="submit"]:hover {
    background-color: #0056b3;
}

/* Эффект при нажатии на кнопку */
button:active, 
input[type="submit"]:active {
    transform: scale(0.98);
}
"""