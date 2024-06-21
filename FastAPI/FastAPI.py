
from fastapi import FastAPI, Request, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from starlette.responses import StreamingResponse

app = FastAPI()
#Method GET, POST, PUT, DELETE, PATCH, OPTIONS, HEAD

# Cấu hình CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://172.24.192.1:8000"],  # Chỉ cho phép origin http://127.0.0.1:8000
    allow_credentials=True,
    allow_methods=["GET", "OPTIONS"],  # Chỉ cho phép phương thức GET và OPTIONS cho các origin khác
    allow_headers=["*"],  # Cho phép tất cả các headers
)

# Middleware để xử lý phản hồi cho các origin khác
@app.middleware("http")
async def add_cors_header(request: Request, call_next):
    response = await call_next(request)
    if "http://127.0.0.1:8000" in request.headers.get("origin", ""):
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    else:
        response.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    return response

class ItemBase(BaseModel):
    title: str
    description: str | None = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True
        
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.get("/")
def home():
    return "Trang Home"

@app.post("/items/")
def create_item(item: Item):
    return {"item": item}

@app.put("/items/{item_id}")
def update_item(item_id: int, name: str):
    return {"item_id": item_id, "name": name}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    # Mở file ở chế độ "rb" (read binary)
    file_content = b""
    async for chunk in file.file:
        file_content += chunk
    return {"filename": file.filename, "content_length": len(file_content)}

@app.get("/download/")
async def download_file():
    # Tạo dữ liệu để stream
    async def generate():
        yield b"hello\n"
        yield b"world\n"
    return StreamingResponse(generate(), media_type="text/plain")

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response