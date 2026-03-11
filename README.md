# 项目背景与需求设计
法律条文智能问答系统，要求如下：
1.需要实时更新法律条文
2.支持对法律条款的精确引用
3.处理复杂的法律条款的关联查询

# 数据处理
origin_data:
中华人民共和国劳动法：https://www.samr.gov.cn/zw/zfxxgk/fdzdgknr/bgt/art/2023/art_d9aa750028b14b99a776cb93726a360d.html
中华人民共和国劳动合同法：https://www.samr.gov.cn/zw/zfxxgk/fdzdgknr/bgt/art/2023/art_0abfdd261c03417b949df19d869add8d.html
爬虫保存为data.json文件


# 项目选型
选择使用RAG方案，有如下原因：
1.法律条文存在一定的更新频率，微调模型难以快速同步最新信息
2.需要精确引用条款原文(微调的话涉及到文本生成，模型会有一部分创造性)
3.法律知识体系比较庞大，微调需要海量标注数据
4.RAG机制天然支持条款溯源，符合法律场景需求


