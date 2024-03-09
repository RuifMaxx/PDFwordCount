import re  
  
def count_words(text):  
    """  
    统计文本中的单词数（英文单词和中文通常被视为单个词）  
    """  
    def count_chinese_char(chars):  
        """  
        判断一个字符是否为中文  
        """  
        # 中文Unicode范围（基本的多文种平面BMP）大致是\u4e00到\u9fff  
        # 但也包括一些扩展区，如扩展A区等，这里只检查基本范围
        count = 0
        biaodian = ['。', '，', '；', '：', '？', '！', '——', '……', '“', '”', '‘', '’', '（', '）', '《', '》', '【', '】']
        for char in chars:  
            if ('\u4e00' <= char <= '\u9fff' 
                or '\u3400' <= char <= '\u4dbf' or char in biaodian):   
                count += 1
        return count
  
    # 使用正则表达式匹配英文单词，这里假设单词由字母组成，可能包含连字符'-'  
    english_words = re.findall(r'\b[A-Za-z-]+\b', text)  
    english_word_count = len(english_words)  
    numbers = re.findall(r'\d+', text) 
    numbers_count = len(numbers)
  
    # 中文通常按字计算，但如果需要按词语计算，需要更复杂的分词处理  
    # 这里我们简单地假设每个中文字符是一个词  
    chinese_word_count = count_chinese_char(text)  
  
    return {  
        "字数": english_word_count + chinese_word_count+numbers_count,  
        "非中文单词": english_word_count+numbers_count,  
        "中文单词": chinese_word_count  
    }  
    
if __name__ == "__main__":
    # 示例用法  
    text = "这是一个示例文本，用于测试单词计数功能。Hello, world，2024.6! This is a test."  
    stats = count_words(text)  
    print(f"总单词数: {stats['字数']}")  
    print(f"英文单词数: {stats['非中文单词']}")  
    print(f"中文词语数: {stats['中文单词']}")