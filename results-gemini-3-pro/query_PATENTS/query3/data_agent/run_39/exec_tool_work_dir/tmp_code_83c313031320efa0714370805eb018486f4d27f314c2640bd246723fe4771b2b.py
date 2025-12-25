code = """import json
import re

# Load UC patents
with open(locals()['var_function-call-13972872434933459375'], 'r') as f:
    uc_data = json.load(f)

uc_pub_nums = set()
# Pattern to extract publication number from Patents_info
# Examples:
# "... with publication number US-11081687-B2."
# "... has pub. number US-2022074631-A1."
# "... publication no. US-11072681-B2."
pub_num_pattern = re.compile(r'(?:publication|pub\.|pub)\s+(?:number|no\.|num)\s+([A-Z0-9-]+)', re.IGNORECASE)

for row in uc_data:
    text = row['Patents_info']
    match = pub_num_pattern.search(text)
    if match:
        uc_pub_nums.add(match.group(1))

print(f"Found {len(uc_pub_nums)} UC publication numbers.")

# Load potential citing patents
with open(locals()['var_function-call-11543704403283529100'], 'r') as f:
    citing_data = json.load(f)

results = []
cpc_codes_to_lookup = set()

# Regex for assignee
# "PANASONIC IP MAN CO LTD holds..."
# "... is owned by UNIV CALIFORNIA and ..."
# "... is assigned to UNIV CALIFORNIA and ..."
# "... belonging to UNIV CALIFORNIA and ..."
# "... held by UNIV CALIFORNIA and ..."
assignee_patterns = [
    re.compile(r'^(.*?) holds the'),
    re.compile(r'is owned by (.*?) and'),
    re.compile(r'is assigned to (.*?) and'),
    re.compile(r'belonging to (.*?) and'),
    re.compile(r'held by (.*?) and')
]

for row in citing_data:
    # Check citations
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
        # Extract Assignee
        info = row['Patents_info']
        assignee = None
        for pat in assignee_patterns:
            m = pat.search(info)
            if m:
                assignee = m.group(1).strip()
                # Clean up "In US, the application..." prefix if present in "is owned by" type matches?
                # The regex captures the assignee name.
                # However, sometimes the sentence starts with "In US, ...".
                # But the assignee is captured in group 1.
                # Example: "In US, the application ... is owned by UNIV CALIFORNIA and" -> "UNIV CALIFORNIA"
                break
        
        if not assignee:
            # Fallback or skip?
            # Maybe the assignee is at the start but doesn't match "holds the".
            continue
            
        # Clean assignee name if it contains "In US," etc?
        # Usually "is owned by X" works.
        # Check if assignee is UNIV CALIFORNIA (should be filtered by SQL but double check)
        if "UNIV CALIFORNIA" in assignee:
            continue
            
        # Extract Primary CPC
        try:
            cpc_list = json.loads(row['cpc'])
        except:
            continue
            
        if not cpc_list:
            continue
            
        # Assume first is primary or check logic.
        # Usually CPC list is ordered or has tags.
        # Let's assume the first entry in the list is the primary classification.
        # If it's a list of strings:
        # If it's a list of objects:
        first_cpc = cpc_list[0]
        if isinstance(first_cpc, dict):
            code = first_cpc.get('code', '')
        elif isinstance(first_cpc, str):
            code = first_cpc
        else:
            continue
            
        # CPC Subclass is first 4 chars? e.g. H04W
        # Code might be "H04W 72/04"
        subclass = code.split(' ')[0]
        if len(subclass) > 4:
            subclass = subclass[:4]
            
        results.append({"assignee": assignee, "subclass": subclass})
        cpc_codes_to_lookup.add(subclass)

print("__RESULT__:")
print(json.dumps({"matches": results, "cpc_subclasses": list(cpc_codes_to_lookup)}))"""

env_args = {'var_function-call-2968436080769144402': ['publicationinfo'], 'var_function-call-13127344599484423401': 'file_storage/function-call-13127344599484423401.json', 'var_function-call-901618133185780750': [{'COUNT(*)': '277813'}], 'var_function-call-13972872434933459375': 'file_storage/function-call-13972872434933459375.json', 'var_function-call-11543704403283529100': 'file_storage/function-call-11543704403283529100.json'}

exec(code, env_args)
