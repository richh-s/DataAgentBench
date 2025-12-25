code = """import json
import re

uc_file = locals()['var_function-call-11770702646543958360']
citing_file = locals()['var_function-call-17903063529508047535']

# Load UC patents
uc_pub_nums = set()
pub_num_regex = re.compile(r"(?:publication|pub\.)\s+(?:number|no\.)\s+([\w-]+)", re.IGNORECASE)

with open(uc_file, 'r') as f:
    uc_records = json.load(f)
    for rec in uc_records:
        match = pub_num_regex.search(rec['Patents_info'])
        if match:
            uc_pub_nums.add(match.group(1))

# Process citing patents
assignee_subclasses = set()

# Regexes for assignee
# 1. NAME holds...
re_holds = re.compile(r"^(.*?)\s+holds\s+the", re.IGNORECASE)
# 2. In XX, ... owned/assigned/belonging/held by NAME ...
re_in = re.compile(r"^In\s+\w+,\s+.*?\s+(?:owned by|belonging to|assigned to|held by)\s+(.*?)\s+(?:and|with|,)", re.IGNORECASE)
# 3. The XX ... owned/assigned/belonging/held by NAME ...
re_the = re.compile(r"^The\s+.*?\s+(?:owned by|belonging to|assigned to|held by)\s+(.*?)\s+(?:and|with|,)", re.IGNORECASE)
# 4. Patent filing ... owned/assigned/belonging/held by NAME ...
re_pat = re.compile(r"^Patent\s+filing\s+.*?\s+(?:owned by|belonging to|assigned to|held by)\s+(.*?)\s+(?:and|with|,)", re.IGNORECASE)
# 5. Application ... assigned to NAME ...
re_app = re.compile(r"^Application\s+.*?\s+(?:owned by|belonging to|assigned to|held by)\s+(.*?)\s+(?:and|with|,)", re.IGNORECASE)


def extract_assignee(text):
    m = re_holds.search(text)
    if m: return m.group(1)
    m = re_in.search(text)
    if m: return m.group(1)
    m = re_the.search(text)
    if m: return m.group(1)
    m = re_pat.search(text)
    if m: return m.group(1)
    m = re_app.search(text)
    if m: return m.group(1)
    return None

with open(citing_file, 'r') as f:
    citing_records = json.load(f)
    for rec in citing_records:
        p_info = rec['Patents_info']
        assignee = extract_assignee(p_info)
        
        if not assignee:
            continue
            
        if "UNIV CALIFORNIA" in assignee.upper():
            continue
            
        # Check citations
        citations = []
        try:
            citations = json.loads(rec['citation'])
        except:
            continue
            
        has_citation = False
        for cit in citations:
            if cit.get('publication_number') in uc_pub_nums:
                has_citation = True
                break
        
        if has_citation:
            # Get primary CPC subclass
            cpc_list = []
            try:
                cpc_list = json.loads(rec['cpc'])
            except:
                pass
            
            primary_codes = []
            if cpc_list:
                # Find all with first=True
                primary_codes = [c['code'] for c in cpc_list if c.get('first') is True]
                # If none, take the first one
                if not primary_codes and len(cpc_list) > 0:
                    primary_codes = [cpc_list[0]['code']]
            
            for code in primary_codes:
                if len(code) >= 4:
                    subclass = code[:4]
                    assignee_subclasses.add((assignee, subclass))

# Convert to list for printing
result_list = list(assignee_subclasses)
print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_function-call-16690190514013585570': 'file_storage/function-call-16690190514013585570.json', 'var_function-call-11770702646543958360': 'file_storage/function-call-11770702646543958360.json', 'var_function-call-17903063529508047535': 'file_storage/function-call-17903063529508047535.json', 'var_function-call-3858104597170721102': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02E60/10",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/582",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}

exec(code, env_args)
