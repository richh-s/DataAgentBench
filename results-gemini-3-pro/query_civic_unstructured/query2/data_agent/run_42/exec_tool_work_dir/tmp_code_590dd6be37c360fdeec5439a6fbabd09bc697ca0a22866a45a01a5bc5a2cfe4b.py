code = """import json
import pandas as pd

# Load Funding Data
with open(locals()['var_function-call-6201891487600376940'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

# Load Civic Docs
with open(locals()['var_function-call-6201891487600376067'], 'r') as f:
    civic_docs = json.load(f)

# Get unique project names from funding
project_names = funding_df['Project_Name'].unique().tolist()
project_names.sort(key=len, reverse=True)

completed_park_projects = set()

def is_completed_in_2022(text):
    text_lower = text.lower()
    if '2022' not in text_lower:
        return False
    if 'completed' not in text_lower:
        return False
    
    lines = text_lower.split('\n')
    for line in lines:
        if '2022' in line and 'completed' in line:
            # Avoid "complete design"
            if 'design' in line:
                if 'construction' in line:
                    return True
                # Skip if only design
                continue
            return True
    return False

for doc in civic_docs:
    content = doc['text']
    content_lower = content.lower()
    
    positions = []
    for p_name in project_names:
        idx = content_lower.find(p_name.lower())
        while idx != -1:
            positions.append((idx, p_name))
            idx = content_lower.find(p_name.lower(), idx + 1)
            
    positions.sort(key=lambda x: x[0])
    
    unique_positions = []
    if positions:
        curr_idx, curr_name = positions[0]
        unique_positions.append((curr_idx, curr_name))
        for i in range(1, len(positions)):
            idx, name = positions[i]
            last_idx, last_name = unique_positions[-1]
            if idx < last_idx + len(last_name):
                continue
            unique_positions.append((idx, name))
            
    for i in range(len(unique_positions)):
        start_idx, p_name = unique_positions[i]
        if i < len(unique_positions) - 1:
            end_idx = unique_positions[i+1][0]
        else:
            end_idx = len(content)
            
        segment = content[start_idx:end_idx]
        
        is_park = False
        if 'park' in p_name.lower() or 'playground' in p_name.lower():
            is_park = True
        elif 'park' in segment.lower() or 'playground' in segment.lower():
             is_park = True
             
        if is_park:
            if is_completed_in_2022(segment):
                completed_park_projects.add(p_name)

matched_rows = funding_df[funding_df['Project_Name'].isin(completed_park_projects)]
total_funding = matched_rows['Amount'].astype(float).sum()

print("__RESULT__:")
print(json.dumps({
    "completed_park_projects": list(completed_park_projects),
    "total_funding": total_funding
}))"""

env_args = {'var_function-call-6201891487600376067': 'file_storage/function-call-6201891487600376067.json', 'var_function-call-6201891487600376940': 'file_storage/function-call-6201891487600376940.json'}

exec(code, env_args)
