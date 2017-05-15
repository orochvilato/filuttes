from flask import Blueprint, render_template

home = Blueprint('home', __name__)

@home.route('/')
def _home():
    # Do some stuff
    return render_template('lutte.html')

@home.route('/twitter/<msg>')
def _twitter(msg):
    from app.util.twitter import twitter
    api = twitter()
    print msg
    tweet = "Hello, world ! (%s)" % msg
    status = api.update_status(status=tweet)
    return "done"
