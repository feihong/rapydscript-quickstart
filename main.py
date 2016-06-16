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


jq = window.jQuery


def main():
    change_greeting()
    jq('button.change').on('click', change_greeting)
    jq('button.error').on('click', cause_trouble)
    jq('button.debug').on('click', debug)


def change_greeting():
    p = jq('#content')
    p.empty()

    color = random.choice(COLORS)
    text_color = 'black' if color in ['lime', 'yellow', 'amber'] else 'white'

    (jq('<span class="greeting">')
        .text(random.choice(GREETINGS))
        .addClass('z-depth-1')
        .addClass(color)
        .addClass(text_color + '-text')
        .appendTo(p))


def cause_trouble():
    a = 1/0     # won't trigger an error in JS
    print(a)    # Infinity

    b = c + 1   # c doesn't exist


def debug():
    chrs = []
    for i in range(5):
        chrs.append(chr(random.randint(945, 969)))

    # Note that this is the JS array version of join().
    result = chrs.join('')
    print(result)

    # You have to use literal JS to activate the debugger, because the compiler
    # treats 'debugger' as a reserved keyword.
    v'debugger'

    jq('span.greeting').text(result)


main()
