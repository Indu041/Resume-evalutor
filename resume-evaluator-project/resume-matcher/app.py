
import streamlit as st
from parser import extract_text_from_pdf
from matcher import compute_similarity

st.set_page_config(page_title="Resume Evaluator", layout="centered")
st.title("📄 Resume Evaluator with Role Matching")

job_description = st.text_area("Paste Job Description", height=200)

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file and job_description:
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())

    resume_text = extract_text_from_pdf("temp_resume.pdf")
    score = compute_similarity(resume_text, job_description)
    st.success(f"Matching Score: {score}%")

    if score > 75:
        st.markdown("✅ **Excellent Match** — Your resume strongly aligns with the job description. You're likely well-qualified for this role. Consider applying with confidence! ")
    elif score > 50:
        st.markdown("🟡**Moderate Match** — Your resume matches the job description to some extent, but there’s room for improvement. Consider adding more relevant skills or experiences.")
    else:
        st.markdown("Try including more relevant skills and keywords from the job description in your resume.")

