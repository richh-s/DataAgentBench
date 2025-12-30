code = """import json
import pandas as pd
import re

# Load Funding Data
funding_file = locals()['var_function-call-5321786749699906543']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)
df_funding = pd.DataFrame(funding_data)

# Load Civic Docs
docs_file = locals()['var_function-call-13929900393569377328']
with open(docs_file, 'r') as f:
    civic_docs = json.load(f)

projects = {} # Name -> {starts_2022: bool, is_disaster: bool}

def check_disaster(text_context):
    keywords = ["FEMA", "CalOES", "CalJPIA", "Disaster Recovery"]
    for k in keywords:
        if k.lower() in text_context.lower():
            return True
    return False

# Patterns to look for start date
# We escape backslashes for JSON: \\s, \\d
start_patterns = [
    r"Begin Construction:?\\s*(\\w+\\s*\\d{4})",
    r"Construction Start:?\\s*(\\w+\\s*\\d{4})",
    r"Start Date:?\\s*(\\w+\\s*\\d{4})"
]

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_section = ""
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
            
        # Check for Section Headers
        if "Capital Improvement Projects" in line or "Disaster Recovery Projects" in line:
            if "Disaster" in line:
                current_section = "Disaster"
            elif "Capital" in line:
                current_section = "Capital"
                
        # Check for Project Name
        is_project = False
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            if next_line.startswith("(cid:190)") and ("Updates" in next_line or "Description" in next_line or "Status" in next_line):
                is_project = True
        
        if not is_project and i + 2 < len(lines) and not lines[i+1].strip():
            next_next_line = lines[i+2].strip()
            if next_next_line.startswith("(cid:190)") and ("Updates" in next_next_line or "Description" in next_next_line or "Status" in next_next_line):
                is_project = True
        
        if is_project:
            p_name = line.strip()
            
            is_dis = False
            if current_section == "Disaster":
                is_dis = True
            if check_disaster(p_name):
                is_dis = True
            
            started_2022 = False
            # Scan next 50 lines for dates
            block_text = ""
            for j in range(i+1, min(i+50, len(lines))):
                subline = lines[j].strip()
                # Stop if next project
                if j + 1 < len(lines) and lines[j+1].strip().startswith("(cid:190)"):
                     # This check is weak because (cid:190) is inside the project too.
                     # But a *new* project starts with a Name (no (cid:190)) followed by (cid:190).
                     # So if we see a line that looks like a name...
                     pass
                block_text += subline + " "
            
            # Check patterns in block_text
            for pat in start_patterns:
                match = re.search(pat, block_text, re.IGNORECASE)
                if match:
                    date_str = match.group(1)
                    if "2022" in date_str:
                        started_2022 = True
            
            # Also check simpler string match if regex fails
            if not started_2022:
                if "Begin Construction: Fall 2022" in block_text or \
                   "Begin Construction: Spring 2022" in block_text or \
                   "Begin Construction: Summer 2022" in block_text or \
                   "Begin Construction: Winter 2022" in block_text:
                    started_2022 = True

            if p_name not in projects:
                projects[p_name] = {'is_disaster': is_dis, 'started_2022': started_2022}
            else:
                if is_dis: projects[p_name]['is_disaster'] = True
                if started_2022: projects[p_name]['started_2022'] = True

target_projects = []
for name, info in projects.items():
    if info['is_disaster'] and info['started_2022']:
        target_projects.append(name)

# Join and Sum
total_funding = 0
matched_details = []

# Build funding dict
funding_dict = {} # normalized -> amount
# Also keep original names to handle suffixes
funding_originals = {}

for idx, row in df_funding.iterrows():
    orig = row['Project_Name']
    norm = orig.strip().lower()
    amt = int(row['Amount'])
    # Handle duplicates by summing?
    if norm in funding_dict:
        funding_dict[norm] += amt
    else:
        funding_dict[norm] = amt
        funding_originals[norm] = [orig]

for tp in target_projects:
    tp_norm = tp.strip().lower()
    
    # Try exact match
    if tp_norm in funding_dict:
        total_funding += funding_dict[tp_norm]
        matched_details.append((tp, funding_dict[tp_norm]))
        continue
    
    # Try finding funding entry that contains this project name (suffix match)
    # e.g. tp="Project A", funding="Project A (FEMA)"
    matched = False
    for fnorm in funding_dict:
        if fnorm.startswith(tp_norm):
             # Ensure it's not a false positive
             total_funding += funding_dict[fnorm]
             matched_details.append((fnorm, funding_dict[fnorm]))
             matched = True
             # We might match multiple funding entries (e.g. Project A (FEMA) and Project A (CalOES))
             # This is good.
    
    if not matched:
        # Try finding funding entry that is contained in tp (tp has suffix?)
        # e.g. tp="Project A (FEMA)", funding="Project A"
        # The prompt says "Project_Name in Funding... matches project names extracted".
        # But extracted names might be "Project A (FEMA Project)" if header included it.
        for fnorm in funding_dict:
            if tp_norm.startswith(fnorm):
                 total_funding += funding_dict[fnorm]
                 matched_details.append((fnorm, funding_dict[fnorm]))
                 matched = True
                 break # Only match one funding source if it's the base name? 
                       # Or maybe we should match specific one?
                       # If I have "Project A" in funding and "Project A (FEMA)" in docs, and "Project A" funding is general.
                       # This seems less likely for "Disaster" funding.
                       # The funding table has source "Government Grant" etc.

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": matched_details}))"""

env_args = {'var_function-call-1518905300948613366': ['Funding'], 'var_function-call-1518905300948614017': ['civic_docs'], 'var_function-call-5321786749699906543': 'file_storage/function-call-5321786749699906543.json', 'var_function-call-5321786749699905058': 'file_storage/function-call-5321786749699905058.json', 'var_function-call-130987581307727602': 'file_storage/function-call-130987581307727602.json', 'var_function-call-13929900393569377328': 'file_storage/function-call-13929900393569377328.json'}

exec(code, env_args)
