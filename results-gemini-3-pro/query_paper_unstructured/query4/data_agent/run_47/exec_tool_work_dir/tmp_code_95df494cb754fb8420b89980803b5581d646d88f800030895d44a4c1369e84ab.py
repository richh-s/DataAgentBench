code = """import json
import re

# Load papers from the previously stored file
file_path = locals()['var_function-call-1660175416261696799']
with open(file_path, 'r') as f:
    papers = json.load(f)

target_titles = []

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    if not filename:
        continue
    title = filename.replace('.txt', '')
    
    # 1. Extract Year
    # Look for "2016" in the first 500 characters (Header usually contains venue and year)
    header = text[:500]
    
    # Sometimes header might be messy.
    # Let's look for strict 2016.
    if '2016' in header:
        # 2. Extract Domain
        # Check for 'physical activity' in Title, Abstract, Keywords.
        # We limit search to first 3000 chars to avoid catching references.
        # Also check title explicitly.
        
        search_area = (title + "\n" + text[:3000]).lower()
        
        if 'physical activity' in search_area:
            target_titles.append(title)

print("__RESULT__:")
print(json.dumps(target_titles))"""

env_args = {'var_function-call-8186241074131223286': ['paper_docs'], 'var_function-call-8186241074131224069': ['Citations', 'sqlite_sequence'], 'var_function-call-11444584410328735250': 'file_storage/function-call-11444584410328735250.json', 'var_function-call-1660175416261696799': 'file_storage/function-call-1660175416261696799.json'}

exec(code, env_args)
