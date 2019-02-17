# coding:utf-8
"""
@file: 6.2.py
@time: 2/17/2019 12:11 PM
@contact: dabuwang
@content:
6.2　“命令”模式

"""

class MacroCommand:
    """一个执行一组命令的命令"""

    def __init__(self, commands):
        self.commands = list(commands) # ➊

    def __call__(self):
        for command in self.commands: # ➋
            command()

"""
❶ 使用 commands 参数构建一个列表，这样能确保参数是可迭代对象，还能在各个 MacroCommand 实例中保存各个命令引用的副本。

❷ 调用 MacroCommand 实例时，self.commands 中的各个命令依序执行。

复杂的“命令”模式（如支持撤销操作）可能需要更多，而不仅是简单的回调函数。即便如此，也可以考虑使用 Python 提供的几个替代品。

像示例 6-9 中 MacroCommand 那样的可调用实例，可以保存任何所需的状态，而且除了 __call__ 之外还可以提供其他方法。

可以使用闭包在调用之间保存函数的内部状态。
"""