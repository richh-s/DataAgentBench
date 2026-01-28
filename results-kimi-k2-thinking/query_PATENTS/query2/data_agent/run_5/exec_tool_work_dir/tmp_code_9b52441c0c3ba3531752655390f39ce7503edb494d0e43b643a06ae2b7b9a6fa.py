code = """import json
import re
from collections import Counter

# Load all 2019 patents
all_2019_file_path = locals()['var_functions.query_db:24']
with open(all_2019_file_path, 'r') as f:
    all_2019_patents = json.load(f)

# Pattern matching for Germany/German connections
germany_pattern = re.compile(r'Germany|GERMANY|DEUTSCHLAND|germany|DE-|\.DE\b|Deutschland', re.IGNORECASE)
german_company_pattern = re.compile(r'\b(gmbh|GmbH|GMBH|Daimler|Siemens|Bosch|Bayer|BASF|Merck|SAP|Volkswagen|Continental|Adidas|Allianz|BMW|Henkel|Fresenius|Mercedes|Audi|Porsche|Thyssenkrupp|E\.ON|RWE|Deutsche)\b', re.IGNORECASE)

# Extract patents related to Germany from second half of 2019
germany_patents = []
for patent in all_2019_patents:
    patents_info = patent['Patents_info']
    if germany_pattern.search(patents_info) or german_company_pattern.search(patents_info):
        # Extract month from grant_date
        grant_date = patent['grant_date']
        month_match = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)', grant_date, re.IGNORECASE)
        
        if month_match:
            month_name = month_match.group(1)[:3].capitalize()
            month_map = {
                'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
                'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
            }
            month_num = month_map.get(month_name, 0)
            
            if month_num >= 7:  # Second half of 2019 (July-December)
                year_match = re.search(r'(\d{4})', grant_date)
                if year_match and year_match.group(1) == '2019':
                    # Parse CPC codes
                    try:
                        cpc_codes = json.loads(patent['cpc'])
                        for cpc in cpc_codes:
                            code = cpc.get('code', '')
                            # Extract level 4 code (format: XXXX or XX/XX)
                            level4_code = code.split('/')[0] if '/' in code else code[:4]
                            if len(level4_code) >= 3:
                                germany_patents.append({
                                    'level4_code': level4_code,
                                    'full_code': code,
                                    'title_localized': patent['title_localized']
                                })
                    except:
                        pass

# Count by level 4 CPC code
cpc_counts = Counter([p['level4_code'] for p in germany_patents])

print('__RESULT__:')
print(json.dumps({
    'total_germany_patents_2nd_half_2019': len(germany_patents),
    'unique_cpc_level4_codes': len(cpc_counts),
    'top_cpc_codes': cpc_counts.most_common(10)
}))"""

env_args = {'var_functions.query_db:0': [{'grant_date': '3rd August 2021'}, {'grant_date': 'dated 6th October 2020'}, {'grant_date': '21st of September, 2021'}, {'grant_date': 'on April 7th, 2020'}, {'grant_date': 'Mar 23rd, 2021'}], 'var_functions.list_db:2': ['publicationinfo'], 'var_functions.query_db:6': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0'}], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_patents': 5, 'sample_grant_dates': ['January 23rd, 2019', '5th Jun 2019', 'dated 10th September 2019', 'Mar 19th, 2019', '10th of December, 2019']}, 'var_functions.execute_python:22': {'total_germany_2019_patents': 5}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:28': {'total_2019_patents': 3838}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:36': {'total_2019_germany_patents': 26}}

exec(code, env_args)
