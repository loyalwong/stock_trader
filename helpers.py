import json

def file2dict(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)