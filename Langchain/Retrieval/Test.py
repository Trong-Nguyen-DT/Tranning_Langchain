import os

from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma
 
from langchain_community.vectorstores import FAISS


OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

raw_documents = TextLoader('/home/trongnguyendt/PartTimeDAC/Training/Langchain/Retrieval/db/onepiece.txt').load()
text_splitter = CharacterTextSplitter(chunk_size=512, chunk_overlap=50)
documents = text_splitter.split_documents(raw_documents)
db = FAISS.from_documents(documents, OpenAIEmbeddings())

# In các vector và tài liệu từ cơ sở dữ liệu FAISS
print("Vectors:\n", db.index.reconstruct_n(0, db.index.ntotal))

# response = db.similarity_search("Cốt truyện của One Piece là gì?")
# print(response[0].page_content)





