from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
@app.route('/')
def transportation_type():
    return render_template('transportation_type.html')
@app.route('/', methods=['GET', 'POST'])
def book_ticket():
    if request.method == 'POST':
         return render_template('book_ticket.html')
@app.route('/confirm', methods=['GET', 'POST'])
def booking_confirm_message():
    if request.method == 'POST':
        return render_template('booking_confirm_message.html')
    else:
        return redirect(url_for('transportation_type'))
if __name__ == '__main__':
    app.run()
