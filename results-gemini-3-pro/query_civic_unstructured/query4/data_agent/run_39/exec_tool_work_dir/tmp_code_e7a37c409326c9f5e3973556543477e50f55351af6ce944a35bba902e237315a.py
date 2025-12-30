code = """import json
import sqlite3
import pandas as pd
import re

# Load Funding data
funding_path = locals()['var_function-call-5679613479952350120']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
# Create a set of project names for lookup
project_names = set(df_funding['Project_Name'].unique())
project_funding_map = df_funding.set_index('Project_Name')['Amount'].to_dict()

# Load Civic Docs
docs_path = locals()['var_function-call-5679613479952350149']
with open(docs_path, 'r') as f:
    docs_data = json.load(f)

# Define target dates
target_months = ["march", "april", "may"]

found_projects = set()

for doc in docs_data:
    text = doc.get('text', '')
    if not text:
        continue
        
    for proj in project_names:
        if proj in found_projects:
            continue
            
        if proj in text:
            # Find all occurrences of the project name
            start_indices = [m.start() for m in re.finditer(re.escape(proj), text)]
            
            for idx in start_indices:
                # Look at context window after the name
                window = text[idx:idx+2000]
                
                # Check for "Begin Construction" or similar
                # Regex to capture the date part
                # We look for "Begin Construction" followed by some text that contains our date
                # Or just check for the presence of "Begin Construction" ... "Spring 2022" near each other?
                # The structure is usually key: value.
                
                # Let's extract lines that contain "Begin Construction"
                lines = window.split('\n')
                for line in lines:
                    if "Begin Construction" in line or "Start Date" in line:
                        lower_line = line.lower()
                        if "2022" in lower_line:
                            if "spring" in lower_line:
                                found_projects.add(proj)
                            elif any(m in lower_line for m in target_months):
                                found_projects.add(proj)

# Calculate total funding
total_funding = 0
count = 0
for proj in found_projects:
    amt = project_funding_map.get(proj, 0)
    if isinstance(amt, str):
        try:
            amt = int(amt)
        except:
            amt = 0
    total_funding += amt
    count += 1

result = {"count": count, "total_funding": total_funding, "projects": list(found_projects)}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-10787328583776950224': ['civic_docs'], 'var_function-call-10787328583776949317': ['Funding'], 'var_function-call-8503351920656414567': 'file_storage/function-call-8503351920656414567.json', 'var_function-call-5679613479952350149': 'file_storage/function-call-5679613479952350149.json', 'var_function-call-5679613479952350120': 'file_storage/function-call-5679613479952350120.json'}

exec(code, env_args)
