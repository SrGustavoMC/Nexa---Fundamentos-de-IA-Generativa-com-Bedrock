# Strans AI Agent AWS
from strands import Agent
from strands_tools import calculator # O original não usa o llama3, mas é o que tenho acesso.
from bedrock_agentcore.runtime import BedrockAgentCoreApp

app = BedrockAgentCoreApp()

@app.entrypoint
def invoke(payload, context):
    SYSTEM_PROMPT = """Você é um assistente útil e prestativo. Utilize as ferramentas disponíveis para responder às perguntas dos usuários de forma precisa e eficiente."""

    MODEL_ID="us.amazom.nova-premier-v1:0" #Não vai funcionar porque minha conta na AWS foi encerrada.
    agent = Agent(system_prompt = SYSTEM_PROMPT, model = MODEL_ID, tools=[calculator])

    prompt = payload.get("prompt")
    result = agent(prompt)
    return {
        "response": result.message.get("content", [{}]).get("text", str(result))
        }

if __name__ == "__main__":
    app.run()