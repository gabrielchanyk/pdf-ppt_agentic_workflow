from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks:
    def __tip_section(self):
        return "I'll give you a huge commission for your work!"
    
    def finder_task(self, agent, var1):
        return Task(
            description=dedent(
                f"""
            Identify which pdfs uses the "{var1}" keyword and list the pdfs
                                       
            {self.__tip_section()}
        """
            ),
            expected_output="Give the names of the pdfs with the relevant information to the analysis agent for use",
            agent=agent,
        )

    def analyze_task(self, agent, var1):
        return Task(
            description=dedent(
                f"""
            Summarize each of the pdfs in the list given by the finder agent and return the title and a bullet point of the summaries if there is no list, reply with finder agent did not find anything relevant.
            
            {self.__tip_section()}
    
            Make sure to be as accurate as possible. 
        """
            ),
            expected_output="Only give information of the pdfs that are given by finder agent. Give the name of the pdf, and a summary of the the document with a TL:DR about {var1}",
            agent=agent,
            # context=self.finder_task
        )

