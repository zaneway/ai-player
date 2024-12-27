from langchain_text_splitters import (MarkdownTextSplitter,MarkdownHeaderTextSplitter,CharacterTextSplitter)
from langchain.document_loaders import TextLoader

# 读取文本文件进行拆分
loader = TextLoader("/Users/xxx/Downloads/test.md")
load = loader.load()

text_splitter = MarkdownTextSplitter()
documents = text_splitter.split_documents(load)

for document in documents:
    print(document)
