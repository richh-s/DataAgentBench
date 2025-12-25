code = """import json
import re

# Load Univ California patents
with open(locals()['var_function-call-6208598717252469004'], 'r') as f:
    uc_data = json.load(f)

uc_pubs = set()
pub_num_pattern = re.compile(r'(?:publication|pub\.)\s*(?:number|no\.)\s*([A-Z0-9-]+)', re.IGNORECASE)

for row in uc_data:
    info = row.get('Patents_info', '')
    match = pub_num_pattern.search(info)
    if match:
        uc_pubs.add(match.group(1))

# Load Citing patents
with open(locals()['var_function-call-3788592202713596077'], 'r') as f:
    citing_data = json.load(f)

results = []
needed_subclasses = set()

# Regex for assignee extraction
assignee_pattern_1 = re.compile(r'^(.*?)\s+holds\s+the', re.IGNORECASE)
assignee_pattern_2 = re.compile(r'(?:assigned\s+to|owned\s+by|held\s+by|belonging\s+to)\s+(.*?)(?:\s+and|\s*,?\s+with)', re.IGNORECASE)

for row in citing_data:
    info = row.get('Patents_info', '')
    
    # Exclude if Univ California is the assignee (simple check first)
    # But wait, "UNIV CALIFORNIA" might appear in citations text or title? No, Patents_info is summary.
    # If it is the assignee, it will be in the patterns.
    # Let's extract assignee first.
    assignee = None
    m1 = assignee_pattern_1.search(info)
    if m1:
        assignee = m1.group(1).strip()
    else:
        m2 = assignee_pattern_2.search(info)
        if m2:
            assignee = m2.group(1).strip()
    
    if not assignee:
        continue

    # Exclude Univ Cal
    if "UNIV CALIFORNIA" in assignee.upper():
        continue
        
    # Check citations
    citations_str = row.get('citation', '[]')
    try:
        citations = json.loads(citations_str)
    except:
        citations = []
        
    cited_uc = False
    for cit in citations:
        if cit.get('publication_number') in uc_pubs:
            cited_uc = True
            break
            
    if cited_uc:
        # Get CPC
        cpc_str = row.get('cpc', '[]')
        try:
            cpcs = json.loads(cpc_str)
        except:
            cpcs = []
            
        if not cpcs:
            continue
            
        # Find primary
        primary_code = None
        for c in cpcs:
            if c.get('first') is True:
                primary_code = c.get('code')
                break
        if not primary_code and cpcs:
            primary_code = cpcs[0].get('code')
            
        if primary_code:
            subclass = primary_code[:4]
            needed_subclasses.add(subclass)
            results.append({"assignee": assignee, "subclass": subclass})

# Prepare output
output = {
    "subclasses": list(needed_subclasses),
    "matches": results
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_function-call-2384644610489396991': 'file_storage/function-call-2384644610489396991.json', 'var_function-call-6208598717252469004': 'file_storage/function-call-6208598717252469004.json', 'var_function-call-16806662649883327073': [{'count(*)': '277813'}], 'var_function-call-3788592202713596077': 'file_storage/function-call-3788592202713596077.json'}

exec(code, env_args)
