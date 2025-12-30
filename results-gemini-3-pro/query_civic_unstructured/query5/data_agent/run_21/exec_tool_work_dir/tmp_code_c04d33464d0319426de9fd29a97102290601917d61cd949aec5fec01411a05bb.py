code = """import json
import re

with open(locals()['var_function-call-1312699190325446696'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-18394559643170776925'], 'r') as f:
    civic_docs = json.load(f)
    text = civic_docs[0]['text'] if civic_docs else ""

# Extract projects from text (reuse previous logic)
lines = text.splitlines()
projects = {}
current_p = None
current_buff = []

# Get all names from funding for matching
all_funding_names = set(r['Project_Name'] for r in funding_data)
# We need a robust extraction. Let's assume the headers are exact matches to Funding names (or close).
# We'll use the "normalized" map from before to finding known headers.

def normalize_match(name):
    # simple lower case
    return name.lower().strip()

funding_names_norm = set(normalize_match(n) for n in all_funding_names)
# Create a lookup for exact matching
# But "Broad Beach Road Water Quality Repair" might not be in funding EXACTLY if it's "Infrastructure Repairs" there.
# Wait, ID 12 IS "Broad Beach Road Water Quality Repair".
# So exact match works for the name in the text if it exists in Funding.

known_names = list(funding_names_norm)
known_names.sort(key=len, reverse=True)

for i, line in enumerate(lines):
    l = line.strip()
    if not l: continue
    l_norm = normalize_match(l)
    
    match = None
    if l_norm in known_names:
        match = l_norm
    else:
        # Check if line is contained in a known name? No, line should BE the name.
        pass
        
    if match:
        # Header check
        is_header = False
        for offset in range(1, 6):
            if i + offset < len(lines):
                nl = lines[i+offset].strip().lower()
                if "updates" in nl or "project description" in nl or "project schedule" in nl or "estimated schedule" in nl:
                    is_header = True
                    break
        if is_header:
            if current_p:
                projects[current_p] = current_buff
            current_p = match
            current_buff = []
            continue
            
    if current_p:
        current_buff.append(line)

if current_p:
    projects[current_p] = current_buff

# Now checking candidates
candidates = []
for p_norm, p_lines in projects.items():
    # Check for 2022 activity
    relevant_2022 = False
    start_type = "unknown"
    p_text = " ".join(p_lines).lower()
    
    # Check start specifically
    if "begin construction" in p_text and "2022" in p_text:
         # Need to be sure they are in the same sentence/line
         for l in p_lines:
             if "begin construction" in l.lower() and "2022" in l:
                 relevant_2022 = True
                 start_type = "explicit_start"
    
    if not relevant_2022:
        if "completed" in p_text and "2022" in p_text:
             for l in p_lines:
                 if "completed" in l.lower() and "2022" in l:
                     relevant_2022 = True
                     start_type = "completed_2022"
    
    if relevant_2022:
        # Check if disaster related
        # 1. Name match with disaster suffix in Funding
        # 2. Keywords in text
        is_disaster = False
        
        # Check keywords
        if "fema" in p_text or "caloes" in p_text or "caljpia" in p_text or "disaster" in p_text:
            is_disaster = True
        
        # Check Funding names
        # Find all funding records that "match" this project name
        # Logic: If p_norm is a substring of funding name (or vice versa) AND funding name has disaster suffix.
        # e.g. p_norm="broad beach road water quality repair"
        # Funding="Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)"
        # "water quality repair" matches "water quality infrastructure repairs"?? Fuzzy.
        
        # Let's check if any funding name containing "FEMA"/"CalOES" contains the main words of p_norm?
        p_words = set(p_norm.split())
        
        related_funding = []
        has_disaster_funding = False
        
        for rec in funding_data:
            f_name = rec['Project_Name']
            f_norm = normalize_match(f_name)
            
            # Match?
            # Start with exact match of base?
            # If f_norm starts with p_norm?
            if p_norm in f_norm or f_norm in p_norm:
                # Check for "Infrastructure" mismatch?
                # "broad beach road water quality repair" in "broad beach road water quality infrastructure repairs" -> No.
                # "broad beach road water quality repair" is NOT in "...infrastructure repairs".
                # But ID 12 "Broad Beach Road Water Quality Repair" IS exact match.
                
                # So we catch ID 12.
                # Do we catch ID 11 "Broad Beach Road Water Quality Infrastructure Repairs..."?
                # No.
                
                # We need to bridge ID 12 and ID 11.
                # They share "Broad Beach Road Water Quality".
                pass
            
            # Simple fuzzy: if share > 80% words?
            f_words = set(normalize_match(re.sub(r'\(.*?\)', '', f_name)).split())
            common = p_words.intersection(f_words)
            if len(common) / len(p_words) > 0.8:
                related_funding.append(rec)
                if 'FEMA' in f_name or 'CalOES' in f_name or 'CalJPIA' in f_name:
                    has_disaster_funding = True
        
        if is_disaster or has_disaster_funding:
            # Sum funding
            amt = sum(int(r['Amount']) for r in related_funding)
            candidates.append({
                "name": p_norm,
                "start_type": start_type,
                "amount": amt,
                "related_records": [r['Project_Name'] for r in related_funding]
            })

print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_function-call-7116383370985667147': ['Funding'], 'var_function-call-7116383370985666072': 'file_storage/function-call-7116383370985666072.json', 'var_function-call-1312699190325446696': 'file_storage/function-call-1312699190325446696.json', 'var_function-call-18394559643170776925': 'file_storage/function-call-18394559643170776925.json', 'var_function-call-12510491390566766671': {'projects': [], 'total': 0}, 'var_function-call-10071232624019186144': [{'name': 'clover heights storm drainage improvements', 'text_snippet': ['(cid:131) Final Design: Summer, 2023', '(cid:131) Advertise: Summer 2023', '(cid:131) Begin Construction: Fall 2023']}, {'name': 'latigo canyon road retaining wall repair project', 'text_snippet': ['(cid:131) Plans and specifications have been completed', '(cid:131) Advertise: Spring 2023', '(cid:131) Begin Construction: Summer 2023']}, {'name': 'storm drain master plan', 'text_snippet': ['(cid:131) Field data collection has been completed and storm drain inventory has']}, {'name': 'malibu road slope repairs', 'text_snippet': ['(cid:190) Updates: Project is currently under construction', '(cid:190) Complete Construction: April 2023']}]}

exec(code, env_args)
