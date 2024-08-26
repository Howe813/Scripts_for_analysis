import re

def remove_parentheses_content(file_path, output_file_path=None):
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 使用正则表达式删除所有类型的括号及其中的内容
    modified_content = re.sub(r'\(.*?\)|\[.*?\]|\{.*?\}', '', content)
    
    # 如果指定了输出文件路径，则写入新文件，否则覆盖原文件
    if output_file_path:
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(modified_content)
    else:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(modified_content)

# 使用示例
input_file_path = 'example.txt'  # 输入文件的路径
output_file_path = 'modified_example.txt'  # 输出文件的路径（可选）

# 调用函数
remove_parentheses_content(input_file_path, output_file_path)