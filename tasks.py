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
            Within the pdf files available there is revelant information on the topic of {var1}. Please create appropriate summaries for each pdf file with at least 5-6 sentences in json format.
            
            {self.__tip_section()}
    
            Make sure to be as accurate as possible. 
        """
            ),
            expected_output="Provide concise summaries of 5-6 sentences for each PDF document in JSON format, where the key is the file name.",
            agent=agent,
            output_file="output/summaries.json",
        )
    
    def ppt_task(self, agent, var1):
        return Task(
            description=dedent(
                f"""
            Create a detailed PowerPoint template in TXT format specifying what goes into each slide. 
            Include potential graphs and graphics based on the data provided by the pdf agent.
            
            {self.__tip_section()}
    
            Make sure to be as accurate as possible. 
            """
            ),
            expected_output="PowerPoint presentation template was created about {var1} with information provided by the pdf agent summaries, including potential graphs and graphics.",
            agent=agent,
            output_file="output/presentation.txt"
        )
