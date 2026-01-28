code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-11339180666459361146'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

with open(locals()['var_function-call-11339180666459360437'], 'r') as f:
    civic_docs_data = json.load(f)

# Funding Names
funding_names = funding_df['Project_Name'].unique().tolist()
funding_names.sort(key=len, reverse=True)

matched_projects = set()
debug_list = []

start_keywords = ["begin", "start", "advertise", "award"]

def check_line(line):
    line_lower = line.lower()
    # Check for date strings
    # "spring 2022"
    # "march 2022", "april 2022", "may 2022"
    # "march, 2022"
    date_found = False
    if "spring 2022" in line_lower: date_found = True
    elif "spring, 2022" in line_lower: date_found = True
    elif "march 2022" in line_lower: date_found = True
    elif "april 2022" in line_lower: date_found = True
    elif "may 2022" in line_lower: date_found = True
    elif "march, 2022" in line_lower: date_found = True
    elif "april, 2022" in line_lower: date_found = True
    elif "may, 2022" in line_lower: date_found = True
    
    if date_found:
        # Check start keywords
        for kw in start_keywords:
            if kw in line_lower:
                return True
    return False

for doc in civic_docs_data:
    text = doc['text']
    # Identify project positions
    # Use simple string search to avoid regex issues
    project_locs = []
    text_lower = text.lower()
    
    for name in funding_names:
        # Find all occurrences
        start = 0
        name_lower = name.lower()
        while True:
            idx = text_lower.find(name_lower, start)
            if idx == -1:
                break
            project_locs.append((idx, name))
            start = idx + len(name)
            
    project_locs.sort()
    
    # Check segments
    for i in range(len(project_locs)):
        start_idx, p_name = project_locs[i]
        if i < len(project_locs) - 1:
            end_idx = project_locs[i+1][0]
        else:
            end_idx = len(text)
            
        segment = text[start_idx:end_idx]
        lines = segment.split('\n')
        for line in lines:
            if check_line(line):
                matched_projects.add(p_name)
                debug_list.append([p_name, line])

# Results
filtered_funding = funding_df[funding_df['Project_Name'].isin(matched_projects)]
total_funding = filtered_funding['Amount'].astype(int).sum()
num_projects = len(matched_projects)

print("__RESULT__:")
print(json.dumps({
    "num_projects": num_projects,
    "total_funding": int(total_funding),
    "debug": debug_list
}))"""

env_args = {'var_function-call-2238045295135148005': ['civic_docs'], 'var_function-call-2238045295135146372': 'file_storage/function-call-2238045295135146372.json', 'var_function-call-2238045295135148835': ['Funding'], 'var_function-call-2238045295135147202': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-11339180666459360437': 'file_storage/function-call-11339180666459360437.json', 'var_function-call-11339180666459361146': 'file_storage/function-call-11339180666459361146.json'}

exec(code, env_args)
