import os
import re

# Đường dẫn đến thư mục chứa các tệp HTML
folder_path = 'D:\\workspace\\uppercaseconverter\\layouts\\yaytext-social'

# Hàm để thực hiện thay thế trong từng tệp HTML
def replace_in_file(file_path):
    file_name = os.path.splitext(os.path.basename(file_path))[0]  # Tên tệp không có đuôi
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Thay thế "result-01" thành "tenfile-result-01" đến "result-08"
    for i in range(1, 9):
        content = re.sub(f'result-0{i}', f'{file_name}-result-0{i}', content)
        content = re.sub(f'copy-result-0{i}', f'{file_name}-copy-result-0{i}', content)

    # Ghi lại nội dung đã thay thế vào tệp
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# Duyệt qua từng tệp HTML trong thư mục và thực hiện thay thế
for file_name in os.listdir(folder_path):
    if file_name.endswith('.html'):
        file_path = os.path.join(folder_path, file_name)
        replace_in_file(file_path)

print("Hoàn thành thay thế các từ khóa trong các tệp HTML.")
