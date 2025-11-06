# Strans AI Agent AWS
from strands import Agent
from strands_tools import calculator # O original não usa o llama3, mas é o que tenho acesso.

SYSTEM_PROMPT = """Você é um assistente útil e prestativo. Utilize as ferramentas disponíveis para responder às perguntas dos usuários de forma precisa e eficiente."""

MODEL_ID="meta.llama3-8b-instruct" #Não vai funcionar porque minha conta na AWS foi encerrada.

agent = Agent(system_prompt = SYSTEM_PROMPT, model = MODEL_ID, tools=[calculator])

agent("Qual é a raiz quadrada de 256?") 
