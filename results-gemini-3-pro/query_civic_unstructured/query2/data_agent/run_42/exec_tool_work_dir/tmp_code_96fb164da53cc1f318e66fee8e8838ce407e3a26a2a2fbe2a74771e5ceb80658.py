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
debug_snippets = {}

def check_completion_strict(text):
    text_lower = text.lower()
    # Regex for "construction/project/work ... completed ... 2022" or "completed ... 2022"
    # We want to catch "Construction was completed November 2022"
    # Or "Project completed in 2022"
    
    # Simple lines check is robust if we look for keywords
    lines = text_lower.splitlines()
    for line in lines:
        if '2022' in line and 'completed' in line:
            # Must mention construction, project, work, or be "construction was completed"
            # And MUST NOT be "design completed" or "study completed" or "review completed"
            
            bad_keywords = ['design', 'study', 'review', 'application', 'phase 1'] 
            # phase 1 completion might be partial. Prompt says "projects that were completed".
            # Usually means the whole project.
            
            # Good keywords
            good_keywords = ['construction', 'project', 'work', 'installation']
            
            has_bad = any(bk in line for bk in bad_keywords)
            has_good = any(gk in line for gk in good_keywords)
            
            if has_bad and not has_good:
                continue
            
            # If it has "completed" and "2022" and not explicitly a bad thing
            # We accept "Construction was completed..." -> "construction" is good.
            # "Notice of completion filed January 2023" -> mentions "completion" but date is 2023.
            # "Construction was completed November 2022" -> Match.
            
            # Ensure 2022 is the completion year.
            # "Construction completed November 2021. Notice filed 2022." -> Should not match.
            # We need to associate 2022 with "completed".
            # Regex: completed.{0,50}2022  or  2022.{0,50}completed
            
            if re.search(r'completed.{0,50}2022', line) or re.search(r'2022.{0,50}completed', line):
                 # One last check for bad keywords in the specific match vicinity?
                 # If line is short, previous check is fine.
                 return True, line
                 
    return False, None

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
            is_completed, snippet = check_completion_strict(segment)
            if is_completed:
                completed_park_projects.add(p_name)
                debug_snippets[p_name] = snippet

matched_rows = funding_df[funding_df['Project_Name'].isin(completed_park_projects)]
total_funding = matched_rows['Amount'].astype(float).sum()

print("__RESULT__:")
print(json.dumps({
    "completed_park_projects": list(completed_park_projects),
    "total_funding": total_funding,
    "debug_snippets": debug_snippets
}))"""

env_args = {'var_function-call-6201891487600376067': 'file_storage/function-call-6201891487600376067.json', 'var_function-call-6201891487600376940': 'file_storage/function-call-6201891487600376940.json', 'var_function-call-12487084379305047571': {'completed_park_projects': ['Bluffs Park Shade Structure', 'Permanent Skate Park'], 'total_funding': 118000.0}}

exec(code, env_args)
