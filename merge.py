import os

def merge_txt_files(input_folder_path, output_file_name):
    """合并目录下所有.txt文件的内容到一个单一文件中。"""
    output_file_path = os.path.join(input_folder_path, output_file_name)
    with open(output_file_path, 'w') as outfile:
        for filename in os.listdir(input_folder_path):
            if filename.endswith('.txt'):
                file_path = os.path.join(input_folder_path, filename)
                with open(file_path, 'r') as infile:
                    outfile.write(infile.read() + '\n')  # 在文件内容之间添加换行符
                print(f'已合并文件：{filename}')

# 使用当前目录作为输入和输出目录
current_folder_path = '.'  # 当前目录
output_file_name = 'merged.txt'  # 输出文件名

# 合并文件
merge_txt_files(current_folder_path, output_file_name)
