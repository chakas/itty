from itty import *

@error(500)
def my_great_500(exception, env, start_response):
    start_response('500 APPLICATION ERROR', [('Content-Type', 'text/html')])
    html_output = """
    <html>
        <head>
            <title>Application Error! OH NOES!</title>
        </head>
        
        <body>
            <h1>OH NOES!</h1>
            
            <p>Yep, you broke it.</p>
            
            <p>Exception: %s</p>
        </body>
    </html>
    """ % exception[0]
    return [html_output]

@get('/test_404')
def test_404(request):
    raise NotFound('Not here, sorry.')
    return 'This should never happen.'

@get('/test_500')
def test_500(request):
    raise RuntimeError('Oops.')
    return 'This should never happen either.'

@get('/test_redirect')
def test_redirect(request):
    raise Redirect('/hello')

run_itty()
