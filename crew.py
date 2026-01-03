# from crewai import Crew,Process
# from tools import yt_tool
# from agents import blog_researcher,blog_writter

# from tasks import research_task,write_task

# crew = Crew(
#   agents=[researcher,writter],
#   tasks=[research_task,write_task],
#   process=Process.sequential,
#   memory =True,
#   cache=True,
#   max_rpm=100,
#   share_crew=True






# )


# ## start the task execution process with enhenced feedback
# result= crew.kickoff(inputs=('topic': 'AI VS ML VS DL vs Data Science '))

# print(result)







from crewai import Crew, Process
from tools import yt_tool
from agents import blog_researcher, blog_writter
from tasks import research_task, write_task

# Initialize the Crew
crew = Crew(
    agents=[blog_researcher, blog_writter], # Matches your import names
    tasks=[research_task, write_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

## Start the task execution process with enhanced feedback
# Fixed the inputs syntax to use a proper dictionary {}
result = crew.kickoff(inputs={'topic': 'AI VS ML VS DL vs Data Science'})

print(result)