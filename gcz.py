#!/usr/bin/env python3

import numpy

GCZ_MAGIC = 0xB10BC001


TEST_GCZ = '/media/jimnarey/HDD_Data_B/gamecube/Testing/mario_kart.nkit.gcz'


# data = numpy.fromfile(TEST_GCZ, dtype='f').byteswap()

# data = data.byteswap()

# print(type(data))
# print(data.shape)
# x = data[:32]
# print(str(x.tobytes()))


def get_header(file_path):
    data = numpy.fromfile(file_path, dtype='>i4', count=8).byteswap()
    return {
        'magic_cookie': data[:1].tobytes(),
        'sub_type': data[1:2].tobytes(),
        'compressed_size': data[2:4].tobytes(),
        'data_size': data[4:6].tobytes(),
        'block_size': data[6:7].tobytes(),
        'num_blocks': data[7].tobytes()
    }


if __name__ == "__main__":
    header = get_header(TEST_GCZ)
    print(header)

