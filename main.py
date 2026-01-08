import streamlit as st
from dotenv import load_dotenv
import os
import zipfile
import pymupdf
import pandas as pd
import shutil
import time
from typing import TypedDict, Annotated
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GEM")


model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2
)


class ResumeOutput(TypedDict):
    name: Annotated[str, "Extract the full name of the candidate"]
    experience: Annotated[int, "Total years of experience"]
    qualification: Annotated[str, "Highest qualification"]
    skills: Annotated[list[str], "List of technical skills"]
    summary: Annotated[str, "Short professional summary"]
    projects: Annotated[list[str], "Key projects mentioned"]
    links: Annotated[list[str], "Professional or portfolio links"]

model_with_schema = model.with_structured_output(ResumeOutput)


st.set_page_config(
    page_title="AI Resume Intelligence System",
    page_icon="📄",
    layout="centered"
)

st.title("📄 AI-Driven Resume Intelligence System")
st.write("Upload a ZIP file containing resumes (PDF format)")
st.write("The system will extract structured data and export it as a CSV file")


uploaded_zip = st.file_uploader(
    "Upload ZIP file",
    type=["zip"]
)

process_btn = st.button("🚀 Process Resumes")


if process_btn:
    if uploaded_zip is None:
        st.warning("Please upload a ZIP file before processing.")
    else:
        with st.spinner("Processing resumes..."):
            extracted_data = []
            extract_folder = "temp_resumes"

            # Create temp folder
            os.makedirs(extract_folder, exist_ok=True)

            try:
                # Extract ZIP
                with zipfile.ZipFile(uploaded_zip, "r") as zip_ref:
                    zip_ref.extractall(extract_folder)

                # Process each PDF resume
                for file in os.listdir(extract_folder):
                    if file.lower().endswith(".pdf"):
                        file_path = os.path.join(extract_folder, file)

                        # Extract text from PDF
                        doc = pymupdf.open(file_path)
                        resume_text = ""
                        for page in doc:
                            resume_text += page.get_text()
                        doc.close()

                        # Invoke LLM with structured output
                        result = model_with_schema.invoke(resume_text)
                        extracted_data.append(result)

                        # Delay to avoid API rate limits
                        time.sleep(2)

                # Convert to CSV
                df = pd.DataFrame(extracted_data)
                csv_output = df.to_csv(index=False)

                st.success("✅ Resumes processed successfully!")

                st.download_button(
                    label="⬇️ Download CSV",
                    data=csv_output,
                    file_name="resume_data.csv",
                    mime="text/csv"
                )

            finally:
                
                shutil.rmtree(extract_folder, ignore_errors=True)

