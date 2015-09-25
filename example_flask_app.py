import flask
import flask.ext.stacksentinel

app = flask.Flask(__name__)
app.debug = False

#
# Just a couple of example handlers. The second will generate a URL for testing.
#
@app.route('/')
def hello_world():
    return flask.Response("Extension installed: %s" % flask.ext.stacksentinel, mimetype='text/plain')

@app.route('/cause-error')
def cause_error():
    raise AttributeError('This is a test!')

#
# Configure StackSentinel client, extension -- replace values with your own
app.config['STACKSENTINEL_ACCOUNT_TOKEN'] = 'YOUR ACCOUNT TOKEN'
app.config['STACKSENTINEL_PROJECT_TOKEN'] = 'YOUR PROJECT TOKEN'

stacksentinel = flask.ext.stacksentinel.StackSentinelHandler(app)

if __name__ == '__main__':
    app.run()
