code = """import json
import re

# Load civic docs
with open(locals()['var_function-call-4378397036862682776'], 'r') as f:
    civic_docs = json.load(f)

# Load funding data
with open(locals()['var_function-call-15946472843602217785'], 'r') as f:
    funding_data = json.load(f)

# Parse projects from text
projects = []
# There is only one doc in the list based on the preview, but code should handle list
full_text = "\n".join([d['text'] for d in civic_docs])

# Split by project headers. 
# Observation: Projects are followed by "(cid:190) Updates:" or "(cid:190) Project Description:"
# We can find all occurrences of these markers and look at the preceding lines.
# Refined regex: Look for a line that is not empty, then optionally some newlines, then the marker.
# We'll use a split strategy.
# Split by "\n\n(cid:190) Updates:" or "\n\n(cid:190) Project Description:"

# First, normalize the markers
text = full_text.replace("(cid:190) Updates:", "__MARKER__").replace("(cid:190) Project Description:", "__MARKER__")

segments = text.split("__MARKER__")

# The first segment is the header/intro. The last part of it is the first project name.
# Subsequent segments contain the body of the previous project and the name of the next project at the end.
# This logic is a bit flawy if the name is not at the very end.
# Let's look at the pattern: 
# [Body of Project A]
# [Project B Name]
# __MARKER__ [Body of Project B]

parsed_projects = []

for i in range(len(segments) - 1):
    # Segment i ends with Project Name for (i+1)th marker
    # Segment i+1 starts with Body for (i+1)th marker
    
    current_segment = segments[i].strip()
    next_segment = segments[i+1]
    
    # Get the project name from the end of current_segment
    lines = current_segment.split('\n')
    # Filter empty lines
    lines = [l.strip() for l in lines if l.strip()]
    
    if not lines:
        continue
        
    project_name = lines[-1]
    # Sometimes there might be a "Capital Improvement Projects (Design)" header before it.
    # We should ignore known section headers.
    ignore_headers = [
        "Capital Improvement Projects (Design)",
        "Capital Improvement Projects (Construction)",
        "Capital Improvement Projects (Not Started)",
        "Capital Improvement Projects and Disaster Recovery Projects Status",
        "Report"
    ]
    
    if project_name in ignore_headers:
        if len(lines) > 1:
            project_name = lines[-2]
    
    # Extract body from next_segment
    # The body goes until the end of next_segment, but next_segment also contains the name of the next project at the end.
    # Actually, we don't need to split perfectly. We just need to search the *start* of next_segment for dates/keywords.
    # Because the name of the *next* project is at the end, the bulk is the body of *current* project.
    
    body = next_segment
    
    parsed_projects.append({
        "name": project_name,
        "body": body
    })

# Now filter and process
target_projects = []

for p in parsed_projects:
    name = p['name']
    body = p['body']
    
    # 1. Check Disaster
    # Keywords: FEMA, CalOES, Disaster, Woolsey, Fire
    is_disaster = False
    keywords = ["FEMA", "CalOES", "Disaster", "Woolsey", "Fire"]
    
    if any(k.upper() in name.upper() for k in keywords):
        is_disaster = True
    elif any(k.upper() in body.upper() for k in keywords):
        is_disaster = True
        
    # 2. Check Start Date 2022
    # Look for "Begin Construction: ... 2022" or "Start: ... 2022"
    # Regex for date
    # We need to be careful. "Begin Construction: Fall 2023" is NOT 2022.
    # "Begin Construction: ... 2022"
    
    starts_in_2022 = False
    
    # Find "Begin Construction" line
    # (cid:131) Begin Construction: Fall 2023
    # (cid:131) Begin construction: April 2023
    
    match = re.search(r"Begin [Cc]onstruction:?\s*(.*?)\n", body)
    if match:
        date_str = match.group(1)
        if "2022" in date_str:
            starts_in_2022 = True
            
    # Also check "Start Date" just in case
    if not starts_in_2022:
        match_start = re.search(r"Start [Dd]ate:?\s*(.*?)\n", body)
        if match_start:
            if "2022" in match_start.group(1):
                starts_in_2022 = True

    # Check "Construction was completed" - this implies it started before completion.
    # If completed in 2022, did it start in 2022?
    # "Construction was completed November 2022". Maybe started in 2022.
    # But strict "started in 2022" query usually looks for start date.
    # I will stick to "Begin Construction ... 2022".
    
    if is_disaster and starts_in_2022:
        target_projects.append(name)

# Match with Funding
total_funding = 0
matched_records = []

for text_name in target_projects:
    # Find in Funding
    # We use startswith or exact match.
    # Clean text name (remove special chars if any)
    clean_text_name = text_name.replace("Project", "").strip() 
    # Wait, "Birdview Avenue Improvements Project" vs "Birdview Avenue Improvements"
    # Better to match if funding name starts with text name (or vice versa?)
    # Hint says: "Project_Name in Funding ... matches ... extracted".
    # I'll try exact match of the extracted name first.
    
    # Logic:
    # 1. Try Exact Match
    # 2. Try `Funding Name` starts with `Text Name`
    # 3. Try `Text Name` starts with `Funding Name`
    
    project_sum = 0
    found = False
    
    for row in funding_data:
        f_name = row['Project_Name']
        amount = int(row['Amount'])
        
        # Check match
        # Normalize spaces
        t_n = " ".join(text_name.split())
        f_n = " ".join(f_name.split())
        
        if f_n == t_n:
            project_sum += amount
            found = True
        elif f_n.startswith(t_n): # Funding has suffix
             project_sum += amount
             found = True
        # What if text name has "Project" at end but funding doesn't?
        # e.g. text: "Westward Beach Road Repair Project"
        # funding: "Westward Beach Road Repair" (hypothetically)
        # Let's try removing "Project" from text name for matching
        elif t_n.endswith(" Project"):
             short_t_n = t_n[:-8].strip()
             if f_n == short_t_n or f_n.startswith(short_t_n):
                 project_sum += amount
                 found = True
                 
    matched_records.append({"name": text_name, "sum": project_sum})
    total_funding += project_sum

print("__RESULT__:")
print(json.dumps({"target_projects": target_projects, "matched_details": matched_records, "total_funding": total_funding}))"""

env_args = {'var_function-call-7229016850937380290': ['civic_docs'], 'var_function-call-7229016850937378739': ['Funding'], 'var_function-call-15946472843602215220': 'file_storage/function-call-15946472843602215220.json', 'var_function-call-15946472843602217785': 'file_storage/function-call-15946472843602217785.json', 'var_function-call-4378397036862682776': 'file_storage/function-call-4378397036862682776.json'}

exec(code, env_args)
