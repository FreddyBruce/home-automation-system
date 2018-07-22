import markdown
import os

# Import the framework
from flask import Flask

# Create an instance of flask
app = Flask(__name__)

@app.route("/")
def index():
    """PResent some documentation"""

    # Open the README file
    with open(os.path.dirname(app.root_path) + '/READEM.md', 'r') as markdown_file:

        # Read the content of the markdown_file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)
