code = """import json
import re
import difflib

# Load civic docs
with open(locals()['var_function-call-14396097720879051946'], 'r') as f:
    civic_docs = json.load(f)

# Find latest document
date_pattern = re.compile(r"(\d{8})")
latest_date = 0
latest_doc = None

for doc in civic_docs:
    filename = doc.get('filename', '')
    match = date_pattern.search(filename)
    if match:
        date_str = match.group(1)
        # Assuming MMDDYYYY
        yyyymmdd = int(date_str[4:] + date_str[:4])
        if yyyymmdd > latest_date:
            latest_date = yyyymmdd
            latest_doc = doc

if not latest_doc:
    latest_doc = civic_docs[0]

text = latest_doc['text']
lines = text.splitlines()

# Load funding data
with open(locals()['var_function-call-14381109173196317470'], 'r') as f:
    funding_data = json.load(f)

funding_map = {item['Project_Name'].strip(): item for item in funding_data}

design_projects = set()
in_design_section = False

for line in lines:
    line = line.strip()
    if not line:
        continue
        
    if "Capital Improvement Projects (Design)" in line:
        in_design_section = True
        continue
    elif "Capital Improvement Projects" in line and "(Design)" not in line:
        in_design_section = False
    elif "Disaster Recovery Projects" in line:
        in_design_section = False
        
    if in_design_section:
        if line.startswith("(") or "Updates:" in line or "Project Schedule:" in line or "Page " in line or "Agenda Item" in line:
            continue
        if "Complete Design:" in line or "Advertise:" in line or "Begin Construction:" in line:
            continue
        
        design_projects.add(line)

count = 0
matched_list = []
unmatched_list = []

for dp in design_projects:
    found = False
    
    # 1. Exact match
    if dp in funding_map:
        if float(funding_map[dp]['Amount']) > 50000:
            count += 1
            matched_list.append(dp)
        found = True
    
    # 2. Substring match
    if not found:
        for fp in funding_map:
            if fp in dp or dp in fp:
                # Need to be careful with short strings like "Road" or "Park"
                # Check length to avoid false positives
                if len(fp) < 10 or len(dp) < 10:
                    continue
                
                if float(funding_map[fp]['Amount']) > 50000:
                    count += 1
                    matched_list.append(f"{dp} (substr: {fp})")
                found = True
                break
    
    # 3. Fuzzy match
    if not found:
        matches = difflib.get_close_matches(dp, funding_map.keys(), n=1, cutoff=0.7)
        if matches:
            fp = matches[0]
            if float(funding_map[fp]['Amount']) > 50000:
                count += 1
                matched_list.append(f"{dp} (fuzzy: {fp})")
            found = True
            
    if not found:
        unmatched_list.append(dp)

print("__RESULT__:")
print(json.dumps({"count": count, "matched": matched_list, "unmatched": unmatched_list}))"""

env_args = {'var_function-call-14381109173196317470': 'file_storage/function-call-14381109173196317470.json', 'var_function-call-14381109173196319441': 'file_storage/function-call-14381109173196319441.json', 'var_function-call-3599675758928509690': 'file_storage/function-call-3599675758928509690.json', 'var_function-call-7727963684795353611': 10, 'var_function-call-7768305805941479735': 'file_storage/function-call-7768305805941479735.json', 'var_function-call-14396097720879051946': 'file_storage/function-call-14396097720879051946.json'}

exec(code, env_args)
