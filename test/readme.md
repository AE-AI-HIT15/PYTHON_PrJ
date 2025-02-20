# House Price Prediction

## Overview
This is a Streamlit-based web application designed to predict house prices based on user-provided features. It utilizes a Random Forest Regressor model for making predictions. The application is simple to use and provides instant results based on the input data.

## Features
The app takes the following inputs:
- **Lot Area (sq ft)**: The total size of the lot.
- **Year Built**: The year the house was constructed.
- **1st Floor Area (sq ft)**: The area of the first floor in square feet.
- **2nd Floor Area (sq ft)**: The area of the second floor in square feet.
- **Bedrooms Above Ground**: The number of bedrooms above ground level.
- **Total Rooms Above Ground**: The total number of rooms above ground level.

The app predicts the house price based on these features using a pre-trained Random Forest Regressor.

## How to Run
1. Ensure you have Python installed on your system.
2. Install the required libraries by running:
   ```bash
   pip install streamlit scikit-learn pandas numpy
   ```
3. Save the code in a file named `app.py`.
4. Run the app using Streamlit:
   ```bash
   streamlit run app.py
   ```
5. Enter the required inputs in the web interface and click "Predict Price" to see the predicted house price.

## Dependencies
- `streamlit`: For building the web interface.
- `pandas`: For handling tabular data.
- `numpy`: For numerical computations.
- `scikit-learn`: For machine learning models and preprocessing.

## How It Works
1. The app simulates a dataset to train a Random Forest Regressor model if no pre-trained model exists.
2. The user provides the input features through the app interface.
3. The app preprocesses the inputs and uses the trained model to predict the house price.
4. The predicted price is displayed on the app.

## Example
### Input:
- Lot Area: 5000 sq ft
- Year Built: 2000
- 1st Floor Area: 800 sq ft
- 2nd Floor Area: 0 sq ft
- Bedrooms Above Ground: 3
- Total Rooms Above Ground: 6

### Output:
Predicted House Price: `$150,000`

## Future Improvements
- Add more features for a more accurate prediction.
- Allow users to upload their own dataset for model training.
- Improve the UI/UX of the application.

## Author
This app was created to demonstrate a simple machine learning workflow using Streamlit. Feel free to contribute or suggest improvements!
