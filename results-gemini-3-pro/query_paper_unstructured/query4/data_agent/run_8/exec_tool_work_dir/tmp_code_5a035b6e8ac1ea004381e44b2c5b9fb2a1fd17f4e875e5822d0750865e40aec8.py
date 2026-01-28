code = """import json
import re

# Load the papers potentially from 2016
with open(locals()['var_function-call-2142637407128357390'], 'r') as f:
    papers = json.load(f)

titles_2016_pa = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Check for Physical Activity
    if 'physical activity' in text.lower():
        # Check for Year 2016
        # We look for explicit year indicators
        # 1. Copyright line
        # 2. Conference header
        
        is_2016 = False
        
        # Check first 3000 chars for header info
        header = text[:3000]
        
        # Patterns for 2016
        # "Copyright 2016"
        # "Copyright (c) 2016"
        # "Copyright © 2016"
        # "CHI 2016"
        # "Ubicomp '16"
        # "September ... 2016"
        
        if '2016' in header:
            # Found 2016 in header. 
            # Could be "Copyright 2016" or "2016" in date.
            # Avoid [16] or page 2016 (unlikely in header)
            is_2016 = True
        elif "'16" in header or "’16" in header:
            # Check for conference abbreviation style
            if re.search(r"[A-Z]{3,}\s*'16", header) or re.search(r"[A-Z]{3,}\s*’16", header):
                is_2016 = True
        
        # Double check if it's a false positive (e.g. "Since 2016" in abstract)
        # But for this task, presence in header is the best heuristic.
        
        if is_2016:
            title = filename.replace('.txt', '')
            titles_2016_pa.append(title)

print("__RESULT__:")
print(json.dumps(titles_2016_pa))"""

env_args = {'var_function-call-1760363004607511404': 'file_storage/function-call-1760363004607511404.json', 'var_function-call-1760363004607508631': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}], 'var_function-call-12400401275276692089': 'file_storage/function-call-12400401275276692089.json', 'var_function-call-18372255859020147212': 'file_storage/function-call-18372255859020147212.json', 'var_function-call-6662495405269273368': [], 'var_function-call-11090582513645745945': 'file_storage/function-call-11090582513645745945.json', 'var_function-call-2142637407128357390': 'file_storage/function-call-2142637407128357390.json'}

exec(code, env_args)
