code = """import json
import re

# Get file paths from local variables
funding_file_path = locals()['var_function-call-7345581642634636200']
civic_docs_file_path = locals()['var_function-call-13795452578231862592']

# Load data
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_docs_file_path, 'r') as f:
    civic_docs = json.load(f)

# Create a lookup for funding
funding_map = {item['Project_Name']: int(item['Amount']) for item in funding_data}
project_names = list(funding_map.keys())

# Regex for start date
date_pattern = re.compile(r'(Begin Construction|Advertise|Start Date|Construction started)[:\s]+([A-Za-z0-9,\s]+)', re.IGNORECASE)

matched_projects = {}

for doc in civic_docs:
    text = doc['text']
    
    for proj_name in project_names:
        if proj_name in text:
            # Find the start index
            idx = text.find(proj_name)
            # Take a segment
            segment = text[idx:idx+3000] # Increased window size
            
            # Check for Type: Disaster
            # Hints say: suffixes like (FEMA Project), (CalJPIA Project), (CalOES Project)
            is_disaster = False
            if any(suffix in proj_name for suffix in ['(FEMA Project)', '(CalOES Project)', '(CalJPIA Project)', '(CalJPIA/FEMA Project)', '(FEMA/CalOES Project)', '(FEMA)']):
                is_disaster = True
            
            # Also check if text segment implies disaster type?
            # "Disaster Recovery Projects" usually appears as a header BEFORE the project list.
            # But the suffix check is strong. Let's see if we get hits.
            
            if is_disaster:
                # Check for Start Date in 2022
                started_2022 = False
                dates = date_pattern.findall(segment)
                for action, date_str in dates:
                    if "2022" in date_str:
                        # Prioritize explicit start actions
                        action_lower = action.lower()
                        if "begin construction" in action_lower or "advertise" in action_lower or "start date" in action_lower:
                            started_2022 = True
                            break
                        # What if "Construction started"?
                        if "construction started" in action_lower:
                             started_2022 = True
                             break
                
                if started_2022:
                    matched_projects[proj_name] = funding_map[proj_name]

total_funding = sum(matched_projects.values())

print("__RESULT__:")
print(json.dumps({
    "matched_projects": list(matched_projects.keys()),
    "total_funding": total_funding
}))"""

env_args = {'var_function-call-7345581642634636200': 'file_storage/function-call-7345581642634636200.json', 'var_function-call-13795452578231862592': 'file_storage/function-call-13795452578231862592.json'}

exec(code, env_args)
