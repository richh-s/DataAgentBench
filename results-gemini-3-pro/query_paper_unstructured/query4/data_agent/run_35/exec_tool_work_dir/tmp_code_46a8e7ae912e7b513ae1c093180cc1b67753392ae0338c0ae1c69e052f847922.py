code = """import json
import re

# Load papers from the file path provided in the previous turn
# The key for the file path is 'var_function-call-3854438315303576261'
with open(locals()['var_function-call-3854438315303576261'], 'r') as f:
    papers = json.load(f)

target_titles = []

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check Year 2016
    # Look for "2016" in the first 500 characters (header/copyright usually)
    # Also check for '16 if 2016 is not explicit, but '16 could be risky.
    # The example "UBICOMP '15... 2015" suggests full year is present.
    header = text[:1000]
    if "2016" in header:
        is_2016 = True
    else:
        is_2016 = False
        
    # Check Domain 'physical activity'
    # Look in the first 5000 chars to cover abstract and keywords and intro
    content_sample = text[:5000].lower()
    if "physical activity" in content_sample:
        is_domain = True
    else:
        is_domain = False
    
    if is_2016 and is_domain:
        target_titles.append(title)

print("__RESULT__:")
print(json.dumps(target_titles))"""

env_args = {'var_function-call-13095614406444105074': 'file_storage/function-call-13095614406444105074.json', 'var_function-call-3854438315303576261': 'file_storage/function-call-3854438315303576261.json'}

exec(code, env_args)
