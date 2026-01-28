code = """import json
import pandas as pd
import re
from datetime import datetime

# Read the German patents data
file_path = locals()['var_functions.query_db:12']
with open(file_path, 'r') as f:
    patents_data = json.load(f)

# Parse CPC codes and extract level 4 classifications
def get_cpc_level4(cpc_code):
    """Extract level 4 CPC code (main class + 1-2 digit subclass)"""
    if not cpc_code:
        return None
    
    # CPC format: Section (1 char) + Class (2 digits) + Subclass (1 letter) + Group (1-3 digits) + / + Main group + Subgroup
    # Level 4 typically refers to the main group level (e.g., B41F21 from B41F21/102)
    
    # Remove any whitespace
    cpc_code = cpc_code.strip()
    
    # Pattern: Letter + 2 digits + Letter + digits before /
    match = re.match(r'^([A-Z][0-9]{2}[A-Z][0-9]{1,3})', cpc_code)
    if match:
        return match.group(1)
    
    # Alternative pattern: Just get the part before / or first 4-5 characters
    if '/' in cpc_code:
        parts = cpc_code.split('/')
        main_part = parts[0]
        if len(main_part) >= 4:
            return main_part
    
    return cpc_code[:5] if len(cpc_code) >= 4 else None

# Filter for German patents granted in second half of 2019
month_map = {
    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
    'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
}

# Process all German patents regardless of year first to get historical data
german_patents_all = []
for patent in patents_data:
    patents_info = patent.get('Patents_info', '')
    grant_date = patent.get('grant_date', '')
    cpc = patent.get('cpc', '[]')
    title_localized = patent.get('title_localized', '[]')
    
    # Check if it's a German patent
    if 'DE-' in patents_info:
        # Try to extract year and month
        year_match = re.search(r'(20\d{2})', grant_date)
        month = None
        grant_date_lower = grant_date.lower()
        
        for month_name, month_num in month_map.items():
            if month_name in grant_date_lower:
                month = month_num
                break
        
        if year_match and month:
            year = int(year_match.group(1))
            
            # Extract CPC codes
            try:
                cpc_list = json.loads(cpc) if isinstance(cpc, str) else cpc
                cpc_codes = [item.get('code') for item in cpc_list if item.get('code')]
            except:
                cpc_codes = []
            
            # Extract title
            try:
                title_list = json.loads(title_localized) if isinstance(title_localized, str) else title_localized
                if title_list and len(title_list) > 0:
                    # Try to get German title first, then English
                    title = ''
                    for lang_pref in ['de', 'en']:
                        for t in title_list:
                            if t.get('language') == lang_pref and t.get('text'):
                                title = t.get('text')
                                break
                        if title:
                            break
                    if not title and title_list[0].get('text'):
                        title = title_list[0].get('text')
                else:
                    title = ''
            except:
                title = ''
            
            if cpc_codes:  # Only add if there are CPC codes
                german_patents_all.append({
                    'patents_info': patents_info,
                    'grant_date': grant_date,
                    'grant_month': month,
                    'grant_year': year,
                    'cpc_codes': cpc_codes,
                    'title': title
                })

# Now filter for second half 2019 specifically for the query
german_patents_h2_2019 = [p for p in german_patents_all if p['grant_year'] == 2019 and p['grant_month'] >= 7]

print('__RESULT__:')
print(json.dumps({
    'total_german_patents_all': len(german_patents_all),
    'german_patents_h2_2019': len(german_patents_h2_2019),
    'years_available': sorted(list(set([p['grant_year'] for p in german_patents_all]))),
    'sample_patents': german_patents_h2_2019[:3]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'total_german_patents': 1, 'sample_patents': [{'patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'grant_month': 11, 'cpc_codes': ['B41F21/102', 'B41F22/00', 'B41F21/00']}]}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'total_german_patents_h2_2019': 34, 'sample_patents': [{'patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'grant_month': 11, 'cpc_codes': ['B41F21/102', 'B41F22/00', 'B41F21/00'], 'title': 'Trommel zum Fördern eines Bogens', 'publication_date': '21st November 2019'}, {'patents_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'grant_date': '5th of December, 2019', 'grant_month': 12, 'cpc_codes': ['F02D41/3005', 'F02D41/20', 'F02M65/005', 'F02D41/00', 'F02D41/20', 'F02D41/20'], 'title': 'Ermittlung des Öffnungszeitpunkts eines Steuerventils eines indirekt angetriebenen Kraftstoffinjektors', 'publication_date': 'December the 5th, 2019'}, {'patents_info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'grant_date': '22nd of August, 2019', 'grant_month': 8, 'cpc_codes': ['F02M59/102', 'F02M55/04', 'F02M55/04', 'F02M59/102', 'F02M59/44', 'F02M59/06', 'F04B53/001', 'F02M59/368', 'F04B53/001', 'F02M59/44', 'F02M59/368', 'F02M59/06'], 'title': 'Pulsationsdämpfer und Hochdruckkraftstoffpumpe', 'publication_date': 'on August 22nd, 2019'}]}, 'var_functions.query_db:18': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0'}, {'symbol': 'B99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0'}, {'symbol': 'B29', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL', 'level': '4.0'}, {'symbol': 'B33', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY', 'level': '4.0'}, {'symbol': 'C22', 'titleFull': 'METALLURGY; FERROUS OR NON-FERROUS ALLOYS; TREATMENT OF ALLOYS OR NON-FERROUS METALS', 'level': '4.0'}, {'symbol': 'D99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0'}]}

exec(code, env_args)
