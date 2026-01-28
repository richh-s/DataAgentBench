code = """import json
import re

# Load the result from the previous query
with open(locals()['var_function-call-13279962160185395984'], 'r') as f:
    papers = json.load(f)

titles_2016 = []

for p in papers:
    text = p['text']
    filename = p['filename']
    title = filename.replace('.txt', '')
    
    # Check for 2016 publication year
    # Check first 2000 chars for 2016 in context of conference or copyright
    # e.g., "CHI '16", "UbiComp '16", "2016"
    
    head = text[:3000]
    tail = text[-2000:]
    
    # Heuristic: Look for 2016 near Copyright or Conference Name
    # Regex for "2016" surrounded by non-digits (to avoid 20160 citations or page numbers if possible)
    # But simpler: just "2016" in header usually indicates year.
    # Also " '16 " might indicate year.
    
    is_2016 = False
    if '2016' in head or '2016' in tail:
        is_2016 = True
    elif " '16 " in head:
        is_2016 = True
        
    # Also check if it's NOT 2015, 2014 etc.
    # Sometimes 2016 appears in citations.
    # Ideally we look for "Copyright 2016" or "Conference 2016"
    
    # Better check: 
    # Look for lines like "CHI '16, May 07 - 12 2016" or "Copyright © 2016"
    if re.search(r"Copyright\s+(\u00a9\s+)?2016", text, re.IGNORECASE):
        is_2016 = True
    elif re.search(r"\b2016\b", head): # 2016 in header
        is_2016 = True
    
    if is_2016:
        titles_2016.append(title)

print("__RESULT__:")
print(json.dumps(titles_2016))"""

env_args = {'var_function-call-8316623134633316378': 'file_storage/function-call-8316623134633316378.json', 'var_function-call-14390947822849026991': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}, {'_id': '694f5530284b10b11dc0a86e'}, {'_id': '694f5530284b10b11dc0a86f'}, {'_id': '694f5530284b10b11dc0a870'}, {'_id': '694f5530284b10b11dc0a871'}, {'_id': '694f5530284b10b11dc0a872'}, {'_id': '694f5530284b10b11dc0a873'}, {'_id': '694f5530284b10b11dc0a874'}, {'_id': '694f5530284b10b11dc0a875'}, {'_id': '694f5530284b10b11dc0a876'}, {'_id': '694f5530284b10b11dc0a877'}, {'_id': '694f5530284b10b11dc0a878'}, {'_id': '694f5530284b10b11dc0a879'}, {'_id': '694f5530284b10b11dc0a87a'}, {'_id': '694f5530284b10b11dc0a87b'}, {'_id': '694f5530284b10b11dc0a87c'}, {'_id': '694f5530284b10b11dc0a87d'}, {'_id': '694f5530284b10b11dc0a87e'}, {'_id': '694f5530284b10b11dc0a87f'}, {'_id': '694f5530284b10b11dc0a880'}, {'_id': '694f5530284b10b11dc0a881'}, {'_id': '694f5530284b10b11dc0a882'}, {'_id': '694f5530284b10b11dc0a883'}, {'_id': '694f5530284b10b11dc0a884'}, {'_id': '694f5530284b10b11dc0a885'}, {'_id': '694f5530284b10b11dc0a886'}, {'_id': '694f5530284b10b11dc0a887'}, {'_id': '694f5530284b10b11dc0a888'}, {'_id': '694f5530284b10b11dc0a889'}, {'_id': '694f5530284b10b11dc0a88a'}, {'_id': '694f5530284b10b11dc0a88b'}, {'_id': '694f5530284b10b11dc0a88c'}, {'_id': '694f5530284b10b11dc0a88d'}, {'_id': '694f5530284b10b11dc0a88e'}, {'_id': '694f5530284b10b11dc0a88f'}, {'_id': '694f5530284b10b11dc0a890'}, {'_id': '694f5530284b10b11dc0a891'}, {'_id': '694f5530284b10b11dc0a892'}, {'_id': '694f5530284b10b11dc0a893'}, {'_id': '694f5530284b10b11dc0a894'}, {'_id': '694f5530284b10b11dc0a895'}, {'_id': '694f5530284b10b11dc0a896'}, {'_id': '694f5530284b10b11dc0a897'}, {'_id': '694f5530284b10b11dc0a898'}, {'_id': '694f5530284b10b11dc0a899'}, {'_id': '694f5530284b10b11dc0a89a'}, {'_id': '694f5530284b10b11dc0a89b'}, {'_id': '694f5530284b10b11dc0a89c'}, {'_id': '694f5530284b10b11dc0a89d'}, {'_id': '694f5530284b10b11dc0a89e'}, {'_id': '694f5530284b10b11dc0a89f'}, {'_id': '694f5530284b10b11dc0a8a0'}, {'_id': '694f5530284b10b11dc0a8a1'}, {'_id': '694f5530284b10b11dc0a8a2'}, {'_id': '694f5530284b10b11dc0a8a3'}, {'_id': '694f5530284b10b11dc0a8a4'}, {'_id': '694f5530284b10b11dc0a8a5'}, {'_id': '694f5530284b10b11dc0a8a6'}, {'_id': '694f5530284b10b11dc0a8a7'}, {'_id': '694f5530284b10b11dc0a8a8'}, {'_id': '694f5530284b10b11dc0a8a9'}, {'_id': '694f5530284b10b11dc0a8aa'}, {'_id': '694f5530284b10b11dc0a8ab'}, {'_id': '694f5530284b10b11dc0a8ac'}, {'_id': '694f5530284b10b11dc0a8ad'}, {'_id': '694f5530284b10b11dc0a8ae'}, {'_id': '694f5530284b10b11dc0a8af'}, {'_id': '694f5530284b10b11dc0a8b0'}, {'_id': '694f5530284b10b11dc0a8b1'}, {'_id': '694f5530284b10b11dc0a8b2'}, {'_id': '694f5530284b10b11dc0a8b3'}, {'_id': '694f5530284b10b11dc0a8b4'}, {'_id': '694f5530284b10b11dc0a8b5'}, {'_id': '694f5530284b10b11dc0a8b6'}, {'_id': '694f5530284b10b11dc0a8b7'}, {'_id': '694f5530284b10b11dc0a8b8'}, {'_id': '694f5530284b10b11dc0a8b9'}, {'_id': '694f5530284b10b11dc0a8ba'}, {'_id': '694f5530284b10b11dc0a8bb'}, {'_id': '694f5530284b10b11dc0a8bc'}, {'_id': '694f5530284b10b11dc0a8bd'}, {'_id': '694f5530284b10b11dc0a8be'}, {'_id': '694f5530284b10b11dc0a8bf'}, {'_id': '694f5530284b10b11dc0a8c0'}, {'_id': '694f5530284b10b11dc0a8c1'}, {'_id': '694f5530284b10b11dc0a8c2'}, {'_id': '694f5530284b10b11dc0a8c3'}, {'_id': '694f5530284b10b11dc0a8c4'}, {'_id': '694f5530284b10b11dc0a8c5'}, {'_id': '694f5530284b10b11dc0a8c6'}, {'_id': '694f5530284b10b11dc0a8c7'}, {'_id': '694f5530284b10b11dc0a8c8'}, {'_id': '694f5530284b10b11dc0a8c9'}, {'_id': '694f5530284b10b11dc0a8ca'}, {'_id': '694f5530284b10b11dc0a8cb'}], 'var_function-call-13279962160185395984': 'file_storage/function-call-13279962160185395984.json'}

exec(code, env_args)
