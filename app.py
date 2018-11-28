from flask import Flask, request, url_for, redirect
from flask import render_template
from database import get_all_recipes, get_recipe, create_recipe

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def cookbook_home():
    cats = []#get_all_recipes()
    return render_template("home.html", cats=cats)
 
@app.route('/recipes')
def recipes_page():
    recipes = get_all_recipes()
    return render_template("recipes.html", recipes=recipes)

@app.route('/recipes/<string:id>')
def recipe_page(id):
    recipe = get_recipe(id)
    return render_template("recipe.html", recipe=recipe)

@app.route('/add', methods=['GET', 'POST'])
def add_page():
    if request.method == 'POST':
        #print(request.form)
        ingredients={}
        for key in request.form:
            if 'ingredient_' in key:
                  number = key[11:]
                  #print(number)
                  tup = (request.form["amount_"+number],request.form["measurement_"+number])
                  ingredients[request.form[key]]=tup
        create_recipe(request.form['name'],request.form['servings'],ingredients,request.form['recipe'])
    return render_template("add.html")


if __name__ == '__main__':
   app.run(debug = True)

