code = """import json
import re

# Get file paths from storage
file_path_uc = locals()['var_function-call-15364184124763818634']
file_path_citing = locals()['var_function-call-476752730094882788']

# Load UC patents
with open(file_path_uc, 'r') as f:
    uc_data = json.load(f)

uc_pubs = set()
pub_num_pattern = re.compile(r'(?:publication|pub\.?)\s+(?:number|no\.?)\s+([A-Z0-9-]+)', re.IGNORECASE)

for row in uc_data:
    info = row.get('Patents_info', '')
    m = pub_num_pattern.search(info)
    if m:
        uc_pubs.add(m.group(1))

# Load citing patents
with open(file_path_citing, 'r') as f:
    citing_data = json.load(f)

results = []
seen_subclasses = set()

assignee_patterns = [
    re.compile(r'is owned by (.*?) and'),
    re.compile(r'is assigned to (.*?) and'),
    re.compile(r'is belonging to (.*?) and'),
    re.compile(r'is held by (.*?) and'),
    re.compile(r'owned by (.*?), with'),
    re.compile(r'assigned to (.*?), with'),
    re.compile(r'belonging to (.*?), with'),
    re.compile(r'held by (.*?), with'),
    re.compile(r'^(.*?) holds the'), 
]

for row in citing_data:
    p_info = row.get('Patents_info', '')
    assignee = None
    for pat in assignee_patterns:
        m = pat.search(p_info)
        if m:
            assignee = m.group(1).strip()
            break
            
    if not assignee:
        if " holds " in p_info:
            assignee = p_info.split(" holds ")[0].strip()
            
    if not assignee or "UNIV CALIFORNIA" in assignee:
        continue
        
    citations_str = row.get('citation', '[]')
    if not citations_str or citations_str == '[]':
        continue
        
    try:
        cit_list = json.loads(citations_str)
    except:
        continue
        
    is_citing = False
    for c in cit_list:
        if c.get('publication_number') in uc_pubs:
            is_citing = True
            break
            
    if is_citing:
        cpc_str = row.get('cpc', '[]')
        try:
            cpc_list = json.loads(cpc_str)
        except:
            cpc_list = []
            
        primary_subclass = None
        for item in cpc_list:
            if item.get('first'):
                code = item.get('code', '')
                if len(code) >= 4:
                    primary_subclass = code[:4]
                break
        
        if not primary_subclass and cpc_list:
            code = cpc_list[0].get('code', '')
            if len(code) >= 4:
                primary_subclass = code[:4]
                
        if primary_subclass:
            results.append({"assignee": assignee, "subclass": primary_subclass})
            seen_subclasses.add(primary_subclass)

print("__RESULT__:")
print(json.dumps({"subclasses": list(seen_subclasses), "pairs": results}))"""

env_args = {'var_function-call-11181610767947969327': ['publicationinfo'], 'var_function-call-13957962514650417021': 'file_storage/function-call-13957962514650417021.json', 'var_function-call-11301838258047523575': 'file_storage/function-call-11301838258047523575.json', 'var_function-call-4959706225584442252': [{'count(*)': '277813'}], 'var_function-call-17295612594832481936': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine'}], 'var_function-call-15364184124763818634': 'file_storage/function-call-15364184124763818634.json', 'var_function-call-476752730094882788': 'file_storage/function-call-476752730094882788.json', 'var_function-call-7926337265438187829': {'subclasses': [], 'pairs': []}, 'var_function-call-17160895887024370542': {'uc_records_count': 0, 'uc_pubs_sample': [], 'first_uc_record': None}}

exec(code, env_args)
