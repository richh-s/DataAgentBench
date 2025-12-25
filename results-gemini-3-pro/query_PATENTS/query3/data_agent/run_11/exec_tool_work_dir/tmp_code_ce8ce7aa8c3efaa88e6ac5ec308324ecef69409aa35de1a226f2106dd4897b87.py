code = """import json
import re

# Load UC patents result
try:
    with open('var_function-call-15364184124763818634.json', 'r') as f:
        uc_data = json.load(f)
except FileNotFoundError:
    uc_data = [] # Should not happen

uc_pubs = set()
# Pattern for publication number in Patents_info
pub_num_pattern = re.compile(r'(?:publication|pub\.?)\s+(?:number|no\.?)\s+([A-Z0-9-]+)', re.IGNORECASE)

for row in uc_data:
    info = row.get('Patents_info', '')
    m = pub_num_pattern.search(info)
    if m:
        uc_pubs.add(m.group(1))

# Load potential citing patents
try:
    with open('var_function-call-476752730094882788.json', 'r') as f:
        citing_data = json.load(f)
except FileNotFoundError:
    citing_data = []

results = []
seen_subclasses = set()

# Regex patterns for Assignee
assignee_patterns = [
    re.compile(r'is owned by (.*?) and'),
    re.compile(r'is assigned to (.*?) and'),
    re.compile(r'is belonging to (.*?) and'),
    re.compile(r'is held by (.*?) and'),
    re.compile(r'owned by (.*?), with'),
    re.compile(r'assigned to (.*?), with'),
    re.compile(r'belonging to (.*?), with'),
    re.compile(r'held by (.*?), with'),
    re.compile(r'^(.*?) holds the'), # Must be last as it is greedy if applied to "In US, ... holds..." which is unlikely but possible
]

for row in citing_data:
    p_info = row.get('Patents_info', '')
    
    # Extract Assignee
    assignee = None
    
    # Try patterns
    for pat in assignee_patterns:
        m = pat.search(p_info)
        if m:
            candidate = m.group(1).strip()
            # Clean up if needed (e.g. remove "In US, the application ...") if the greedy match caught it
            # But the patterns like "is owned by" are specific. 
            # The "holds the" pattern is the one to be careful with.
            # E.g. "PANASONIC ... holds the ..." -> candidate="PANASONIC ..."
            assignee = candidate
            break
            
    if not assignee:
        # Fallback split
        if " holds " in p_info:
            assignee = p_info.split(" holds ")[0].strip()
            
    if not assignee:
        continue

    # Exclude UNIV CALIFORNIA
    if "UNIV CALIFORNIA" in assignee:
        continue
        
    # Check citations
    citations_str = row.get('citation', '[]')
    # citation is sometimes empty string or '[]'
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
        # Extract CPC Subclass
        cpc_str = row.get('cpc', '[]')
        try:
            cpc_list = json.loads(cpc_str)
        except:
            cpc_list = []
            
        primary_subclass = None
        
        # Priority: First entry marked "first": true
        for item in cpc_list:
            if item.get('first'):
                code = item.get('code', '')
                if len(code) >= 4:
                    primary_subclass = code[:4]
                break
        
        # Fallback: First entry in list
        if not primary_subclass and cpc_list:
            code = cpc_list[0].get('code', '')
            if len(code) >= 4:
                primary_subclass = code[:4]
                
        if primary_subclass:
            # Clean assignee name if it contains "In US, the application..." prefixes which might happen with greedy regexes?
            # The patterns "is owned by (.*?) and" capture what's in between. 
            # e.g. "In US, ... is owned by X and ..." -> X. Correct.
            # "X holds the ..." -> X. Correct.
            results.append({"assignee": assignee, "subclass": primary_subclass})
            seen_subclasses.add(primary_subclass)

print("__RESULT__:")
print(json.dumps({"subclasses": list(seen_subclasses), "pairs": results}))"""

env_args = {'var_function-call-11181610767947969327': ['publicationinfo'], 'var_function-call-13957962514650417021': 'file_storage/function-call-13957962514650417021.json', 'var_function-call-11301838258047523575': 'file_storage/function-call-11301838258047523575.json', 'var_function-call-4959706225584442252': [{'count(*)': '277813'}], 'var_function-call-17295612594832481936': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine'}], 'var_function-call-15364184124763818634': 'file_storage/function-call-15364184124763818634.json', 'var_function-call-476752730094882788': 'file_storage/function-call-476752730094882788.json'}

exec(code, env_args)
