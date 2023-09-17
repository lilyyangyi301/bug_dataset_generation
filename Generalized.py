import os
import ast
import json
import glob
from pathlib import Path
import sys

from Tokenizing import *
# path = open("C:\Users\miche\Documents\school\jaar2\MIK\2.6\vektis_agb_zorgverlener")
# data = csv.reader(data)  
# def tokenize(file_path):
#     lines = []
#     with open(file_path) as f:
#         lines = f.readlines()

#     key = ''
#     value = ''
#     pairs = []
#     for line in lines:
#         if ':' in line:
#             key = line.split(':')[-1].strip()
            
#         elif line.strip().startswith('[') and line.strip().endswith(']'):
#             value = line.strip()[1:-1]
#             pairs.append((key, ast.literal_eval('[' + value + ']')))
#             key, value = '', ''

#         elif line.startswith('  '):
#             value += line

#         elif line.strip() == ']':
#             pairs.append((key, ast.literal_eval('[' + value + ']')))
#             key, value = '', ''
#         else:
#             value = line.strip()[1:-1]
#             pairs.append((key, ast.literal_eval('[' + value + ']')))
#     name = Path.GetFileName(file_path)
#     file1 = open(name + "_tokenized.txt","w")
#     for token, scope in pairs:
#         if token == '': continue
#         if 'punctuation.definition.comment.java' in scope or 'comment.block.javadoc.java' in scope or 'comment.line.double-slash.java' in scope: continue
#         file1.write(token)

def looping_directories(path):
    os.chdir(path)
    # print(os.getcwd())
    # Check for folders inside folders
    # directories = set([os.path.dirname(p) for p in glob.glob(path)])
    # if len(directories) > 0:
    #     for i in directories:
    #         # Get path and recursive call
    #         print(i)
    #         directory_path = os.getcwd(i)
    #         looping_directories(directory_path)
    # Loop through the folder to search for Java files
    for file in os.listdir():
        if file.endswith(".jsonl"):
            file_name = file[:-6]
            # print(file)
            file_path = path + "/" + file
            # file_path = os.getcwd(file)
            # Exporting information to a string
            # text_file = open(file_path, 'r')
            # data = text_file.read()
            # text_file.close()

            # # Exporting information to txt file
            # file_name = Path.GetFileName()
            # text = open(file_name + ".txt", 'w')
            # text.write(data)
            # text.close()

            # # Calling the tokenizer function
            # path_of_file = os.getcwd(text)
            tokenize(file_path, file_name)

looping_directories(sys.argv[1])

# /Users/lilyyang/Desktop/bug_dataset_generation/java_transformed/train.jsonl
# /Users/lilyyang/Desktop/bug_dataset_generation/java_transformed