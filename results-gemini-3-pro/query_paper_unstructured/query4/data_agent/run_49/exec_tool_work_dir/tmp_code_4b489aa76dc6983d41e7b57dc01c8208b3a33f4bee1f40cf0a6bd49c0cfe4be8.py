code = """import json
import re

# Load the result from the previous query_db call
# The key for the file path is var_function-call-11172061455759427872
try:
    with open('var_function-call-11172061455759427872', 'r') as f:
        papers = json.load(f)
except Exception as e:
    # Fallback if variable name is different or file not found (should not happen if flow is correct)
    # Accessing via locals() if needed, but the instruction says the result is stored in a file.
    # If the key was provided as a string in the message, I should use that filename.
    # But wait, the system prompt says "the storage entry will be the .json file path".
    # So the variable `var_function-call-...` contains the path string?
    # No, the previous message said: "The file path is stored under key: var_function-call-..."
    # So I should read the variable `var_function-call...` to get the path.
    # Ah, "Inside execute_python code you may read storage entries using the provided key names... e.g. locals()['var_call-1']".
    pass

# Retrieve the file path from the variable
file_path = locals()['var_function-call-11172061455759427872']
with open(file_path, 'r') as f:
    papers = json.load(f)

titles_2016 = []

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check domain
    if 'physical activity' not in text.lower():
        continue

    # Check year in header (first 500 chars)
    header = text[:500]
    
    # Regex to find years like 2010-2020 or '10-'20
    # Prioritize 4-digit years
    years_4d = re.findall(r'\b(201[0-9])\b', header)
    # Years like '16 (need to be careful not to match '1', '2' etc. usually preceeded by space or punctuation)
    years_2d = re.findall(r"['’](1[0-9])\b", header)
    
    candidates = []
    if years_4d:
        candidates.extend([int(y) for y in years_4d])
    if years_2d:
        candidates.extend([int('20' + y) for y in years_2d])
        
    if not candidates:
        continue
        
    # Heuristic: Pick the first year found.
    # If the first year is 2016, keep it.
    if candidates[0] == 2016:
        titles_2016.append(title)

print("__RESULT__:")
print(json.dumps(titles_2016))"""

env_args = {'var_function-call-3489125586506889844': 'file_storage/function-call-3489125586506889844.json', 'var_function-call-3489125586506887483': ['Citations', 'sqlite_sequence'], 'var_function-call-13585702268998000327': 'file_storage/function-call-13585702268998000327.json', 'var_function-call-13585702268998000192': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-11172061455759427872': 'file_storage/function-call-11172061455759427872.json'}

exec(code, env_args)
