code = """import json
import re

# Load UC patents info
with open(locals()['var_function-call-12269876163500430087'], 'r') as f:
    uc_records = json.load(f)

# Extract UC pub numbers
p_pub = re.compile(r"publication (?:number|no\.)\s*([A-Za-z0-9-]+)", re.IGNORECASE)
uc_pub_nums = set()
for r in uc_records:
    m = p_pub.search(r.get('Patents_info', ''))
    if m:
        uc_pub_nums.add(m.group(1).strip())

# Prepare search strings (quoted) to avoid partial matches in JSON
uc_search_tokens = [f'"{num}"' for num in uc_pub_nums]

# Load all records
with open(locals()['var_function-call-18023938407390002815'], 'r') as f:
    all_records = json.load(f)

citing_pairs = []
unique_subclasses = set()

# Regex for assignee
# "X holds the ... publication"
# "... is (owned by|assigned to|...) X and has ..."
# "Patent filing ... held by X, with ..."
p_assignee_1 = re.compile(r"^(.*?)\s+holds\s+the", re.IGNORECASE)
p_assignee_2 = re.compile(r"is\s+(?:owned\s+by|assigned\s+to|held\s+by|belonging\s+to)\s+(.*?)\s+and\s+has", re.IGNORECASE)
p_assignee_3 = re.compile(r"held\s+by\s+(.*?),\s+with", re.IGNORECASE)
p_assignee_4 = re.compile(r"assigned\s+to\s+(.*?),\s+with", re.IGNORECASE)

for rec in all_records:
    citation_str = rec.get('citation', '')
    if not citation_str or citation_str == '[]':
        continue
    
    # Fast check
    # Check if any UC token is in citation_str
    # Using a simple loop or any()
    found = False
    for token in uc_search_tokens:
        if token in citation_str:
            found = True
            break
    
    if found:
        # Extract assignee
        info = rec.get('Patents_info', '')
        assignee = None
        
        m1 = p_assignee_1.search(info)
        if m1:
            assignee = m1.group(1).strip()
        else:
            m2 = p_assignee_2.search(info)
            if m2:
                assignee = m2.group(1).strip()
            else:
                m3 = p_assignee_3.search(info)
                if m3:
                    assignee = m3.group(1).strip()
                else:
                    m4 = p_assignee_4.search(info)
                    if m4:
                        assignee = m4.group(1).strip()
        
        if assignee:
            # Exclude UC
            if "UNIV CALIFORNIA" in assignee.upper():
                continue
            
            # Extract primary CPC subclass
            cpc_str = rec.get('cpc', '')
            if cpc_str and cpc_str != '[]':
                try:
                    cpc_list = json.loads(cpc_str)
                    for c in cpc_list:
                        if c.get('first') is True:
                            code = c.get('code', '')
                            if len(code) >= 4:
                                subclass = code[:4]
                                citing_pairs.append({
                                    "assignee": assignee,
                                    "subclass": subclass
                                })
                                unique_subclasses.add(subclass)
                                # Break after finding the first primary? 
                                # The question asks for "titles of the primary CPC subclasses". 
                                # If there are multiple primaries, maybe include all?
                                # Usually there is one main classification. 
                                # But `first` might be true for multiple.
                                # Let's assume we capture all primary subclasses for this patent.
                                # Removing break to capture all primaries.
                                # However, duplicates (same assignee, same subclass) should probably be handled?
                                # The query asks: "Please provide the name of each citing assignee together with the full title of the CPC subclass."
                                # If assignee A cites UC in patent P1 (subclass S1) and patent P2 (subclass S1), do we list A-S1 twice?
                                # "Which assignees ... have cited ... and what are the titles ... associated with these citations?"
                                # It implies a list of unique (assignee, subclass) pairs or maybe all instances.
                                # Given "provide the name of each citing assignee together with the full title", I'll provide unique pairs to avoid clutter.
                except:
                    pass

# Deduplicate pairs
unique_pairs = []
seen = set()
for p in citing_pairs:
    key = (p['assignee'], p['subclass'])
    if key not in seen:
        seen.add(key)
        unique_pairs.append(p)

print("__RESULT__:")
print(json.dumps({
    "subclasses": list(unique_subclasses),
    "pairs": unique_pairs
}))"""

env_args = {'var_function-call-1367330438255836590': 'file_storage/function-call-1367330438255836590.json', 'var_function-call-12269876163500430087': 'file_storage/function-call-12269876163500430087.json', 'var_function-call-5808706916839624310': [{'COUNT(*)': '277813'}], 'var_function-call-14023183219460800893': [{'cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02E60/10",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/582",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_function-call-16779859309264347738': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine'}], 'var_function-call-18023938407390002815': 'file_storage/function-call-18023938407390002815.json', 'var_function-call-16018124554775173394': 110}

exec(code, env_args)
