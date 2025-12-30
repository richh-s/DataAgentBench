code = """import json
import pandas as pd
import re

# Load Funding Data
with open(locals()['var_function-call-11339180666459361146'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

# Load Civic Docs
with open(locals()['var_function-call-11339180666459360437'], 'r') as f:
    civic_docs_data = json.load(f)

# Normalize project names
funding_names = funding_df['Project_Name'].unique().tolist()
# Sort by length descending to match longer names first
funding_names.sort(key=len, reverse=True)

matched_projects = set()
debug_info = []

# Keywords
spring_months = ["march 2022", "april 2022", "may 2022"]
spring_terms = ["spring 2022", "spring, 2022"] + spring_months
start_terms = ["begin", "start", "advertise", "award"] 
# "Award" contract might be start. "Advertise" is start of bidding.
# Let's be generous with "Start" indicators but strict on date.

def is_start_date_in_spring(text_segment):
    lines = text_segment.split('\n')
    for line in lines:
        line_lower = line.lower()
        # Check date
        has_spring = any(t in line_lower for t in spring_terms)
        if has_spring:
            # Check context
            if any(s in line_lower for s in start_terms):
                return True, line
    return False, None

# Process each doc
for doc in civic_docs_data:
    full_text = doc['text']
    
    # Find all project name occurrences
    # We map start_index -> project_name
    project_indices = []
    
    for name in funding_names:
        # Simple string find might be too loose if name is short, but project names seem specific enough.
        # We assume headers are exact matches or close.
        # Let's try to find exact string match (case insensitive)
        pattern = re.escape(name)
        for match in re.finditer(pattern, full_text, re.IGNORECASE):
            project_indices.append((match.start(), name))
            
    # Sort indices
    project_indices.sort()
    
    # Iterate through segments
    for i in range(len(project_indices)):
        start_pos, p_name = project_indices[i]
        # End pos is start of next project or reasonable limit
        if i < len(project_indices) - 1:
            end_pos = project_indices[i+1][0]
        else:
            end_pos = len(full_text)
            
        # Extract segment
        segment = full_text[start_pos:end_pos]
        
        # Check for start in spring 2022
        is_start, line = is_start_date_in_spring(segment)
        if is_start:
            matched_projects.add(p_name)
            debug_info.append({"project": p_name, "line": line})

# Calculate result
filtered_funding = funding_df[funding_df['Project_Name'].isin(matched_projects)]
total_funding = filtered_funding['Amount'].astype(int).sum()
count = len(filtered_funding)

print("__RESULT__:")
print(json.dumps({
    "count": count,
    "total_funding": int(total_funding),
    "projects": list(matched_projects),
    "debug": debug_info
}))"""

env_args = {'var_function-call-2238045295135148005': ['civic_docs'], 'var_function-call-2238045295135146372': 'file_storage/function-call-2238045295135146372.json', 'var_function-call-2238045295135148835': ['Funding'], 'var_function-call-2238045295135147202': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-11339180666459360437': 'file_storage/function-call-11339180666459360437.json', 'var_function-call-11339180666459361146': 'file_storage/function-call-11339180666459361146.json'}

exec(code, env_args)
