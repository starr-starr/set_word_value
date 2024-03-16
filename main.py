from src.save_doc_to_docx import save_doc_to_docx
from src.set_value import set_value
from utils.utils import process_file_path

if __name__ == '__main__':
    print("请注意！这个脚本会改变该目录下的所有 .doc 文件\n路径直接从资源管理器复制即可")
    path = process_file_path(input("文件存放地址:")).replace("\\", "\\\\")
    convert_docx_path = save_doc_to_docx(path)
    set_value(convert_docx_path)
