code = """import json
import re
from collections import defaultdict, Counter

# Load the German patents data from the file
result_file = locals()['var_functions.query_db:17']
with open(result_file, 'r') as f:
    german_patents = json.load(f)

# Extract and process the data
yearly_counts = defaultdict(Counter)  # CPC level 4 -> year -> count
cpc_definitions = {}  # To store CPC codes for later lookup

# Regular expression to extract year from grant_date
year_pattern = re.compile(r'(\d{4})')

for patent in german_patents:
    try:
        cpc_list = json.loads(patent['cpc'])
        grant_date = patent['grant_date']
        
        # Extract year from grant_date
        year_match = year_pattern.search(grant_date)
        if not year_match:
            continue
        year = int(year_match.group(1))
        
        # Process each CPC code
        for cpc in cpc_list:
            code = cpc['code']
            if '/' not in code:
                continue
                
            # Parse CPC code structure
            # Format: Section (A-H, Y), Class (2 digits), Subclass (letter), Main Group (1-4 digits)
            main_part, subgroup = code.split('/')
            section = main_part[0]
            class_num = main_part[1:3]
            subclass = main_part[3] if len(main_part) > 3 else ''
            
            # Extract main group - digits after subclass
            if len(main_part) > 4:
                group_digits = main_part[4:]
                # Get level 4 code (main group level)
                level4_code = f"{section}{class_num}{subclass}{group_digits}"
                
                # Update counts
                yearly_counts[level4_code][year] += 1
                
                # Store full CPC for this level4 group for title lookup
                if level4_code not in cpc_definitions:
                    # Create the CPC code at group level (without subgroup)
                    cpc_definitions[level4_code] = f"{section}{class_num}{subclass}/{group_digits}"
    except Exception as e:
        continue

print(f"__RESULT__:")
print(json.dumps({
    "total_patents_processed": len(german_patents),
    "cpc_level4_groups": len(yearly_counts),
    "year_range": f"{min([min(counts.keys()) for counts in yearly_counts.values()]) if yearly_counts else 'N/A'} - {max([max(counts.keys()) for counts in yearly_counts.values()]) if yearly_counts else 'N/A'}",
    "sample_cpc_groups": list(yearly_counts.keys())[:10],
    "sample_yearly_counts": {k: dict(v) for k, v in list(yearly_counts.items())[:3]}
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'total_patents': 18, 'first_patent': {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'dated 21st November 2019'}, 'sample_cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"'}, 'var_functions.execute_python:14': {'total_level4_codes': 219, 'unique_level4_codes': 69, 'top_level4_codes': {'C04B2235': 32, 'H04W52': 12, 'C04B35': 12, 'H04L1': 10, 'H04W72': 9, 'B29C2049': 9, 'F02M59': 8, 'F02D41': 6, 'A61F5': 6, 'B29C49': 5}, 'all_level4_codes': ['B41F21', 'B41F22', 'F02D41', 'F02M65', 'F02M59', 'F02M55', 'F04B53', 'G01D11', 'B23K1', 'B63B21', 'H04W72', 'H04L5', 'H04L1', 'H04W52', 'H04W76', 'Y02D30', 'B66C23', 'E02F9', 'B60S9', 'F02D15', 'F02D13', 'Y02T10', 'A61F5', 'A43B17', 'A43B7', 'A43B13', 'F24B5', 'F23L15', 'F23L1', 'F23B60', 'F23B50', 'F23N1', 'Y02E20', 'H01R35', 'B64D11', 'H01R2201', 'H01R24', 'H01R13', 'B60R16', 'F02N2200', 'F02N2300', 'F02N11', 'B60K6', 'B60W30', 'C04B2235', 'C04B35', 'C09K11', 'C04B40', 'B29C49', 'B29C2049', 'B29C2949', 'G02B15', 'A61B1', 'G02B13', 'G02B23', 'Y10T70', 'G07C9', 'B29C2045', 'B29D99', 'H01H9', 'B29C45', 'H01H2009', 'E05B19', 'F16H37', 'F16H2200', 'F16H3', 'E02F3', 'F42B3', 'F41H11']}, 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json'}

exec(code, env_args)
