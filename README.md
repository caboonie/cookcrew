# y2l-flask-catbook
## Before you start: Fork and clone this repository

1. Fork this repository by clicking "Fork" on this page:
![forking](https://image.ibb.co/jHRieT/forking.png)

2. Copy this repository's url by clicking the green clone button:
![copying url](https://image.ibb.co/n2wYeT/copying_clone.png)


## Before you code: Try to understand the codebase
This repository is a sample flask app for the famous Catbook, the world's next most famous website, where you can see Cats play piano, eat ice cream, and rock the best hair cuts. 

This app uses a lot of the tools we have learned ove the yearlong, bootstrap, databases, and flask. Make sure you understand how these different components interact. If you have questions, this is a good time to ask a TA or an instructor

After you have an idea about the app, start the server by running `python app.py`

During this lab you will need to remember some concepts we talked about from previous lectures. Some resources that might help:
https://go.meet.sh/y2l-databases
https://go.meet.sh/y2l-flask-routing

## The lab
### Part 1: Cat's detail page
If you click on the view detail button on the home page, you'll notice that the browser returns a 404 (Not Found page).

Using variable routes, your first task is to fix this and instead return the profile page of a cat. The profile page should have a vote button and the name of the cat
(Hint: you'll need to change the app.py and a couple of other files)

**Bonus:** change the models.py file to have the cat model accept an image for the cat and store it in the DB. Change the home.html and cat.html to dispaly the right picture for the cat (note you will need to delete the cats.db file if you make changes to the models.db file)

### Part 2: Implement adding a new Cat
Using your knowledge with working for forms add a button for adding a new cat. When the button is clicked, it should take you to a new page where you can input the name of the cat. Once the name is specified you should be able to click on a "Add new cat" button to add it to the db. (hint: see create_cat in the database.py file)

**Bonus:** In the header, you can see there is a search text box, implement a functionlity where you can write a cat's name in the search text box and using forms it will GET all the cats that match that name


### Part 3: Implementing a vote function
Let's make the vote functionality work, make the vote functionlity work (how do you do that in the db?). When the vote button is clicked on a cat's profile it will add to the number of votes a has. You should update the home.html to show the total votes that a cat has

**Bonus:** change the order of how cats are displayed on the home page to show the most popular cat first (notice how models.py has a relevant attribute for this)


