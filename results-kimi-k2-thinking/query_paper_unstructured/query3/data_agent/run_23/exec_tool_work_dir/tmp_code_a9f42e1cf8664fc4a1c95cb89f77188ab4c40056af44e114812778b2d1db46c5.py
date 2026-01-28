code = """import json, re

# Load the papers from the file path stored in var_functions.query_db:20
file_path = locals()['var_functions.query_db:20']
with open(file_path, 'r') as f:
    papers = json.load(f)

print(f"Loaded {len(papers)} papers")

# Extract paper info: title, year, and check for empirical contribution
empirical_papers_after_2016 = []
for paper in papers:
    text = paper['text']
    filename = paper['filename']
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Extract year - look for patterns like CHI 2018, Ubicomp 2017, etc.
    # Common venues: CHI, Ubicomp, CSCW, DIS, PervasiveHealth, WWW, IUI, OzCHI, TEI, AH
    year_match = re.search(r'(CHI|CSCW|Ubicomp|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\D*(\d{4})', text)
    
    year = int(year_match.group(2)) if year_match else 0
    
    # Check for empirical contribution - look for "empirical" in text
    # The hint says to use substring/contains matching
    has_empirical = 'empirical' in text.lower()
    
    # Filter: empirical contribution AND year > 2016
    if has_empirical and year > 2016:
        empirical_papers_after_2016.append({
            'title': title,
            'year': year
        })

print(f"Found {len(empirical_papers_after_2016)} papers with empirical contribution published after 2016")

# Save result for next steps
result = json.dumps(empirical_papers_after_2016)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': [{'title': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'year': 2018}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
