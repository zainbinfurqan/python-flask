from flask import Flask, render_template
import datetime
app = Flask(__name__)

posts = [
    {'id': 1, 'title': 'Article', 'author': 'Zain Ahmed',
        'postedDate': datetime.datetime.now()
     },
    {'id': 2, 'title': 'Article', 'author': 'Faraz Ahmed',
     'postedDate': datetime.datetime.now()
     },
    {'id': 3, 'title': 'Article', 'author': 'Arsalan Ahmed',
     'postedDate': datetime.datetime.now()
     },
    {'id': 4, 'title': 'Article', 'author': 'Shariq',
     'postedDate': datetime.datetime.now()
     },
    {'id': 5, 'title': 'Article', 'author': 'Ammad Imran',
     'postedDate': datetime.datetime.now()
     },
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('Home.html', posts=posts)


@app.route('/aboutus')
def aboutus():
    return render_template('AboutUs.html')


if(__name__) == '__main__':
    app.run(debug=True)
