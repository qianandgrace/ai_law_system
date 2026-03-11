# -*- coding: utf-8 -*-
import time
from pathlib import Path

from llama_index.core import Settings
from llama_index.core import PromptTemplate

from configs import Config
from prompt_template import QA_TEMPLATE
from llms import init_models 
from data_process import load_and_validate_json_files, create_nodes
from vector_save import init_vector_store


def main():
    # 模型初始化
    embed_model, llm = init_models()
    Settings.embed_model = embed_model
    Settings.llm = llm
    
    # 数据处理index
    if not Path(Config.VECTOR_DB_DIR).exists():
        print("\n初始化数据...")
        raw_data = load_and_validate_json_files(Config.DATA_DIR)
        nodes = create_nodes(raw_data)
    else:
        nodes = None  # 已有数据时不加载
    
    # 向量存储
    print("\n初始化向量存储...")
    start_time = time.time()
    index = init_vector_store(nodes,
                              Config.VECTOR_DB_DIR,
                              Config.COLLECTION_NAME,
                              embed_model)
    print(f"索引加载耗时：{time.time()-start_time:.2f}s")
    
    # 查询引擎
    query_engine = index.as_query_engine(
        similarity_top_k=Config.TOP_K,
        text_qa_template=PromptTemplate(QA_TEMPLATE),
        verbose=True
    )
    
    # 示例查询
    while True:
        question = input("\n请输入劳动法相关问题（输入q退出）: ")
        if question.lower() == 'q':
            break
        
        # 执行查询
        response = query_engine.query(question)
        
        # 显示结果
        print(f"\n智能助手回答：\n{response.response}")
        print("\n支持依据：")
        for idx, node in enumerate(response.source_nodes, 1):
            meta = node.metadata
            print(f"\n[{idx}] {meta['full_title']}")
            print(f"  来源文件：{meta['source_file']}")
            print(f"  法律名称：{meta['law_name']}")
            print(f"  条款内容：{node.text[:100]}...")
            print(f"  相关度得分：{node.score:.4f}")

if __name__ == "__main__":
    main()