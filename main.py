import random

GREETINGS = [
    'Hello World',
    'Hola Mundo',
    'ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ ਦੁਨਿਆ',
    'こんにちは世界',
    '你好世界',
    'Përshendetje Botë',
    'مرحبا بالعالم',
    'Բարեւ, աշխարհ',
    'হ্যালো দুনিয়া',
    'Saluton mondo',
    'გამარჯობა მსოფლიო',
]

COLORS = ('red pink purple deep-purple indigo blue light-blue cyan teal green '
    'light-green lime yellow amber orange deep-orange blue-grey').split(' ')


def change_greeting():
    p = $('#content')
    p.empty()

    color = random.choice(COLORS)
    text_color = 'black' if color in ['lime', 'yellow', 'amber'] else 'white'

    ($('<span class="greeting">')
        .text(random.choice(GREETINGS))
        .addClass('z-depth-1')
        .addClass(color)
        .addClass(text_color + '-text')
        .appendTo(p))


def cause_trouble():
    a = 1/0     # won't trigger an error in JS
    print(a)    # Infinity

    b = c + 1   # c doesn't exist


change_greeting()
$('button.change').on('click', change_greeting)
$('button.error').on('click', cause_trouble)
