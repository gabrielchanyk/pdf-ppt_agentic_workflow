from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks:
    def __tip_section(self):
        return "I'll give you a huge commission for your work!"
    
    def pdf_task(self, agent, var1):
        return Task(
            description=dedent(
                f"""
            Tell me precisely what I need to know from the pdfs with the focus of {var1}.
            
            {self.__tip_section()}
    
            Make sure to be as accurate as possible. 
        """
            ),
            expected_output="Full analysis on the topic given by {var1} providing all information in json format. Give summaries at least 5 - 10 sentences long of all pdf files.",
            agent=agent,
            output_file="output/summaries.json",
        )
    
    def ppt_task(self, agent, var1):
        return Task(
            description=dedent(
                f"""
            Pip installs the python-pptx using a code interpreter.
            After that, run the code to create graphs from the data.
            Then, write the code using Python-pptx to create a PowerPoint.

            Ensure that the ppt is detailed and has proper formatting 
            that makes it look good. The graphs in it should be factual. 
            
            {self.__tip_section()}
    
            Make sure to be as accurate as possible. 
            """
            ),
            expected_output="Powerpoint presentation was created about {var1} with all information provided by the pdf agent not just an outline.",
            agent=agent,
            output_file="output/presentation.txt"
        )
