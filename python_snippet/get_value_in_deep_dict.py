# coding:utf-8
"""
@file: get_value_in_deep_dict.py
@time: 2018/9/20 15:31
@contact: dabuwang
"""
__author__ = 'dabuwang'

t_dict = {
    "LV1": {
        "LV2": "value2"
    }
}

def test():
    print t_dict['LV1']
    print t_dict['LV1']['LV2']
    l = ['LV1', 'LV2']

    print my_test(t_dict, *l)

    print deep_get(t_dict, 'LV1', 'LV2')
    print deep_get(t_dict, *['LV1', 'LV2'])
    print deep_get(t_dict, *l)

def my_test(xdict, *key_list):
    if not isinstance(xdict, dict):
        return None
    if len(key_list) == 0:
        return None
    elif len(key_list) == 1:
        return xdict.get(key_list[0])
    else:
        return my_test(xdict.get(key_list[0]), *key_list[1:])

def deep_get(dictionary, *keys):
    return reduce(lambda d, key: d.get(key) if d else None, keys, dictionary)


if __name__ == '__main__':
    test()
