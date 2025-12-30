code = """import json
import re

# Load data
with open(locals()['var_function-call-7626705312140276657'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-7626705312140279754'], 'r') as f:
    civic_docs = json.load(f)

projects = []
for row in funding_data:
    projects.append({
        "name": row['Project_Name'],
        "amount": int(row['Amount']),
        "is_disaster": False,
        "started_2022": False,
        "raw_text": ""
    })

# Regex for start date - using simple strings and checking content
# We will search for lines containing specific keywords and "2022"

total_funding = 0
found_projects_list = []

for p in projects:
    p_name = p['name']
    
    # 1. Determine Type based on Name
    # Hints say: "Disaster project names often include suffixes like '(FEMA Project)', '(CalJPIA Project)', or '(CalOES Project)'."
    if any(sub in p_name for sub in ["FEMA", "CalOES", "CalJPIA", "Disaster"]):
        p['is_disaster'] = True
    
    # If not disaster, skip checking dates to save time (or check all?)
    # The query is specific to disaster projects.
    if not p['is_disaster']:
        continue

    # 2. Scan docs for Start Date
    found_start_2022 = False
    
    for doc in civic_docs:
        text = doc['text']
        if p_name in text:
            # Simple line-based scanning around the project name
            # Split text into lines
            lines = text.split('\n')
            # Find line with project name
            for i, line in enumerate(lines):
                if p_name in line:
                    # Scan next 20 lines for dates
                    context_lines = lines[i:i+25]
                    context_str = " ".join(context_lines)
                    
                    # Check for explicit start indicators
                    # "Begin Construction: <Date>"
                    # "Advertise: <Date>" (Process start)
                    # "Project Start: <Date>"
                    
                    # Pattern matching
                    # Look for "Begin Construction" followed by "2022"
                    if re.search(r"Begin Construction.*2022", context_str, re.IGNORECASE):
                        found_start_2022 = True
                    elif re.search(r"Advertise.*2022", context_str, re.IGNORECASE):
                        found_start_2022 = True
                    elif re.search(r"Start.*2022", context_str, re.IGNORECASE):
                        found_start_2022 = True
                    # Also, some projects might be "Completed" in 2022, which means they were active. 
                    # But "started" is the keyword. 
                    # If "Construction was completed November 2022", it definitely started before or in 2022.
                    # But does it count as "Started in 2022"?
                    # If it started in 2021, the answer is NO.
                    # Usually "Completed in 2022" -> Started earlier.
                    # So I will NOT count "Completed" unless it also says "Begin Construction: 2022".
                    
                    if found_start_2022: break
        if found_start_2022: break
    
    if found_start_2022:
        p['started_2022'] = True
        total_funding += p['amount']
        found_projects_list.append(p_name)

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": found_projects_list}))"""

env_args = {'var_function-call-7626705312140276657': 'file_storage/function-call-7626705312140276657.json', 'var_function-call-7626705312140279754': 'file_storage/function-call-7626705312140279754.json'}

exec(code, env_args)
