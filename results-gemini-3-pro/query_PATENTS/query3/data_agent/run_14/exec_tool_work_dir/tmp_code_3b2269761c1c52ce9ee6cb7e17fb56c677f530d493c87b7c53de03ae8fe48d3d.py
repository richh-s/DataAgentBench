code = """import json
import re

# Load UC patents info
# The key is from the previous query_db call
uc_patents_file = locals()['var_function-call-13027160717181148026']

with open(uc_patents_file, 'r') as f:
    uc_records = json.load(f)

# Extract publication numbers
uc_pub_nums = []
# Regex patterns based on samples:
# "publication number US-11081687-B2"
# "pub. number US-2022074631-A1"
# "publication no. US-..."
patterns = [
    r"publication number\s+([A-Z]{2}-[\w\d]+-[A-Z0-9]+)",
    r"pub\. number\s+([A-Z]{2}-[\w\d]+-[A-Z0-9]+)",
    r"publication no\.\s+([A-Z]{2}-[\w\d]+-[A-Z0-9]+)"
]

for rec in uc_records:
    info = rec.get('Patents_info', '')
    found = False
    for pat in patterns:
        m = re.search(pat, info)
        if m:
            uc_pub_nums.append(m.group(1))
            found = True
            break
    if not found:
        # Fallback or log? Maybe print one that failed?
        pass

# Deduplicate
uc_pub_nums = list(set(uc_pub_nums))

# Construct WHERE clause
# WHERE citation LIKE '%ID%' OR ...
# We need to escape patterns if necessary, but these are simple strings.
# The citation field contains JSON, e.g. "publication_number": "ID"
# So we can search for the ID.
# To be safer/more specific, we could search for '"publication_number": "ID"' but spacing might vary.
# Just searching for the ID is probably safe enough given the specific format "CC-Number-Kind".

clauses = [f"citation LIKE '%{num}%'" for num in uc_pub_nums]
where_clause = " OR ".join(clauses)

print("__RESULT__:")
print(json.dumps(where_clause))"""

env_args = {'var_function-call-13811376273087574273': ['publicationinfo'], 'var_function-call-10872988402276381523': 'file_storage/function-call-10872988402276381523.json', 'var_function-call-17042696772208400852': [{'count(*)': '169'}], 'var_function-call-6428592153986141567': [{'count(*)': '277813'}], 'var_function-call-13027160717181148026': 'file_storage/function-call-13027160717181148026.json', 'var_function-call-16488212861975409757': [{'cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02E60/10",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/582",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_function-call-3459253379493329129': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine', 'level': '9.0'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine', 'level': '9.0'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine', 'level': '9.0'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit', 'level': '9.0'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine', 'level': '9.0'}], 'var_function-call-15859640498280473242': [{'symbol': 'A01K', 'titleFull': 'ANIMAL HUSBANDRY; AVICULTURE; APICULTURE; PISCICULTURE; FISHING; REARING OR BREEDING ANIMALS, NOT OTHERWISE PROVIDED FOR; NEW BREEDS OF ANIMALS', 'level': '5.0'}]}

exec(code, env_args)
