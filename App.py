import streamlit as st
import joblib
import pandas as pd

def main():
    # Load the trained model
    tree_model = joblib.load('tree_model.pkl')

    # Set page title
    st.title("Climate Effect On Grapes")

    # Input fields for each parameter
    Temp = st.number_input("Air Temperature ", value=0.0)
    relativeHumidity = st.number_input("Relative Humidity  ", value=0.0)
    rain = st.number_input("Enter Rain", value=0.0)
    windSpeed = st.number_input("Enter Wind Speed ", value=0.0)
    leafWetnessHour = st.number_input("Enter leaf Wetness/hr", value=0.0)

    # Button to make predictions
    if st.button("Predict"):
        # Create a DataFrame with the user input
        user_input = pd.DataFrame({
            'Airtemp': [Temp],
            'Rel.Hum': [relativeHumidity],
            'Rain': [rain],
            'W.Speed': [windSpeed],
            'leaf wetness hr.': [leafWetnessHour]
        })

        # Use the loaded model to make predictions
        prediction = tree_model.predict(user_input)

        # Display the predicted value to the user
        st.write("Predicted value:", prediction)

if __name__ == "__main__":
    main()
