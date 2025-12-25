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
    
    # Extract PubNum
    match = pub_num_pattern.search(p_info)
    if match:
        pub_num = match.group(1)
        
        # Extract CPC
        try:
            cpcs = json.loads(cpc_json)
            primary_code = None
            # Strategy: Find first where 'first' is true, else take the very first one
            first_true = [c['code'] for c in cpcs if c.get('first') is True]
            if first_true:
                primary_code = first_true[0]
            elif cpcs:
                primary_code = cpcs[0]['code']
            
            if primary_code:
                # Subclass is first 4 chars (e.g. H04W)
                subclass = primary_code[:4]
                uc_map[pub_num] = subclass
        except:
            pass

# Load Citing Patents
with open(locals()['var_function-call-14873846412749198602'], 'r') as f:
    citing_data = json.load(f)

results = {} # Assignee -> Set of Subclasses

assignee_splitters = [" holds the", " is owned by ", " is assigned to "]

for row in citing_data:
    p_info = row.get('Patents_info', '')
    
    # Extract Assignee
    assignee = None
    for splitter in assignee_splitters:
        if splitter in p_info:
            if p_info.startswith("In US, the"):
                 # "In US, the application ... is owned by ASSIGNEE and..."
                 parts = p_info.split(splitter)
                 if len(parts) > 1:
                     assignee = parts[1].split(" and")[0].strip()
            else:
                 assignee = p_info.split(splitter)[0].strip()
            break
    
    if not assignee:
        continue
        
    if "UNIV CALIFORNIA" in assignee:
        continue
        
    # Check citations
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
            results[assignee] = list()
        results[assignee].extend(list(found_subclasses))

# Deduplicate subclasses in results
final_results = {}
all_subclasses = set()
for assignee, subs in results.items():
    unique_subs = sorted(list(set(subs)))
    final_results[assignee] = unique_subs
    for s in unique_subs:
        all_subclasses.add(s)

print("__RESULT__:")
print(json.dumps({"assignees": final_results, "subclasses": list(all_subclasses)}))"""

env_args = {'var_function-call-4259792549996489843': 'file_storage/function-call-4259792549996489843.json', 'var_function-call-15585418792872598116': [{'count(*)': '169'}], 'var_function-call-8682010113825761861': [{'count(*)': '277813'}], 'var_function-call-14825995027994472833': 'file_storage/function-call-14825995027994472833.json', 'var_function-call-14873846412749198602': 'file_storage/function-call-14873846412749198602.json'}

exec(code, env_args)
