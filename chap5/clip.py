# coding:utf-8
"""
@file: clip.py
@time: 2/10/2019 9:18 PM
@contact: dabuwang
"""


"""
函数声明中的各个参数可以在 : 之后增加注解表达式。
如果参数有默认值，注解放在参数名和 = 号之间。
如果想注解返回值，在 ) 和函数声明末尾的 : 之间添加 -> 和一个表达式。
那个表达式可以是任何类型。注解中最常用的类型是类（如 str 或 int）和字符串（如 'int > 0'）。
在下面示例中，max_len 参数的注解用的是字符串。
"""
# def clip_cmt(text:str, max_len:'int > 0'=80) -> str:  # python3中支持的 函数注释（5.9）

def clip(text, max_len=80):
    """在max_len前面或后面的第一个空格处截断文本
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:  # 没找到空格
        end = len(text)
    return text[:end].rstrip()

    """在max_len前面或后面的第一个空格处截断文本
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:  # 没找到空格
        end = len(text)
    return text[:end].rstrip()