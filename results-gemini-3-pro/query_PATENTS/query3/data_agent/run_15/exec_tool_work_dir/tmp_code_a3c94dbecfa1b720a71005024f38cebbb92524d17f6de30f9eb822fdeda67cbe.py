code = """import json
import re

# Load UC Patents
with open(locals()['var_function-call-14825995027994472833'], 'r') as f:
    uc_data = json.load(f)

uc_map = {} # PubNum -> Primary CPC Subclass

pub_num_pattern = re.compile(r"(?:publication number|pub\. number)\s+([A-Za-z0-9-]+)")

for row in uc_data:
    p_info = row.get('Patents_info', '')
    cpc_json = row.get('cpc', '[]')
    
    match = pub_num_pattern.search(p_info)
    if match:
        pub_num = match.group(1)
        try:
            cpcs = json.loads(cpc_json)
            primary_code = None
            first_true = [c['code'] for c in cpcs if c.get('first') is True]
            if first_true:
                primary_code = first_true[0]
            elif cpcs:
                primary_code = cpcs[0]['code']
            
            if primary_code:
                subclass = primary_code[:4]
                uc_map[pub_num] = subclass
        except:
            pass

# Load Citing Patents
with open(locals()['var_function-call-14873846412749198602'], 'r') as f:
    citing_data = json.load(f)

results = {} # Assignee -> Set of Subclasses
all_subclasses = set()

for row in citing_data:
    p_info = row.get('Patents_info', '')
    
    assignee = None
    
    if " holds the " in p_info:
        assignee = p_info.split(" holds the ")[0].strip()
    elif " is owned by " in p_info:
        # "... is owned by ASSIGNEE and ..."
        part = p_info.split(" is owned by ")[1]
        assignee = part.split(" and ")[0].strip()
        # Sometimes there's no " and ", but ends with "."? 
        # The examples show "... and has pub. number..."
        if " and " not in part and "," in part:
             assignee = part.split(",")[0].strip()
    elif " is assigned to " in p_info:
        part = p_info.split(" is assigned to ")[1]
        assignee = part.split(" and ")[0].strip()
        if " and " not in part and "," in part:
             assignee = part.split(",")[0].strip()
    
    if not assignee:
        continue
        
    # Clean up assignee (remove trailing periods if any, though strip handles spaces)
    if assignee.endswith('.'):
        assignee = assignee[:-1]
        
    if "UNIV CALIFORNIA" in assignee:
        continue
        
    citations_json = row.get('citation', '[]')
    try:
        citations = json.loads(citations_json)
    except:
        continue
        
    found_subclasses = set()
    for cit in citations:
        c_pub = cit.get('publication_number', '')
        if c_pub in uc_map:
            found_subclasses.add(uc_map[c_pub])
            
    if found_subclasses:
        if assignee not in results:
            results[assignee] = set()
        results[assignee].update(found_subclasses)
        all_subclasses.update(found_subclasses)

# Convert sets to lists for JSON
final_results = {k: list(v) for k, v in results.items()}
print("__RESULT__:")
print(json.dumps({"assignees": final_results, "subclasses": list(all_subclasses)}))"""

env_args = {'var_function-call-4259792549996489843': 'file_storage/function-call-4259792549996489843.json', 'var_function-call-15585418792872598116': [{'count(*)': '169'}], 'var_function-call-8682010113825761861': [{'count(*)': '277813'}], 'var_function-call-14825995027994472833': 'file_storage/function-call-14825995027994472833.json', 'var_function-call-14873846412749198602': 'file_storage/function-call-14873846412749198602.json', 'var_function-call-8404277136128006363': {'assignees': {'The US patent filing (application number US-4007205-A)': ['E04H'], 'The US application (ID US-201414520615-A)': ['H01L'], 'SCHOWALTER LEO J': ['H01L']}, 'subclasses': ['E04H', 'H01L']}, 'var_function-call-16868214245621169854': ['The US patent filing (application number US-4007205-A) is assigned to CALIFORNIA INST OF TECHN and has publication number US-2005165588-A1.', 'The US application (ID US-201414520615-A) is owned by CRYSTAL IS INC and has publication no. US-9447521-B2.', 'SCHOWALTER LEO J holds the US application (number US-2000608-A), with publication number US-9437430-B2.']}

exec(code, env_args)
