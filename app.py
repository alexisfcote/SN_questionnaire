# encoding: utf-8
import os
import sys
import json
import time
from collections import OrderedDict
import random
import webbrowser
import threading
import sys
from flask import Flask, render_template, request, url_for, redirect, flash, session, abort

from forms import *

from flask import Flask, render_template, request

if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template_folder,
                          static_folder = static_folder)
else:
    app = Flask(__name__)


app.secret_key = os.environ.get('secretkey', 'qweqwe1e2e')


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
    threading.Timer(4, lambda: sys.exit()).start()
    return render_template("fin.html")


if __name__ == '__main__':
    threading.Timer(2, lambda: webbrowser.open(url="http://127.0.0.1:5000")).start()
    app.run(debug=False, port=5000)
