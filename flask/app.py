from flask import Flask, render_template
import subprocess
import os

# Execute the create_home_html.py script to generate the home.html file
subprocess.run(["python", "create_home_html.py"])

# Get the path to the directory containing the home.html file
template_dir = os.path.abspath('template')

# Initialize the Flask app
app = Flask(__name__, template_folder=template_dir, static_url_path='/static')

# Define a route to render the home.html template
@app.route('/')
def hello():
    return render_template('home.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

