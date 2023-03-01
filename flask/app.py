from flask import Flask, render_template


# Initialize the Flask app
app = Flask(__name__, template_folder='template', static_folder='static')

# Define a route to render the home.html template
@app.route('/')
def hello():
    return render_template('home.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

