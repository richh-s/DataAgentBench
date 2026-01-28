code = """import json
import pandas as pd

# Load MongoDB results
path_civic = locals()['var_function-call-956811650377216769']
with open(path_civic, 'r') as f:
    civic_docs = json.load(f)

# Load Funding results
path_funding = locals()['var_function-call-956811650377216698']
with open(path_funding, 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)

matching_projects = set()
target_terms = ["Spring 2022", "Spring, 2022", "March 2022", "April 2022", "May 2022", "March, 2022", "April, 2022", "May, 2022"]
start_terms = ["Begin Construction", "Start Construction", "Construction Start", "Start Date"]

for doc in civic_docs:
    text = doc.get("text", "")
    lines = text.split("\n")
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check for project name trigger
        if "Updates:" in line or "Project Description:" in line:
            # Get project name from previous lines
            project_name = ""
            for j in range(i-1, -1, -1):
                prev = lines[j].strip()
                if not prev:
                    continue
                if "Agenda" in prev or "Page" in prev or "Capital Improvement" in prev:
                    break
                project_name = prev
                break
            
            if project_name:
                # Look ahead for start date
                found_date = False
                for k in range(i, min(i+50, len(lines))):
                    curr = lines[k].strip()
                    if k > i and ("Updates:" in curr or "Project Description:" in curr):
                        break
                    
                    # Check start terms
                    is_start_line = False
                    for sterm in start_terms:
                        if sterm.lower() in curr.lower():
                            is_start_line = True
                            break
                    
                    if is_start_line:
                        # Check date terms
                        for dterm in target_terms:
                            if dterm.lower() in curr.lower():
                                found_date = True
                                break
                        if not found_date:
                            if "2022" in curr and "Spring" in curr:
                                found_date = True
                            if "2022-03" in curr or "2022-04" in curr or "2022-05" in curr:
                                found_date = True
                                
                    if found_date:
                        matching_projects.add(project_name)
                        break

# Filter funding
df_filtered = df_funding[df_funding["Project_Name"].isin(matching_projects)]
count = len(df_filtered)
total = df_filtered["Amount"].astype(float).sum()

print("__RESULT__:")
print(json.dumps({
    "matching_projects_list": list(matching_projects),
    "count": count,
    "total_funding": total
}))"""

env_args = {'var_function-call-956811650377216769': 'file_storage/function-call-956811650377216769.json', 'var_function-call-956811650377216698': 'file_storage/function-call-956811650377216698.json'}

exec(code, env_args)
