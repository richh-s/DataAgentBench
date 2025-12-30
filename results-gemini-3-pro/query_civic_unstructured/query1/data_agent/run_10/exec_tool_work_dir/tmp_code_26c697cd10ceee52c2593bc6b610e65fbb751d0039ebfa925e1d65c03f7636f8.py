code = """import json
import re

# Load civic docs
with open(locals()['var_function-call-3599675758928509690'], 'r') as f:
    civic_docs = json.load(f)

# Find latest document
# Filename format: malibucity_agenda__MMDDYYYY-....txt or similar
# Regex to extract date
date_pattern = re.compile(r"(\d{8})")

latest_date = 0
latest_doc = None

for doc in civic_docs:
    filename = doc.get('filename', '')
    match = date_pattern.search(filename)
    if match:
        date_str = match.group(1)
        # MMDDYYYY -> YYYYMMDD for comparison
        yyyymmdd = int(date_str[4:] + date_str[:4])
        if yyyymmdd > latest_date:
            latest_date = yyyymmdd
            latest_doc = doc

print(f"Latest Doc: {latest_doc['filename']} (Date: {latest_date})")

# Now parse the latest doc
text = latest_doc['text']
lines = text.splitlines()

# Load funding data
with open(locals()['var_function-call-14381109173196317470'], 'r') as f:
    funding_data = json.load(f)

# Create a mapping of simplified name to full project record for easier matching
# Simplified: lower case, strip non-alphanumeric? Or just strip.
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
        # Filtering headers/bullets
        if line.startswith("(") or "Updates:" in line or "Project Schedule:" in line or "Page " in line or "Agenda Item" in line:
            continue
        if "Complete Design:" in line or "Advertise:" in line or "Begin Construction:" in line:
            continue
            
        design_projects.add(line)

print(f"Design Projects extracted: {list(design_projects)}")

# Match with funding
count = 0
matched_list = []
unmatched_list = []

for dp in design_projects:
    # 1. Exact match
    if dp in funding_map:
        amt = float(funding_map[dp]['Amount'])
        if amt > 50000:
            count += 1
            matched_list.append(dp)
    else:
        # 2. Try to find a match
        # Check if dp is a substring of any funding project or vice versa
        # Or fuzzy match
        found = False
        for fp in funding_map:
            # Check for substring match (common in these tasks)
            # e.g. "Clover Heights Storm Drainage Improvements" vs "Clover Heights Storm Drain"
            if fp in dp or dp in fp:
                # Potential match
                # Verify logic: "Clover Heights Storm Drain" is in "Clover Heights Storm Drainage Improvements"
                # Check funding amount
                amt = float(funding_map[fp]['Amount'])
                if amt > 50000:
                    count += 1
                    matched_list.append(dp + " (matched via substring " + fp + ")")
                    found = True
                    break
        
        if not found:
            # Try fuzzy
            import difflib
            matches = difflib.get_close_matches(dp, funding_map.keys(), n=1, cutoff=0.6)
            if matches:
                fp = matches[0]
                amt = float(funding_map[fp]['Amount'])
                if amt > 50000:
                    count += 1
                    matched_list.append(dp + " (matched via fuzzy " + fp + ")")
                else:
                    unmatched_list.append(dp + " (found " + fp + " but < 50k)")
            else:
                unmatched_list.append(dp)

print("__RESULT__:")
result = {
    "count": count,
    "matched": matched_list,
    "unmatched": unmatched_list
}
print(json.dumps(result))"""

env_args = {'var_function-call-14381109173196317470': 'file_storage/function-call-14381109173196317470.json', 'var_function-call-14381109173196319441': 'file_storage/function-call-14381109173196319441.json', 'var_function-call-3599675758928509690': 'file_storage/function-call-3599675758928509690.json', 'var_function-call-7727963684795353611': 10, 'var_function-call-7768305805941479735': 'file_storage/function-call-7768305805941479735.json'}

exec(code, env_args)
