from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import fitz  # PyMuPDF
import google.generativeai as genai
import io
import base64
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,pdf_text,prompt):
    model=genai.GenerativeModel('gemini-2.5-flash')
    full_prompt = f"{prompt}\n\nJob Description:\n{input}\n\nResume Content:\n{pdf_text}"
    response=model.generate_content(full_prompt)
    return response.text

def input_pdf_convert(uploaded_file):
    if uploaded_file is not None:
        # Open PDF with PyMuPDF and extract text
        pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text = ""
        for page in pdf_document:
            text += page.get_text()
        pdf_document.close()
        return text
    else:
        raise FileNotFoundError("No file uploaded")

st.set_page_config(page_title="Resume ATS Tracker",page_icon="📄",layout="wide")

# Professional CSS styling
st.markdown("""
    <style>
    /* Main container styling */
    .main {
        padding: 2rem;
    }
    
    /* Header styling */
    .header-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2.5rem 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .header-title {
        color: white;
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
        margin: 0;
        letter-spacing: -0.5px;
    }
    
    .header-subtitle {
        color: rgba(255,255,255,0.9);
        font-size: 1.1rem;
        text-align: center;
        margin-top: 0.5rem;
        font-weight: 400;
    }
    
    /* Button styling */
    div.stButton > button {
        width: 100%;
        height: 65px;
        border-radius: 10px;
        font-weight: 600;
        font-size: 0.95rem;
        border: 2px solid transparent;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    div.stButton > button:hover {
        background-color: #667eea !important;
        border-color: #667eea !important;
        color: white !important;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(102,126,234,0.3);
    }
    
    div.stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
    }
    
    /* Text area styling */
    .stTextArea textarea {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        font-size: 0.95rem;
        padding: 1rem;
    }
    
    .stTextArea textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 2px rgba(102,126,234,0.2);
    }
    
    /* File uploader styling */
    .uploadedFile {
        border-radius: 10px;
    }
    
    /* Section headers */
    .section-header {
        color: #2c3e50;
        font-size: 1.3rem;
        font-weight: 600;
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #667eea;
    }
    
    /* Success message */
    .stSuccess {
        border-radius: 10px;
    }
    
    /* Response container */
    .response-box {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Professional Header
st.markdown("""
    <div class="header-container">
        <h1 class="header-title">Resume ATS Tracker</h1>
        <p class="header-subtitle">Optimize your resume and ace your interviews with AI-powered insights</p>
    </div>
""", unsafe_allow_html=True)

# Create two columns for input layout
col1, col2 = st.columns([1.2, 1], gap="large")

with col1:
    st.markdown("### 📋 Job Description")
    input_text=st.text_area(
        "Paste the job description here",
        key="input", 
        height=320, 
        placeholder="Enter the complete job description including requirements, responsibilities, and qualifications...",
        label_visibility="collapsed"
    )

with col2:
    st.markdown("### 📄 Upload Resume")
    uploaded_file=st.file_uploader(
        "Choose PDF file",
        type=["pdf"],
        label_visibility="collapsed"
    )
    if uploaded_file is not None:
        st.success("✅ Resume uploaded successfully!")
        st.info(f"📎 {uploaded_file.name}")

# Initialize session state
if 'selected_button' not in st.session_state:
    st.session_state.selected_button = None

# Section divider
st.markdown("<div class='section-header'>🔍 Choose Analysis Type</div>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# First row of buttons
col_btn1, col_btn2, col_btn3 = st.columns(3)

with col_btn1:
    submit1=st.button("📊 Analyze Resume", use_container_width=True, 
                      type="primary" if st.session_state.selected_button == 1 else "secondary")
    if submit1:
        st.session_state.selected_button = 1
    
with col_btn2:
    submit2=st.button("💡 Skill Tips", use_container_width=True, 
                      type="primary" if st.session_state.selected_button == 2 else "secondary")
    if submit2:
        st.session_state.selected_button = 2
    
with col_btn3:
    submit3=st.button("🎯 Match Score", use_container_width=True, 
                      type="primary" if st.session_state.selected_button == 3 else "secondary")
    if submit3:
        st.session_state.selected_button = 3

# Second row of buttons
st.markdown("<br>", unsafe_allow_html=True)
col_btn4, col_btn5 = st.columns(2)

with col_btn4:
    submit4=st.button("💬 Interview Questions", use_container_width=True, 
                      type="primary" if st.session_state.selected_button == 4 else "secondary")
    if submit4:
        st.session_state.selected_button = 4

with col_btn5:
    submit5=st.button("✍️ Answer Guide", use_container_width=True, 
                      type="primary" if st.session_state.selected_button == 5 else "secondary")
    if submit5:
        st.session_state.selected_button = 5

input_prompt1="You are an experienced HR person in field of devops, web development, data science. Your job is to analyze the resume and give a brief summary of the candidate's skills, experience, and qualifications based on the resume provided. Provide insights into the candidate's strengths and areas for improvement. Highlight the strengths and weaknesses of the candidate."

input_prompt2="You are an experienced HR person in field of devops, web development, data science. Your task is to provide suggestions on how the candidate can improve their skills based on the resume and job description provided. Focus on specific skills, certifications, or experiences that would make the candidate more competitive."

input_prompt3="""
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. 
Your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

input_prompt4="""
Based on the job requirements and the candidate's background, create 8-10 thoughtful interview questions that would naturally come up in a real conversation. 

Mix different types:
- A couple questions about their specific experience with [key technologies/tools from job description]
- Questions about how they've handled real situations (like debugging tough problems or working with teams)
- One or two technical scenarios they might face in this role
- Questions about their approach to learning new things or staying current

Keep the tone conversational and direct - how a hiring manager would actually ask them, not overly formal. Focus on what would genuinely help assess if they're a good fit for this specific role.
"""

input_prompt5="""
You're helping someone prepare for an interview. Based on the job description and their resume, create sample answers to likely interview questions.

For each answer:
- Draw from their actual experience mentioned in the resume
- Use the STAR method where it makes sense (Situation, Task, Action, Result) but keep it natural
- Keep answers between 1-2 minutes when spoken (about 150-250 words)
- Sound like a real person talking, not rehearsed or robotic
- Include specific examples and metrics when possible
- Show enthusiasm for the role without overdoing it

Cover these types of questions:
1. "Tell me about yourself" - professional summary
2. "Why are you interested in this position?"
3. A technical question about their main skill
4. A behavioral question about handling challenges
5. "Where do you see yourself in a few years?"
6. "Do you have any questions for us?" - suggest 2-3 smart questions they could ask

Make it sound authentic - like advice from an experienced colleague, not a script.
"""

if submit1:
    if uploaded_file is not None:
        with st.spinner("Analyzing resume..."):
            pdf_content=input_pdf_convert(uploaded_file)
            response=get_gemini_response(input_text,pdf_content,input_prompt1)
        st.markdown("---")
        st.markdown("### 📊 Resume Analysis")
        st.write(response)
    else:
        st.warning("⚠️ Please upload a resume to proceed.")

elif submit2:
    if uploaded_file is not None:
        with st.spinner("Generating skill recommendations..."):
            pdf_content=input_pdf_convert(uploaded_file)
            response=get_gemini_response(input_text,pdf_content,input_prompt2)
        st.markdown("---")
        st.markdown("### 💡 Skill Improvement Recommendations")
        st.write(response)
    else:
        st.warning("⚠️ Please upload a resume to proceed.")

elif submit3:
    if uploaded_file is not None:
        with st.spinner("Calculating match score..."):
            pdf_content=input_pdf_convert(uploaded_file)
            response=get_gemini_response(input_text,pdf_content,input_prompt3)
        st.markdown("---")
        st.markdown("### 🎯 ATS Match Score")
        st.write(response)
    else:
        st.warning("⚠️ Please upload a resume to proceed.")

elif submit4:
    if uploaded_file is not None:
        with st.spinner("Preparing interview questions..."):
            pdf_content=input_pdf_convert(uploaded_file)
            response=get_gemini_response(input_text,pdf_content,input_prompt4)
        st.markdown("---")
        st.markdown("### 💬 Interview Questions")
        st.write(response)
    else:
        st.warning("⚠️ Please upload a resume to proceed.")

elif submit5:
    if uploaded_file is not None:
        with st.spinner("Creating answer guide..."):
            pdf_content=input_pdf_convert(uploaded_file)
            response=get_gemini_response(input_text,pdf_content,input_prompt5)
        st.markdown("---")
        st.markdown("### ✍️ Professional Answer Guide")
        st.write(response)
    else:
        st.warning("⚠️ Please upload a resume to proceed.")



