from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings

def create_db_form_text():
    raw_text = """One Piece (ワンピース Wan Pīsu?), từng được xuất bản tại Việt Nam dưới tên gọi Đảo Hải Tặc là bộ manga dành cho lứa tuổi thiếu niên của tác giả Oda Eiichiro, được đăng định kì trên tạp chí Weekly Shōnen Jump, ra mắt lần đầu trên ấn bản số 34 vào ngày 19 tháng 7 năm 1997. 
    Bản tankōbon của truyện do Shueisha phát hành với tập đầu tiên vào ngày 24 tháng 12 năm 1997.
    One Piece kể về cuộc hành trình của Monkey D. Luffy - thuyền trưởng của băng hải tặc Mũ Rơm và các đồng đội của cậu.
    Luffy tìm kiếm vùng biển bí ẩn nơi cất giữ kho báu lớn nhất thế giới One Piece, với ước mơ trở thành Vua Hải Tặc."""
    
    text_splitter = CharacterTextSplitter(
        separator=".",
        chunk_size=100,
        chunk_overlap=20,
        length_function=len
    )
    
    chunks = text_splitter.split_text(raw_text)
    
    emmbedding_model = OpenAIEmbeddings(model="text-embedding-ada-002")

    db = FAISS.from_texts(chunks, emmbedding_model)
    db.save_local("one_piece_db")
    return db


create_db_form_text()