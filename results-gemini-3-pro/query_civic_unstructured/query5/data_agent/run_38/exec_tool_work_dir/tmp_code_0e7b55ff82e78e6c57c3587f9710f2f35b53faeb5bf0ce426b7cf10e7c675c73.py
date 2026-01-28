code = """import json
import re

# Load data
funding_path = locals()['var_function-call-8835626806368298115']
docs_path = locals()['var_function-call-9685015997201823152']

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

with open(docs_path, 'r') as f:
    docs = json.load(f)

full_text = " ".join([d['text'] for d in docs])

# Identify Disaster Projects in Funding
# Heuristic: Suffixes or "Disaster" in name?
# Prompt says: "Disaster project names often include suffixes like '(FEMA Project)', '(CalJPIA Project)', or '(CalOES Project)'"
# Also hints: "Projects have two types: 'capital' and 'disaster'".
# Let's assume all projects with these suffixes are Disaster.
# What about projects WITHOUT suffixes?
# Maybe "Birdview Avenue Improvements" (no suffix) is Capital?
# And "Birdview Avenue Improvements (CalOES Project)" is Disaster?
# If so, I only care about the rows with Disaster indication.

disaster_keywords = ["FEMA", "CalOES", "CalJPIA", "Woolsey"]
disaster_rows = []

for row in funding_records:
    name = row['Project_Name']
    # Check if name indicates disaster
    if any(k in name for k in disaster_keywords):
        disaster_rows.append(row)

# For these disaster rows, check start date in text.
# Strategy: Find the Project Name (or Base Name) in text.
# Look for "Begin Construction: <Date>" or similar.

total_funding = 0
matched_projects = []

for row in disaster_rows:
    original_name = row['Project_Name']
    # Create base name by removing suffixes
    # Remove (...) at the end
    base_name = re.sub(r'\s*\(.*?\)$', '', original_name)
    
    # Search for base_name in text
    # We need to find the specific section.
    # We can regex for: base_name + (some chars) + "Begin Construction:" + (date)
    # The text structure in preview:
    # "Project Name"
    # ...
    # "Project Schedule:"
    # ...
    # "Begin Construction: Fall 2023"
    
    # Let's try to capture the date.
    # Pattern: base_name followed by "Begin Construction:" within say 1000 chars.
    pattern = re.escape(base_name) + r'.{0,1000}?Begin Construction:\s*(.*?)\n'
    match = re.search(pattern, full_text, re.DOTALL | re.IGNORECASE)
    
    start_date = None
    if match:
        date_str = match.group(1).strip()
        start_date = date_str
    
    # Check if started in 2022
    # The date string might be "Fall 2023", "November 2022", etc.
    if start_date and "2022" in start_date:
        total_funding += int(row['Amount'])
        matched_projects.append({
            "name": original_name,
            "base_name": base_name,
            "start_date": start_date,
            "amount": row['Amount']
        })

print(f"Disaster Rows: {len(disaster_rows)}")
print(f"Matched 2022 Projects: {len(matched_projects)}")
print(f"Total Funding: {total_funding}")

print("__RESULT__:")
print(json.dumps(matched_projects))"""

env_args = {'var_function-call-6821876032245033894': ['Funding'], 'var_function-call-8835626806368298115': 'file_storage/function-call-8835626806368298115.json', 'var_function-call-9685015997201823152': 'file_storage/function-call-9685015997201823152.json'}

exec(code, env_args)
