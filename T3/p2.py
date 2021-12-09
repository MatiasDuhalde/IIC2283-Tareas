"""
Solucion al problema 2 de la Tarea 3
"""
from os import read, fstat
from io import BytesIO

# Use fast read
input_buffer = BytesIO(read(0, fstat(0).st_size))
input = input_buffer.readline  # pylint: disable=redefined-builtin


def main():
    """Main function"""


if __name__ == '__main__':
    main()
