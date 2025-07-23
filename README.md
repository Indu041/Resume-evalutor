App Link:https://resume-evalutor-vdvjvni3nz7sqtvblkmahu.streamlit.app/

The Resume Evaluator is an intelligent web-based tool that helps users analyze their resumes and get matched with suitable job roles based on their skills, experience, and keywords. Powered by Natural Language Processing (NLP), the system parses uploaded resumes, extracts relevant skills and qualifications, and compares them with predefined job role templates using similarity scores.

💡 Key Features:
Resume Parsing: Automatically extracts skills, education, experience, and project details from a user's resume (PDF or DOCX).

Skill Extraction using NLP: Uses spaCy and custom keyword dictionaries to identify technical and soft skills.

Role Matching: Compares extracted skills with a database of job roles using cosine similarity or embeddings to find the best fit.

Job Role Generator (Optional): Recommends roles not only from existing data but can also generate personalized role titles using Generative AI (GPT).

Match Score: Displays a match percentage between the resume and each job role.

Feedback & Recommendations: Provides suggestions to improve resume relevance for the target roles.

⚙️ Tech Stack:
Frontend: Streamlit 

Backend: Python

NLP Libraries: spaCy, scikit-learn

Similarity: Cosine similarity or semantic embeddings
