code = """import json
import re

# Load data
with open(locals()['var_function-call-1156938048168678441'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-1156938048168679978'], 'r') as f:
    civic_docs = json.load(f)

# Create a map of project name to funding info
project_funding = {}
for item in funding_data:
    project_funding[item['Project_Name']] = item

# List of all project names to search for
# Sort by length descending
all_project_names = sorted(project_funding.keys(), key=len, reverse=True)

# Function to check relevance
def is_relevant(text, name):
    keywords = ['emergency', 'FEMA']
    text_lower = text.lower()
    name_lower = name.lower()
    for kw in keywords:
        if kw.lower() in name_lower or kw.lower() in text_lower:
            return True
    return False

# Function to determine status
def determine_status(header, text):
    header_lower = header.lower()
    text_lower = text.lower()
    
    if 'completed' in text_lower and 'construction' in header_lower:
        return 'completed'
    if 'completed' in text_lower and 'completed' in header_lower:
        return 'completed'
        
    if 'not started' in header_lower:
        return 'not started'
    
    if 'design' in header_lower:
        return 'design'
    
    # Fallback/Refinement
    if 'construction' in header_lower:
        if 'completed' in text_lower:
            return 'completed'
        # If not completed, assumes active construction. 
        # The hint only gives 3 statuses. 
        # Usually "design" is the active phase before completion if "construction" isn't an option?
        # Or maybe I should output "construction" and let the user decide.
        # But instructions say "Projects have three statuses...".
        # Let's check if 'design' is a good fallback. Or maybe 'not started'? No.
        # Maybe I'll output 'design' (as in "in progress") if forced, but 'construction' is more precise.
        # I will leave it as 'construction' if I can't map it, or map to 'design'.
        # Let's try to map to 'design' if 'construction' is not in the allowed list, but wait.
        # "design" (in planning/design phase). Construction is AFTER design.
        # So it doesn't fit 'design'.
        # It fits 'not started' even less.
        # It fits 'completed' only if done.
        # Maybe there are only 3 statuses *of interest* or *possible*?
        # Or maybe the hint is just a guide.
        # I'll output "construction" if it's in construction.
        return 'construction'

    return 'unknown'

results = []
seen_projects = set()

# Headers to look for
section_headers_strings = [
    "Capital Improvement Projects (Design)",
    "Capital Improvement Projects (Construction)",
    "Capital Improvement Projects (Not Started)",
    "Disaster Recovery Projects"
]

for doc in civic_docs:
    text = doc['text']
    
    # 1. Find matches
    matches = []
    
    # Headers
    for header_str in section_headers_strings:
        # Use re.escape for safety
        pat = re.escape(header_str)
        for m in re.finditer(pat, text, re.IGNORECASE):
            matches.append({'pos': m.start(), 'type': 'header', 'text': header_str}) # Use canonical text for header
            
    # Projects
    for proj_name in all_project_names:
        pat = re.escape(proj_name)
        for m in re.finditer(pat, text, re.IGNORECASE):
            matches.append({'pos': m.start(), 'end': m.end(), 'type': 'project', 'key': proj_name, 'text': m.group()})
            
    matches.sort(key=lambda x: x['pos'])
    
    # 2. Filter overlapping projects (keep longest)
    # Using the same logic: group by start pos, pick longest.
    # But also need to handle nested matches (shorter starts later but ends earlier).
    # Since we sorted names by length desc, usually the longest match is found first for a position.
    
    # Let's do a pass to remove any project match that is contained within another project match.
    # Note: Headers are distinct.
    
    # Separate projects
    projects = [m for m in matches if m['type'] == 'project']
    headers = [m for m in matches if m['type'] == 'header']
    
    # Filter contained projects
    # A match A contains B if A.start <= B.start and A.end >= B.end
    # Since we have many matches, this is O(N^2). N is small enough (hundreds?).
    valid_projects = []
    # Sort projects by length desc to prioritize keeping larger ones
    projects.sort(key=lambda x: x['end'] - x['pos'], reverse=True)
    
    keep_indices = set(range(len(projects)))
    for i in range(len(projects)):
        if i not in keep_indices: continue
        for j in range(len(projects)):
            if i == j: continue
            if j not in keep_indices: continue
            
            # Check if i contains j
            if projects[i]['pos'] <= projects[j]['pos'] and projects[i]['end'] >= projects[j]['end']:
                # i contains j. Remove j.
                keep_indices.remove(j)
    
    cleaned_projects = [projects[i] for i in sorted(keep_indices)]
    
    # Merge back
    all_items = sorted(headers + cleaned_projects, key=lambda x: x['pos'])
    
    # 3. Iterate and extract
    current_header = None
    
    for i, item in enumerate(all_items):
        if item['type'] == 'header':
            current_header = item['text']
        elif item['type'] == 'project':
            # Extract text
            start_text = item['end']
            if i + 1 < len(all_items):
                end_text = all_items[i+1]['pos']
            else:
                end_text = len(text)
            
            proj_text = text[start_text:end_text]
            
            proj_name = item['key']
            
            if is_relevant(proj_text, proj_name):
                status = determine_status(current_header or "", proj_text)
                
                # Check mapping for construction
                # If status is construction, and user wants strict list?
                # I'll just leave it.
                
                f_info = project_funding.get(proj_name, {})
                
                record = {
                    "Project_Name": proj_name,
                    "Funding_Source": f_info.get("Funding_Source"),
                    "Amount": f_info.get("Amount"),
                    "Status": status
                }
                
                if proj_name not in seen_projects:
                    results.append(record)
                    seen_projects.add(proj_name)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-1156938048168678441': 'file_storage/function-call-1156938048168678441.json', 'var_function-call-1156938048168679978': 'file_storage/function-call-1156938048168679978.json'}

exec(code, env_args)
