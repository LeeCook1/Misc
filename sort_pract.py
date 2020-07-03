import collections
import itertools
import random


def init_objs(delim):
    objs = ["{}".format(x) for x in range(1, 4)]
    str_combo = list(itertools.product(range(1, 5), range(8)))
    objs += ["{}{}{}".format(x, delim, y) for x, y in str_combo]
    random.shuffle(objs)
    return {o: o for o in objs}


def main():
    delim = '-'
    d = {'type1': init_objs(delim), 'type2': init_objs(delim)}
    for dtype, objs in d.items():
        d[dtype] = collections.OrderedDict()
        sorted_keys = sorted(objs.keys(), key=lambda s: (
            s.count(delim), s.split(delim)))
        d[dtype].update({k: objs[k] for k in sorted_keys})
    print(d)


if __name__ == '__main__':
    main()
