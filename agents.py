from crewai import Agent
# this import helps clean up strings from whitespaces
from textwrap import dedent
from langchain_openai import ChatOpenAI
from crewai_tools import PDFSearchTool
import os


class CustomAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)


    def finder_agent(self):
        pdf_folder = "pdfs"  # Folder name containing PDF files
        pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
        pdf_tools = [PDFSearchTool(os.path.join(pdf_folder, pdf_file)) for pdf_file in pdf_files]
        
        return Agent(
            role="Senior Information Finder",
            backstory=dedent(f"""You are the expert of finding where information lives!"""),
            goal=dedent(f"""Find the relevant pdf file with the information needed."""),
            verbose=True,
            tools=pdf_tools,
            llm=self.OpenAIGPT35,
        )
    
    def analysis_agent(self):
        pdf_folder = "pdfs"  # Folder name containing PDF files
        pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
        pdf_tools = [PDFSearchTool(os.path.join(pdf_folder, pdf_file)) for pdf_file in pdf_files]

        return Agent(
            role="Senior Document Analyst",
            backstory=dedent(f"""You are an expert at analyzing multiple documents. 
            Your ability to find and summarize information across various PDFs is unparalleled."""),
            goal=dedent(f"""Give a summary for each pdf document given by the finder agent. Each summary should have the pdf file name and a list of bullet point summary."""),
            verbose=True,
            tools=pdf_tools,
            llm=self.OpenAIGPT4,
        )
    
