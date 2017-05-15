# app/util/assets.py

from flask_assets import Bundle, Environment
from .. import app

bundles = {

    'home_js': Bundle(
        'vendor/leaflet/leaflet.js',
        'js/init.js',
        output='gen/home.js'),

    'home_css': Bundle(
        'vendor/leaflet/leaflet.css',
        'css/style.css',
        output='gen/home.css'),
}

assets = Environment(app)

assets.register(bundles)
