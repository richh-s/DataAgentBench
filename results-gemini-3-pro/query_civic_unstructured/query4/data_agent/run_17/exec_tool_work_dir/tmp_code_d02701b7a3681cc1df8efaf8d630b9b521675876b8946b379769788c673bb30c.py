code = """import json
import pandas as pd
import re

# Load funding data
funding_path = locals()['var_function-call-7306303962980445652']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

# Load civic docs
docs_path = locals()['var_function-call-7306303962980444991']
with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

# Helper function to check if a date string is Spring 2022
def is_spring_2022(date_str):
    if not date_str:
        return False
    date_str = date_str.lower()
    # Check for Spring 2022
    if 'spring' in date_str and '2022' in date_str:
        return True
    # Check for months in 2022
    if '2022' in date_str:
        if 'march' in date_str or 'april' in date_str or 'may' in date_str:
            return True
        # Check numeric formats like 03/2022, 3/2022, 2022-03
        # Simple regex for numerics
        # 03, 04, 05 followed by 2022 or 22
        # or 2022 followed by 03, 04, 05
        # patterns: (03|04|05)/(\d{1,2}/)?2022
        if re.search(r'(03|04|05)/2022', date_str):
            return True
        if re.search(r'2022-(03|04|05)', date_str):
            return True
    return False

# Extract projects and start dates
# We will iterate over each project from the funding table and try to find it in the documents
# This approach handles the "matching project name" requirement.

matched_projects = set()
project_names = funding_df['Project_Name'].unique()

# Pre-process docs text to make searching easier? No, raw text is fine.
# But we need to be careful about finding the *correct* date for the project.
# The text structure suggests: Project Name -> info -> Project Name -> info
# We should parse the text into chunks per project.

# Strategy: For each document, identify start positions of all known projects.
# Sort positions. Valid chunk is from pos[i] to pos[i+1].
# In that chunk, look for start date.

matches = []

for doc in civic_docs:
    text = doc['text']
    # Find all project occurrences in this doc
    # We store (start_index, project_name)
    found_projects = []
    for pname in project_names:
        # Simple string search. case insensitive? The names seem to match casing.
        # Let's try case sensitive first as per hint, but maybe case insensitive if fails.
        # Using re.escape to handle special chars in project name
        # We need to find the headers. 
        # Warning: A project name might be mentioned in passing. 
        # But usually the header is prominent.
        # Let's assume the first occurrence or occurrences followed by newline/structure are headers.
        # For now, find all occurrences.
        for m in re.finditer(re.escape(pname), text, re.IGNORECASE):
            found_projects.append((m.start(), pname))
            
    # Sort by position
    found_projects.sort(key=lambda x: x[0])
    
    # Process chunks
    for i in range(len(found_projects)):
        start_idx, pname = found_projects[i]
        
        # Determine end index
        if i < len(found_projects) - 1:
            end_idx = found_projects[i+1][0]
        else:
            end_idx = len(text)
            
        chunk = text[start_idx:end_idx]
        
        # Look for start date in chunk
        # Keywords: "Begin Construction", "Start Date", "Construction Start", "Timeline"
        # The example shows: "(cid:131) Begin Construction: Fall 2023"
        # We can regex for "Begin Construction:? (.*)"
        
        date_match = re.search(r'(?:Begin Construction|Start Construction|Construction Start|Construction Begins)[\s:]*([^\n\r]*)', chunk, re.IGNORECASE)
        if date_match:
            date_str = date_match.group(1).strip()
            if is_spring_2022(date_str):
                # Found a match
                matches.append(pname)
                # print(f"Found match: {pname} in {doc['filename']} with date {date_str}")

# Deduplicate matches
unique_matches = set(matches)
count = len(unique_matches)

# Calculate total funding
total_funding = funding_df[funding_df['Project_Name'].isin(unique_matches)]['Amount'].astype(float).sum()

result = {
    "count": count,
    "total_funding": total_funding,
    "projects": list(unique_matches)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-13605293396723611551': 'file_storage/function-call-13605293396723611551.json', 'var_function-call-13605293396723609998': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-7306303962980445652': 'file_storage/function-call-7306303962980445652.json', 'var_function-call-7306303962980444991': 'file_storage/function-call-7306303962980444991.json'}

exec(code, env_args)
