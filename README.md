AI Blog Generator from YouTube 🤖🎥
This project leverages CrewAI to build a multi-agent system that researches YouTube content from a specific creator and automatically transforms that data into a structured blog post.

🏗️ Project Structure
The project is split into modular components for better maintainability:

main.py: The entry point that initializes the Crew and executes the tasks.

agents.py: Defines the Blog Researcher and Blog Writer agents.

tasks.py: Contains the instructions and expected outputs for the research and writing phases.

tools.py: Initializes the YoutubeChannelSearchTool targeted at a specific handle.

🛠️ Installation
Clone the repository:

Bash

git clone https://github.com/yourusername/yt-crewai-blogger.git
cd yt-crewai-blogger
Install the required libraries:

Bash

pip install crewai crewai_tools
Configure Environment Variables: You must provide an OpenAI API key for the agents to think and for the tool to create embeddings of the video content.

Bash

export OPENAI_API_KEY='your-api-key-here'
🤖 The Workflow
The system uses a Sequential Process to ensure quality:

Research Phase: The blog_researcher uses the YoutubeChannelSearchTool to scan @krishnaik06 for a specific topic. It extracts key insights and organizes them into a 3-paragraph report.

Writing Phase: The blog_writter takes that report and converts it into a professional Markdown blog post, saving it to new-blog-post.md.

🚀 Usage
To run the generator, simply execute the main.py script:

Python

# In main.py
result = crew.kickoff(inputs={'topic': 'AI VS ML VS DL vs Data Science'})
print(result)
📝 Output
The final output is saved automatically as new-blog-post.md. It includes:

A summary of the video content.

Structured headings based on the topic.

Technical insights gathered from the YouTube channel.
