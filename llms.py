from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.openai_like import OpenAILike

from configs import Config

# 拉起模型命令
# VLLM_USE_MODELSCOPE=true vllm serve Qwen/Qwen1.5-7B-Chat --port7860 --max-model-len4096 --gpu-memory-utilization0.95

# ================== 初始化模型 ==================
def init_models():
    """初始化模型并验证"""
    # Embedding模型
    embed_model = HuggingFaceEmbedding(
        model_name=Config.EMBED_MODEL_PATH,
        # encode_kwargs = {
        #     'normalize_embeddings': True,
        #     'device': 'cuda' if hasattr(Settings, 'device') else 'cpu'
        # }
    )
    
    # LLM
    # llm = HuggingFaceLLM(
    #     model_name=Config.LLM_MODEL_PATH,
    #     tokenizer_name=Config.LLM_MODEL_PATH,
    #     model_kwargs={
    #         "trust_remote_code": True,
    #         # "device_map": "auto"
    #     },
    #     tokenizer_kwargs={"trust_remote_code": True},
    #     generate_kwargs={"temperature": 0.3}
    # )

    llm = OpenAILike(model="Qwen/Qwen1.5-7B-Chat",
        api_base="http://ai.bygpu.com:58111/v1",
        api_key="no-key-required",
        temperature=0.3,
        max_tokens=1024,
        timeout=60,
        is_chat_model=True,
    )
    
    return embed_model, llm


if __name__ == "__main__":
    embed_model, llm = init_models()
    # 验证LLM生成
    test_response = llm.complete("请简要介绍一下中华人民共和国劳动法的适用范围。")
    print(f"LLM生成验证：{test_response}")

    # 验证embedding生成
    test_embedding = embed_model.get_text_embedding("测试文本")
    print(f"Embedding维度验证：{len(test_embedding)}")
