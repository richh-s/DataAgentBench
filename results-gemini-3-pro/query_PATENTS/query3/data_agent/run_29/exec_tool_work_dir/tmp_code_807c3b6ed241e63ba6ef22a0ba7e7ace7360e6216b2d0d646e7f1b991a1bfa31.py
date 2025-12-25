code = """import json

# Read the file from the previous tool call
# var_function-call-3522050226317471560 contains the path
file_path = locals()['var_function-call-3522050226317471560']
with open(file_path, 'r') as f:
    uc_records = json.load(f)

# Extract publication numbers
uc_pub_nums = []
for rec in uc_records:
    # Patents_info string: "... has publication number US-11081687-B2." or "... with pub. number X."
    info = rec['Patents_info']
    # I need a robust regex to extract publication number
    import re
    # Patterns:
    # "publication number [A-Z0-9-]+"
    # "publication no. [A-Z0-9-]+"
    # "pub. number [A-Z0-9-]+"
    # "pub. no. [A-Z0-9-]+"
    match = re.search(r'(?:publication|pub\.?)\s+(?:number|no\.)\s+([A-Z0-9-]+)', info)
    if match:
        uc_pub_nums.append(match.group(1))

print(f"__RESULT__:\n{json.dumps({'count': len(uc_pub_nums), 'sample': uc_pub_nums[:5]})}")"""

env_args = {'var_function-call-13677460212293356387': 'file_storage/function-call-13677460212293356387.json', 'var_function-call-7850291326944532935': [{'cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02E60/10",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/582",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_function-call-3522050226317471560': 'file_storage/function-call-3522050226317471560.json'}

exec(code, env_args)
