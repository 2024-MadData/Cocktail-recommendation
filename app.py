from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def recommendation():
    if request.method == 'POST':
        try:
            user_flavor = request.form['flavor']
            user_color = request.form['color']
            print(user_flavor,user_color)
        except:
            print("exception")
        
    
    return render_template('a.html')

if __name__ == '__main__':
    app.run(debug=True)
