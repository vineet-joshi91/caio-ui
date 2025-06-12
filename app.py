import streamlit as st
import os
from main import process_document

st.set_page_config(page_title="CAIO", layout="centered")
st.title("🤖 CAIO – Chief AI Officer")

# === TIER SIMULATION (for now) ===
st.sidebar.header("Choose Your Plan")
user_tier = st.sidebar.radio(
    "Current Tier",
    options=["Free", "Pro", "Premium"],
    help="(In production, this is set by login/payment status)"
)

st.markdown(f"**Active Tier:** `{user_tier}`")

# === FILE UPLOAD ===
uploaded_file = st.file_uploader(
    "📄 Upload your document (.pdf, .docx, .txt)", 
    type=["pdf", "docx", "txt"]
)

# === OPTIONAL PROMPT (reserved for future) ===
optional_prompt = st.text_area(
    "Optional Prompt (not active yet)",
    placeholder="E.g., Summarize main financial risks. (Coming soon!)"
)

# === MAIN ACTION BUTTON ===
if st.button("Analyze with CAIO"):
    if uploaded_file is not None:
        # Ensure input directory exists
        os.makedirs("data/inputs", exist_ok=True)

        # Save file to disk
        input_path = os.path.join("data", "inputs", uploaded_file.name)
        with open(input_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.info("🧠 Processing... This may take a few seconds.")

        # MAIN ENGINE CALL
        summary = process_document(input_path, user_tier=user_tier)

        st.success("✅ Analysis Complete!")
        st.text_area(
            "Your CAIO Output:",
            value=summary,
            height=350
        )

        # Tiered upgrade suggestions
        if user_tier == "Free":
            st.warning("🚀 Unlock advanced CXO insights, full entity extraction, and multi-brain analysis with Pro or Premium plans!")
        elif user_tier == "Pro":
            st.info("⭐ Upgrade to Premium for deeper benchmarking, multi-language support, and priority insights.")

    else:
        st.warning("⚠️ Please upload a file to proceed.")

# === Footer / Legal ===
st.markdown("---")
st.caption("CAIO 2.0 by Vineet Joshi | For demo use only. Actual login/tier integration coming soon.")
