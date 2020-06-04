from flask import Flask, render_template, request
import model

# Create the application object
app = Flask(__name__)


@app.route('/', methods=["GET","POST"])
def home_page():
    # render a template when the user accesses the root of your website
    # Flask will look at the 'templates' folder for index.html
    return render_template('index.html')


@app.route('/output')  # this is linked to the form action="/output" attribute
def recommendation_output():
    # Pull input from form
    some_input = request.args.get('user_input')            
    
    # Case if empty
    if some_input =="":
        return render_template("index.html",
                                my_input = some_input,
                                my_form_result="Empty")
    else:
        # Run model code here (see model.py)
        some_output = model.run_model(some_input)
        # Update template
        return render_template("index.html",
                                my_input=some_input,
                                my_output=some_output,
                                my_form_result="NotEmpty")


# start the server with the 'run()' method when you run `python server.py`
if __name__ == "__main__":
    app.run(debug=True)  # will run locally http://127.0.0.1:5000/
