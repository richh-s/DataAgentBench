code = """import json
import re

# Load UNIV CALIFORNIA patents
with open(locals()['var_function-call-9917849686855537236'], 'r') as f:
    uc_data = json.load(f)

# Helper to extract pub number from Patents_info
# Patents_info example: "In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1."
# "UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A."
# "In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2."

def extract_pub_num_from_info(info):
    # Pattern 1: "... pub. number X."
    m = re.search(r"pub\. number ([A-Z0-9\-]+)", info)
    if m: return m.group(1)
    # Pattern 2: "... publication number X."
    m = re.search(r"publication number ([A-Z0-9\-]+)", info)
    if m: return m.group(1)
    return None

uc_lookup = {} # pub_num -> primary_cpc_subclass

for item in uc_data:
    pub_num = extract_pub_num_from_info(item['Patents_info'])
    if not pub_num:
        continue
    
    # Extract Primary CPC Subclass
    # cpc is a JSON string
    try:
        cpc_list = json.loads(item['cpc'])
        # Find primary (first=True) or just take the first one if not marked?
        # The prompt says "primary CPC subclasses".
        # Usually 'first': true indicates primary.
        primary = next((x for x in cpc_list if x.get('first')), None)
        if not primary and cpc_list:
            primary = cpc_list[0]
        
        if primary:
            code = primary.get('code', '')
            # Extract subclass (first 4 chars, e.g., H04L)
            # Code format usually: "H04L5/00" or similar.
            if len(code) >= 4:
                subclass = code[:4]
                uc_lookup[pub_num] = subclass
    except:
        continue

# Load All Citations
with open(locals()['var_function-call-13214224881594147749'], 'r') as f:
    citing_data = json.load(f)

results = [] # (citing_assignee, subclass)
needed_subclasses = set()

# Helper to extract Assignee
def extract_assignee(info):
    # Exclude if it contains UNIV CALIFORNIA
    if "UNIV CALIFORNIA" in info:
        return None
    
    # Patterns
    # "X holds the ..."
    m = re.match(r"^(.*?) holds the ", info)
    if m: return m.group(1).strip()
    
    # "... is owned by X and ..."
    m = re.search(r" is owned by (.*?) and ", info)
    if m: return m.group(1).strip()
    
    # "... is assigned to X and ..."
    m = re.search(r" is assigned to (.*?) and ", info)
    if m: return m.group(1).strip()
    
    return None

for item in citing_data:
    assignee = extract_assignee(item['Patents_info'])
    if not assignee:
        continue
        
    try:
        citations = json.loads(item['citation'])
        for cit in citations:
            cited_num = cit.get('publication_number')
            if cited_num in uc_lookup:
                subclass = uc_lookup[cited_num]
                results.append({"assignee": assignee, "subclass": subclass})
                needed_subclasses.add(subclass)
    except:
        continue

print("__RESULT__:")
print(json.dumps({"needed_subclasses": list(needed_subclasses), "matches": results}))"""

env_args = {'var_function-call-17578166237612950624': 'file_storage/function-call-17578166237612950624.json', 'var_function-call-96563173023511429': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine'}], 'var_function-call-9952371370514509504': [{'count(*)': '277813'}], 'var_function-call-9917849686855537236': 'file_storage/function-call-9917849686855537236.json', 'var_function-call-13214224881594147749': 'file_storage/function-call-13214224881594147749.json'}

exec(code, env_args)
