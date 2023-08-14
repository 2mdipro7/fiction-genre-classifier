from flask import Flask, render_template, request
from gradio_client import Client
import json

app = Flask(__name__)

client = Client("https://dipro7-story-genre-classifier.hf.space/")

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        input_text = request.form['text']
        result = client.predict(
            input_text,
            api_name="/predict"
        )

        try:
            # Load the JSON content from the result path
            with open(result, 'r') as json_file:
                json_data = json.load(json_file)
                genres_list = json_data["confidences"]

                # Convert the genres list elements to strings
                genres_text = ", ".join([f"{item['label']} ({item['confidence']:.2f})" for item in genres_list])

                return render_template("result.html", input_text=input_text, output_text=genres_text)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            error_message = f"Error reading JSON file: {e}"
            return render_template("error.html", input_text=input_text, error_message=error_message)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
