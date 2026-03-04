import streamlit as st

from utils.parser import extract_text_from_pdf
from utils.jd_analyzer import analyze_job_description
from utils.resume_analyzer import analyze_resume
from utils.matcher import compute_match_score
from utils.skill_gap import compute_skill_gap
from utils.tailor import generate_tailored_resume

st.set_page_config(page_title="AI Resume Tailor", layout="wide")

st.title("🚀 AI Resume Tailoring Tool")

# ---- Model Selection ----
model_choice = st.selectbox(
    "Select Model",
    ["gemini"]
)

# ---- Upload Resume ----
resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description Here", height=250)

generate_button = st.button("Generate Tailored Resume")

if generate_button:

    if resume_file is None or not job_description:
        st.warning("Please upload resume and paste job description.")
    else:
        with st.spinner("Analyzing..."):

            resume_text = extract_text_from_pdf(resume_file)

            # Structured extraction
            jd_data = analyze_job_description(model_choice, job_description)
            resume_data = analyze_resume(model_choice, resume_text)

            # Skill gap
            # skill_gap = compute_skill_gap(jd_data, resume_data)
            skill_gap = compute_skill_gap(jd_data, resume_data)

            matched = skill_gap["matched_skills"]
            missing = skill_gap["missing_skills"]
            
            total_skills = len(matched) + len(missing)
            
            if total_skills > 0:
                coverage_score = (len(matched)/total_skills) * 100
            else:
                coverage_score = 0

            # Match score
            match_score = compute_match_score(resume_text, job_description)

            # Tailored resume
            tailored_output = generate_tailored_resume(
                model_choice,
                resume_text,
                jd_data,
                skill_gap
            )

        # ---- Display Results ----
        st.success("Analysis Complete")

        # ---------- MATCH SCORE ----------
        st.subheader("Similarity Score")
        st.markdown(f"### {match_score:.2f}%")
        st.progress(float(match_score) / 100)

        # ---------- COVERAGE SCORE ----------
        st.subheader("Skill Coverage Score")
        st.markdown(f"### {coverage_score:.2f}%")
        st.progress(float(coverage_score) / 100)

        # ---------- SKILL ALIGNMENT ----------
        st.subheader("Skill Alignment")

        col1, col2 = st.columns(2)

        def render_skill_bubbles(skills, color, icon, empty_message):

            # if not skills:
            #     st.info("None")
            #     return

            if skills:
                bubbles = "<div style='display:flex; flex-wrap:wrap;'>"

                for skill in skills:
                    bubbles += (
                        f"<span style='background-color:{color}; "
                        f"padding:6px 14px; "
                        f"border-radius:20px; "
                        f"margin:6px; "
                        f"font-size:14px; "
                        f"border:1px solid rgba(255,255,255,0.08); '>"
                        f"{icon} {skill.title()}</span>"
                    )

                bubbles += "</div>"
                st.markdown(bubbles, unsafe_allow_html=True)
            else:
                st.info(empty_message)

        with col1:
            st.markdown("### Matched Skills")
            render_skill_bubbles(matched, "#123524", "✔", "No strong skill matches detected :(")

        with col2:
            st.markdown("### Missing Skills")
            render_skill_bubbles(missing, "#3b1f1f", "✖", "No major skill gap found!")

        # ---------- TAILORED RESUME ----------
        st.subheader("Tailored Resume")
        st.text_area("Rewritten Content", tailored_output, height=450)
