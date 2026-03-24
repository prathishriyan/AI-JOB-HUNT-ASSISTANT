import streamlit as st
from orchestrator import run_pipeline
import pdfplumber
from docx import Document

st.set_page_config(page_title="AI Job Hunt Assistant", layout="centered")

st.title("AI Job Hunt Assistant")
st.markdown("Use AI agents to analyze jobs, tailor your resume, and write outreach messages - all from one interface.")

# ---------------- INPUT FIELDS ----------------
keyword = st.text_input("Job Keyword")
location = st.text_input("Location", "New York")

uploaded_file = st.file_uploader("Upload Your Resume", type=["txt", "pdf", "docx"])

user_bio = st.text_area(
    "Short Bio (for outreach tone)",
    "I'm a data professional passionate about public service."
)

# ---------------- BUTTON ACTION ----------------
if st.button("Run Job Hunt Assistant"):

    resume_text = ""

    # ---------------- FILE PROCESSING ----------------
    if uploaded_file is not None:

        st.success(f"Uploaded: {uploaded_file.name}")

        file_type = uploaded_file.type

        try:
            if file_type == "text/plain":
                resume_text = uploaded_file.read().decode("utf-8")

            elif file_type == "application/pdf":
                with pdfplumber.open(uploaded_file) as pdf:
                    resume_text = "\n".join(
                        [page.extract_text() or "" for page in pdf.pages]
                    )

            elif "word" in file_type:
                doc = Document(uploaded_file)
                resume_text = "\n".join([para.text for para in doc.paragraphs])

            else:
                st.error("Unsupported file type!")
                st.stop()

        except Exception as e:
            st.error(f"Error reading file: {e}")
            st.stop()

    else:
        st.warning("Please upload your resume!")
        st.stop()

    # ---------------- RUN PIPELINE ----------------
    if resume_text.strip():
        with st.spinner("Running AI agents..."):

            result = run_pipeline(
                keyword=keyword,
                location=location,
                resume_text=resume_text,
                user_bio=user_bio
            )

        st.success("Agents completed their tasks! ✅")

        st.markdown("---")

        # ---------------- DISPLAY OUTPUT ----------------
        st.markdown("## 📊 AI Generated Output")
        st.text(result)

        # ---------------- DOWNLOAD BUTTON ----------------
        st.download_button(
            label="⬇ Download Result",
            data=result,
            file_name="ai_job_assistant_output.txt",
            mime="text/plain"
        )