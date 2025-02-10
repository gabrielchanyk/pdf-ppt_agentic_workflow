from crewai import Agent, LLM
# this import helps clean up strings from whitespaces
from textwrap import dedent
from langchain_openai import ChatOpenAI
from crewai_tools import PDFSearchTool
import os

class CustomAgents:
    def __init__(self):
        self.llm = LLM(model="ollama/phi3:3.8b")


    def finder_agent(self):
        pdf_folder = "pdfs"  # Folder name containing PDF files
        pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
        pdf_tools = [PDFSearchTool(os.path.join(pdf_folder, pdf_file)) for pdf_file in pdf_files]
        
        return Agent(
            role="Senior Information Finder",
            backstory=dedent(f"""You can find anything in a pdf.  The people need you."""),
            goal=dedent(f"""Uncover any information from pdf files exceptionally well and provide amazing summaries of key topics."""),
            verbose=True,
            tools=pdf_tools,
            llm=self.llm,
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
            llm=self.llm,
        )

 #powerpoint agent
# ppt_agent = Agent(
#     role="Google Sheets Assistant",
#     goal="Read Google Sheets Data",
#     backstory=f"""
#             You are an AI assistant specialising in creating PowerPoint presentations using the Python-PPTX library. 
#             Your task is to analyze the Google Sheets data from the provided spreadsheet ID: {GOOGLE_SHEET_ID}. 
#             Extract critical insights and generate relevant charts based on this data. 
#             Finally, create a well-structured presentation that includes these charts and any necessary images, ensuring the formatting is professional and visually appealing. 
#             Only the spreadsheet ID should be passed as input parameters when utilising the Google Sheets tool.
#             NOTE: The user usually passes small sheets, so try to read the whole sheet at once and not via ranges.
#     """,
#     tools=tools,
# )

# agent_task = Task(
#     description=f"""
#     Create a ppt on the google sheets: {GOOGLE_SHEET_ID}. 
#     Create a sandbox
#     First, retrieve the sheet's content, and then pip installs the python-pptx using a code interpreter.
#     After that, run the code to create graphs from the data.
#     Then, write the code using Python-pptx to create a PowerPoint.

#     Ensure that the ppt is detailed and has proper formatting 
#     that makes it look good. The graphs in it should be factual. 
#     NOTE: Mostly, the user passes small sheets, so try to read the whole sheet at once and not via ranges.
#     """,
#     expected_output="Sheet was read, graphs were plotted, and Presentation was created",
#     tools=tools,
#     agent=ppt_agent,
#     verbose=True,
# )