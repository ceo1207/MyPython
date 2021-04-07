# -*- coding: utf-8 -*-
# Author: Kayi
# create time: 2021/4/7
'''
功能：批处理 修改目录下文件名
常用函数： os.listdir os.rename os.path.join
'''
import os
def batch_rename(args):
    work_dir = args.work_dir
    old_ext = args.old_extension
    new_ext = args.new_extension
    old_length = len(old_ext)
    for file_name in os.listdir(work_dir):
        if old_length:
            if file_name.endswith(old_ext):
                new_file_name = file_name[:-old_length] + new_ext
                _rename(work_dir, file_name, new_file_name)
        else:
            new_file_name = file_name + new_ext
            _rename(work_dir, file_name, new_file_name)



def _rename(work_dir, old_name, new_name):
    os.rename(
        os.path.join(work_dir, old_name),
        os.path.join(work_dir, new_name)
    )


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    # add_argument 详见注释 https://docs.python.org/2.7/
    parser.add_argument('--work_dir', default='.', type=str, help='working directory')
    parser.add_argument('--old_extension', default='', type=str, help='old extension')
    parser.add_argument('-new', '--new_extension', default='', type=str, help='new extension')
    args = parser.parse_args()
    # args.new error
    # print args.old_extension, args.new_extension
    batch_rename(args)


