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


@external
class Promise: pass


def main():
    change_greeting()
    jq('button.change').on('click', change_greeting)
    jq('button.error').on('click', cause_trouble)
    jq('button.debug').on('click', debug)
    jq('button.generator').on('click', generator_function)
    jq('button.promise').on('click', promise)
    jq('button.co').on('click', generator_control_flow)


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

    # Note that this is the Array.join() method.
    result = chrs.join('')
    print('Using JS join:', result)

    # Pythonic string methods can be accessed via functions in the str module.
    result2 = str.join('', chrs)
    print('Using Python join:', result2)

    # You have to use literal JS to activate the debugger, because the compiler
    # treats 'debugger' as a reserved keyword.
    v'debugger'

    jq('span.greeting').text(result)


def generator_function():
    def func(start, end):
        for i in range(start, end):
            yield i*2 + 1

    gen = func(random.randint(4, 11), random.randint(12, 20))
    jq('span.greeting').text(str.join(', ', gen))


def sleep(delay):
    def fn(resolve, reject):
        window.setTimeout(resolve, delay * 1000)
    return Promise(fn)


def promise():
    sleep(1).then(def():
        jq('span.greeting').text('1 second later')
    )
    sleep(2).then(def():
        jq('span.greeting').text('2 seconds later')
    )


def generator_control_flow():
    co(def():
        words = ['eenie', 'meenie', 'minie', 'mo']
        for word in words:
            jq('span.greeting').text(word)
            yield sleep(1)
    )


main()
