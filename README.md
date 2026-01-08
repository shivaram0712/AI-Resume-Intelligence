📄 AI-Driven Resume Intelligence System
📌 Project Overview
The AI-Driven Resume Intelligence System is a Streamlit-based application that automates the process of analyzing multiple resumes using Artificial Intelligence.
Instead of manually reading resumes one by one, this system:


Accepts resumes in bulk (ZIP format)


Extracts text from PDF resumes


Uses an AI model to convert unstructured resume data into structured information


Exports the final result as a CSV file for easy analysis


This project focuses on prompt engineering, structured output, and real-world AI application design.

🎯 Objective of the Project
The main objectives of this project are:


To automate resume screening using AI


To convert unstructured resume text into structured data


To demonstrate effective use of prompt templates


To generate HR-friendly outputs in CSV format


To build a clean and simple AI application using Streamlit



🧠 How the System Works


User uploads a ZIP file containing multiple PDF resumes


The system extracts all resumes from the ZIP file


Text is extracted from each PDF resume


The extracted text is passed to an AI model with a clear prompt


The AI extracts structured fields such as:


Name


Experience


Qualification


Skills


Projects


Summary


Links




All extracted data is combined into a single CSV file


User downloads the CSV file through the Streamlit interface



📂 Project Structure
resume_ai_project/
│
├── main.py        # Main Streamlit application
├── req.txt        # Required dependencies
├── .env           # API key configuration (ignored by Git)
├── .gitignore     # Prevents sensitive files from being pushed


🛠️ Technology Stack
LayerTechnologyFrontendStreamlitAI FrameworkLangChainLLMGoogle Gemini 2.5 FlashPDF ParsingPyMuPDFData HandlingPandasEnvironment Managementpython-dotenv

🔐 Prompt Engineering & Structured Output


A prompt template is used to instruct the AI on what information to extract


Structured output (TypedDict) is enforced to ensure:


Consistent fields for every resume


No missing or hallucinated data


Reliable CSV generation




This approach simulates real-world enterprise AI pipelines.

▶️ How to Run the Project
1️⃣ Install dependencies
pip install -r req.txt

2️⃣ Add API key
Create a .env file:
GEM=your_google_api_key_here

3️⃣ Run the application
streamlit run main.py

4️⃣ Use the app


Upload a ZIP file containing PDF resumes


Click Process Resumes


Download the generated CSV file



📈 Learning Outcomes
By completing this project, I gained hands-on experience in:


Prompt engineering for structured AI outputs


Using LangChain with Gemini LLMs


Processing unstructured documents using AI


Building interactive AI applications with Streamlit


Converting AI output into usable business data formats



🚀 Future Improvements


Support for DOCX resumes


Enhanced UI design


Resume ranking and scoring


Deployment on Streamlit Cloud


Error handling for scanned resumes



👤 Author
Sangem Shiva Ram
Agentic AI Student | AI & Data Enthusiast

⭐ Final Note
This project demonstrates how AI can be applied to solve practical problems such as resume screening while maintaining control, structure, and reliability in AI outputs.

I
