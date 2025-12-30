code = """import json
import sqlite3
import pandas as pd
import re

# Load Funding
with open(locals()['var_function-call-7108995134629171603'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)
project_names = funding_df['Project_Name'].unique().tolist()
# Sort by length descending to match longest first (greedy match)
project_names.sort(key=len, reverse=True)

# Load Civic Docs
with open(locals()['var_function-call-11351715847749976099'], 'r') as f:
    civic_docs = json.load(f)

# Helper to normalize text for searching
def normalize(text):
    return text.lower().strip()

# Helper to check date in Spring 2022
spring_2022_patterns = [
    r'spring 2022',
    r'march 2022', r'april 2022', r'may 2022',
    r'mar 2022', r'apr 2022',
    r'03/2022', r'04/2022', r'05/2022',
    r'03-2022', r'04-2022', r'05-2022',
    r'2022-03', r'2022-04', r'2022-05'
]

start_keywords = ['begin', 'start', 'advertise', 'initiate', 'commence']
end_keywords = ['complete', 'finish', 'end', 'conclusion']

projects_started_spring_2022 = set()

for doc in civic_docs:
    text = doc['text']
    # We will look for project names in the text
    # To avoid overlapping matches, we'll search and store positions
    found_projects = []
    text_lower = text.lower()
    
    for pname in project_names:
        pname_lower = pname.lower()
        idx = text_lower.find(pname_lower)
        while idx != -1:
            found_projects.append((idx, pname))
            idx = text_lower.find(pname_lower, idx + 1)
            
    # Sort matches by position
    found_projects.sort(key=lambda x: x[0])
    
    # Process each project segment
    for i in range(len(found_projects)):
        start_idx, pname = found_projects[i]
        # End of segment is start of next project or reasonable buffer or end of text
        if i < len(found_projects) - 1:
            end_idx = found_projects[i+1][0]
        else:
            end_idx = len(text)
            
        segment = text[start_idx:end_idx]
        segment_lower = segment.lower()
        
        # Check for Spring 2022 dates in this segment
        matched_date_str = None
        for pattern in spring_2022_patterns:
            match = re.search(pattern, segment_lower)
            if match:
                matched_date_str = match.group(0)
                # Check context (line containing the date)
                # Find line with matching date
                lines = segment.split('\n')
                for line in lines:
                    if re.search(pattern, line.lower()):
                        # Check keywords in line
                        line_lower = line.lower()
                        is_start = any(k in line_lower for k in start_keywords)
                        is_end = any(k in line_lower for k in end_keywords)
                        
                        # Logic:
                        # If "Begin" or "Start" or "Advertise" is present -> Start
                        # If "Complete" is present -> Not Start (End)
                        # If both? "Begin Construction" vs "Complete Design". 
                        # "Complete Design: Spring 2022" -> Design End.
                        # "Begin Construction: Spring 2022" -> Construction Start.
                        # If just "Spring 2022" without keywords? Ambiguous.
                        
                        if is_start and not is_end:
                            projects_started_spring_2022.add(pname)
                        elif is_start and is_end:
                            # E.g. "Complete Design and Begin Construction"
                            # Check proximity?
                            pass
                        elif "design" in line_lower and "complete" in line_lower:
                            # Not a start of project execution?
                            pass
                        elif "construction" in line_lower and "begin" in line_lower:
                             projects_started_spring_2022.add(pname)
                        elif "advertise" in line_lower:
                             # Advertising is a start of the bidding phase
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
