code = """import json
import pandas as pd

funding_path = locals()['var_function-call-13193485311528156786']
civic_docs_path = locals()['var_function-call-13193485311528154511']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

extracted_projects = []

for doc in civic_docs:
    lines = doc['text'].split(chr(10))
    
    markers = []
    for i, line in enumerate(lines):
        line = line.strip()
        if ("Updates:" in line or "Project Description:" in line) and "(cid:" in line:
            markers.append(i)
            
    for k in range(len(markers)):
        marker_idx = markers[k]
        name_idx = marker_idx - 1
        while name_idx >= 0 and not lines[name_idx].strip():
            name_idx -= 1
        
        if name_idx >= 0:
            project_name = lines[name_idx].strip()
            
            if k + 1 < len(markers):
                end_idx = markers[k+1]
                # Refine end_idx: stop before the next project name
                # Next project name is at markers[k+1]-1 usually
                # Let's stop at markers[k+1] - 2 to be safe or just split by double space later
                end_idx = markers[k+1]
            else:
                end_idx = len(lines)
            
            block_lines = lines[marker_idx:end_idx]
            block_text = " ".join(block_lines)
            
            start_date = None
            # Search for Begin Construction or Construction Start
            # We look for the phrase and capture until double space or end of line equivalent
            # In block_text, lines are joined by space. Double spaces might exist if originally there.
            
            # Use regex to find date more accurately?
            # Or just string find
            keywords = ["Begin Construction:", "Construction Start:", "Begin construction:"]
            for kw in keywords:
                if kw in block_text:
                    parts = block_text.split(kw)
                    if len(parts) > 1:
                        remainder = parts[1].strip()
                        # The date is usually short, e.g. "Spring 2022" or "Fall 2023"
                        # It might be followed by "  " or just text.
                        # Let's take the first 4 words as a heuristic or split by "  "
                        if "  " in remainder:
                            candidate = remainder.split("  ")[0]
                        else:
                            # If no double space, maybe it runs into text. 
                            # Take first 20 chars? 
                            candidate = remainder[:30]
                        
                        start_date = candidate.strip()
                        break
            
            is_disaster = False
            disaster_keywords = ["FEMA", "CalOES", "CalJPIA", "Disaster", "Woolsey"]
            for dkw in disaster_keywords:
                if dkw in project_name:
                    is_disaster = True
                    break
            
            extracted_projects.append({
                "Project_Name": project_name,
                "Start_Date": start_date,
                "Is_Disaster": is_disaster
            })

# Filter
target_projects = []
for p in extracted_projects:
    if p['Is_Disaster'] and p['Start_Date']:
        # Check if 2022 in start date
        if "2022" in p['Start_Date']:
            target_projects.append(p['Project_Name'])

# Remove duplicates if any
target_projects = list(set(target_projects))

# Sum funding
total_funding = 0
matched_projects = []
for record in funding_data:
    if record['Project_Name'] in target_projects:
        amount = float(record['Amount'])
        total_funding += amount
        matched_projects.append(record['Project_Name'])

print("__RESULT__:")
print(json.dumps({
    "total_funding": total_funding,
    "matched_projects": matched_projects,
    "debug_targets": target_projects
}))"""

env_args = {'var_function-call-11217381671134747036': ['Funding'], 'var_function-call-11217381671134747201': ['civic_docs'], 'var_function-call-13193485311528156786': 'file_storage/function-call-13193485311528156786.json', 'var_function-call-13193485311528154511': 'file_storage/function-call-13193485311528154511.json', 'var_function-call-16349189720385277872': 'file_storage/function-call-16349189720385277872.json'}

exec(code, env_args)
