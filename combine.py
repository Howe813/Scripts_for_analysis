import os

def process_sequences(file_path, output_file_path):
    """处理每个文件中的序列，将每个序列合并为一行。"""
    with open(file_path, 'r') as file:
        with open(output_file_path, 'w') as outfile:
            output = []
            for line in file:
                if line.startswith('>'):
                    if output:
                        outfile.write(''.join(output) + '\n')
                    outfile.write(line)
                    output = []
                else:
                    output.append(line.strip())
            if output:
                outfile.write(''.join(output) + '\n')
    print(f"文件已处理并保存为：{output_file_path}")

def batch_process_files(input_folder_path, output_folder_path):
    """批量处理目录中的所有.txt文件，并将输出保存到指定的目录。"""
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)  # 创建输出目录，如果不存在的话
    files_processed = 0
    for filename in os.listdir(input_folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(input_folder_path, filename)
            output_file_path = os.path.join(output_folder_path, 'processed_' + filename)
            process_sequences(file_path, output_file_path)
            files_processed += 1
            print(f'正在处理：{filename}')
        else:
            print(f'跳过文件：{filename}（不是.txt文件）')
    if files_processed == 0:
        print("未找到任何.txt文件进行处理。")
    else:
        print(f"共处理了 {files_processed} 个文件。")

# 定义输入和输出目录
input_folder_path = '.'  # 当前目录作为输入目录
output_folder_path = 'C:/Users/Howeg/Desktop/Research/Project/Hydrogel/Data/16S/分析/MEGA_发育树/blast/Combine'  # 替换为你想要的输出目录路径

# 处理文件并输出到指定目录
batch_process_files(input_folder_path, output_folder_path)