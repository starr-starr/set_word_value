import os
from win32com import client as wc


def save_doc_to_docx(doc_path):
    convert_docx_path = ''
    word = wc.Dispatch("Word.Application")
    filename = os.listdir(doc_path)
    for i in filename:
        # 找出以 .doc 结尾且不是临时文件
        if i.endswith('.doc') and not i.startswith('~$'):
            doc = word.Documents.Open(doc_path + i)
            # 分割文件名与后缀
            rename = os.path.splitext(i)
            convert_docx_path = doc_path + rename[0] + '.docx'
            # 另存为 .docx
            doc.SaveAs(convert_docx_path, 12)  # 12 表示 docx 格式
            doc.Close()
    word.Quit()
    return convert_docx_path
