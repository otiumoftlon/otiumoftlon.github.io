from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/linear_regression')
def linear_regression():
    return render_template('linear_regression.html')

@app.route('/logistic_regression')
def logistic_regression():
    return render_template('logistic_regression.html')

@app.route('/knn')
def knn():
    return render_template('knn.html')

@app.route('/svm')
def svm():
    return render_template('svm.html')

if __name__ == "__main__":
    app.run(debug=True)