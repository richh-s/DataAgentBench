code = """import json
import pandas as pd

# Load civic docs
with open(locals()['var_function-call-2498552123289550299'], 'r') as f:
    docs = json.load(f)

# Load funding data
funding_df = pd.DataFrame(json.load(open(locals()['var_function-call-4052442815910590834'])))

projects = []

for doc in docs:
    text = doc['text']
    lines = text.splitlines()
    
    current_project = None
    project_content_lines = []
    
    for i, line in enumerate(lines):
        line = line.strip()
        # check for Updates
        if "Updates:" in line:
            # Found updates, title is previous line
            title = None
            for j in range(i - 1, -1, -1):
                prev_line = lines[j].strip()
                if prev_line:
                    title = prev_line
                    break
            
            if title:
                if current_project:
                    # process previous
                    content = " ".join(project_content_lines)
                    st = None
                    if "Begin Construction:" in content:
                        # Extract date
                        start_part = content.split("Begin Construction:")[1]
                        # Take first few words
                        st = start_part.strip().split("  ")[0] 
                        # just heuristic to get the date part
                    
                    is_disaster = False
                    upper_content = content.upper()
                    upper_name = current_project['name'].upper()
                    if any(x in upper_name or x in upper_content for x in ["FEMA", "CALOES", "CALJPIA", "DISASTER"]):
                        is_disaster = True
                    
                    current_project['st'] = st
                    current_project['is_disaster'] = is_disaster
                    projects.append(current_project)
                
                current_project = {'name': title}
                project_content_lines = []
        
        if current_project:
            project_content_lines.append(line)

    # Last project
    if current_project:
        content = " ".join(project_content_lines)
        st = None
        if "Begin Construction:" in content:
            start_part = content.split("Begin Construction:")[1]
            st = start_part.strip().split("  ")[0]
            
        is_disaster = False
        upper_content = content.upper()
        upper_name = current_project['name'].upper()
        if any(x in upper_name or x in upper_content for x in ["FEMA", "CALOES", "CALJPIA", "DISASTER"]):
            is_disaster = True
            
        current_project['st'] = st
        current_project['is_disaster'] = is_disaster
        projects.append(current_project)

# Filter
target_projects = []
for p in projects:
    if p['is_disaster'] and p['st'] and '2022' in p['st']:
        target_projects.append(p)

# Sum
total_funding = 0
matched_records = []

for p in target_projects:
    p_name = p['name']
    
    # Simple logic for matching
    matches = funding_df[
        (funding_df['Project_Name'] == p_name) | 
        (funding_df['Project_Name'].str.startswith(p_name + " ("))
    ]
    
    amount_sum = pd.to_numeric(matches['Amount']).sum()
    if amount_sum > 0:
        total_funding += amount_sum
        matched_records.append({"name": p_name, "amount": amount_sum})

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "breakdown": matched_records}))"""

env_args = {'var_function-call-2498552123289550299': 'file_storage/function-call-2498552123289550299.json', 'var_function-call-4052442815910590834': 'file_storage/function-call-4052442815910590834.json'}

exec(code, env_args)
