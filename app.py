
import streamlit as st
from PIL import Image

st.set_page_config(page_title="AgriSmart AI", page_icon="🌱")
st.title("🌱 AgriSmart AI - Kabale")
st.write("Maize | Tomato | Cabbage Disease Detection")

DISEASE_DB = {
    "Maize Leaf Blight": {"symptoms": ["brown spots", "yellow halos"], "treatment": "Mancozeb spray, crop rotation"},
    "Tomato Early Blight": {"symptoms": ["dark spots", "leaf curl"], "treatment": "Copper fungicide"},
    "Cabbage Black Rot": {"symptoms": ["V-shaped lesions", "black veins"], "treatment": "Hot water seed treatment"},
}

st.header("🩺 Step 1: Symptom Checker")
crop = st.selectbox("Select crop", ["Maize", "Tomato", "Cabbage"])
symptoms = st.text_input("Describe symptoms e.g. brown spots")

if st.button("Check Symptoms"):
    for disease, info in DISEASE_DB.items():
        if crop.lower() in disease.lower() and symptoms:
            st.warning(f"Possible: {disease}")
            st.info(f"Treatment: {info['treatment']}")

st.header("📸 Step 2: AI Image Detection")
uploaded = st.file_uploader("Upload leaf photo", type=["jpg","png","jpeg"])
if uploaded:
    img = Image.open(uploaded).resize((224,224))
    st.image(img, caption="Your leaf")
    st.success("Demo: Maize Leaf Blight - 85% confidence")
    st.write("Treatment: Apply Mancozeb, remove infected leaves")

st.header("📊 Objective 4")
st.write("Model: MobileNetV2 | Params: 2.4M | Target >90% accuracy")
