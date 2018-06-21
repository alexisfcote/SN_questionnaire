# encoding: utf-8
import os
import sys
import json
import time
from collections import OrderedDict
import random
from flask import Flask, render_template, request, url_for, redirect, flash, session, abort

from forms import *

from webui import WebUI # Add WebUI to your imports
from flask import Flask, render_template, request

if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template_folder,
                          static_folder = static_folder)
else:
    app = Flask(__name__)


app.secret_key = os.environ.get('secretkey', 'qweqwe1e2e')

ui = WebUI(app, debug=True) # Create a WebUI instance

@app.route('/', methods=['GET', 'POST'])
def index():
  
    form = SNForm(request.form)
    if request.method == 'POST' and form.validate():
        with open(os.path.join(os.path.dirname(sys.executable),
                  'SN-Journal-de-bord-' + time.strftime('%Y-%m-%d', time.localtime()) + '.json'),
                   mode='w') as f:
            json.dump(form.data, f)
        return redirect(url_for('fin'))

    if request.method == 'POST' and not form.validate():
        for error in form.errors:
            flash(form.errors.get(error)[-1])

    return render_template("index.html", form=form)


@app.route('/fin', methods=['GET'])
def fin():
    return render_template("fin.html")


if __name__ == '__main__':
    ui.run() 
    #app.run(debug=False, port=5000)
