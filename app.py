# A flask app that  will count numbers from 1 to 1,000,000
# i.   Display every 10th number in the series in Bold
# ii.  Display every 3rd number in the series in Italics
# iii. Bonus: Underline every Prime number in this series.

import flask
from flask import Flask, render_template


app = Flask(__name__)


def count_to_million():
    data = []
    for i in range(1, 1000001):
        # every 10th number in bold
        if i % 10 == 0:
            data.append("<b>{}</b>".format(i))
        # every 3rd number in italics
        elif i % 3 == 0:
            data.append("<i>{}</i>".format(i))
        # every prime number in underline
        elif is_prime(i):
            data.append("<u>{}</u>".format(i))
        else:
            data.append(i)
    return data

# function to check if a number is prime
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


@app.route('/')
def index():
    data = count_to_million()
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
    