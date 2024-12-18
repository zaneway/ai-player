from langchain_text_splitters import (MarkdownTextSplitter,MarkdownHeaderTextSplitter,CharacterTextSplitter)
from langchain.document_loaders import PyPDFLoader

# 读取PDF文件进行拆分
loader = PyPDFLoader("/Users/xxx/xxx/learn-something/GM-AND-GB/GBT/GBT19714-征求意见稿(最新版).pdf")
load = loader.load()

text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=150, length_function=len)
documents = text_splitter.split_documents(load)

for document in documents:
    print(document)

# 直接拆分文字
splitter = MarkdownTextSplitter()
text = splitter.split_text("afda,asdfasdf,asdfasdfasfd,asdf234,df")
print(text)
