from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def recommendation():
    if request.method == 'POST':
        try:
            user_color = request.form['color']         
            user_flavor = request.form['flavor']
            user_spirit = request.form['spirit']
            print('--------',user_flavor,user_color,user_spirit)
        except:
            print("exception")
        
    
    return render_template('a.html')

@app.route('/cocktail')
def cocktail_page():
    return render_template('cocktail_page.html')
    
if __name__ == '__main__':
    app.run(debug=True)
