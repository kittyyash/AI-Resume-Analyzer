import streamlit as st
from PyPDF2 import PdfReader
from docx import Document
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main-title {
    font-size: 42px;
    font-weight: 700;
    text-align: center;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #666;
    margin-bottom: 30px;
}

.section-title {
    font-size: 25px;
    font-weight: 650;
    margin-top: 30px;
    margin-bottom: 15px;
}

.footer {
    text-align: center;
    color: #777;
    margin-top: 50px;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🤖 AI Resume Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Analyze your resume, check ATS readiness, match job descriptions, '
    'and get intelligent improvement suggestions.'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# RESUME UPLOAD
# =========================================================

st.markdown(
    '<div class="section-title">📄 Upload Your Resume</div>',
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "Choose your resume",
    type=["pdf", "docx"]
)


# =========================================================
# PDF TEXT EXTRACTION
# =========================================================

def extract_pdf_text(file):

    reader = PdfReader(file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


# =========================================================
# DOCX TEXT EXTRACTION
# =========================================================

def extract_docx_text(file):

    document = Document(file)

    text = ""

    for paragraph in document.paragraphs:

        text += paragraph.text + "\n"

    return text


# =========================================================
# SKILLS DETECTION
# =========================================================

def detect_skills(resume_text):

    skills_list = [
        "Python",
        "Java",
        "C",
        "C++",
        "JavaScript",
        "HTML",
        "CSS",
        "SQL",
        "Git",
        "GitHub",
        "Microsoft Excel",
        "PowerPoint",
        "Word",
        "Machine Learning",
        "Artificial Intelligence",
        "Data Science",
        "Cloud Computing",
        "AWS",
        "Microsoft Azure",
        "MATLAB",
        "Arduino",
        "Embedded Systems",
        "IoT",
        "UI/UX",
        "Figma",
        "Communication",
        "Leadership",
        "Problem Solving"
    ]

    resume_lower = resume_text.lower()

    detected_skills = []

    for skill in skills_list:

        if skill.lower() in resume_lower:

            detected_skills.append(skill)

    return detected_skills


# =========================================================
# EDUCATION DETECTION
# =========================================================

def detect_education(resume_text):

    education_keywords = [
        "B.E",
        "B.Tech",
        "M.E",
        "M.Tech",
        "B.Sc",
        "M.Sc",
        "BCA",
        "MCA",
        "MBA",
        "Diploma",
        "12th",
        "HSC",
        "10th",
        "SSLC"
    ]

    detected_education = []

    for education in education_keywords:

        if education.lower() in resume_text.lower():

            detected_education.append(education)

    return detected_education


# =========================================================
# EXPERIENCE DETECTION
# =========================================================

def detect_experience(resume_text):

    experience_keywords = [
        "internship",
        "intern",
        "experience",
        "work experience",
        "worked",
        "trainee",
        "training",
        "developer",
        "engineer",
        "designer",
        "project intern"
    ]

    detected_experience = []

    resume_lower = resume_text.lower()

    for experience in experience_keywords:

        if experience.lower() in resume_lower:

            detected_experience.append(
                experience.title()
            )

    return detected_experience


# =========================================================
# PROJECT DETECTION
# =========================================================

def detect_projects(resume_text):

    project_keywords = [
        "project",
        "projects",
        "mini project",
        "major project",
        "final year project",
        "academic project",
        "personal project",
        "web project",
        "software project",
        "hardware project"
    ]

    detected_projects = []

    resume_lower = resume_text.lower()

    for project in project_keywords:

        if project.lower() in resume_lower:

            detected_projects.append(
                project.title()
            )

    return list(dict.fromkeys(detected_projects))


# =========================================================
# CERTIFICATION DETECTION
# =========================================================

def detect_certifications(resume_text):

    certification_keywords = [
        "certification",
        "certifications",
        "certificate",
        "certificates",
        "certified",
        "course",
        "courses",
        "training",
        "workshop",
        "online course",
        "python certification",
        "cloud computing",
        "microsoft azure",
        "design thinking"
    ]

    detected_certifications = []

    resume_lower = resume_text.lower()

    for certification in certification_keywords:

        if certification.lower() in resume_lower:

            detected_certifications.append(
                certification.title()
            )

    return list(dict.fromkeys(detected_certifications))


# =========================================================
# ATS SCORE
# =========================================================

def calculate_ats_score(
    resume_text,
    skills,
    education,
    experience,
    projects,
    certifications
):

    score = 0

    if len(resume_text.strip()) >= 300:
        score += 20

    elif len(resume_text.strip()) >= 150:
        score += 10

    if len(skills) >= 5:
        score += 20

    elif len(skills) >= 3:
        score += 15

    elif len(skills) >= 1:
        score += 10

    if len(education) >= 1:
        score += 15

    if len(experience) >= 2:
        score += 15

    elif len(experience) >= 1:
        score += 10

    if len(projects) >= 1:
        score += 15

    if len(certifications) >= 1:
        score += 15

    return min(score, 100)


# =========================================================
# JOB DESCRIPTION KEYWORD MATCHING
# =========================================================

def match_job_description(
    resume_text,
    job_description
):

    resume_lower = resume_text.lower()
    job_lower = job_description.lower()

    skills_list = [
        "Python",
        "Java",
        "C",
        "C++",
        "JavaScript",
        "HTML",
        "CSS",
        "SQL",
        "Git",
        "GitHub",
        "Microsoft Excel",
        "PowerPoint",
        "Word",
        "Machine Learning",
        "Artificial Intelligence",
        "Data Science",
        "Cloud Computing",
        "AWS",
        "Microsoft Azure",
        "MATLAB",
        "Arduino",
        "Embedded Systems",
        "IoT",
        "UI/UX",
        "Figma",
        "Communication",
        "Leadership",
        "Problem Solving"
    ]

    required_skills = []

    for skill in skills_list:

        if skill.lower() in job_lower:

            required_skills.append(skill)

    matching_skills = []
    missing_skills = []

    for skill in required_skills:

        if skill.lower() in resume_lower:

            matching_skills.append(skill)

        else:

            missing_skills.append(skill)

    if required_skills:

        match_score = int(
            (len(matching_skills) /
             len(required_skills)) * 100
        )

    else:

        match_score = 0

    return (
        match_score,
        matching_skills,
        missing_skills
    )


# =========================================================
# NLP SIMILARITY
# =========================================================

def calculate_nlp_similarity(
    resume_text,
    job_description
):

    try:

        documents = [
            resume_text,
            job_description
        ]

        vectorizer = TfidfVectorizer(
            stop_words="english"
        )

        tfidf_matrix = vectorizer.fit_transform(
            documents
        )

        similarity = cosine_similarity(
            tfidf_matrix[0:1],
            tfidf_matrix[1:2]
        )[0][0]

        return round(
            similarity * 100,
            2
        )

    except ValueError:

        return 0


# =========================================================
# OVERALL JOB MATCH SCORE
# =========================================================

def calculate_overall_match(
    keyword_score,
    nlp_score
):

    overall_score = (
        (keyword_score * 0.60)
        +
        (nlp_score * 0.40)
    )

    return round(overall_score)


# =========================================================
# IMPROVEMENT SUGGESTIONS
# =========================================================

def generate_suggestions(
    skills,
    education,
    experience,
    projects,
    certifications,
    missing_skills
):

    suggestions = []

    if len(skills) < 5:

        suggestions.append(
            "💡 Add more relevant technical and soft skills."
        )

    if missing_skills:

        suggestions.append(
            "🎯 Consider learning or adding these "
            "job-related skills: "
            + ", ".join(missing_skills)
        )

    if not education:

        suggestions.append(
            "🎓 Add your educational qualification clearly "
            "with degree, college and graduation year."
        )

    if not experience:

        suggestions.append(
            "💼 Add internship, training, volunteer "
            "or work experience if applicable."
        )

    if not projects:

        suggestions.append(
            "📂 Add academic or personal projects "
            "with a short description."
        )

    if not certifications:

        suggestions.append(
            "📜 Add relevant certifications, courses "
            "or workshops."
        )

    suggestions.append(
        "📝 Use clear section headings such as "
        "Skills, Education, Experience, Projects "
        "and Certifications."
    )

    suggestions.append(
        "🚀 Use action words such as Developed, "
        "Designed, Implemented, Created and Analyzed."
    )

    suggestions.append(
        "📊 Add measurable results or achievements "
        "wherever possible."
    )

    return suggestions


# =========================================================
# REPORT GENERATION
# =========================================================

def create_report(
    resume_name,
    ats_score,
    skills,
    education,
    experience,
    projects,
    certifications,
    match_score,
    matching_skills,
    missing_skills,
    nlp_score,
    overall_match_score,
    suggestions
):

    report = ""

    report += "=" * 60 + "\n"
    report += "              AI RESUME ANALYZER\n"
    report += "=" * 60 + "\n\n"

    report += f"Resume: {resume_name}\n\n"

    report += "-" * 60 + "\n"
    report += "ATS RESUME SCORE\n"
    report += "-" * 60 + "\n"
    report += f"Overall ATS Score: {ats_score}/100\n\n"

    report += "-" * 60 + "\n"
    report += "DETECTED SKILLS\n"
    report += "-" * 60 + "\n"

    if skills:

        for skill in skills:
            report += f"- {skill}\n"

    else:

        report += "No skills detected.\n"

    report += "\n"

    report += "-" * 60 + "\n"
    report += "EDUCATION\n"
    report += "-" * 60 + "\n"

    if education:

        for item in education:
            report += f"- {item}\n"

    else:

        report += "No education details detected.\n"

    report += "\n"

    report += "-" * 60 + "\n"
    report += "EXPERIENCE\n"
    report += "-" * 60 + "\n"

    if experience:

        for item in experience:
            report += f"- {item}\n"

    else:

        report += "No experience details detected.\n"

    report += "\n"

    report += "-" * 60 + "\n"
    report += "PROJECTS\n"
    report += "-" * 60 + "\n"

    if projects:

        for item in projects:
            report += f"- {item}\n"

    else:

        report += "No projects detected.\n"

    report += "\n"

    report += "-" * 60 + "\n"
    report += "CERTIFICATIONS\n"
    report += "-" * 60 + "\n"

    if certifications:

        for item in certifications:
            report += f"- {item}\n"

    else:

        report += "No certifications detected.\n"

    report += "\n"

    report += "-" * 60 + "\n"
    report += "JOB DESCRIPTION ANALYSIS\n"
    report += "-" * 60 + "\n"

    report += (
        f"Overall Job Match Score: "
        f"{overall_match_score}%\n"
    )

    report += (
        f"Keyword Skill Match: "
        f"{match_score}%\n"
    )

    report += (
        f"NLP Relevance Score: "
        f"{nlp_score}%\n\n"
    )

    report += "Matching Skills:\n"

    if matching_skills:

        for skill in matching_skills:
            report += f"- {skill}\n"

    else:

        report += "- None\n"

    report += "\nMissing Skills:\n"

    if missing_skills:

        for skill in missing_skills:
            report += f"- {skill}\n"

    else:

        report += "- None\n"

    report += "\n"

    report += "-" * 60 + "\n"
    report += "RESUME IMPROVEMENT SUGGESTIONS\n"
    report += "-" * 60 + "\n"

    for suggestion in suggestions:

        clean_suggestion = (
            suggestion
            .replace("💡 ", "")
            .replace("🎯 ", "")
            .replace("🎓 ", "")
            .replace("💼 ", "")
            .replace("📂 ", "")
            .replace("📜 ", "")
            .replace("📝 ", "")
            .replace("🚀 ", "")
            .replace("📊 ", "")
        )

        report += f"- {clean_suggestion}\n"

    report += "\n"

    report += "=" * 60 + "\n"
    report += "Generated by AI Resume Analyzer\n"
    report += "=" * 60 + "\n"

    return report


# =========================================================
# MAIN APPLICATION
# =========================================================

if uploaded_file is not None:

    st.success(
        "Resume uploaded successfully! ✅"
    )

    if uploaded_file.name.lower().endswith(".pdf"):

        resume_text = extract_pdf_text(
            uploaded_file
        )

    elif uploaded_file.name.lower().endswith(".docx"):

        resume_text = extract_docx_text(
            uploaded_file
        )

    else:

        resume_text = ""


    if resume_text.strip():

        # -------------------------------------------------
        # RESUME CONTENT
        # -------------------------------------------------

        st.markdown(
            '<div class="section-title">'
            '📝 Resume Content'
            '</div>',
            unsafe_allow_html=True
        )

        st.text_area(
            "Extracted Resume Text",
            resume_text,
            height=300
        )


        # -------------------------------------------------
        # DETECTION
        # -------------------------------------------------

        detected_skills = detect_skills(
            resume_text
        )

        detected_education = detect_education(
            resume_text
        )

        detected_experience = detect_experience(
            resume_text
        )

        detected_projects = detect_projects(
            resume_text
        )

        detected_certifications = detect_certifications(
            resume_text
        )


        # -------------------------------------------------
        # DASHBOARD
        # -------------------------------------------------

        st.markdown(
            '<div class="section-title">'
            '📊 Resume Dashboard'
            '</div>',
            unsafe_allow_html=True
        )

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.metric(
                "🛠️ Skills",
                len(detected_skills)
            )

        with col2:
            st.metric(
                "🎓 Education",
                len(detected_education)
            )

        with col3:
            st.metric(
                "💼 Experience",
                len(detected_experience)
            )

        with col4:
            st.metric(
                "📂 Projects",
                len(detected_projects)
            )

        with col5:
            st.metric(
                "📜 Certifications",
                len(detected_certifications)
            )


        # -------------------------------------------------
        # SKILLS
        # -------------------------------------------------

        st.markdown(
            '<div class="section-title">'
            '🛠️ Detected Skills'
            '</div>',
            unsafe_allow_html=True
        )

        if detected_skills:

            columns = st.columns(3)

            for index, skill in enumerate(
                detected_skills
            ):

                with columns[index % 3]:

                    st.success(
                        f"✓ {skill}"
                    )

        else:

            st.warning(
                "No matching skills detected."
            )


        # -------------------------------------------------
        # EDUCATION
        # -------------------------------------------------

        st.markdown(
            '<div class="section-title">'
            '🎓 Education'
            '</div>',
            unsafe_allow_html=True
        )

        if detected_education:

            for education in detected_education:

                st.info(
                    f"🎓 {education}"
                )

        else:

            st.warning(
                "No education details detected."
            )


        # -------------------------------------------------
        # EXPERIENCE
        # -------------------------------------------------

        st.markdown(
            '<div class="section-title">'
            '💼 Experience'
            '</div>',
            unsafe_allow_html=True
        )

        if detected_experience:

            for experience in detected_experience:

                st.warning(
                    f"💼 {experience}"
                )

        else:

            st.warning(
                "No experience details detected."
            )


        # -------------------------------------------------
        # PROJECTS
        # -------------------------------------------------

        st.markdown(
            '<div class="section-title">'
            '📂 Projects'
            '</div>',
            unsafe_allow_html=True
        )

        if detected_projects:

            for project in detected_projects:

                st.info(
                    f"📂 {project}"
                )

        else:

            st.warning(
                "No project details detected."
            )


        # -------------------------------------------------
        # CERTIFICATIONS
        # -------------------------------------------------

        st.markdown(
            '<div class="section-title">'
            '📜 Certifications'
            '</div>',
            unsafe_allow_html=True
        )

        if detected_certifications:

            for certification in detected_certifications:

                st.success(
                    f"📜 {certification}"
                )

        else:

            st.warning(
                "No certification details detected."
            )


        # -------------------------------------------------
        # ATS SCORE
        # -------------------------------------------------

        ats_score = calculate_ats_score(
            resume_text,
            detected_skills,
            detected_education,
            detected_experience,
            detected_projects,
            detected_certifications
        )

        st.markdown(
            '<div class="section-title">'
            '📊 ATS Resume Score'
            '</div>',
            unsafe_allow_html=True
        )

        score_col1, score_col2 = st.columns(2)

        with score_col1:

            st.metric(
                "Overall ATS Score",
                f"{ats_score}/100"
            )

        with score_col2:

            if ats_score >= 80:

                st.success(
                    "🎉 Excellent resume! "
                    "Your ATS score is strong."
                )

            elif ats_score >= 60:

                st.info(
                    "👍 Good resume! "
                    "There is room for improvement."
                )

            else:

                st.warning(
                    "⚠️ Your resume needs improvement."
                )

        st.progress(
            ats_score / 100
        )


        # -------------------------------------------------
        # JOB DESCRIPTION MATCHING
        # -------------------------------------------------

        st.markdown(
            '<div class="section-title">'
            '🎯 Job Description Matching'
            '</div>',
            unsafe_allow_html=True
        )

        job_description = st.text_area(
            "Paste the Job Description here",
            height=200,
            placeholder=(
                "Example: Looking for a Python Developer "
                "with SQL, Git, Machine Learning and "
                "Communication skills."
            )
        )

        match_score = 0
        matching_skills = []
        missing_skills = []
        nlp_score = 0
        overall_match_score = 0


        if job_description.strip():

            # ---------------------------------------------
            # KEYWORD MATCH
            # ---------------------------------------------

            (
                match_score,
                matching_skills,
                missing_skills
            ) = match_job_description(
                resume_text,
                job_description
            )


            # ---------------------------------------------
            # NLP MATCH
            # ---------------------------------------------

            nlp_score = calculate_nlp_similarity(
                resume_text,
                job_description
            )


            # ---------------------------------------------
            # OVERALL MATCH
            # ---------------------------------------------

            overall_match_score = calculate_overall_match(
                match_score,
                nlp_score
            )


            # ---------------------------------------------
            # OVERALL SCORE
            # ---------------------------------------------

            st.markdown(
                "### 🏆 Overall Job Match Score"
            )

            st.metric(
                "Resume ↔ Job Description Match",
                f"{overall_match_score}%"
            )

            st.progress(
                overall_match_score / 100
            )


            if overall_match_score >= 80:

                st.success(
                    "🎉 Excellent match! "
                    "Your resume is highly relevant to this job."
                )

            elif overall_match_score >= 60:

                st.info(
                    "👍 Good match! "
                    "A few improvements can make your resume stronger."
                )

            else:

                st.warning(
                    "⚠️ Low match. "
                    "Consider improving your resume for this job."
                )


            # ---------------------------------------------
            # SCORE BREAKDOWN
            # ---------------------------------------------

            st.markdown(
                "### 📊 Match Score Breakdown"
            )

            score_col1, score_col2 = st.columns(2)

            with score_col1:

                st.metric(
                    "🎯 Keyword Skill Match",
                    f"{match_score}%"
                )

                st.progress(
                    match_score / 100
                )

            with score_col2:

                st.metric(
                    "🧠 NLP Relevance",
                    f"{nlp_score}%"
                )

                st.progress(
                    nlp_score / 100
                )


            # ---------------------------------------------
            # MATCHING SKILLS
            # ---------------------------------------------

            skill_col1, skill_col2 = st.columns(2)

            with skill_col1:

                st.markdown(
                    "### ✅ Matching Skills"
                )

                if matching_skills:

                    for skill in matching_skills:

                        st.success(
                            f"✓ {skill}"
                        )

                else:

                    st.info(
                        "No matching skills found."
                    )


            with skill_col2:

                st.markdown(
                    "### ❌ Missing Skills"
                )

                if missing_skills:

                    for skill in missing_skills:

                        st.error(
                            f"✗ {skill}"
                        )

                else:

                    st.success(
                        "🎉 No missing skills!"
                    )


            st.info(
                "🧠 The overall match combines keyword skill "
                "matching and TF-IDF text similarity. "
                "It is an automated relevance estimate, "
                "not a hiring decision."
            )


        # -------------------------------------------------
        # SUGGESTIONS
        # -------------------------------------------------

        st.markdown(
            '<div class="section-title">'
            '💡 Resume Improvement Suggestions'
            '</div>',
            unsafe_allow_html=True
        )

        suggestions = generate_suggestions(
            detected_skills,
            detected_education,
            detected_experience,
            detected_projects,
            detected_certifications,
            missing_skills
        )

        for suggestion in suggestions:

            st.info(
                suggestion
            )


        # -------------------------------------------------
        # DOWNLOAD REPORT
        # -------------------------------------------------

        st.markdown(
            '<div class="section-title">'
            '📥 Download Analysis Report'
            '</div>',
            unsafe_allow_html=True
        )

        report = create_report(
            uploaded_file.name,
            ats_score,
            detected_skills,
            detected_education,
            detected_experience,
            detected_projects,
            detected_certifications,
            match_score,
            matching_skills,
            missing_skills,
            nlp_score,
            overall_match_score,
            suggestions
        )

        st.download_button(
            label="📥 Download Resume Analysis Report",
            data=report,
            file_name="resume_analysis_report.txt",
            mime="text/plain"
        )


        # -------------------------------------------------
        # FOOTER
        # -------------------------------------------------

        st.markdown(
            '<div class="footer">'
            '🤖 AI Resume Analyzer | '
            'Built with Python, Streamlit & Scikit-learn'
            '</div>',
            unsafe_allow_html=True
        )


    else:

        st.warning(
            "Could not extract text from this resume."
        )