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
# Escape backslashes for JSON string transport
block_trigger = re.compile(r'\(cid:190\)\s*(Updates|Project Description|Project Updates)', re.IGNORECASE)
start_key_pattern = re.compile(r'(Begin Construction|Start Construction|Construction Start|Start Date)', re.IGNORECASE)

# Date formats: Spring 2022, 2022-Spring, March 2022, etc.
# Note: I am using \\s and \\d in the string below to ensure they survive JSON decoding and Python string parsing correctly if needed.
# Actually, inside execute_python, the string is executed. 
# If I write r'\s', and pass it via JSON, I must write '\\s'.
date_pattern_str = r'(Spring[\s,]*2022|2022[\s-]*Spring|March[\s,]*2022|April[\s,]*2022|May[\s,]*2022|2022[\s-]*0?3|2022[\s-]*0?4|2022[\s-]*0?5|0?3/\d{0,2}/?2022|0?4/\d{0,2}/?2022|0?5/\d{0,2}/?2022)'
date_pattern = re.compile(date_pattern_str, re.IGNORECASE)

matching_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line_clean = line.strip()
        
        if block_trigger.search(line_clean):
            # Find project name in previous lines
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
                # Find schedule lines
                project_lines = []
                for k in range(i, len(lines)):
                    curr_line = lines[k].strip()
                    if k > i and block_trigger.search(curr_line):
                        break
                    project_lines.append(curr_line)
                
                # Check for start date
                started_spring_2022 = False
                for pline in project_lines:
                    if start_key_pattern.search(pline):
                        if date_pattern.search(pline):
                            started_spring_2022 = True
                            break
                
                if started_spring_2022:
                    matching_projects.add(project_name.strip())

df_filtered = df_funding[df_funding['Project_Name'].isin(matching_projects)]

num_projects = len(df_filtered)
total_funding = df_filtered['Amount'].astype(float).sum()

print("__RESULT__:")
print(json.dumps({
    "matching_projects_list": list(matching_projects),
    "found_in_funding": df_filtered['Project_Name'].tolist(),
    "count": num_projects,
    "total_funding": total_funding
}))"""

env_args = {'var_function-call-956811650377216769': 'file_storage/function-call-956811650377216769.json', 'var_function-call-956811650377216698': 'file_storage/function-call-956811650377216698.json'}

exec(code, env_args)
