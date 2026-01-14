import streamlit as st

st.set_page_config(page_title="CongestiQ", layout="centered")

st.title("CongestiQ")
st.subheader("Early Urban Traffic Congestion Predictor")

st.write("This MVP predicts congestion level and identifies its cause using traffic flow patterns.")

speed = st.slider("Average traffic speed (km/h)", 5, 80, 40)

if st.button("Predict Congestion"):
    if speed < 20:
        congestion = "High Congestion"
        cause = "Temporary bottleneck or lane restriction"
    elif speed < 35:
        congestion = "Moderate Congestion"
        cause = "Irregular driving behavior"
    else:
        congestion = "Low Congestion"
        cause = "Normal traffic flow"

    st.success(f"Congestion Level: {congestion}")
    st.info(f"Predicted Cause: {cause}")
