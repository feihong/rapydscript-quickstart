$('#content').text('Hello World!')

def on_click():
    $('#content').text('Goodbye World!')
$('button').on('click', on_click)
