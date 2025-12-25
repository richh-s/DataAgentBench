code = """import json
import re

with open(locals()['var_function-call-14825995027994472833'], 'r') as f:
    uc_data = json.load(f)

uc_map = {}
pub_num_pattern = re.compile(r"(?:publication number|pub\. number)\s+([A-Za-z0-9-]+)")
for row in uc_data:
    p_info = row.get('Patents_info', '')
    cpc_json = row.get('cpc', '[]')
    match = pub_num_pattern.search(p_info)
    if match:
        pub_num = match.group(1)
        # Extract CPC
        try:
            cpcs = json.loads(cpc_json)
            primary_code = None
            first_true = [c['code'] for c in cpcs if c.get('first') is True]
            if first_true:
                primary_code = first_true[0]
            elif cpcs:
                primary_code = cpcs[0]['code']
            if primary_code:
                uc_map[pub_num] = primary_code[:4]
        except:
            pass

with open(locals()['var_function-call-14873846412749198602'], 'r') as f:
    citing_data = json.load(f)

matches = []
for row in citing_data:
    p_info = row.get('Patents_info', '')
    if "CALIFORNIA INST OF TECHN" in p_info or "CRYSTAL IS INC" in p_info or "SCHOWALTER LEO J" in p_info:
        citations = json.loads(row.get('citation', '[]'))
        for cit in citations:
            c_pub = cit.get('publication_number', '')
            if c_pub in uc_map:
                matches.append({
                    "citing_info": p_info,
                    "cited_pub": c_pub,
                    "cited_cpc": uc_map[c_pub]
                })

print("__RESULT__:")
print(json.dumps(matches))"""

env_args = {'var_function-call-4259792549996489843': 'file_storage/function-call-4259792549996489843.json', 'var_function-call-15585418792872598116': [{'count(*)': '169'}], 'var_function-call-8682010113825761861': [{'count(*)': '277813'}], 'var_function-call-14825995027994472833': 'file_storage/function-call-14825995027994472833.json', 'var_function-call-14873846412749198602': 'file_storage/function-call-14873846412749198602.json', 'var_function-call-8404277136128006363': {'assignees': {'The US patent filing (application number US-4007205-A)': ['E04H'], 'The US application (ID US-201414520615-A)': ['H01L'], 'SCHOWALTER LEO J': ['H01L']}, 'subclasses': ['E04H', 'H01L']}, 'var_function-call-16868214245621169854': ['The US patent filing (application number US-4007205-A) is assigned to CALIFORNIA INST OF TECHN and has publication number US-2005165588-A1.', 'The US application (ID US-201414520615-A) is owned by CRYSTAL IS INC and has publication no. US-9447521-B2.', 'SCHOWALTER LEO J holds the US application (number US-2000608-A), with publication number US-9437430-B2.'], 'var_function-call-13438093673823815979': {'assignees': {'CALIFORNIA INST OF TECHN': ['E04H'], 'CRYSTAL IS INC': ['H01L'], 'SCHOWALTER LEO J': ['H01L']}, 'subclasses': ['H01L', 'E04H']}, 'var_function-call-4696276935591129986': [{'symbol': 'E04H', 'titleFull': 'BUILDINGS OR LIKE STRUCTURES FOR PARTICULAR PURPOSES; SWIMMING OR SPLASH BATHS OR POOLS; MASTS; FENCING; TENTS OR CANOPIES, IN GENERAL'}, {'symbol': 'H01L', 'titleFull': 'SEMICONDUCTOR DEVICES NOT COVERED BY CLASS H10'}]}

exec(code, env_args)
