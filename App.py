import streamlit as st

def main():
    # Set page title
    st.title("Climate Effect On Grapes")

    # Create two columns for input fields
    col1, col2 = st.columns(2)

    # Input fields for each parameter in the first column
    with col1:
        months = st.number_input("Enter months", min_value=1, max_value=12, value=1)
        airtemp_mean = st.number_input("Enter Airtemp mean", value=0.0)
        rel_hum_mean = st.number_input("Enter Rel.Hum mean", value=0.0)
        rain = st.number_input("Enter Rain", value=0.0)

    # Input fields for each parameter in the second column
    with col2:
        radiation_mean = st.number_input("Enter Radiation mean", value=0.0)
        w_speed_mean = st.number_input("Enter W.Speed mean", value=0.0)
        day_length_hrs = st.number_input("Enter Day length hrs.", value=0.0)
        leaf_wetness_hr = st.number_input("Enter leaf wetness hr.", value=0.0)

    # Button to display input values
    if st.button("Print Input Values"):
        st.write("Months:", months)
        st.write("Airtemp mean:", airtemp_mean)
        st.write("Rel.Hum mean:", rel_hum_mean)
        st.write("Rain:", rain)
        st.write("Radiation mean:", radiation_mean)
        st.write("W.Speed mean:", w_speed_mean)
        st.write("Day length hrs.:", day_length_hrs)
        st.write("Leaf wetness hr.:", leaf_wetness_hr)

if __name__ == "__main__":
    main()
