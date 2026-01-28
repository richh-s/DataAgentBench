code = """import json
import re

# Load data
with open(locals()['var_function-call-8238280487498580574'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-8238280487498581651'], 'r') as f:
    civic_docs = json.load(f)

# Get all project names from funding table
# Sort by length descending to avoid partial matching issues (e.g. "Road Repair" vs "Road Repair Phase 2")
project_names = sorted(list(set(item['Project_Name'] for item in funding_data)), key=len, reverse=True)

# Define Spring 2022 patterns
spring_2022_patterns = [
    r'Spring 2022',
    r'March 2022',
    r'April 2022',
    r'May 2022',
    r'March, 2022',
    r'April, 2022',
    r'May, 2022'
]

def is_spring_2022(date_str):
    if not date_str:
        return False
    for pat in spring_2022_patterns:
        if re.search(pat, date_str, re.IGNORECASE):
            return True
    return False

found_projects = set()

# Normalize text function
def normalize(text):
    return text.replace('\n', ' ').replace('\r', ' ')

count = 0
for doc in civic_docs:
    text = doc['text']
    # We want to segment text by project.
    # We'll find the start indices of all project names in this doc.
    
    project_indices = []
    for pname in project_names:
        # Simple string find might match inside other words, but project names are usually distinct phrases.
        # Using regex to ensure boundaries might be safer, but names contain punctuation.
        # Let's try simple find first, but check for multiple occurrences.
        
        start = 0
        while True:
            idx = text.find(pname, start)
            if idx == -1:
                break
            project_indices.append((idx, pname))
            start = idx + len(pname)
            
    # Sort by index
    project_indices.sort(key=lambda x: x[0])
    
    # Iterate through found projects and extract their text block
    for i in range(len(project_indices)):
        start_idx, pname = project_indices[i]
        
        # End index is the start of the next project or end of text
        if i < len(project_indices) - 1:
            end_idx = project_indices[i+1][0]
        else:
            end_idx = len(text)
            
        block = text[start_idx:end_idx]
        
        # Look for start date in this block
        # Pattern: "Begin [cC]onstruction: <Date>"
        # Or "Start Date: <Date>"
        # Also handle the bullet points in the preview: "(cid:131) Begin Construction: Fall 2023"
        
        # Regex to capture the date line
        # We look for "Begin Construction" followed by some text until newline or bullet
        
        match = re.search(r'Begin [cC]onstruction:?\s*(.*?)(?:\n|\r|\(cid:)', block)
        if match:
            date_str = match.group(1).strip()
            if is_spring_2022(date_str):
                found_projects.add(pname)
        
        # Also check for "Advertise" or other indicators? 
        # "started in Spring 2022" usually means construction start.
        # But maybe "st" field extraction logic implies looking for "Start: ..." or similar.
        # Given the preview "Begin Construction: ...", I will stick to that.
        # Let's also check just "Start: ..." if "Begin Construction" is not found?
        # The prompt mentions "st: Start time/date".
        
        if not match:
             match_st = re.search(r'Start [tT]ime:?\s*(.*?)(?:\n|\r|\(cid:)', block)
             if match_st:
                 date_str = match_st.group(1).strip()
                 if is_spring_2022(date_str):
                     found_projects.add(pname)


# Calculate total funding
total_funding = 0
matched_funding_projects = []

for pname in found_projects:
    # Find amount in funding_data
    # A project name might appear multiple times in funding? Assuming unique ID per project name or we sum all matches.
    # The table description says "Project names can be joined...".
    # Funding table has Funding_ID, so maybe multiple entries per project?
    # "Each document describes multiple civic projects... For each project mentioned... Project_Name"
    # "Funding table... Project_Name (str): Name of the project receiving funding"
    # It's possible one project has multiple funding sources.
    
    # We should sum all funding records for the identified project names.
    
    records = [f for f in funding_data if f['Project_Name'] == pname]
    for r in records:
        total_funding += int(r['Amount'])
        matched_funding_projects.append(r)

result = {
    "project_count": len(found_projects),
    "projects": list(found_projects),
    "total_funding": total_funding
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-8238280487498580574': 'file_storage/function-call-8238280487498580574.json', 'var_function-call-8238280487498581651': 'file_storage/function-call-8238280487498581651.json'}

exec(code, env_args)
