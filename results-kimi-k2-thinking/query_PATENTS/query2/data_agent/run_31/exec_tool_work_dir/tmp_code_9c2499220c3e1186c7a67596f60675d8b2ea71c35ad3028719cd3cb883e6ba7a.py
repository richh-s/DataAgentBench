code = """import json

# Load the German patents data from the file
result_file = locals()['var_functions.query_db:8']
with open(result_file, 'r') as f:
    german_patents = json.load(f)

# Extract CPC codes at level 4
level4_codes = []
for patent in german_patents:
    try:
        cpc_list = json.loads(patent['cpc'])
        for cpc in cpc_list:
            code = cpc['code']
            # Split section, class, subclass, group
            # Format: A61B17/64 (example)
            if '/' in code:
                main_part, subgroup = code.split('/')
                # Extract level 4 (main group) - digits at the end of main_part
                section = main_part[0]  # A-H, Y
                class_num = main_part[1:3]  # 2 digits
                subclass = main_part[3] if len(main_part) > 3 else ''  # 1 letter
                
                # The rest should be the main group
                if len(main_part) > 4:
                    group = main_part[4:]  # digits
                    level4_code = f"{section}{class_num}{subclass}{group}"
                    level4_codes.append({
                        'code': code,
                        'level4': level4_code,
                        'original_cpc': cpc
                    })
    except Exception as e:
        continue

# Count occurrences of each level 4 code
from collections import Counter
level4_counts = Counter([item['level4'] for item in level4_codes])

print(f"__RESULT__:")
print(json.dumps({
    "total_level4_codes": len(level4_codes),
    "unique_level4_codes": len(level4_counts),
    "top_level4_codes": dict(level4_counts.most_common(10)),
    "all_level4_codes": list(level4_counts.keys())
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'total_patents': 18, 'first_patent': {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'dated 21st November 2019'}, 'sample_cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"'}}

exec(code, env_args)
