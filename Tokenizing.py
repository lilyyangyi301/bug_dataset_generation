import os
import ast
import json
import glob
from pathlib import Path

def tokenize(file_path, file_name):
    lines = []
    with open(file_path) as f:
        lines = f.readlines()

    # key = ''
    # value = ''
    # pairs = []
    i = 0
    for line in lines:
        i += 1
        # print(line)
        data = json.loads(line)
        # print(data)
        original_file = data['original']
        name_of_original_file = str(i) + "_original.java"
        with open(name_of_original_file, 'w') as fw:
            fw.write(original_file)
        transformed_file = data['transformed']
        name_of_transformed_file = str(i) + "_transformed.java"
        with open(name_of_transformed_file, 'w') as fw:
            fw.write(transformed_file)
        os.system(f"python3 tokenizing_file.py {name_of_original_file} > original_temp.txt")
        os.system(f"python3 tokenizing_file.py {name_of_transformed_file} > transformed_temp.txt")
        break
        converting(original_file_path, file_name, "original")
        converting(transformed_file_path, file_name, "transformed")
    #     if ':' in line:
    #         key = line.split(':')[-1].strip()
            
    #     elif line.strip().startswith('[') and line.strip().endswith(']'):
    #         value = line.strip()[1:-1]
    #         pairs.append((key, ast.literal_eval('[' + value + ']')))
    #         key, value = '', ''

    #     elif line.startswith('  '):
    #         value += line

    #     elif line.strip() == ']':
    #         pairs.append((key, ast.literal_eval('[' + value + ']')))
    #         key, value = '', ''
    #     else:
    #         value = line.strip()[1:-1]
    #         pairs.append((key, ast.literal_eval('[' + value + ']')))
    # # name = Path.GetFileName(file_path)
    # file1 = open(file_name + "_tokenized.txt","w")
    # for token, scope in pairs:
    #     if token == '': continue
    #     if 'punctuation.definition.comment.java' in scope or 'comment.block.javadoc.java' in scope or 'comment.line.double-slash.java' in scope: continue
    #     file1.write(token)
    
def converting(file_path, file_name, type):
    lines = []
    with open(file_path) as f:
        lines = f.readlines()

    key = ''
    value = ''
    pairs = []
    i = 0
    for line in lines:
        if ':' in line:
            key = line.split(':')[-1].strip()
            
        elif line.strip().startswith('[') and line.strip().endswith(']'):
            value = line.strip()[1:-1]
            pairs.append((key, ast.literal_eval('[' + value + ']')))
            key, value = '', ''

        elif line.startswith('  '):
            value += line

        elif line.strip() == ']':
            pairs.append((key, ast.literal_eval('[' + value + ']')))
            key, value = '', ''
        else:
            value = line.strip()[1:-1]
            pairs.append((key, ast.literal_eval('[' + value + ']')))
    # name = Path.GetFileName(file_path)
    file1 = open(file_name + "_" + type + "_tokenized.txt","w")
    for token, scope in pairs:
        if token == '': continue
        if 'punctuation.definition.comment.java' in scope or 'comment.block.javadoc.java' in scope or 'comment.line.double-slash.java' in scope: continue
        file1.write(token)
