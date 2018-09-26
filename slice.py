import argparse
import os

parser=argparse.ArgumentParser()

parser.add_argument('--file', help='The file containing the word embeddings, separated by newlines')
parser.add_argument('--chunk_size', help='The number of lines per chunk', default=5)

args=parser.parse_args()

if not os.path.isfile(args.file):
    raise Exception("File could not be found")

print(args.chunk_size)
