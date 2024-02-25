from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Load your data file into a DataFrame (assuming your data file is named 'cocktails_data.csv')
datas = pd.read_csv('popcorn.csv')

def cosine_sim(flavor,spirit,season,occasion,color):
    # User input
    user_flavor = flavor
    user_main_spirit = spirit
    user_season = season
    user_other_occasion = occasion
    user_color = color

    # Combine user input into a user profile
    user_occasion = f"{user_season}, {user_other_occasion}"
    user_profile = f"{user_flavor} {user_main_spirit} {user_occasion} {user_color}"

    # Selected columns for analysis
    selected_columns = ['Flavor', 'Main Spirit', 'Occasion', 'Color']

    # Combine the selected columns from the DataFrame with the user profile
    corpus = [' '.join(str(row[column]) for column in selected_columns) for _, row in datas.iterrows()]

    # Vectorize the corpus using TfidfVectorizer
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)

    # Vectorize the user profile separately
    user_tfidf = vectorizer.transform([user_profile])

    # Compute cosine similarity between the user profile and each cocktail in the dataset
    similarities = cosine_similarity(tfidf_matrix, user_tfidf)

    # Find the indices of the top 3 most similar cocktails
    top_indices = similarities.flatten().argsort()[:-4:-1]

    # Get the recommended cocktails (excluding the user profile)
    recommended_cocktails = [datas.iloc[idx].to_dict() for idx in top_indices]

    # Print the recommended cocktails
    return recommended_cocktails

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def recommendation():
    return render_template('test.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        try:
            user_color = request.form['color']         
            user_flavor = request.form['flavor']
            user_spirit = request.form['spirit']
            user_season = request.form['season']
            user_occasion = request.form['occasion']
        except:
            print("exception")
    cocktail_list = cosine_sim(user_flavor,user_spirit,user_season,user_occasion,user_color)
    print(cocktail_list)
    main_cocktail = cocktail_list[0]
    sub1_cocktail = cocktail_list[1]
    sub2_cocktail = cocktail_list[2]
    return render_template('result.html',main_cocktail=main_cocktail,sub1_cocktail=sub1_cocktail,sub2_cocktail=sub2_cocktail)
    
if __name__ == '__main__':
    app.run(debug=True)
