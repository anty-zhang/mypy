# -*- coding: utf-8 -*-

import os


def deal_file():
    all_info = []
    all_info.append('df1')
    all_info.append(''.join(['http://reader.comqq', 'baidu.com']))
    '''
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    all_info.append(title)
    all_info.append(url)
    '''
    with open(file_path, 'rb') as f:
        f.write(''.join(all_info).encode('utf-8'))
        f.write('\n')


if __name__ == '__main__':
    file_path = os.path.join(os.getcwd(), 'tt.txt')
    with open(file_path, 'rb') as f:
        lines = f.read()
        lines = lines.split('\n')
        sorted(lines)
        for line in lines:
            print line
