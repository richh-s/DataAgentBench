code = """import json
import re

# Load UNIV CAL patents
univ_cal_file = locals()['var_function-call-7667597160845419365']
with open(univ_cal_file, 'r') as f:
    univ_cal_data = json.load(f)

# Regex for publication number
pub_num_pattern = re.compile(r"(?:publication|pub\.|pub)\s+(?:number|no\.|no)\s+([A-Z]{2}-[\w-]+(?:-[A-Z0-9]+)?)")

univ_cal_numbers = set()
for record in univ_cal_data:
    info = record.get('Patents_info', '')
    match = pub_num_pattern.search(info)
    if match:
        univ_cal_numbers.add(match.group(1))

# Load all patents
all_patents_file = locals()['var_function-call-15969671756553337737']
# This file might be large, but json.load reads it all.
with open(all_patents_file, 'r') as f:
    all_patents_data = json.load(f)

# Assignee regexes
assignee_patterns = [
    re.compile(r"^(.*?) holds the"),
    re.compile(r"is owned by (.*?) and"),
    re.compile(r"is assigned to (.*?) and"),
    re.compile(r"is belonging to (.*?) and"),
    re.compile(r"held by (.*?)(?:,| with)"),
    re.compile(r"owned by (.*?)(?:,| with)"),
    re.compile(r"belonging to (.*?)(?:,| with)")
]

results = []
cpc_codes_to_query = set()

for record in all_patents_data:
    citations_str = record.get('citation', '[]')
    try:
        citations = json.loads(citations_str)
    except:
        citations = []
    
    # Check if any citation is in univ_cal_numbers
    found = False
    for cit in citations:
        if cit.get('publication_number') in univ_cal_numbers:
            found = True
            break
    
    if found:
        # Extract assignee
        info = record.get('Patents_info', '')
        assignee = None
        for pat in assignee_patterns:
            m = pat.search(info)
            if m:
                assignee = m.group(1).strip()
                # Clean up "In US, the application..." or "The US patent filing..." prefixes if captured?
                # The patterns like "is owned by (.*?) and" capture the assignee directly.
                # But pattern 1 "^(.*?) holds the" might capture "PANASONIC IP MAN CO LTD".
                # It should be fine.
                break
        
        if assignee:
            # Check if assignee is UNIV CALIFORNIA
            if "UNIV CALIFORNIA" in assignee.upper():
                continue
            
            # Extract CPC
            cpc_str = record.get('cpc', '[]')
            try:
                cpc_list = json.loads(cpc_str)
            except:
                cpc_list = []
            
            primary_subclass = None
            if cpc_list:
                # Assuming first is primary or just taking first
                first_code = cpc_list[0].get('code', '')
                # Subclass is first 4 chars, e.g., H04W
                if len(first_code) >= 4:
                    primary_subclass = first_code[:4]
            
            if primary_subclass:
                results.append({"assignee": assignee, "cpc_subclass": primary_subclass})
                cpc_codes_to_query.add(primary_subclass)

print("__RESULT__:")
print(json.dumps({"results": results, "cpc_codes": list(cpc_codes_to_query)}))"""

env_args = {'var_function-call-4352193024332615796': 'file_storage/function-call-4352193024332615796.json', 'var_function-call-7568456659698935399': [{'count(*)': '169'}], 'var_function-call-7667597160845419365': 'file_storage/function-call-7667597160845419365.json', 'var_function-call-17545159733475639746': [{'count(*)': '277813'}], 'var_function-call-15969671756553337737': 'file_storage/function-call-15969671756553337737.json'}

exec(code, env_args)
