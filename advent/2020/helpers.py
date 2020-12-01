def get_int_values(filename):
    return list(int(x) for x in open(filename).readlines())