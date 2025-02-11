import langchain_ollama
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_text_splitters import (MarkdownTextSplitter)
from langchain.document_loaders import TextLoader
from langchain_chroma import Chroma

from langchain_ollama import OllamaLLM

embeddings = langchain_ollama.OllamaEmbeddings(
    model="deepseek-r1:14b"  # 替换为你的 Ollama 服务 URL
)


# 初始化 Chroma,//,persist_directory="zaneway"
chroma = Chroma(collection_name="zaneway_demo", embedding_function=embeddings )

# 读取文本文件进行拆分
# loader = TextLoader("/Users/zhangzhenwei/Downloads/test.md")
loader = TextLoader(
    "/Users/zhangzhenwei/SynologyDrive/code-space/IdeaProjects/work/calogs/bjca_all_log_zhangzhenweideMacBook-Pro-2.local_Oct-16-000951-2024_Conflict.log")
load = loader.load()

text_splitter = MarkdownTextSplitter()
documents = text_splitter.split_documents(load)
# 存储到数据库
# chroma.add_documents(documents)
# query="CA服务使用的数据库是什么版本？"
query = "静云的私房钱藏在哪里？"
# db = Chroma.from_documents(documents, embeddings)
result = chroma.search(query=query, k=2, search_type="similarity")
# result = Chroma.similarity_search(query)

print("查询结果：", result)

ollama = OllamaLLM(model="llama3.1:8b")

# 提取文档内容
retrieved_content = "\n\n".join([doc.page_content for doc in result])

prompt_template = """
以下是与问题相关的文档内容：
{context}

基于以上内容，回答以下问题：
{question}
"""
# 填充 Prompt
final_prompt = prompt_template.format(context=retrieved_content, question=query)

# 调用 Ollama 模型
response = ollama.invoke(final_prompt)

# 输出结果
print("模型的回答：", response)
