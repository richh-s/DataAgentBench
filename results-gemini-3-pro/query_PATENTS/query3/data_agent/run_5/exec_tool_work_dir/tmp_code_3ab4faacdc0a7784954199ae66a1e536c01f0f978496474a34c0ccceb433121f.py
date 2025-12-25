code = """import pandas as pd
import json
import re

# Load Univ Cal Patents
try:
    with open('var_function-call-211574417866392703.json', 'r') as f:
        univ_cal_data = json.load(f)
except FileNotFoundError:
    # If the previous query returned a direct result instead of file, 
    # but the tool output said "stored in a file".
    # I'll rely on the variable name provided by the tool.
    # Actually, I should use the path provided in the previous message.
    # The previous message said: "The file path is stored under key: var_function-call-211574417866392703"
    # But usually, I can access it via the variable name if it was a file path string.
    # Wait, the prompt says "the storage entry will be the .json file path (a string)".
    # So locals()['var_function-call-211574417866392703'] is the path.
    pass

univ_cal_path = locals()['var_function-call-211574417866392703']
with open(univ_cal_path, 'r') as f:
    univ_cal_data = json.load(f)

univ_cal_pubs = set()
pub_num_pattern = re.compile(r'(?:publication(?: no\.| number) )([A-Z]{2}-[A-Za-z0-9-]+)')

for entry in univ_cal_data:
    info = entry.get('Patents_info', '')
    match = pub_num_pattern.search(info)
    if match:
        univ_cal_pubs.add(match.group(1))

# Load Citing Candidates
citing_path = locals()['var_function-call-9346024746778074669']
with open(citing_path, 'r') as f:
    citing_data = json.load(f)

subclasses = set()
final_list = []

for entry in citing_data:
    citations_str = entry.get('citation', '[]')
    if not citations_str:
        continue
    try:
        citations = json.loads(citations_str)
    except:
        continue
        
    # Check if any citation is in univ_cal_pubs
    found = False
    for cit in citations:
        if isinstance(cit, dict):
            p_num = cit.get('publication_number')
            if p_num in univ_cal_pubs:
                found = True
                break
            
    if found:
        # Extract Assignee
        p_info = entry.get('Patents_info', '')
        assignee = None
        
        # Regex strategy
        # 1. "X holds the..."
        m1 = re.search(r'^(.*?) holds the', p_info)
        if m1:
            assignee = m1.group(1).strip()
        else:
            # 2. "... is owned/held/belonging/assigned to X ... "
            # We want to capture X. It usually ends with "and has", "with", ",", or ".".
            # Pattern: is ... to (GROUP) (?:and has|with|,|\.)
            m2 = re.search(r'is (?:owned by|held by|belonging to|assigned to) (.*?)(?: and has| with|,|\.)', p_info)
            if m2:
                assignee = m2.group(1).strip()
            else:
                 # 3. "from COUNTRY, held/owned/assigned to X,"
                 m3 = re.search(r', (?:held by|owned by|belonging to|assigned to) (.*?)(?: and has| with|,|\.)', p_info)
                 if m3:
                     assignee = m3.group(1).strip()

        if assignee:
            # Clean up assignee if it contains "from CA" or similar?
            # Usually the regex captures just the name if the delimiters are correct.
            
            # Extract Primary CPC
            cpc_str = entry.get('cpc', '[]')
            cpc_list = []
            if cpc_str:
                try:
                    cpc_list = json.loads(cpc_str)
                except:
                    pass
                
            primary_code = None
            # Look for "first": true
            for c in cpc_list:
                if isinstance(c, dict) and c.get('first') == True:
                    primary_code = c.get('code')
                    break
            # If no "first", take the first item
            if not primary_code and len(cpc_list) > 0 and isinstance(cpc_list[0], dict):
                primary_code = cpc_list[0].get('code')
            
            if primary_code:
                # Subclass is first 4 chars
                subclass = primary_code[:4]
                subclasses.add(subclass)
                final_list.append({"assignee": assignee, "subclass": subclass})

print("__RESULT__:")
print(json.dumps({"subclasses": list(subclasses), "matches": final_list}))"""

env_args = {'var_function-call-14908749720947207705': ['publicationinfo'], 'var_function-call-10236399998378093271': 'file_storage/function-call-10236399998378093271.json', 'var_function-call-15012256495208175949': [{'COUNT(*)': '277813'}], 'var_function-call-211574417866392703': 'file_storage/function-call-211574417866392703.json', 'var_function-call-9558925481114175387': [{'symbol': 'A01K2227/108', 'level': '9.0', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'level': '9.0', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'level': '9.0', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'level': '9.0', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'level': '9.0', 'titleFull': 'Ovine'}], 'var_function-call-11281286099715272978': [{'symbol': 'A01K', 'level': '5.0', 'titleFull': 'ANIMAL HUSBANDRY; AVICULTURE; APICULTURE; PISCICULTURE; FISHING; REARING OR BREEDING ANIMALS, NOT OTHERWISE PROVIDED FOR; NEW BREEDS OF ANIMALS'}], 'var_function-call-9346024746778074669': 'file_storage/function-call-9346024746778074669.json', 'var_function-call-521529268174262345': [{'cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02E60/10",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/582",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}]}

exec(code, env_args)
