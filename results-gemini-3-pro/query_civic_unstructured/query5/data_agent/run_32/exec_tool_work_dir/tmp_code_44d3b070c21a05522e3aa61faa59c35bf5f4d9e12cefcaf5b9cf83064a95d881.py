code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-10835669272488718990'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-10835669272488721645'], 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
funding_names = set(df_funding['Project_Name'].unique())

extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    # Split by the "Updates:" line marker
    # The marker seems to be (cid:190) Updates:
    # We'll regex split
    segments = re.split(r'\(cid:190\)\s*Updates:', text)
    
    # segments[0] is preamble + Name of Project 1
    # segments[1] is body of Project 1 + ... + Name of Project 2
    
    for i in range(1, len(segments)):
        # Extract Name from the end of the previous segment
        prev_segment = segments[i-1].strip()
        prev_lines = [line.strip() for line in prev_segment.split('\n') if line.strip()]
        
        if not prev_lines:
            continue
            
        # Candidate name is the last line
        candidate_name = prev_lines[-1]
        
        # If candidate name is a section header, take the one before
        headers = ["Capital Improvement Projects (Design)", "Capital Improvement Projects (Construction)", 
                   "Capital Improvement Projects (Not Started)", "Disaster Recovery Projects"]
        
        if candidate_name in headers and len(prev_lines) > 1:
            candidate_name = prev_lines[-2]
            
        # Current segment body (up to next project name)
        # We need to act carefully because the next project name is at the end of THIS segment.
        # But we don't know where it starts exactly.
        # However, for finding the Start Date and Type within THIS project, we just search the beginning of the segment.
        # The project details usually come before the next project's title.
        # We can assume the first 10-20 lines contain the relevant info or search until we see a double newline followed by something that looks like a title?
        # Simpler: just search the whole segment. If "Begin Construction" appears multiple times, well, usually it appears once per "Updates" block.
        # But wait, if segments[i] contains Project 1 body AND Project 2 Name, Project 2 Name is at the very end.
        # "Begin Construction" for Project 2 would be in segments[i+1].
        # So we represent Project 1 using `candidate_name` and `segments[i]`.
        
        body = segments[i]
        
        # Extract Start Date (st)
        st = None
        # Pattern: Begin Construction: <Month Year> or <Season Year>
        st_match = re.search(r'Begin [Cc]onstruction:\s*([A-Za-z0-9\s]+)', body)
        if st_match:
            # Take only the first line of the match
            st = st_match.group(1).split('\n')[0].strip()
            
        # Check type/topic
        is_disaster = False
        # Check explicit keywords in name
        name_lower = candidate_name.lower()
        if "fema" in name_lower or "caloes" in name_lower or "disaster" in name_lower:
            is_disaster = True
        
        # Check keywords in body
        # Limit body search to avoid catching next project's context if it's long?
        # But usually updates are short.
        body_lower = body.lower()
        if "fema" in body_lower or "caloes" in body_lower or "disaster" in body_lower or "woolsey" in body_lower:
            is_disaster = True
            
        extracted_projects.append({
            "name": candidate_name,
            "st": st,
            "is_disaster": is_disaster,
            "raw_name": candidate_name
        })

# Filter for started in 2022 and disaster
target_projects = []
for p in extracted_projects:
    if p['st'] and '2022' in p['st'] and p['is_disaster']:
        target_projects.append(p)

# Match with funding
# We need to match `p['name']` with `df_funding['Project_Name']`
# Exact match might fail due to whitespace or cleaning.
# Let's try to find matches.

matched_funding = []
total_amount = 0

for p in target_projects:
    p_name = p['name']
    # Try exact match
    match = df_funding[df_funding['Project_Name'] == p_name]
    if match.empty:
        # Try stripping or partial?
        # Maybe the name in text is "Project Name" and in DB is "Project Name (FEMA Project)"
        # Let's try to match if p_name is a substring of DB name or vice versa?
        # Or look for p_name in DB names
        # "Birdview Avenue Improvements" in text vs "Birdview Avenue Improvements (CalOES Project)" in DB.
        
        # Strategy: find db names that start with p_name
        potential_matches = df_funding[df_funding['Project_Name'].str.contains(re.escape(p_name), case=False, na=False)]
        if not potential_matches.empty:
            match = potential_matches
        else:
            # Try matching if DB name is substring of p_name?
            pass
            
    if not match.empty:
        # If multiple matches, which one?
        # The query asks for total funding for the project. 
        # If there are multiple funding sources/records for the same project, we sum them?
        # "What is the total funding for disaster-related projects..."
        # Yes, sum all related funding records.
        for _, row in match.iterrows():
            matched_funding.append({
                "Project_Name": row['Project_Name'],
                "Amount": row['Amount'],
                "Source_Text_Project": p_name,
                "Start": p['st']
            })
            total_amount += row['Amount']

print("__RESULT__:")
print(json.dumps({"projects": matched_funding, "total_amount": total_amount, "debug_target_projects": target_projects}, indent=2))"""

env_args = {'var_function-call-10835669272488718990': 'file_storage/function-call-10835669272488718990.json', 'var_function-call-10835669272488721645': 'file_storage/function-call-10835669272488721645.json'}

exec(code, env_args)
