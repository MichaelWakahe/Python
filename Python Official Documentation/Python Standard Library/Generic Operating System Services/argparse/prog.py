"""Try running this sample script with arguments as follows:

python prog.py
python prog.py -h
python prog.py --help
python prog.py 1 2 3 4
python prog.py 1 2 3 4 --sum
python prog.py a b c
"""
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))