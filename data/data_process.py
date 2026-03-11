from exact_web_data import extract_law_articles, fetch_and_parse

def process_law_data(url, law_name):
    # 获取网页内容并提取文本
    law_text = fetch_and_parse(url)
    breakpoint()
    # 提取法律条款并转换为JSON格式
    law_articles_json = extract_law_articles(law_text, law_name)
    return law_articles_json

def save_to_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(data)


if __name__ == "__main__":
    # 示例URL和法律名称
    data_list = []
    laodongfa_url = "https://www.samr.gov.cn/zw/zfxxgk/fdzdgknr/bgt/art/2023/art_d9aa750028b14b99a776cb93726a360d.html"
    laodongfa_name = "中华人民共和国劳动法"
    
    # 处理劳动法数据
    law_articles_json = process_law_data(laodongfa_url, laodongfa_name)
    data_list.append(law_articles_json)

    # 处理劳动合同法数据
    laodongbaohu_url = "https://www.samr.gov.cn/zw/zfxxgk/fdzdgknr/bgt/art/2023/art_0abfdd261c03417b949df19d869add8d.html"
    laodongbaohu_name = "中华人民共和国劳动合同法"
    law_protect_json = process_law_data(laodongbaohu_url, laodongbaohu_name)
    data_list.append(law_protect_json)
    breakpoint()
    # 保存结果到文件
    save_to_file(data_list, "data.json")