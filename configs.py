class Config:
    EMBED_MODEL_PATH = r"C:\Users\qian gao\models\BAAI\bge-base-zh-v1___5"
    LLM_MODEL_PATH = r"C:\Users\qian gao\models\qwen_1.5" # qwen_1.5-1.8B-chat
    
    DATA_DIR = "./data"
    VECTOR_DB_DIR = "./chroma_db"
    PERSIST_DIR = "./storage"
    
    COLLECTION_NAME = "chinese_labor_laws"
    TOP_K = 3

config = Config()