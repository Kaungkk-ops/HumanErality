import streamlit as st

# --- Data for historical eras and changes ---
era_data = {
    1990: {
        "Era Name": "End of Cold War / Globalization",
        "Key Changes": [
            "Collapse of communist regimes and Soviet Union disintegration",
            "German reunification, Mandela’s release, Hubble launch",
            "Start of the Gulf War, rise of multiparty democracies"
        ]
    },
    2010: {
        "Era Name": "Digital Revolution / Post-Recession Recovery",
        "Key Changes": [
            "Smartphone and social media boom",
            "Economic recovery after 2008 crisis",
            "Major social movements and cultural shifts"
        ]
    },
    2020: {
        "Era Name": "COVID-19 Pandemic / Decisive Decade",
        "Key Changes": [
            "Global COVID-19 pandemic and lockdowns",
            "Acceleration of remote work and digitalization",
            "Major climate events, rise of AI and cryptocurrencies"
        ]
    },
    2025: {
        "Era Name": "Age of Transformation / AGI Emergence",
        "Key Changes": [
            "Predicted breakthroughs in AI and AGI",
            "Intensified climate crisis, global recalibration post-pandemic",
            "Digitalization, urban innovation, and geopolitical shifts"
        ]
    }
}

# --- Prediction logic for building and infrastructure ---
def predict_infrastructure(years_ahead):
    if years_ahead == 5:
        return {
            "Title": "2030: Digitalized & Sustainable Construction",
            "Predictions": [
                "Widespread adoption of Building Information Modeling (BIM) for project management and sustainability[2].",
                "3D printing, drones, and smart materials (e.g., green and self-repairing concrete) become standard[2].",
                "Robotics and AI automate construction tasks, improving safety and productivity[2].",
                "Civil engineering costs expected to rise by 16-17%[5][7].",
                "Significant growth in electricity and energy infrastructure[7]."
            ]
        }
    elif years_ahead == 10:
        return {
            "Title": "2035: Massive Infrastructure Expansion",
            "Predictions": [
                "Global construction market continues rapid growth, with demand far outpacing supply[3].",
                "Most new urban infrastructure will be built using advanced automation and sustainable materials[2][3].",
                "Data center and decarbonization projects drive infrastructure investment[6].",
                "Labour shortages persist, driving further automation and digital solutions[1]."
            ]
        }
    elif years_ahead == 15:
        return {
            "Title": "2040: Unprecedented Construction Boom",
            "Predictions": [
                "Global construction market reaches $22 trillion, with much of the world’s 2050 infrastructure still being built[3].",
                "Urbanization and population growth drive demand, especially in developing and developed nations alike[3].",
                "AI, robotics, and green tech dominate building and infrastructure projects[2][3].",
                "Continued focus on decarbonization, smart cities, and resilient infrastructure[2][6]."
            ]
        }
    else:
        return None

# --- Streamlit UI ---
st.title("Historical Eras & Future Predictions: Building and Infrastructure")

st.header("Historical Eras (1990–2025)")
for year in [1990, 2010, 2020, 2025]:
    with st.expander(f"{year}: {era_data[year]['Era Name']}"):
        for change in era_data[year]["Key Changes"]:
            st.write(f"- {change}")

st.header("Predict the Future of Building & Infrastructure")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Next 5 Years"):
        result = predict_infrastructure(5)
        st.subheader(result["Title"])
        for item in result["Predictions"]:
            st.write(f"- {item}")

with col2:
    if st.button("Next 10 Years"):
        result = predict_infrastructure(10)
        st.subheader(result["Title"])
        for item in result["Predictions"]:
            st.write(f"- {item}")

with col3:
    if st.button("Next 15 Years"):
        result = predict_infrastructure(15)
        st.subheader(result["Title"])
        for item in result["Predictions"]:
            st.write(f"- {item}")

st.info("Predictions based on current industry outlooks and trends in construction, digitalization, and sustainability[1][2][3][4][5][6][7].")
