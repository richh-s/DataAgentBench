code = """import json
import re

with open(locals()['var_function-call-5605292304546820245'], 'r') as f:
    docs = json.load(f)
text = docs[0]['text']
norm_text = " ".join(text.split())

with open(locals()['var_function-call-3657045741871633664'], 'r') as f:
    funding_data = json.load(f)

funding_map = {item['Project_Name']: int(item['Amount']) for item in funding_data}

total_funding = 0
found_projects = []

# Locate "Disaster Recovery Projects" section start
# We look for the phrase in norm_text, but we need to verify it's a header.
# In norm_text, headers lose structure.
# But we can look for "Disaster Recovery Projects" followed by a project name?
# Or just use position. The Title is at the beginning.
# If there is a second occurrence, it's likely the section header.
disaster_header_indices = [m.start() for m in re.finditer(r"Disaster Recovery Projects", norm_text)]
# If we have > 1, the second one is likely the section.
disaster_section_start = -1
if len(disaster_header_indices) > 1:
    disaster_section_start = disaster_header_indices[1]

# Also locate "Capital Improvement Projects" to bound it?
# Assuming Disaster comes after Capital or vice versa.
# Usually Capital, then Disaster.

for name, amount in funding_map.items():
    norm_name = " ".join(name.split())
    
    # Search in text
    # We use regex to ensure we match the full name? 
    # Or just string find. String find is fine if names are unique enough.
    idx = norm_text.find(norm_name)
    if idx != -1:
        # Context (look ahead 1000 chars)
        context = norm_text[idx:idx+1500]
        
        # Check Type
        is_disaster = False
        # Suffix check
        if "(FEMA" in name or "(CalOES" in name or "CalJPIA" in name:
            is_disaster = True
        
        # Section check
        if disaster_section_start != -1 and idx > disaster_section_start:
            # It is after the disaster header. 
            # Check if another "Capital" header appeared in between?
            # If "Capital Improvement Projects" appears after disaster_section_start and before idx, then it might be back to capital.
            # But usually sections are contiguous.
            # Let's verify if a Capital header exists between.
            pass # Skipping complex logic, suffixes are strong.
            # But what if a disaster project doesn't have suffix?
            # "Woolsey Fire" related?
            # The prompt says: "Disaster Recovery Projects, often FEMA-funded or related to Woolsey Fire recovery".
            # "Disaster project names often include suffixes...".
            # If it's in the Disaster section, it counts.
            is_disaster = True
            
        if not is_disaster:
            continue
            
        # Check Start Date
        started_2022 = False
        
        # Name check
        if "2022" in name:
            started_2022 = True
            
        # Context check
        # "Begin Construction: ... 2022"
        # "Advertise: ... 2022"
        # "Construction was completed ... 2022"
        # "Updates: ... 2022" (weak, but maybe)
        
        # Regex on normalized text (spaces instead of newlines)
        # Patterns like "Begin Construction: Fall 2022"
        if re.search(r"Begin Construction[:\s]+[A-Za-z]+\s+2022", context, re.IGNORECASE):
            started_2022 = True
        elif re.search(r"Advertise[:\s]+[A-Za-z]+\s+2022", context, re.IGNORECASE):
            started_2022 = True
        elif re.search(r"Construction was completed[:\s,]+[A-Za-z]+\s+2022", context, re.IGNORECASE):
            started_2022 = True
        elif re.search(r"Construction was completed[:\s,]+2022", context, re.IGNORECASE):
             started_2022 = True
        
        # Also check numeric dates e.g. "09/2022"? "September 2022"?
        # "On September 22, 2022 ... received bids" -> "received ... bids ... 2022"
        if re.search(r"received.*bids.*2022", context, re.IGNORECASE):
            started_2022 = True
            
        if started_2022:
            total_funding += amount
            found_projects.append({"name": name, "amount": amount})

print("__RESULT__:")
print(json.dumps({"found_projects": found_projects, "total": total_funding}))"""

env_args = {'var_function-call-5605292304546820245': 'file_storage/function-call-5605292304546820245.json', 'var_function-call-3657045741871633664': 'file_storage/function-call-3657045741871633664.json', 'var_function-call-3095873966328679813': {'projects': [], 'total': 0}, 'var_function-call-4623292609862033463': {'headers': [{'Capital Improvement Projects': 332}, {'Disaster Recovery Projects': 365}], 'found_count': 2, 'examples': ['2022 Morning View Resurfacing & Storm Drain Improvements', 'Bluffs Park Shade Structure']}}

exec(code, env_args)
