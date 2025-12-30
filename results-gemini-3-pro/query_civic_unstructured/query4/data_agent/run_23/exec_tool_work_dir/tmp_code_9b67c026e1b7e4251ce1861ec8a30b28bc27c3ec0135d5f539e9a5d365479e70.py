code = """import json
import pandas as pd
import re

# Load data
docs_path = locals()['var_function-call-12003933845837938718']
funding_path = locals()['var_function-call-7144794427946386972']

with open(docs_path, 'r') as f:
    docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
project_names = set(funding_df['Project_Name'].unique())

matches = []

for doc in docs:
    text = doc['text']
    # Find all start indices of "Spring 2022"
    # Regex for Spring 2022
    # Case insensitive
    date_matches = list(re.finditer(r'(Spring[\s,-]*2022|2022[\s,-]*Spring)', text, re.IGNORECASE))
    
    for dm in date_matches:
        date_start = dm.start()
        match_str = dm.group()
        
        # Find the nearest preceding project name
        # We search for all project names in the text up to date_start
        # and pick the one with the largest start index (closest to date)
        
        closest_project = None
        closest_dist = float('inf')
        
        # Optimization: Scan the text backwards from date_start?
        # Or scan all project names?
        # Scanning all project names (70+) against the text might be slow if text is huge, but it's likely fine.
        # But scanning backwards from date_start is better if we can identify headers.
        # Since we don't know header format, checking all names is safer.
        
        best_pn = None
        max_idx = -1
        
        for pn in project_names:
            # Find the last occurrence of pn before date_start
            # We can substring text[:date_start] and rfind
            idx = text.rfind(pn, 0, date_start)
            if idx != -1:
                if idx > max_idx:
                    max_idx = idx
                    best_pn = pn
        
        # Check if the distance is reasonable (e.g., within 2000 characters)
        # to avoid associating with a project mentioned pages ago.
        if max_idx != -1 and (date_start - max_idx) < 3000:
            # Extract the line or context
            # Find the line boundaries
            line_start = text.rfind('\n', 0, date_start) + 1
            line_end = text.find('\n', date_start)
            if line_end == -1: line_end = len(text)
            line = text[line_start:line_end].strip()
            
            matches.append({
                "project": best_pn,
                "context_line": line,
                "filename": doc['filename']
            })

print("__RESULT__:")
print(json.dumps(matches))"""

env_args = {'var_function-call-7144794427946386357': 'file_storage/function-call-7144794427946386357.json', 'var_function-call-7144794427946386972': 'file_storage/function-call-7144794427946386972.json', 'var_function-call-12003933845837938718': 'file_storage/function-call-12003933845837938718.json', 'var_function-call-16291157491090177624': {'doc_count': 5, 'funding_count': 500, 'matches': ['malibucity_agenda__01262022-1835.txt', 'malibucity_agenda__01272021-1626.txt', 'malibucity_agenda__03022021-1648.txt', 'malibucity_agenda__03232022-1869.txt']}}

exec(code, env_args)
