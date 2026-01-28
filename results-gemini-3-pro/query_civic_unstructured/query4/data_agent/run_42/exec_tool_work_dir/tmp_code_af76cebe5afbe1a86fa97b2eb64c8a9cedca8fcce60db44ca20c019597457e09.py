code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-6790771977792377935'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

with open(locals()['var_function-call-17703270697767214172'], 'r') as f:
    civic_docs = json.load(f)

found_projects = set()
start_terms = ["Begin Construction", "Start Construction", "Construction Start", "Project Start"]
target_dates = ["Spring 2022", "March 2022", "April 2022", "May 2022"]

for doc in civic_docs:
    text = doc.get('text', '')
    # Use splitlines to be safe
    lines = text.splitlines()
    
    for i in range(len(lines) - 1):
        line = lines[i].strip()
        next_line = lines[i+1].strip()
        
        # Check markers
        if ("Updates:" in next_line or "Project Description:" in next_line) and line:
            project_name = line
            
            # Extract block
            block_content = ""
            for j in range(i+1, min(len(lines), i+100)):
                # Stop if next line is a header
                if j < len(lines)-1:
                    nxt = lines[j+1]
                    if ("Updates:" in nxt or "Project Description:" in nxt) and lines[j].strip():
                        break
                block_content += lines[j] + " "
            
            # Check for dates
            found = False
            for term in start_terms:
                for date in target_dates:
                    # Simple check: term followed by date within some char limit
                    # Use string find
                    t_idx = block_content.lower().find(term.lower())
                    if t_idx != -1:
                        # Look for date in the chunk after term
                        chunk = block_content[t_idx:t_idx+100].lower()
                        if date.lower() in chunk:
                            found_projects.add(project_name)
                            found = True
                            break
                if found: break

clean_found = {p.strip() for p in found_projects}
matched = funding_df[funding_df['Project_Name'].isin(clean_found)]

print("__RESULT__:")
print(json.dumps({
    "found_projects": list(clean_found),
    "matched_projects": matched['Project_Name'].tolist(),
    "matched_count": len(matched),
    "total_funding": int(matched['Amount'].astype(int).sum())
}))"""

env_args = {'var_function-call-6629743294879476725': ['civic_docs'], 'var_function-call-6629743294879475928': ['Funding'], 'var_function-call-6790771977792377935': 'file_storage/function-call-6790771977792377935.json', 'var_function-call-6790771977792376994': 'file_storage/function-call-6790771977792376994.json', 'var_function-call-17703270697767214172': 'file_storage/function-call-17703270697767214172.json'}

exec(code, env_args)
