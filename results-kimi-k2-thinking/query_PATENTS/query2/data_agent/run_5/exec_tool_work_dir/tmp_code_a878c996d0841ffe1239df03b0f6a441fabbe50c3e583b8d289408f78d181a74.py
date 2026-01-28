code = """import json
import re
from datetime import datetime

# Load all 2019 patents
all_2019_file_path = locals()['var_functions.query_db:24']
with open(all_2019_file_path, 'r') as f:
    all_2019_patents = json.load(f)

print(f"Total 2019 patents: {len(all_2019_patents)}")

# Pattern matching for Germany/German connections
germany_pattern = re.compile(r'Germany|GERMANY|DEUTSCHLAND|germany|DE-|\.DE\b|Deutschland', re.IGNORECASE)
german_company_pattern = re.compile(r'\b(gmbh|GmbH|GMBH|Daimler|Siemens|Bosch|Bayer|BASF|Merck|SAP|Volkswagen|Continental|Adidas|Allianz|BMW|Henkel|Fresenius|Mercedes|Audi|Porsche|Thyssenkrupp|E.ON|RWE|Deutsche|GERMANY)\b', re.IGNORECASE)

germany_patents = []
for patent in all_2019_patents:
    if germany_pattern.search(patent['Patents_info']) or german_company_pattern.search(patent['Patents_info']):
        germany_patents.append(patent)

print(f"Germany-related patents: {len(germany_patents)}")

# Extract and parse grant dates
patents_with_dates = []

for patent in germany_patents:
    grant_date = patent['grant_date']
    month_num = None
    
    # Try to extract month name
    month_match = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)', grant_date, re.IGNORECASE)
    if month_match:
        month_name = month_match.group(1)[:3].capitalize()
        month_map = {
            'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
            'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
        }
        month_num = month_map.get(month_name, 0)
        
        if month_num:
            patents_with_dates.append({
                **patent,
                'month': month_num
            })

# Filter for second half of 2019 (July-December)
second_half_patents = [p for p in patents_with_dates if p['month'] >= 7]

print(f"Germany patents in second half of 2019: {len(second_half_patents)}")

# Show distribution by month
from collections import Counter
month_counts = Counter([p['month'] for p in second_half_patents])
print(f"Patents by month in second half: {sorted(month_counts.items())}")"""

env_args = {'var_functions.query_db:0': [{'grant_date': '3rd August 2021'}, {'grant_date': 'dated 6th October 2020'}, {'grant_date': '21st of September, 2021'}, {'grant_date': 'on April 7th, 2020'}, {'grant_date': 'Mar 23rd, 2021'}], 'var_functions.list_db:2': ['publicationinfo'], 'var_functions.query_db:6': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0'}], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_patents': 5, 'sample_grant_dates': ['January 23rd, 2019', '5th Jun 2019', 'dated 10th September 2019', 'Mar 19th, 2019', '10th of December, 2019']}, 'var_functions.execute_python:22': {'total_germany_2019_patents': 5}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:28': {'total_2019_patents': 3838}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
