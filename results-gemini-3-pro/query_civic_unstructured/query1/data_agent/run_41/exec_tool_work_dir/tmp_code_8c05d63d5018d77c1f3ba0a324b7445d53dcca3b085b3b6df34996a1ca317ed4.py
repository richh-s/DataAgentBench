code = """import json
import re

# Load funding data
with open(locals()['var_function-call-11382907056012316849'], 'r') as f:
    funding_data = json.load(f)

# Load civic docs
with open(locals()['var_function-call-11382907056012318432'], 'r') as f:
    civic_docs = json.load(f)

capital_design_projects = set()

# Normalize funding data
funded_high = {}
for item in funding_data:
    try:
        amt = float(item['Amount'])
    except:
        amt = 0
    if amt > 50000:
        funded_high[item['Project_Name'].strip()] = amt

debug_log = []

for doc in civic_docs:
    text = doc['text']
    lines = text.splitlines()
    
    in_design_section = False
    
    # We loop through lines
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Detect section start
        if "Capital Improvement Projects (Design)" in line:
            in_design_section = True
            i += 1
            continue
        
        # Detect section end
        # Any line containing "Capital Improvement Projects (" but NOT "Design"
        # Or "Disaster Recovery Projects"
        if in_design_section:
            if "Capital Improvement Projects" in line and "(Design)" not in line:
                in_design_section = False
            elif "Disaster Recovery Projects" in line:
                in_design_section = False
            elif "Agenda Item" in line and len(line) < 30: # Page footer often has this
                pass # Just footer, don't stop section? Or maybe end of page? 
                     # Usually sections span pages.
            
            if not in_design_section:
                i += 1
                continue
            
            # Extract Project Name
            # Criteria:
            # 1. Not empty
            # 2. Not starting with bullets (cid:), Page, etc.
            # 3. Next non-empty line starts with "(cid:190) Updates:"
            
            if not line:
                i += 1
                continue
            
            if line.startswith("(cid:") or line.startswith("Page ") or line.startswith("Subject:") or line.startswith("Date "):
                i += 1
                continue
            
            # Check next line
            is_valid_project = False
            j = i + 1
            while j < len(lines):
                next_l = lines[j].strip()
                if not next_l:
                    j += 1
                    continue
                # Check for Updates or specific status lines
                if "(cid:190) Updates:" in next_l or "(cid:190) Project Description:" in next_l:
                    is_valid_project = True
                break
            
            if is_valid_project:
                capital_design_projects.add(line)
        
        i += 1

# Match logic
matches = []
# Funding DB names are keys in funded_high
db_names = list(funded_high.keys())

for proj in capital_design_projects:
    matched = False
    # Exact match
    if proj in funded_high:
        matches.append(proj)
        matched = True
    else:
        # Fuzzy match
        # 1. Remove leading year (e.g. "2022 Morning View...")
        cleaned_proj = re.sub(r'^\d{4}\s+', '', proj)
        if cleaned_proj in funded_high:
            matches.append(cleaned_proj)
            matched = True
        else:
            # 2. Check if DB name is contained in Project name (substring)
            # e.g. DB: "Morning View..." in Proj: "Morning View... & Storm Drain"
            for db_n in db_names:
                if db_n in proj: # DB name is substring of extracted name
                     matches.append(db_n)
                     matched = True
                     break
                # Or vice versa?
                # "Westward Beach Road Drainage Improvements" (Text) vs "Westward Beach Road Drainage Improvements Project" (DB)
                if proj in db_n:
                    matches.append(db_n)
                    matched = True
                    break
    
    if not matched:
        debug_log.append(f"Unmatched: {proj}")

print("__RESULT__:")
print(json.dumps({
    "extracted": list(capital_design_projects),
    "matches": list(set(matches)),
    "count": len(set(matches)),
    "unmatched": debug_log
}))"""

env_args = {'var_function-call-11382907056012316849': 'file_storage/function-call-11382907056012316849.json', 'var_function-call-11382907056012318432': 'file_storage/function-call-11382907056012318432.json', 'var_function-call-9551194131001190579': {'extracted_projects': ['and rejected all bids due to a budget shortfall', 'Marie Canyon Green Streets', 'bidding.', 'management.', 'project and will submit to the County for review.', 'or phasing out the project', '2022 Morning View Resurfacing & Storm Drain Improvements', 'construction bids.', 'advertised for construction bids shortly after this date.', 'PCH Median Improvements Project'], 'matches': ['PCH Median Improvements Project'], 'match_count': 1, 'unmatched': ['Unmatched extracted: and rejected all bids due to a budget shortfall', 'Unmatched extracted: Marie Canyon Green Streets', 'Unmatched extracted: bidding.', 'Unmatched extracted: management.', 'Unmatched extracted: project and will submit to the County for review.', 'Unmatched extracted: or phasing out the project', 'Unmatched extracted: 2022 Morning View Resurfacing & Storm Drain Improvements', 'Unmatched extracted: construction bids.', 'Unmatched extracted: advertised for construction bids shortly after this date.']}}

exec(code, env_args)
