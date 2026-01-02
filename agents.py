from crew import Agent
##Create a senior blog content resercher
from tools import yt_tool

blog_researcher = Agent(
  role='Blog Researcher from Youtube Videos',
  goals='get the relevant video content for the topic {topic} from Yt channel'
  verbose=True,
  memory=True,
backstory=(
   "Expert in understanding videos in AI Data Sccience , Machine Learing And GEN AI tools."

   tools=[tool],
   allow_dlelegation=True




)
)

blog_writter = Agent(
 role='writer',
 goal='Narrate compelling tech stories about the video{topic}',

 verbose=True,
memory =True,

backstory=(
   "With a flair for simplifying complex topics ,you craft"
   "engaging narratives that captivate and educate ,brinw new "
   "discoveries to light in an  accessible manner ."

   tools=[tool],
   allow_dlelegation=False
)








)













 