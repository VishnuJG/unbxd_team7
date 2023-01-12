from flask import Flask, render_template, url_for, request, redirect


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Category.html')


@app.route('/product/')
def product():
    return render_template('Product.html')



if __name__ == "__main__":
    app.run(debug=True)