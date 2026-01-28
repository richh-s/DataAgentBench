code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-11339180666459361146'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

with open(locals()['var_function-call-11339180666459360437'], 'r') as f:
    civic_docs_data = json.load(f)

# Normalize names
funding_names = funding_df['Project_Name'].unique().tolist()
funding_names.sort(key=len, reverse=True)

matched_projects = set()
debug_info = []

spring_patterns = [r"spring\s*,?\s*2022", r"march\s*,?\s*2022", r"april\s*,?\s*2022", r"may\s*,?\s*2022"]
start_keywords = ["begin", "start", "advertise", "award"]

def check_segment(segment):
    lines = segment.split('\n')
    for line in lines:
        line_lower = line.lower()
        # Check for spring date
        has_spring = False
        for pat in spring_patterns:
            if re.search(pat, line_lower):
                has_spring = True
                break
        
        if has_spring:
            # Check for start keyword
            if any(kw in line_lower for kw in start_keywords):
                return True, line
    return False, None

for doc in civic_docs_data:
    text = doc['text']
    # Find positions of projects
    project_locs = []
    for name in funding_names:
        # Simple find, assuming distinct names
        # Use re.escape to handle special chars in name
        for match in re.finditer(re.escape(name), text, re.IGNORECASE):
            project_locs.append((match.start(), name))
            
    project_locs.sort()
    
    # Analyze segments
    for i in range(len(project_locs)):
        start_idx, p_name = project_locs[i]
        if i < len(project_locs) - 1:
            end_idx = project_locs[i+1][0]
        else:
            end_idx = len(text)
            
        segment = text[start_idx:end_idx]
        is_match, line = check_segment(segment)
        if is_match:
            matched_projects.add(p_name)
            debug_info.append((p_name, line))

# Calc totals
filtered_funding = funding_df[funding_df['Project_Name'].isin(matched_projects)]
# Remove duplicates if any (Funding_ID should be unique but Project_Name might repeat? No, distinct projects)
# Wait, Funding table has Funding_ID. Can a project have multiple funding sources?
# Preview showed: "Birdview Avenue Improvements" has multiple entries with different Funding_ID and Sources.
# "Project_Name" is the join key.
# The query asks "what is their total funding?".
# This implies summing ALL funding records for the matched projects.
total_funding = filtered_funding['Amount'].astype(int).sum()
# "How many projects started..."
# This implies the count of unique *projects*, not funding records.
num_projects = len(matched_projects)

print("__RESULT__:")
print(json.dumps({
    "num_projects": num_projects,
    "total_funding": int(total_funding),
    "matched_projects_list": list(matched_projects),
    "debug": debug_info
}))"""

env_args = {'var_function-call-2238045295135148005': ['civic_docs'], 'var_function-call-2238045295135146372': 'file_storage/function-call-2238045295135146372.json', 'var_function-call-2238045295135148835': ['Funding'], 'var_function-call-2238045295135147202': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-11339180666459360437': 'file_storage/function-call-11339180666459360437.json', 'var_function-call-11339180666459361146': 'file_storage/function-call-11339180666459361146.json'}

exec(code, env_args)
