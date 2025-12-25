code = """import json
import re

# Load the data
with open(locals()['var_function-call-18023938407390002815'], 'r') as f:
    records = json.load(f)

uc_pub_nums = set()
patent_map = [] # List of dicts with assignee, citation, cpc

# Regex patterns
# Pattern 1: "X holds the ... publication number Y."
p1 = re.compile(r"^(.*?)\s+holds\s+the\s+.*publication\s+(?:number|no\.)\s*([A-Za-z0-9-]+)", re.IGNORECASE)
# Pattern 2: "... is (owned by|assigned to|held by|belonging to) X and has pub... number Y."
p2 = re.compile(r".*?\s+is\s+(?:owned\s+by|assigned\s+to|held\s+by|belonging\s+to)\s+(.*?)\s+and\s+has\s+pub.*?\s+number\s+([A-Za-z0-9-]+)", re.IGNORECASE)

parsed_records = []

for r in records:
    info = r.get('Patents_info', '')
    assignee = None
    pub_num = None
    
    m1 = p1.search(info)
    if m1:
        assignee = m1.group(1).strip()
        pub_num = m1.group(2).strip()
    else:
        m2 = p2.search(info)
        if m2:
            assignee = m2.group(1).strip()
            pub_num = m2.group(2).strip()
    
    # Handle cases like "In US, the application ... is owned by ..." 
    # The regex p2 should catch assignee. 
    # However, sometimes assignee might have extra text. "Patent filing ... from AU, held by UNIV CALIFORNIA, with ..."
    # "Patent filing ... from AU, held by (.*?), with ..."
    if not assignee:
        # Pattern 3: "Patent filing ... held by X, with publication number Y"
        p3 = re.compile(r".*?held\s+by\s+(.*?),\s+with\s+publication\s+number\s+([A-Za-z0-9-]+)", re.IGNORECASE)
        m3 = p3.search(info)
        if m3:
            assignee = m3.group(1).strip()
            pub_num = m3.group(2).strip()
            
    if not assignee:
        # Pattern 4: "Application ... assigned to X, with publication no. Y"
        p4 = re.compile(r".*?assigned\s+to\s+(.*?),\s+with\s+publication\s+no\.\s+([A-Za-z0-9-]+)", re.IGNORECASE)
        m4 = p4.search(info)
        if m4:
            assignee = m4.group(1).strip()
            pub_num = m4.group(2).strip()

    if assignee and pub_num:
        # Check if assignee is UC
        is_uc = "UNIV CALIFORNIA" in assignee.upper()
        
        if is_uc:
            uc_pub_nums.add(pub_num)
        
        parsed_records.append({
            'assignee': assignee,
            'pub_num': pub_num,
            'citation': r.get('citation', '[]'),
            'cpc': r.get('cpc', '[]'),
            'is_uc': is_uc
        })

# Find citing patents
citing_pairs = [] # (assignee, subclass)
unique_subclasses = set()

for rec in parsed_records:
    if rec['is_uc']:
        continue
    
    citations = []
    try:
        citations = json.loads(rec['citation'])
    except:
        continue
        
    cites_uc = False
    for cit in citations:
        if cit.get('publication_number') in uc_pub_nums:
            cites_uc = True
            break
    
    if cites_uc:
        # Get primary CPC subclass
        try:
            cpc_list = json.loads(rec['cpc'])
            primary_subclass = None
            for c in cpc_list:
                if c.get('first') is True:
                    code = c.get('code', '')
                    # Subclass is first 4 chars, e.g. H01M
                    if len(code) >= 4:
                        primary_subclass = code[:4]
                        break
            
            if primary_subclass:
                citing_pairs.append({
                    'assignee': rec['assignee'],
                    'subclass': primary_subclass
                })
                unique_subclasses.add(primary_subclass)
        except:
            pass

print("__RESULT__:")
print(json.dumps({
    "subclasses": list(unique_subclasses),
    "pairs": citing_pairs
}))"""

env_args = {'var_function-call-1367330438255836590': 'file_storage/function-call-1367330438255836590.json', 'var_function-call-12269876163500430087': 'file_storage/function-call-12269876163500430087.json', 'var_function-call-5808706916839624310': [{'COUNT(*)': '277813'}], 'var_function-call-14023183219460800893': [{'cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02E60/10",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/582",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_function-call-16779859309264347738': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine'}], 'var_function-call-18023938407390002815': 'file_storage/function-call-18023938407390002815.json'}

exec(code, env_args)
