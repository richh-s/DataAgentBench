code = """import json
import re

# Load the query result
file_path = locals()['var_function-call-5896966146300588964']
with open(file_path, 'r') as f:
    papers = json.load(f)

# Filter papers
matches = []
for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check domain
    if 'physical activity' not in text.lower():
        continue
        
    # Check year in header (first 1000 chars)
    header = text[:1000]
    
    # Heuristics for 2016
    # Look for "2016" or "'16" associated with typical conference words or copyright
    # Pattern examples: "CHI 2016", "UbiComp '16", "Copyright 2016", "September 7-11, 2016"
    
    is_2016 = False
    
    # Specific patterns
    if re.search(r'\b2016\b', header):
        # Check if it's not a reference to a past year like "Since 2016..." (unlikely in header)
        # Check if it's not 2017, 2018 in the same header (which would imply published later)
        if not re.search(r'\b201[7-9]\b', header): 
            is_2016 = True
    elif re.search(r"'\s*16\b", header): # matches '16
        if not re.search(r"'\s*1[7-9]\b", header):
             is_2016 = True

    if is_2016:
        matches.append(title)

print(f"__RESULT__:\n{json.dumps(matches)}")"""

env_args = {'var_function-call-2683298839036433804': ['paper_docs'], 'var_function-call-17469928963468779101': 'file_storage/function-call-17469928963468779101.json', 'var_function-call-5896966146300588964': 'file_storage/function-call-5896966146300588964.json'}

exec(code, env_args)
