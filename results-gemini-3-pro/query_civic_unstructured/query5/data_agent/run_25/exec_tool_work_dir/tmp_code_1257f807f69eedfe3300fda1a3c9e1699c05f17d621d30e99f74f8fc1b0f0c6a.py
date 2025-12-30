code = """import json
import re

# Load data
with open(locals()['var_function-call-10469334728230477233'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-2938925832300121320'], 'r') as f:
    civic_docs = json.load(f)

full_text = ""
for doc in civic_docs:
    full_text += doc['text'] + "\n"

lines = full_text.split('\n')
projects = {}
current_name = None
current_text = []

# Keywords to skip or identify as non-project lines
skip_keywords = ["Page ", "Agenda Item", "Prepared by", "Approved by", "Subject:", "RECOMMENDED ACTION", "DISCUSSION", "Public Works", "Commission Meeting"]
headers = ["Capital Improvement Projects", "Disaster Recovery Projects"]

def is_project_name(line):
    # Heuristic: Uppercase first letter, not a bullet, not too long, not a known skip phrase
    line = line.strip()
    if not line: return False
    if line.startswith("(cid:") or line.startswith("•"): return False
    if any(k in line for k in skip_keywords): return False
    if any(h in line for h in headers): return False
    if len(line) > 100: return False # Titles usually short
    # Assume titles have some length
    if len(line) < 5: return False
    return True

for line in lines:
    line = line.strip()
    if is_project_name(line):
        if current_name:
            projects[current_name] = "\n".join(current_text)
        current_name = line
        current_text = []
    else:
        if current_name:
            current_text.append(line)
if current_name:
    projects[current_name] = "\n".join(current_text)

# Now iterate Funding Data and try to find matches and start dates
results = []
disaster_projects = []

for fund in funding_data:
    p_name = fund['Project_Name']
    amount = float(fund['Amount'])
    
    # Determine if disaster related
    is_disaster = False
    if "FEMA" in p_name or "CalOES" in p_name or "CalJPIA" in p_name:
        is_disaster = True
        
    # Find start date in text
    # We look for the base name in projects keys
    # Base name: remove (FEMA...) suffix if present
    base_name = re.sub(r"\s*\(.*?\)$", "", p_name).strip()
    
    # Try to find match
    match_text = ""
    # Exact match
    if p_name in projects:
        match_text = projects[p_name]
    elif base_name in projects:
        match_text = projects[base_name]
    else:
        # Fuzzy match?
        for k in projects:
            if base_name in k or k in base_name:
                match_text = projects[k]
                break
    
    start_year = None
    if match_text:
        # Extract date
        # Check "Begin Construction: ..."
        # Check "Start Date: ..."
        # Check name for year
        
        # Check explicit patterns
        dates = re.findall(r"(?:Begin [Cc]onstruction|Start [Dd]ate|Advertise)[:\s]+([A-Za-z0-9\s]+)", match_text)
        found_2022 = False
        for d in dates:
            if "2022" in d:
                found_2022 = True
                break
        
        if found_2022:
            start_year = 2022
        
        if not start_year:
             if "2022" in p_name:
                 start_year = 2022
    
    if is_disaster and start_year == 2022:
        disaster_projects.append({"name": p_name, "amount": amount})

total_funding = sum(p['amount'] for p in disaster_projects)

print("__RESULT__:")
print(json.dumps({"disaster_projects": disaster_projects, "total_funding": total_funding, "sample_projects": list(projects.keys())[:10]}))"""

env_args = {'var_function-call-10469334728230477233': 'file_storage/function-call-10469334728230477233.json', 'var_function-call-10469334728230474172': 'file_storage/function-call-10469334728230474172.json', 'var_function-call-2938925832300121320': 'file_storage/function-call-2938925832300121320.json'}

exec(code, env_args)
