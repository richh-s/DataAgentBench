code = """import json
import re
import pandas as pd

# Load MongoDB results
with open(locals()['var_function-call-956811650377216769'], 'r') as f:
    civic_docs = json.load(f)

# Load Funding results
with open(locals()['var_function-call-956811650377216698'], 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)

# Regex patterns
# block_trigger: (cid:190) followed by Updates...
p1 = r"[(]cid:190[)][ ]*(Updates|Project Description|Project Updates)"
block_trigger = re.compile(p1, re.IGNORECASE)

start_key_pattern = re.compile(r"(Begin Construction|Start Construction|Construction Start|Start Date)", re.IGNORECASE)

# Date formats
# Spring 2022, 2022-Spring, March 2022, April 2022, May 2022
parts = []
parts.append(r"Spring[ ,]*2022")
parts.append(r"2022[ -]*Spring")
parts.append(r"March[ ,]*2022")
parts.append(r"April[ ,]*2022")
parts.append(r"May[ ,]*2022")
parts.append(r"2022[ -]*0?3")
parts.append(r"2022[ -]*0?4")
parts.append(r"2022[ -]*0?5")

date_pattern_str = "(" + "|".join(parts) + ")"
date_pattern = re.compile(date_pattern_str, re.IGNORECASE)

matching_projects = set()

for doc in civic_docs:
    text = doc.get("text", "")
    lines = text.split("\n")
    
    for i, line in enumerate(lines):
        line_clean = line.strip()
        
        if block_trigger.search(line_clean):
            project_name = None
            for j in range(i-1, -1, -1):
                prev_line = lines[j].strip()
                if not prev_line:
                    continue
                if "Agenda Item" in prev_line or "Page" in prev_line or "Capital Improvement" in prev_line:
                    break
                project_name = prev_line
                break
            
            if project_name:
                project_lines = []
                for k in range(i, len(lines)):
                    curr_line = lines[k].strip()
                    if k > i and block_trigger.search(curr_line):
                        break
                    project_lines.append(curr_line)
                
                for pline in project_lines:
                    if start_key_pattern.search(pline):
                        if date_pattern.search(pline):
                            matching_projects.add(project_name.strip())
                            break

df_filtered = df_funding[df_funding["Project_Name"].isin(matching_projects)]

num_projects = len(df_filtered)
total_funding = df_filtered["Amount"].astype(float).sum()

print("__RESULT__:")
print(json.dumps({
    "matching_projects_list": list(matching_projects),
    "found_in_funding": df_filtered["Project_Name"].tolist(),
    "count": num_projects,
    "total_funding": total_funding
}))"""

env_args = {'var_function-call-956811650377216769': 'file_storage/function-call-956811650377216769.json', 'var_function-call-956811650377216698': 'file_storage/function-call-956811650377216698.json'}

exec(code, env_args)
