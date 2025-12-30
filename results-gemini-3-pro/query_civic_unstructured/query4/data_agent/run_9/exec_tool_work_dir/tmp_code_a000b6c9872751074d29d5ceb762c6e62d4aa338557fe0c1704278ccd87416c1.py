code = """import json
import sqlite3
import pandas as pd
import re

# Load Funding
with open(locals()['var_function-call-7108995134629171603'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)
project_names = funding_df['Project_Name'].unique().tolist()
project_names.sort(key=len, reverse=True)

# Load Civic Docs
with open(locals()['var_function-call-11351715847749976099'], 'r') as f:
    civic_docs = json.load(f)

spring_2022_patterns = [
    r'spring 2022',
    r'march 2022', r'april 2022', r'may 2022',
    r'mar 2022', r'apr 2022',
    r'03/2022', r'04/2022', r'05/2022',
    r'03-2022', r'04-2022', r'05-2022'
]

start_keywords = ['begin', 'start', 'advertise', 'initiate', 'commence']
end_keywords = ['complete', 'finish', 'end', 'conclusion']

projects_started_spring_2022 = set()

for doc in civic_docs:
    text = doc['text']
    text_lower = text.lower()
    
    # Find all project occurrences
    found_projects = []
    for pname in project_names:
        pname_lower = pname.lower()
        start = 0
        while True:
            idx = text_lower.find(pname_lower, start)
            if idx == -1:
                break
            found_projects.append((idx, pname))
            start = idx + 1
            
    found_projects.sort(key=lambda x: x[0])
    
    for i in range(len(found_projects)):
        start_idx, pname = found_projects[i]
        # End at next project or arbitrary length (e.g. 2000 chars) to capture updates
        if i < len(found_projects) - 1:
            limit = found_projects[i+1][0]
        else:
            limit = len(text)
        
        # Limit segment length to avoid reading into unrelated text if next project is far
        # But here valid text is between headers.
        segment = text[start_idx:limit]
        
        # Analyze lines
        lines = segment.split('\n')
        for line in lines:
            line_lower = line.lower()
            # Check for date match
            matched = False
            for pat in spring_2022_patterns:
                if re.search(pat, line_lower):
                    matched = True
                    break
            
            if matched:
                # Check keywords
                is_start = any(k in line_lower for k in start_keywords)
                is_end = any(k in line_lower for k in end_keywords)
                
                if is_start and not is_end:
                    projects_started_spring_2022.add(pname)
                elif is_start and is_end:
                    # Ambiguous, e.g. "Complete Design, Start Construction"
                    # If "Begin Construction" or "Start Construction" is in the line, count it.
                    if "begin construction" in line_lower or "start construction" in line_lower:
                        projects_started_spring_2022.add(pname)
                    elif "advertise" in line_lower:
                        projects_started_spring_2022.add(pname)

# Calculate total funding
matching_projects = list(projects_started_spring_2022)
funding_df_matched = funding_df[funding_df['Project_Name'].isin(matching_projects)]
total_funding = funding_df_matched['Amount'].astype(int).sum()

print("__RESULT__:")
print(json.dumps({
    "count": len(matching_projects),
    "total_funding": int(total_funding),
    "projects": matching_projects
}))"""

env_args = {'var_function-call-1427040905961591816': ['civic_docs'], 'var_function-call-1427040905961592135': ['Funding'], 'var_function-call-7108995134629171603': 'file_storage/function-call-7108995134629171603.json', 'var_function-call-7108995134629172052': 'file_storage/function-call-7108995134629172052.json', 'var_function-call-11351715847749976099': 'file_storage/function-call-11351715847749976099.json'}

exec(code, env_args)
