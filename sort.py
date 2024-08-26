def sort_sequences_by_title(input_file, sorted_file):
    import re

    # 存储标题和序列的配对
    sequences = []

    # 读取文件并配对标题与序列
    with open(input_file, 'r') as file:
        current_title = None
        current_sequence = []
        for line in file:
            if line.startswith('>'):
                # 如果已存在标题和序列，先保存
                if current_title and current_sequence:
                    sequences.append((current_title, ''.join(current_sequence)))
                # 开始新的标题和序列
                current_title = line.strip()
                current_sequence = []
            else:
                # 继续读取序列
                current_sequence.append(line.strip())
        # 保存文件末尾的最后一个序列
        if current_title and current_sequence:
            sequences.append((current_title, ''.join(current_sequence)))

    # 按标题的首字母排序
    sequences.sort(key=lambda x: re.sub(r'^[^a-zA-Z]+', '', x[0]))  # 移除非字母字符并排序

    # 写入排序后的内容到新文件
    with open(sorted_file, 'w') as file:
        for title, seq in sequences:
            file.write(f"{title}\n{seq}\n")

# 使用函数并指定输入输出文件
sort_sequences_by_title('cleaned_output.txt', 'sorted_output.txt')