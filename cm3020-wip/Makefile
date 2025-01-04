

install:
	pip install poetry llm && \
	pip install docling


llm-plugins:
	llm install llm-ollama && \
	llm install llm-jq && \
	llm install llm-claude-3

# Error: No key found - add one using 'llm keys set openai' or set the OPENAI_API_KEY environment variable
# Error: No key found - add one using 'llm keys set claude' or set the ANTHROPIC_API_KEY environment variable

claude-samples:
	llm -m claude-3.5-sonnet 'describe this image' -a https://static.simonwillison.net/static/2024/pelicans.jpg
	llm -m claude-3-haiku 'extract text' -a CM3020_AI_Coursework.pdf

openai-samples:
	cat CM3020_AI_Coursework.md | llm -m 4o 'Summarize this' --system {}
openai-parta:
	cat parta/parta.md | llm -m 4o '\n plase suggest a study plan for this assignment.' --system {} >> parta/plan-parta.md
openai-parta-1:
	cat parta/parta.md | llm -m 4o '\n you have unlimited resources to fulfill this assignment. break down the tasks and teams we need to hire for this>' --system {} >> parta/plan-parta-1.md
openai-parta-2:
	cat parta/parta.md | llm -m 4o '\n what tools we need to deliver th submission for this assingment' --system {} >> parta/plan-parta-2.md
openai-parta-3:
	cat parta/parta.md | llm -m 4o '\n What is the best suitable talent to supervise a team to accomplish this assignment. Give a job description for this supervisor role.' --system {} >> parta/plan-parta-3.md
openai-parta-4:
	cat parta/parta.md | llm -m 4o '\n What is the best suitable talent to supervise a group of teams to accomplish this assignment. Give a job description for this supervisor role.' --system {} >> parta/plan-parta-4.md
openai-parta-5:
	cat parta/parta.md | llm -m 4o '\n I need your guidence to build a coporate to accomplish the given assigment. Please suggest an organisation hierarcy to accomplish the given assigment. ' --system {} >> parta/plan-parta-5.md
openai-parta-6:
	cat parta/parta.md | llm -m 4o '\n Please suggest ways to find information to answer each of the questions using information that you have found in the literature to accomplish the given assigment. ' --system {} >> parta/plan-parta-6.md

openai-parta-research:
	cat CM3020_AI_Coursework.md | llm -m 4o 'suggest a plan for the task **Research Extensively**: Use reputable sources, including academic papers, books, and conference proceedings, to gather data and insights for each section.' --system {} >> parta/research.md

ollama-host:
	export OLLAMA_HOST=https://192.168.1.131:11434
	