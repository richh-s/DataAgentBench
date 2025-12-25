code = """import json
import re

# Load UC patents
with open(locals()['var_function-call-13972872434933459375'], 'r') as f:
    uc_data = json.load(f)

uc_pub_nums = set()
# Regex to extract publication number
pub_num_pattern = re.compile(r'(?:publication|pub\.|pub)\s+(?:number|no\.|num)\s+([A-Z0-9-]+)', re.IGNORECASE)

for row in uc_data:
    text = row['Patents_info']
    match = pub_num_pattern.search(text)
    if match:
        uc_pub_nums.add(match.group(1))

print(f"DEBUG: Found {len(uc_pub_nums)} UC publication numbers.")

# Load potential citing patents
with open(locals()['var_function-call-11543704403283529100'], 'r') as f:
    citing_data = json.load(f)

results = []
cpc_codes_to_lookup = set()

# Regex for assignee extraction
# We want to capture the text between the keyword and the next delimiter (and, ,, with, etc)
# Keywords: "holds the", "is owned by", "is assigned to", "belonging to", "held by"
# Note: "holds the" is usually at start: "^(.*?) holds the"
# Others are in middle.

assignee_start_pattern = re.compile(r'^(.*?) holds the', re.IGNORECASE)
assignee_middle_pattern = re.compile(r'(?:is owned by|is assigned to|belonging to|held by)\s+(.*?)(?: and|,| with|\()', re.IGNORECASE)

matches_found = 0

for row in citing_data:
    try:
        citations = json.loads(row['citation'])
    except:
        continue
        
    found_citation = False
    for cit in citations:
        if cit.get('publication_number') in uc_pub_nums:
            found_citation = True
            break
    
    if found_citation:
        matches_found += 1
        info = row['Patents_info']
        assignee = None
        
        m_start = assignee_start_pattern.search(info)
        if m_start:
            assignee = m_start.group(1).strip()
        else:
            m_mid = assignee_middle_pattern.search(info)
            if m_mid:
                assignee = m_mid.group(1).strip()
        
        if not assignee:
            # Try to debug one failure
            # print(f"Failed to extract assignee from: {info}")
            continue
            
        # Clean assignee
        # Remove "In US, " etc from start if captured
        if assignee.startswith("In "):
            # Heuristic: "In US, the application ... is owned by X" -> Regex catches X. 
            # But if "In US, X holds the..." -> Regex catches "In US, X".
            # Check for comma
            parts = assignee.split(',')
            if len(parts) > 1:
                # "In US, COMPANY NAME" -> "COMPANY NAME"
                # But careful if Company Name has comma. 
                # Usually "In XX," is short.
                if len(parts[0]) < 10 and " " in parts[0]: 
                     # "In US"
                     assignee = ",".join(parts[1:]).strip()
                elif len(parts[0]) < 10:
                     assignee = ",".join(parts[1:]).strip()
        
        # Filter UC
        if "UNIV CALIFORNIA" in assignee.upper():
            continue
            
        # Extract Primary CPC
        try:
            cpc_list = json.loads(row['cpc'])
        except:
            continue
            
        if not cpc_list:
            continue
            
        first_cpc = cpc_list[0]
        code = ""
        if isinstance(first_cpc, dict):
            code = first_cpc.get('code', '')
        elif isinstance(first_cpc, str):
            code = first_cpc
            
        if not code:
            continue
            
        subclass = code.split(' ')[0]
        if len(subclass) > 4:
            subclass = subclass[:4]
            
        # Store result
        # Use a tuple to deduplicate later
        results.append((assignee, subclass))
        cpc_codes_to_lookup.add(subclass)

# Deduplicate
unique_results = []
seen = set()
for a, s in results:
    if (a,s) not in seen:
        unique_results.append({"assignee": a, "subclass": s})
        seen.add((a,s))

print("__RESULT__:")
print(json.dumps({"matches": unique_results, "cpc_subclasses": list(cpc_codes_to_lookup), "matches_count": matches_found}))"""

env_args = {'var_function-call-2968436080769144402': ['publicationinfo'], 'var_function-call-13127344599484423401': 'file_storage/function-call-13127344599484423401.json', 'var_function-call-901618133185780750': [{'COUNT(*)': '277813'}], 'var_function-call-13972872434933459375': 'file_storage/function-call-13972872434933459375.json', 'var_function-call-11543704403283529100': 'file_storage/function-call-11543704403283529100.json', 'var_function-call-190213338615668536': {'matches': [{'assignee': 'CALIFORNIA INST OF TECHN', 'subclass': 'G01M'}, {'assignee': 'BLOOM ENERGY CORP', 'subclass': 'H01M'}, {'assignee': 'CRYSTAL IS INC', 'subclass': 'H01L'}, {'assignee': 'SCHOWALTER LEO J', 'subclass': 'H01L'}], 'cpc_subclasses': ['G01M', 'H01M', 'H01L']}, 'var_function-call-2728423869347601097': [{'symbol': 'G01M', 'titleFull': 'TESTING STATIC OR DYNAMIC BALANCE OF MACHINES OR STRUCTURES; TESTING OF STRUCTURES OR APPARATUS, NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'H01L', 'titleFull': 'SEMICONDUCTOR DEVICES NOT COVERED BY CLASS H10'}, {'symbol': 'H01M', 'titleFull': 'PROCESSES OR MEANS, e.g. BATTERIES, FOR THE DIRECT CONVERSION OF CHEMICAL ENERGY INTO ELECTRICAL ENERGY'}]}

exec(code, env_args)
