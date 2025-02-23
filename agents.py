from crewai import Agent
# this import helps clean up strings from whitespaces
from textwrap import dedent
from langchain_openai import ChatOpenAI
from crewai_tools import PDFSearchTool, JSONSearchTool
import os


class CustomAgents:
    def __init__(self):
        # temperature is used to control "creativity" or randomness of text generated
        self.OpenAIGPT35_robust = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3)
        self.OpenAIGPT35_creative = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.9)


    def pdf_agent(self):
        pdf_folder = "pdfs"  # Folder name containing PDF files
        pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
        pdf_tools = [PDFSearchTool(os.path.join(pdf_folder, pdf_file)) for pdf_file in pdf_files]
        
        return Agent(
            role="Senior Information Analyst",
            backstory=dedent(f"""   You are a highly skilled AI developed to assist in the extraction and analysis of information from PDF documents. 
            Your expertise lies in sifting through vast amounts of data to uncover critical insights and details that are often overlooked. 
            You provide concise summaries of 5-6 sentences for each document, ensuring that the most important information is highlighted. 
            The people rely on your advanced capabilities to find and interpret information that is crucial for making informed decisions. 
            With your help, they can navigate through complex documents with ease and confidence."""),
            goal=dedent(f"""
            Provide concise summaries of 5-6 sentences for each PDF document in JSON format, where the key is the file name.
            """),
            verbose=True,
            tools=pdf_tools,
            llm=self.OpenAIGPT35_robust,
        )

    #powerpoint agent
    def ppt_agent(self):
        # json_tool = JSONSearchTool("summaries.json")
        return Agent(
            role="PowerPoint Assistant",
            goal="Create PowerPoint presentation text templates",
            backstory=dedent(f"""
            You are an AI assistant specializing in creating PowerPoint presentations. 
            Your task is to analyze the summaries from the pdf agent, 
            extract critical insights, and generate relevant charts based on this data. 
            Finally, create a well-structured presentation that includes these charts and any necessary images, 
            ensuring the formatting is professional and visually appealing. 
            Additionally, provide a template slide deck in TXT format using the information from the pdf agent, 
            ensuring a minimum of 6 slides.
            """),
            verbose=True,
            # tools=[json_tool],
            llm=self.OpenAIGPT35_creative,
        )
