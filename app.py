# ----- Flask Hello World ----- #

# import the Flask class from the flask package
from flask import Flask

# create the application object - create an instance of the Flask class for our web app
# __name__ takes the string value of 'main' when script is executed
app = Flask(__name__)

# use the decorator pattern to 
# link the view function to a url
@app.route("/")
@app.route("/heythere")

# define the view using a function, which returns a string
def hello_world():
	return "Hello, World!"

# Something you should know is that Python assigns the name "__main__" to the script when the script is executed.
# If the script is imported from another script, the script keeps it given name (e.g. hello.py).
# In our case we are executing the script. Therefore, __name__ will be equal to "__main__".
# That means the if conditional statement is satisfied and the app.run() method will be executed.
# This technique allows the programmer to have control over script’s behavior.

if __name__ == "__main__":
	app.run()   #start the development server using the run() method
