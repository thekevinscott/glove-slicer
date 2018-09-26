import argparse
import os
import math
import json
import sys

parser=argparse.ArgumentParser()

parser.add_argument('--file', help='The file containing the word embeddings')
parser.add_argument('--target', help='The folder to write the chunks to')
parser.add_argument('--chunk_size', help='The number of lines per chunk', default=5)

args=parser.parse_args()

if not os.path.isfile(args.file):
    raise Exception("File could not be found")

lines = open(args.file).read().splitlines()

if not os.path.isdir(args.target):
    os.mkdir(args.target)

chunks = int(math.ceil(len(lines) / int(args.chunk_size)))
chunk_size = int(args.chunk_size)

def getFilename(start, end):
    filename = os.path.splitext(args.file)
    ext = filename[1]
    filename = filename[0].split('/').pop()
    return '%s/%s_%s_%s%s' % (args.target, filename, start, end, ext)

manifest = {'files': {}, 'chunk_size': args.chunk_size}
word_manifest = {}
for i in range(chunks):
    start = i * chunk_size
    end = start + chunk_size
    filename = getFilename(start, end)
    ext = 'txt'
    words = []
    for line in lines:
        words.append(line.split(' ')[0])

    data = '\n'.join(lines[start:end])
    size = sys.getsizeof(data)
    manifest['files'][start] = {'filename': filename, 'size': size}
    word_manifest[filename] = words
    file = open(filename, 'w')
    file.write(data)

with open('%s/manifest.json' % args.target, 'w') as outfile:
    manifest = json.dumps(manifest).encode('utf8')
    outfile.write(manifest)
with open('%s/word_manifest.json' % args.target, 'w') as outfile:
    word_manifest = json.dumps(word_manifest).encode('utf8')
    outfile.write(word_manifest)
