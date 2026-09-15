# 🤖 AI Resume Analyzer

> An intelligent web-based Resume Analyzer that evaluates ATS readiness, extracts resume information, matches resumes with job descriptions, and provides actionable improvement suggestions.

## 🚀 Live Demo

👉 **[Try AI Resume Analyzer](https://dharunya-ai-resume-2609.streamlit.app/)**

## 📌 Project Overview

**AI Resume Analyzer** is a Python and Streamlit-based web application designed to help job seekers analyze and improve their resumes.

The application extracts important information from uploaded resumes, evaluates ATS compatibility, compares the resume with a given job description, identifies matching skills, and provides suggestions to improve the resume.

## ✨ Features

* 📄 Upload resumes directly through the web application
* 📝 Extract resume text automatically
* 🛠️ Detect technical and soft skills
* 🎓 Identify education details
* 💼 Extract experience information
* 📂 Detect projects
* 📜 Identify certifications and courses
* 📊 Calculate an ATS Resume Score
* 🎯 Match resumes against job descriptions
* 📈 Generate Job Match Score
* 🔎 Identify matching skills
* ❌ Identify missing skills
* 🧠 Perform NLP-based relevance analysis
* 💡 Provide resume improvement suggestions
* 📥 Download the analysis report

## 📊 Analysis Dashboard

The application provides a dashboard containing:

| Section           | Purpose                                |
| ----------------- | -------------------------------------- |
| 🛠️ Skills        | Detects skills mentioned in the resume |
| 🎓 Education      | Extracts educational qualifications    |
| 💼 Experience     | Identifies work/internship experience  |
| 📂 Projects       | Detects project information            |
| 📜 Certifications | Identifies certifications and courses  |
| 📊 ATS Score      | Evaluates ATS readiness                |
| 🎯 Job Match      | Compares resume with a job description |
| 💡 Suggestions    | Provides improvement recommendations   |

## 🧠 How It Works

```text
User Uploads Resume
        ↓
Resume Text Extraction
        ↓
Resume Information Analysis
        ↓
Skills / Education / Experience / Projects / Certifications
        ↓
ATS Score Calculation
        ↓
Job Description Matching
        ↓
Keyword & NLP Analysis
        ↓
Improvement Suggestions
        ↓
Download Analysis Report
```

## 🎯 Job Description Matching

Users can paste a job description into the application.

The system analyzes the relationship between the resume and the job description using:

* 🔑 Keyword Skill Matching
* 🧠 NLP / TF-IDF Relevance
* 📊 Overall Match Score

The result helps users understand how well their resume aligns with a particular job description.

> **Note:** The match score is an automated relevance estimate and is not a hiring decision.

## 🛠️ Technologies Used

| Technology                   | Purpose                             |
| ---------------------------- | ----------------------------------- |
| 🐍 Python                    | Application development             |
| 🎈 Streamlit                 | Web application framework           |
| 🧠 NLP                       | Resume and job description analysis |
| 📊 TF-IDF                    | Text similarity analysis            |
| 📄 DOCX Processing           | Resume text extraction              |
| 🐙 GitHub                    | Source code management              |
| ☁️ Streamlit Community Cloud | Application deployment              |

## 📸 Screenshots

### 🏠 Resume Upload & Dashboard

![Resume Dashboard](Screenshots/dashboard.png)

### 📊 ATS Resume Score

![ATS Score](Screenshots/ats-score.png)

### 🎯 Job Description Matching

![Job Match](Screenshots/job-match.png)

> **Note:** Make sure the screenshot filenames above match the actual files inside the `Screenshots` folder.

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/kittyyash/AI-Resume-Analyzer.git
```

### 2. Navigate to the project

```bash
cd AI-Resume-Analyzer
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📁 Project Structure

```text
AI-Resume-Analyzer/
│
├── Screenshots/
│   ├── dashboard.png
│   ├── ats-score.png
│   └── job-match.png
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ☁️ Deployment

The application is deployed using **Streamlit Community Cloud**.

### 🌐 Live Application

👉 **https://dharunya-ai-resume-2609.streamlit.app/**

The deployed application can be accessed through a web browser without requiring Python or VS Code on the user's device.

## 🔮 Future Enhancements

* 🤖 AI-powered resume recommendations
* 📑 Support for additional resume formats
* 🎨 Improved dashboard UI
* 📊 Advanced resume analytics
* 💼 Job-specific resume optimization
* 🔐 User authentication
* ☁️ Database integration
* 📈 Resume comparison across multiple job descriptions

## 👩‍💻 Author

**Dharunya**

### 🔗 Project Links

* 🌐 **Live Demo:** [AI Resume Analyzer](https://dharunya-ai-resume-2609.streamlit.app/)
* 🐙 **GitHub Repository:** [AI-Resume-Analyzer](https://github.com/kittyyash/AI-Resume-Analyzer)

---

⭐ **If you find this project useful, consider giving the repository a star!**

**Built with ❤️ using Python and Streamlit**

