code = """import json
import re

# Load UC patents info
with open(locals()['var_function-call-1567418827832031468'], 'r') as f:
    uc_data = json.load(f)

uc_pub_nums = set()
# Regex to extract publication number
# Patterns: "publication number X", "pub. number X", "publication no. X"
# The number usually ends with -A, -B2, etc.
# Example: US-11421276-B2, TW-201925402-A
pub_num_pattern = re.compile(r'(?:publication|pub\.?)\s+(?:number|no\.?)\s+([A-Z]{2}-[A-Z0-9]+-[A-Z0-9]+)', re.IGNORECASE)

for item in uc_data:
    text = item['Patents_info']
    match = pub_num_pattern.search(text)
    if match:
        uc_pub_nums.add(match.group(1))

print(f"Found {len(uc_pub_nums)} UC publication numbers.")

# Load all patents
with open(locals()['var_function-call-16145993914333671322'], 'r') as f:
    all_data = json.load(f)

results = set() # Store (assignee, subclass)

# Regex for assignee extraction
assignee_patterns = [
    re.compile(r'^(.*?) holds the', re.IGNORECASE),
    re.compile(r'is owned by (.*?) and', re.IGNORECASE),
    re.compile(r'is assigned to (.*?) and', re.IGNORECASE),
    re.compile(r'is belonging to (.*?) and', re.IGNORECASE),
    re.compile(r'held by (.*?), with', re.IGNORECASE),
    re.compile(r'held by (.*?) and', re.IGNORECASE),
    re.compile(r'belonging to (.*?), with', re.IGNORECASE),
    re.compile(r'assigned to (.*?), with', re.IGNORECASE),
    re.compile(r'is owned by (.*?), with', re.IGNORECASE)
]

def extract_assignee(text):
    for pat in assignee_patterns:
        m = pat.search(text)
        if m:
            return m.group(1).strip()
    return None

citing_count = 0

for item in all_data:
    p_info = item['Patents_info']
    
    # Check if this patent is owned by UC (exclude)
    # Using a simple string check first for speed
    if "UNIV CALIFORNIA" in p_info.upper() or "UNIVERSITY OF CALIFORNIA" in p_info.upper():
        continue
        
    assignee = extract_assignee(p_info)
    if not assignee:
        continue
    
    # Double check assignee name doesn't contain UC (in case regex captured it differently)
    if "UNIV CALIFORNIA" in assignee.upper() or "UNIVERSITY OF CALIFORNIA" in assignee.upper():
        continue

    # Check citations
    try:
        citations = json.loads(item['citation'])
    except:
        continue
        
    cited_uc = False
    for cit in citations:
        if cit.get('publication_number') in uc_pub_nums:
            cited_uc = True
            break
            
    if cited_uc:
        # Get CPC
        try:
            cpc_list = json.loads(item['cpc'])
            for cpc_item in cpc_list:
                if cpc_item.get('first', False):
                    code = cpc_item.get('code', '')
                    if len(code) >= 4:
                        subclass = code[:4]
                        results.add((assignee, subclass))
        except:
            pass

print(f"Found {len(results)} (Assignee, Subclass) pairs.")
print("__RESULT__:")
print(json.dumps(list(results)))"""

env_args = {'var_function-call-11746665475703242846': 'file_storage/function-call-11746665475703242846.json', 'var_function-call-7331267682893379415': [{'cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02E60/10",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/582",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_function-call-16695682564323016272': [{'count(*)': '277813'}], 'var_function-call-1567418827832031468': 'file_storage/function-call-1567418827832031468.json', 'var_function-call-16145993914333671322': 'file_storage/function-call-16145993914333671322.json'}

exec(code, env_args)
