from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        total_bill = float(request.form['total_bill'])
        tip_percent = float(request.form['tip_percent'])
        tip_amount = total_bill * (tip_percent / 100)
        total_amount = total_bill + tip_amount
        return render_template('index.html', tip_amount=tip_amount, total_amount=total_amount)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)