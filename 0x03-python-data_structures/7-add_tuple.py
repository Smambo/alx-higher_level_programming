#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ta = tuple_a
    tb = tuple_b
    if len(ta) < 2:
        ta = (0, 0)
    elif len(ta) > 2:
        ta = (tuple_a[0], tuple_a[1])
    elif len(ta) == 1:
        ta = (tuple_a[0], 0)

    if len(tb) < 2:
        tb = (0, 0)
    elif len(tb) > 2:
        tb = (tuple_b[0], tuple_b[1])
    elif len(tb) == 1:
        tb = (tuple_b[0], 0)

    return (ta[0] + tb[0], ta[1] + tb[1])
