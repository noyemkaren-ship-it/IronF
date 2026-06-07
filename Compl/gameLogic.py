


def create_sprite(name: str, page: str, controlJsCode: str):
    with open("src/index.html", "a") as file:
        file.write(f'    <img src="{page.strip()}" id="{name.strip()}">\n')
    
    with open("src/scripts/main.js", "a") as file:
        file.write(f"{controlJsCode}\n")


def create_control_Horizontal(name: str):
    control_code = f"""
// Горизонтальное управление для спрайта {name}
document.addEventListener('keydown', function(event) {{
    const sprite = document.getElementById('{name}');
    if (!sprite) return;
    
    const step = 10;
    const currentLeft = parseInt(sprite.style.left) || 0;
    
    if (event.key === 'ArrowLeft' || event.key === 'a') {{
        sprite.style.left = (currentLeft - step) + 'px';
    }}
    if (event.key === 'ArrowRight' || event.key === 'd') {{
        sprite.style.left = (currentLeft + step) + 'px';
    }}
}});
"""
    
    with open("src/scripts/main.js", "a") as file:
        file.write(control_code)
    return control_code

def create_control_Vertical(name: str):
    control_code = f"""
// Вертикальное управление для спрайта {name}
document.addEventListener('keydown', function(event) {{
    const sprite = document.getElementById('{name}');
    if (!sprite) return;
    
    const step = 10;
    const currentTop = parseInt(sprite.style.top) || 0;
    
    if (event.key === 'ArrowUp' || event.key === 'w') {{
        sprite.style.top = (currentTop - step) + 'px';
    }}
    if (event.key === 'ArrowDown' || event.key === 's') {{
        sprite.style.top = (currentTop + step) + 'px';
    }}
}});
"""
    
    with open("src/scripts/main.js", "a") as file:
        file.write(control_code)
    return control_code


def create_control_Full(name: str):
    control_code = f"""
// Полное управление для спрайта {name}
document.addEventListener('keydown', function(event) {{
    const sprite = document.getElementById('{name}');
    if (!sprite) return;
    
    // Устанавливаем абсолютное позиционирование
    sprite.style.position = 'absolute';
    
    const step = 10;
    const currentLeft = parseInt(sprite.style.left) || 0;
    const currentTop = parseInt(sprite.style.top) || 0;
    
    switch(event.key) {{
        case 'ArrowLeft':
        case 'a':
            sprite.style.left = (currentLeft - step) + 'px';
            break;
        case 'ArrowRight':
        case 'd':
            sprite.style.left = (currentLeft + step) + 'px';
            break;
        case 'ArrowUp':
        case 'w':
            sprite.style.top = (currentTop - step) + 'px';
            break;
        case 'ArrowDown':
        case 's':
            sprite.style.top = (currentTop + step) + 'px';
            break;
    }}
}});
"""
    
    with open("src/scripts/main.js", "a") as file:
        file.write(control_code)
    return control_code
