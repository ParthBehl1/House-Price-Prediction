# flask is a module which allows you to write python service which serves http request

from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_locations()
    })
    response.headers.add('Access-Control-Allow-Origin', "*")
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bath, bhk)
    })
    response.headers.add('Access-Control-Allow-Origin', "*")
    return response

if __name__ == "__main__":
    print("Starting Flask server for house prediction..")
    util.load_saved_artifacts()
    app.run(port=5001)





Bengaluru Home Price Prediction

Welcome to the Bengaluru Home Price Prediction repository! This project utilizes machine learning techniques to predict home prices in Bengaluru, India. The Flask web application provides an intuitive interface for users to estimate the price of their homes based on key features such as total area, number of bedrooms (BHK), bathrooms, and location.

Features:

User-friendly web interface for predicting home prices. Machine learning model trained on Bengaluru real estate data. Integration of Flask for creating a robust web application. Interactive form to input property details and receive estimated prices. How to Use:

Enter the total area, number of bedrooms (BHK), bathrooms, and choose the location of your home. Click the "Estimate Price" button to receive an estimated home price. Feel free to explore the code, contribute, and enhance the application! Your feedback is highly appreciated.

Tech Stack:

Python Flask Machine Learning (Scikit-Learn) HTML/CSS JavaScript (jQuery)