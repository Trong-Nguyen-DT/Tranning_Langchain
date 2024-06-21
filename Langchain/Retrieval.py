import os

from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
chat = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.2)

# raw_text = """
# One Piece (ワンピース Wan Pīsu?), từng được xuất bản tại Việt Nam dưới tên gọi Đảo Hải Tặc là bộ manga dành cho lứa tuổi thiếu niên của tác giả Oda Eiichiro, được đăng định kì trên tạp chí Weekly Shōnen Jump, ra mắt lần đầu trên ấn bản số 34 vào ngày 19 tháng 7 năm 1997. 
# Bản tankōbon của truyện do Shueisha phát hành với tập đầu tiên vào ngày 24 tháng 12 năm 1997.
# One Piece kể về cuộc hành trình của Monkey D. Luffy - thuyền trưởng của băng hải tặc Mũ Rơm và các đồng đội của cậu.
# Luffy tìm kiếm vùng biển bí ẩn nơi cất giữ kho báu lớn nhất thế giới One Piece, với ước mơ trở thành Vua Hải Tặc.
# """

raw_text = """Tôi là Nguyễn Văn Trọng Nguyên.
Biệt danh là DT. Sinh ngày 02 tháng 04 năm 2002. Hiện tôi đang sống và làm việc tại thành phố Đà Nẵng, Việt Nam
"""

text_splitter = RecursiveCharacterTextSplitter(chunk_size=30, chunk_overlap=10)
all_splits = text_splitter.split_text(raw_text)

vectorstore = Chroma.from_texts(texts=all_splits, embedding=OpenAIEmbeddings())

retriever = vectorstore.as_retriever()
docs = retriever.invoke("Tôi tên là Nguyễn Văn Trọng Nguyên đúng không?")

print(docs)