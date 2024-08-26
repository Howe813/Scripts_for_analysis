import re
from collections import defaultdict

def process_and_clean_sequences(input_file, cleaned_file, report_file):
    lines_to_process = []
    identifier_counts = defaultdict(list)
    lines_to_keep = []

    # 首先处理输入文件，修改标题行格式
    with open(input_file, 'r') as infile:
        for line in infile:
            if line.startswith('>'):
                # 分割标题行，并提取所需的部分
                identifier = line.split(':')[0][1:]  # 提取冒号前的标识符并去除'>'
                # 去除从冒号到第一个空格的内容
                remaining_title = line.split(' ', 1)[1] if ' ' in line else ''
                # 重新构建标题行，将标识符加到行尾并包含在括号中
                new_title = '>' + remaining_title.strip() + ' (' + identifier + ')' + '\n'
                lines_to_process.append(new_title)
            else:
                lines_to_process.append(line)

    # 检查并移除重复的条目
    for line_number, line in enumerate(lines_to_process, 1):
        if line.startswith('>'):
            # 使用正则表达式查找括号内的内容
            match = re.search(r'\(([^)]+)\)', line)
            if match:
                identifier = match.group(1)
                if identifier not in identifier_counts:
                    # 记录首次出现的标识符和对应的行
                    identifier_counts[identifier].append(line_number)
                    # 将标题和下一行序列加入保留列表
                    lines_to_keep.append(line)
                    if line_number < len(lines_to_process):
                        lines_to_keep.append(lines_to_process[line_number])  # 假设序列紧随其后
                else:
                    # 记录重复的标识符
                    identifier_counts[identifier].append(line_number)

    # 写入cleaned_file，保留非重复项
    with open(cleaned_file, 'w') as file:
        file.writelines(lines_to_keep)
    
    # 写入report文件
    with open(report_file, 'w') as file:
        file.write("Duplicates Report\n")
        file.write("-----------------\n")
        for identifier, lines in identifier_counts.items():
            if len(lines) > 1:  # 只关心出现多于一次的标识符
                file.write(f"Identifier '{identifier}' found on lines {', '.join(map(str, lines))}\n")

# 使用函数并指定输入输出文件
process_and_clean_sequences('input.txt', 'cleaned_output.txt', 'report.txt')