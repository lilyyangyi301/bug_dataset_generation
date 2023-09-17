import sys
import os


def tokenizing_file(file):
    os.system(f"source-code-tokenizer-master/tokenizer {file}")

tokenizing_file(sys.argv[1])