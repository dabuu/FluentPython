# coding:utf-8
"""
@file: 5.7.py
@time: 2/10/2019 8:56 PM
@contact: dabuwang
@content：
5.7 ： 从*定位参数* 到 *仅限关键字参数*
"""

# def tag(name, *content, cls=None, **attrs):   # python3中允许的语法，“仅限关键字参数”
def tag(name, cls=None, *content, **attrs):
    """生成一个或多个HTML标签"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value
                           in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                         (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)

def test_tag():
    print tag('br')
    # python3 中，下面的None可以省略
    print tag('p', None, 'hello')
    print tag('p', None, 'hello', 'world')
    print tag('p', None, 'hello', id=4)
    print tag('p', 'sidebar', 'hello', 'world',id=5)

    # python3 中可以运行
    # python2.7 中TypeError: tag() got multiple values for keyword argument 'cls'
    print tag('p', 'hello', 'world', cls='cls5',id=6)

if __name__ == '__main__':
    test_tag()