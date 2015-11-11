__author__ = 'Jabari'


#CONSTANTS
BUF_SIZE = 121
MACSIZE = 4096
P_TABLE_SIZE = 5
E_TABLE_SIZE = 5
R_TABLE_SIZE = 5
FILE_BUF_SIZE = 12000


class PTYPE:
    address = 0
    symptr = 0


class ETYPE:
    address = 0
    symptr = 0


class RTYPE:
    address = 0
    module_address = 0


buf = [0, 0, 0, 0, 0]
ifilename = [0, 0, 0, 0, 0]
ofilename = [0, 0, 0, 0, 0]
file_buffer = [0, 0, 0, 0, 0]
saves = None