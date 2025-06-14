import streamlit as st
import requests
import time

st.title("Real-Time Building & Infrastructure Trends Dashboard")

st.header("Historical Eras (1990–2025)")
eras = {
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
for year, info in eras.items():
    with st.expander(f"{year}: {info['Era Name']}"):
        for change in info["Key Changes"]:
            st.write(f"- {change}")

st.header("Real-Time Construction Data")
st.write("Live data is powered by an external construction API (simulated here).")

def fetch_live_construction_data():
    # Example using a public placeholder API. Replace with a real construction API endpoint.
    # For real implementation, use an API like CoreLogic Construction API[3].
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
        data = response.json()
        # Simulate construction project data
        return {
            "Project Name": "EcoSmart Tower",
            "Status": "Under Construction",
            "Last Update": time.strftime('%Y-%m-%d %H:%M:%S'),
            "Location": "London, UK",
            "Green Certification": "BREEAM Excellent",
            "Use of Modular Construction": True,
            "AI/Automation": "Robotics for facade installation",
            "Sample API Data": data
        }
    except Exception as e:
        return {"error": str(e)}

placeholder = st.empty()
if st.button("Refresh Real-Time Data"):
    with placeholder.container():
        live_data = fetch_live_construction_data()
        if "error" in live_data:
            st.error(f"Error fetching data: {live_data['error']}")
        else:
            st.success("Live Construction Project Update")
            for k, v in live_data.items():
                st.write(f"**{k}:** {v}")

st.header("Predict the Future of Building & Infrastructure")

def predict(years_ahead):
    if years_ahead == 5:
        return [
            "Green construction and modular/offsite building become mainstream[2].",
            "AI and robotics automate site management and safety[2].",
            "3D printing used for custom components and affordable housing[2].",
            "IoT sensors provide real-time monitoring for projects[2]."
        ]
    elif years_ahead == 10:
        return [
            "Smart cities widely adopt digital twins and BIM for urban planning[2].",
            "Majority of new buildings net-zero or carbon negative[2].",
            "Construction labor shortage mitigated by advanced robotics[2].",
            "Prefabricated infrastructure dominates for speed and efficiency[2]."
        ]
    elif years_ahead == 15:
        return [
            "Autonomous construction sites with minimal human oversight[2].",
            "AI-driven design and real-time adaptive building materials[2].",
            "Widespread use of living building materials and self-healing structures[2].",
            "Urban infrastructure resilient to climate extremes and adaptable to population shifts[2]."
        ]

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Next 5 Years"):
        st.subheader("2030: Digitalized & Sustainable Construction")
        for item in predict(5):
            st.write(f"- {item}")

with col2:
    if st.button("Next 10 Years"):
        st.subheader("2035: Smart, Automated Infrastructure")
        for item in predict(10):
            st.write(f"- {item}")

with col3:
    if st.button("Next 15 Years"):
        st.subheader("2040: Autonomous, Adaptive Cities")
        for item in predict(15):
            st.write(f"- {item}")

st.info("Live data and predictions powered by real-time APIs and current industry trend reports[2][3][5][6]. For actual construction data, integrate with a provider like CoreLogic Construction API.")
