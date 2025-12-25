code = """import json
import re

# Load UC patents info
with open('var_function-call-11388642895548922759.json', 'r') as f:
    uc_data = json.load(f)

# Extract UC publication numbers
uc_pubs = set()
pub_num_regex = re.compile(r"(?:publication|pub\.) (?:number|no\.) ([A-Za-z0-9\-]+)")

for row in uc_data:
    info = row['Patents_info']
    match = pub_num_regex.search(info)
    if match:
        uc_pubs.add(match.group(1))

# Load all patents info
with open('var_function-call-14632246172343747106.json', 'r') as f:
    all_data = json.load(f)

results = []
needed_subclasses = set()

# Regex for assignee
assignee_regex_1 = re.compile(r"(?:owned by|assigned to|held by|belonging to) ([^,]+?)(?: and|,| has| with)")
assignee_regex_2 = re.compile(r"^(.+?) holds the")

for row in all_data:
    citations_str = row.get('citation')
    if not citations_str or citations_str == '[]':
        continue
    
    try:
        citations = json.loads(citations_str)
    except:
        continue

    # Check for citation match
    match_found = False
    for cit in citations:
        if cit.get('publication_number') in uc_pubs:
            match_found = True
            break
    
    if match_found:
        # Extract Assignee
        info = row['Patents_info']
        assignee = None
        m1 = assignee_regex_1.search(info)
        if m1:
            assignee = m1.group(1).strip()
        else:
            m2 = assignee_regex_2.search(info)
            if m2:
                assignee = m2.group(1).strip()
        
        if not assignee:
            continue
            
        # Check if assignee is UC
        if "UNIV CALIFORNIA" in assignee:
            continue
            
        # Get Primary CPC Subclass
        cpc_str = row.get('cpc')
        if not cpc_str or cpc_str == '[]':
            continue
            
        try:
            cpc_list = json.loads(cpc_str)
        except:
            continue
            
        primary_code = None
        # Look for first=True
        for item in cpc_list:
            if item.get('first') is True:
                primary_code = item.get('code')
                break
        
        # If no first=True, take the first one
        if not primary_code and len(cpc_list) > 0:
            primary_code = cpc_list[0].get('code')
            
        if primary_code:
            # Subclass is first 4 chars
            subclass = primary_code[:4]
            results.append({"assignee": assignee, "subclass": subclass})
            needed_subclasses.add(subclass)

print("__RESULT__:")
print(json.dumps({"results": results, "needed_subclasses": list(needed_subclasses)}))"""

env_args = {'var_function-call-11562545934826234823': 'file_storage/function-call-11562545934826234823.json', 'var_function-call-18029382303638022619': [{'cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02E60/10",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/582",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_function-call-11135625336177495705': [{'symbol': 'C01B', 'titleFull': 'NON-METALLIC ELEMENTS; COMPOUNDS THEREOF; METALLOIDS OR COMPOUNDS THEREOF NOT COVERED BY SUBCLASS C01C', 'level': '5.0'}], 'var_function-call-15142459534990072702': [{'count(*)': '277813'}], 'var_function-call-10106849343556396757': [{'count(*)': '169'}], 'var_function-call-11388642895548922759': 'file_storage/function-call-11388642895548922759.json', 'var_function-call-14632246172343747106': 'file_storage/function-call-14632246172343747106.json'}

exec(code, env_args)
