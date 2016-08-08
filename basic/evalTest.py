# -*- coding: utf-8 -*-


def eval_test():
    print 'here'
    return 'test fun'


if __name__ == '__main__':
    param_input_file = '/mnt/mfs/video/tail/joke_tail.mp4'

    # cmd = '/usr/bin/ffmpeg -i ' + param_input_file + eval_test()
    cmd1 = ['/usr/bin/ffmpeg -i ', param_input_file, eval_test()]

    final_cmd = ' '.join(cmd1)

    print 'final_cmd is: ', final_cmd