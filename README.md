# Flask support for Stack Sentinel

Flask support for Stack Sentinel is achieved by installing a simple extension, which uses a logger handler to capture
not just exception information, but also, stateful information about the error, including cookies, Flask request data,
and more.

Adding Stack Sentinel to your app couldn't be easier:

    #
    # Configure StackSentinel client, extension -- replace values with your own
    app.config['STACKSENTINEL_ACCOUNT_TOKEN'] = 'YOUR ACCOUNT TOKEN'
    app.config['STACKSENTINEL_PROJECT_TOKEN'] = 'YOUR PROJECT TOKEN'
    
    stacksentinel = flask.ext.stacksentinel.StackSentinelHandler(app)

That's it. Note that by default, Stack Sentinel's Flask extension uses Python's root logger. To use a custom logger,
just pass it as an argument to StackSentinelHandler.


    #
    # Configure StackSentinel client, extension -- replace values with your own
    app.config['STACKSENTINEL_ACCOUNT_TOKEN'] = 'YOUR ACCOUNT TOKEN'
    app.config['STACKSENTINEL_PROJECT_TOKEN'] = 'YOUR PROJECT TOKEN'
    
    stacksentinel = flask.ext.stacksentinel.StackSentinelHandler(app, logger=app.logger)

## Installation

To install StackSentinel, just use pip:

    pip install flask-stacksentinel

Easy as pie.

## Got questions?

Email us, support@stacksentinel.com

