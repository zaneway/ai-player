# you should exec 'pip install langchain_ollama'
# you can install ollama in pc of yourself

from langchain_ollama import OllamaLLM
model = OllamaLLM(model="llama3.1:8b")
invoke = model.invoke("有什么开源的向量数据库推荐")
print(invoke)