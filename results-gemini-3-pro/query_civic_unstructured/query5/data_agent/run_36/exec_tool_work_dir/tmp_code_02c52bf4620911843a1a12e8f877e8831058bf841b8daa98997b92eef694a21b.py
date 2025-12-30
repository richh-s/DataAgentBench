code = """import json
import re

# Load data
with open('var_function-call-7345581642634636200.json', 'r') as f:
    funding_data = json.load(f)

with open('var_function-call-13795452578231862592.json', 'r') as f:
    civic_docs = json.load(f)

# Helper to normalize strings for matching (optional, but exact match preferred first)
def normalize(s):
    return s.lower().strip()

# Create a lookup for funding
# Project_Name -> Amount
funding_map = {item['Project_Name']: int(item['Amount']) for item in funding_data}
project_names = list(funding_map.keys())

# Pattern to find start dates
# Looking for "Begin Construction: <date>" or "Advertise: <date>" or similar
# Also "Construction started <date>"
date_pattern = re.compile(r'(Begin Construction|Advertise|Start Date|Construction started)[:\s]+([A-Za-z0-9,\s]+)', re.IGNORECASE)

disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'Disaster', 'Woolsey']

matched_projects = {}

for doc in civic_docs:
    text = doc['text']
    # Split text into lines or just search in full text?
    # Full text is better for context.
    
    # Iterate over all known project names to find them in the text
    for proj_name in project_names:
        # Check if project name is in text
        if proj_name in text:
            # Find the start index
            idx = text.find(proj_name)
            # Extract a segment of text following the project name
            # We assume the description follows the name. 
            # We'll take, say, 1000 characters or until the next project name?
            # A safer bet is a fixed window or look for keywords.
            segment = text[idx:idx+2000] # 2000 chars should cover the update
            
            # Check for Type: Disaster
            is_disaster = False
            # 1. Check name suffixes
            if any(k in proj_name for k in ['FEMA', 'CalOES', 'CalJPIA']):
                is_disaster = True
            # 2. Check keywords in the segment (less reliable, could refer to other things)
            # But the prompt says "topic" keywords include FEMA.
            # Let's rely on name suffixes primarily as per hints, and specific phrases in text.
            if "(FEMA Project)" in proj_name or "(CalOES Project)" in proj_name:
                is_disaster = True
                
            # Check for Start Date in 2022
            started_2022 = False
            
            # Search for dates in the segment
            dates = date_pattern.findall(segment)
            for action, date_str in dates:
                # We want 2022
                if "2022" in date_str:
                    # Check the action
                    action = action.lower()
                    if "begin construction" in action or "advertise" in action or "start date" in action or "construction started" in action:
                        started_2022 = True
                        break
            
            # Store if both conditions met
            if is_disaster and started_2022:
                matched_projects[proj_name] = funding_map[proj_name]
            
            # Also, if we haven't determined it's a disaster yet, but the text segment explicitly mentions it?
            # e.g. "Disaster Recovery Projects" header.
            # But "topic" field extraction is mentioned.
            # Let's stick to name suffixes first. If result is 0, we broaden.

# Sum the amounts
total_funding = sum(matched_projects.values())

print("__RESULT__:")
print(json.dumps({
    "matched_projects": list(matched_projects.keys()),
    "total_funding": total_funding
}))"""

env_args = {'var_function-call-7345581642634636200': 'file_storage/function-call-7345581642634636200.json', 'var_function-call-13795452578231862592': 'file_storage/function-call-13795452578231862592.json'}

exec(code, env_args)
