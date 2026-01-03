# from crewai import Agent

# ##Create a senior blog content resercher
# from tools import yt_tool
# from agents import blog_researcher,blog_writter

# ## Research Task
# research_task = Task(
#     description=(
#        "Identify the video{topic}."  
# "Get detailed information about the video from the channel."



#     ),
#     expected_output='A comprehensive 3 paragraphs long report based on the {topic }of video',
#     tools =[yt_tool],
#     agent=blog_researcher,


# #Writting task with language model
# write_task = Task(
#     description=(
#         "get the infor from the yutube channel on the topic{topic}."

#     ),
#     expected_output ='Summarize th einfor from the youtub channel video on the topic {topic} and create the content for the blog',
#     tools=[yt_tool],
#     agent=writter,
#     async_execution=False,
#     output_file='new-blog-post.md'# Example of output customization 



# )









# )













from crewai import Agent, Task  # Added Task import
from tools import yt_tool
from agents import blog_researcher, blog_writter

## Research Task
research_task = Task(
    description=(
        "Identify the video related to the topic: {topic}. "  
        "Get detailed information about the video from the channel."
    ),
    expected_output='A comprehensive 3-paragraph long report based on the {topic} of the video.',
    tools=[yt_tool],
    agent=blog_researcher,
) # Added missing closing parenthesis

# Writing task with language model
write_task = Task(
    description=(
        "Get the information from the YouTube channel on the topic: {topic}."
    ),
    expected_output='Summarize the information from the YouTube channel video on the topic {topic} and create the content for the blog.',
    tools=[yt_tool],
    agent=blog_writter, # Changed 'writter' to 'blog_writter' to match import
    async_execution=False,
    output_file='new-blog-post.md'
)