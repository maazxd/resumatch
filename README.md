# 📄 Resume ATS Tracker

An AI-powered resume analysis and interview preparation tool that helps job seekers optimize their resumes for Applicant Tracking Systems (ATS) and prepare for interviews.

## ✨ Features

- **📊 Resume Analysis** - Get comprehensive insights into your resume's strengths and weaknesses
- **💡 Skill Recommendations** - Receive personalized suggestions to improve your skillset based on job requirements
- **🎯 ATS Match Score** - Calculate how well your resume matches the job description with missing keywords analysis
- **💬 Interview Questions** - Generate relevant interview questions based on the job role and your experience
- **✍️ Answer Guide** - Get professional sample answers tailored to your resume and the position

## 🚀 Demo

Upload your resume and paste a job description to:
- Analyze your resume against job requirements
- Get an ATS compatibility score
- Prepare for interviews with custom questions and answers
- Identify skill gaps and improvement areas

## 🛠️ Technologies Used

- **Python 3.10+**
- **Streamlit** - Web interface
- **Google Gemini AI** - AI-powered analysis
- **PyMuPDF (fitz)** - PDF processing
- **python-dotenv** - Environment management

## 📋 Prerequisites

- Python 3.10 or higher
- Google Gemini API key ([Get it here](https://aistudio.google.com/apikey))
- Virtual environment (recommended)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/maazxd/resume-ats-tracker.git
   cd resume-ats-tracker
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv myvenv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     myvenv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source myvenv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   ```

## 🎯 Usage

1. **Start the application**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser**
   - The app will automatically open at `http://localhost:8501`

3. **Use the application**
   - Paste a job description in the left panel
   - Upload your resume (PDF format) in the right panel
   - Choose an analysis type:
     - **Analyze Resume** - Get detailed resume insights
     - **Skill Tips** - Receive improvement recommendations
     - **Match Score** - Check ATS compatibility
     - **Interview Questions** - Generate relevant questions
     - **Answer Guide** - Get professional answer examples

## 📁 Project Structure

```
resume-ats-tracker/
│
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
├── .gitignore            # Git ignore file
├── README.md             # Project documentation
└── myvenv/               # Virtual environment (not in repo)
```

## 🔑 Getting Your API Key

1. Visit [Google AI Studio](https://aistudio.google.com/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key and add it to your `.env` file

**Note:** The free tier has rate limits (5 requests/minute). Wait between requests or upgrade for higher limits.

## ⚙️ Configuration

The application uses Google's Gemini 2.5 Flash model by default. You can modify the model in `app.py`:

```python
model = genai.GenerativeModel('gemini-2.5-flash')
```

## 🎨 Features in Detail

### Resume Analysis
Provides a comprehensive breakdown of your resume including:
- Skills assessment
- Experience evaluation
- Strengths and weaknesses
- Professional summary

### ATS Match Score
- Percentage match with job description
- Missing keywords identification
- Optimization recommendations
- Final hiring insights

### Interview Preparation
- Role-specific questions
- Behavioral questions
- Technical scenarios
- Sample answers using STAR method

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🐛 Known Issues

- API rate limits on free tier (5 requests/minute)
- PDF text extraction may not work perfectly with image-based PDFs
- Large resumes may take longer to process

## 🔮 Future Enhancements

- [ ] Support for multiple file formats (DOCX, TXT)
- [ ] Resume formatting checker
- [ ] Cover letter generator
- [ ] LinkedIn profile analyzer
- [ ] Salary estimation feature
- [ ] Multiple resume comparison
- [ ] Export results as PDF

## 👤 Author

**Muaaz**
- GitHub: [@maazxd](https://github.com/maazxd)

## 🙏 Acknowledgments

- Google Gemini AI for powerful language models
- Streamlit for the amazing web framework
- PyMuPDF for PDF processing capabilities

---

⭐ If you find this project helpful, please give it a star!
