import streamlit as st
import requests
import base64

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Crop Recommendation", layout="centered")

# -------------------------------
# LOAD LOCAL IMAGE (farm.jpg)
# -------------------------------
def get_base64(img_path):
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("farm.jpg")   # make sure file is in same folder

# -------------------------------
# CUSTOM CSS
# -------------------------------
st.markdown(f"""
<style>

/* 🌄 BACKGROUND IMAGE */
[data-testid="stAppViewContainer"] {{
    background: url("data:image/jpg;base64,{img}") no-repeat center center fixed;
    background-size: cover;
}}

/* 🌿 MAIN CONTAINER */
.block-container {{
    background: rgba(255,255,255,0.92);
    padding: 2rem;
    border-radius: 20px;
}}

/* 🖤 TEXT */
h1, h2, h3, h4, label {{
    color: black !important;
}}

/* ⬜ INPUT BOX */
div[data-baseweb="input"] {{
    background-color: #e5e7eb !important;
    border-radius: 10px !important;
}}

div[data-baseweb="input"] input {{
    background-color: #e5e7eb !important;
    color: black !important;
}}

/* 🔘 + / - BUTTONS */
button {{
    background-color: white !important;
    color: black !important;
    border: none !important;
    border-radius: 6px !important;
}}

/* 🔘 MAIN BUTTON */
.stButton > button {{
    background: linear-gradient(135deg, #22c55e, #16a34a) !important;
    color: white !important;
    border-radius: 12px;
    font-weight: 600;
}}

/* 📊 PROGRESS BAR */
div[data-testid="stProgressBar"] > div > div {{
    background-color: #22c55e;
}}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# TITLE
# -------------------------------
st.title("🌱 Crop Recommendation")

# -------------------------------
# INPUTS
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    N = st.number_input("Nitrogen (N)", 0.0, 140.0)
    P = st.number_input("Phosphorus (P)", 0.0, 145.0)
    K = st.number_input("Potassium (K)", 0.0, 205.0)
    temperature = st.number_input("Temperature (°C)", 0.0, 50.0)

with col2:
    humidity = st.number_input("Humidity (%)", 0.0, 100.0)
    ph = st.number_input("pH Value", 0.0, 14.0)
    rainfall = st.number_input("Rainfall (mm)", 0.0, 300.0)

# -------------------------------
# BUTTON ACTION
# -------------------------------
if st.button("🔍 Recommend Crop"):

    data = {
        "N": N,
        "P": P,
        "K": K,
        "temperature": temperature,
        "humidity": humidity,
        "ph": ph,
        "rainfall": rainfall
    }

    try:
        response = requests.post("http://127.0.0.1:5000/predict", json=data)

        if response.status_code == 200:
            result = response.json()

            if isinstance(result, list) and len(result) > 0:
                top = result[0]

                name = top.get("name", "Unknown")
                conf = round(float(top.get("confidence", 0)), 2)

                # 🌾 RESULT TITLE
                st.markdown("### 🌾 Best Crop for Your Land")

                # 🌾 NAME
                st.markdown(
                    f"<h2 style='text-align:center;'>🌾 {name}</h2>",
                    unsafe_allow_html=True
                )

                # 📊 PROGRESS
                progress_value = int(conf) if conf > 1 else int(conf * 100)
                st.progress(progress_value)

                # 📈 CONFIDENCE
                st.markdown(
                    f"<p style='text-align:center; font-size:18px;'><b>{conf}% Match</b></p>",
                    unsafe_allow_html=True
                )

            else:
                st.warning("⚠️ No result found")

        else:
            st.error("❌ API Error")

    except Exception as e:
        st.error(f"⚠️ Error: {e}")