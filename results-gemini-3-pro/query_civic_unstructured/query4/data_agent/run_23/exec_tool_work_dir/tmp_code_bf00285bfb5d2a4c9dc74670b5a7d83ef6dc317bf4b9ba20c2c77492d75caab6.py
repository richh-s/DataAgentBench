code = """import json
import pandas as pd
import re

docs_path = locals()['var_function-call-12003933845837938718']
funding_path = locals()['var_function-call-7144794427946386972']

with open(docs_path, "r") as f:
    docs = json.load(f)

with open(funding_path, "r") as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
project_names = set(funding_df["Project_Name"].unique())

matches = []

for doc in docs:
    text = doc["text"]
    # regex pattern
    pattern = r"(Spring[\s,-]*2022|2022[\s,-]*Spring)"
    date_matches = list(re.finditer(pattern, text, re.IGNORECASE))
    
    for dm in date_matches:
        date_start = dm.start()
        
        best_pn = None
        max_idx = -1
        
        for pn in project_names:
            idx = text.rfind(pn, 0, date_start)
            if idx != -1:
                if idx > max_idx:
                    max_idx = idx
                    best_pn = pn
        
        if max_idx != -1 and (date_start - max_idx) < 3000:
            line_start = text.rfind("\n", 0, date_start) + 1
            line_end = text.find("\n", date_start)
            if line_end == -1: line_end = len(text)
            line = text[line_start:line_end].strip()
            
            matches.append({
                "project": best_pn,
                "context_line": line,
                "filename": doc["filename"]
            })

print("__RESULT__:")
print(json.dumps(matches))"""

env_args = {'var_function-call-7144794427946386357': 'file_storage/function-call-7144794427946386357.json', 'var_function-call-7144794427946386972': 'file_storage/function-call-7144794427946386972.json', 'var_function-call-12003933845837938718': 'file_storage/function-call-12003933845837938718.json', 'var_function-call-16291157491090177624': {'doc_count': 5, 'funding_count': 500, 'matches': ['malibucity_agenda__01262022-1835.txt', 'malibucity_agenda__01272021-1626.txt', 'malibucity_agenda__03022021-1648.txt', 'malibucity_agenda__03232022-1869.txt']}}

exec(code, env_args)
