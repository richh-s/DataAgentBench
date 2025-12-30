code = """import json
import pandas as pd
import re

with open(locals()['var_function-call-6201891487600376940'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

with open(locals()['var_function-call-6201891487600376067'], 'r') as f:
    civic_docs = json.load(f)

project_names = funding_df['Project_Name'].unique().tolist()
project_names.sort(key=len, reverse=True)

completed_park_projects = set()

def check_completion_strict(text):
    text_lower = text.lower()
    
    lines = text_lower.splitlines()
    for line in lines:
        if '2022' in line and 'completed' in line:
            # Exclusions
            bad_keywords = ['design', 'study', 'review', 'application', 'plans', 'draft', 'expected', 'anticipated', 'schedule']
            if any(bk in line for bk in bad_keywords):
                # But what if "Construction schedule was completed..."? No.
                # "Draft plans completed" -> Bad.
                # "Construction expected to be completed" -> Bad.
                continue
            
            # Must contain construction or project or be "was completed"
            if 'construction' in line or 'project' in line or 'was completed' in line or 'completed on' in line or 'completed in' in line:
                 return True
    return False

# Check Point Dume for curiosity
point_dume_is_park = False

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
        
        # Check Point Dume specifically
        if p_name == "Point Dume Walkway Repairs":
             if 'park' in segment.lower():
                 point_dume_is_park = True

        if is_park:
            if check_completion_strict(segment):
                completed_park_projects.add(p_name)

matched_rows = funding_df[funding_df['Project_Name'].isin(completed_park_projects)]
total_funding = matched_rows['Amount'].astype(float).sum()

print("__RESULT__:")
print(json.dumps({
    "completed_park_projects": list(completed_park_projects),
    "total_funding": total_funding,
    "point_dume_is_park_in_text": point_dume_is_park
}))"""

env_args = {'var_function-call-6201891487600376067': 'file_storage/function-call-6201891487600376067.json', 'var_function-call-6201891487600376940': 'file_storage/function-call-6201891487600376940.json', 'var_function-call-12487084379305047571': {'completed_park_projects': ['Bluffs Park Shade Structure', 'Permanent Skate Park'], 'total_funding': 118000.0}, 'var_function-call-4658572295020172765': {'completed_park_projects': ['Bluffs Park Shade Structure', 'Permanent Skate Park'], 'total_funding': 118000.0, 'debug_snippets': {'Bluffs Park Shade Structure': '(cid:190) updates: construction was completed november 2022. notice of completion', 'Permanent Skate Park': 'draft plans are expected to be completed in early 2022. the planning'}}}

exec(code, env_args)
