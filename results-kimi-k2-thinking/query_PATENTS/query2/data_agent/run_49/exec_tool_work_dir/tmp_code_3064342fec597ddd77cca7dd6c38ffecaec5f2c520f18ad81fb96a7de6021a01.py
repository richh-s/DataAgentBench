code = """import json
import re

# Read all patents data
file_path = locals()['var_functions.query_db:24']
with open(file_path, 'r') as f:
    all_patents_data = json.load(f)

# Extract CPC level 4 codes
def get_cpc_level4(cpc_code):
    if not cpc_code:
        return None
    cpc_code = cpc_code.strip()
    match = re.match(r'^([A-Z][0-9]{2}[A-Z][0-9]{1,3})', cpc_code)
    if match:
        return match.group(1)
    if '/' in cpc_code:
        parts = cpc_code.split('/')
        main_part = parts[0]
        if len(main_part) >= 4:
            return main_part
    return cpc_code[:5] if len(cpc_code) >= 4 else None

# Process German patents specifically
month_map = {
    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
    'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
}

german_cpc_counts_h2_2019 = {}
cpc_to_titles = {}

for patent in all_patents_data:
    patents_info = patent.get('Patents_info', '')
    grant_date = patent.get('grant_date', '')
    cpc = patent.get('cpc', '[]')
    title_localized = patent.get('title_localized', '[]')
    
    if 'DE-' in patents_info and '2019' in grant_date:
        month = None
        grant_date_lower = grant_date.lower()
        for month_name, month_num in month_map.items():
            if month_name in grant_date_lower:
                month = month_num
                break
        
        if month and month >= 7:
            try:
                cpc_list = json.loads(cpc) if isinstance(cpc, str) else cpc
                cpc_codes = [item.get('code') for item in cpc_list if item.get('code')]
            except:
                cpc_codes = []
            
            try:
                title_list = json.loads(title_localized) if isinstance(title_localized, str) else title_localized
                title = ''
                if title_list and len(title_list) > 0:
                    for lang_pref in ['de', 'en']:
                        for t in title_list:
                            if t.get('language') == lang_pref and t.get('text'):
                                title = t.get('text')
                                break
                        if title:
                            break
                    if not title and title_list[0].get('text'):
                        title = title_list[0].get('text')
            except:
                title = ''
            
            for cpc_code in cpc_codes:
                level4_code = get_cpc_level4(cpc_code)
                if level4_code:
                    german_cpc_counts_h2_2019[level4_code] = german_cpc_counts_h2_2019.get(level4_code, 0) + 1
                    if level4_code not in cpc_to_titles:
                        cpc_to_titles[level4_code] = title

# Sort by count descending
sorted_cpc = sorted(german_cpc_counts_h2_2019.items(), key=lambda x: x[1], reverse=True)

print('__RESULT__:')
print(json.dumps({
    'total_cpc_groups': len(sorted_cpc),
    'top_cpc_groups': sorted_cpc[:15],
    'cpc_to_titles': cpc_to_titles
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'total_german_patents': 1, 'sample_patents': [{'patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'grant_month': 11, 'cpc_codes': ['B41F21/102', 'B41F22/00', 'B41F21/00']}]}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'total_german_patents_h2_2019': 34, 'sample_patents': [{'patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'grant_month': 11, 'cpc_codes': ['B41F21/102', 'B41F22/00', 'B41F21/00'], 'title': 'Trommel zum Fördern eines Bogens', 'publication_date': '21st November 2019'}, {'patents_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'grant_date': '5th of December, 2019', 'grant_month': 12, 'cpc_codes': ['F02D41/3005', 'F02D41/20', 'F02M65/005', 'F02D41/00', 'F02D41/20', 'F02D41/20'], 'title': 'Ermittlung des Öffnungszeitpunkts eines Steuerventils eines indirekt angetriebenen Kraftstoffinjektors', 'publication_date': 'December the 5th, 2019'}, {'patents_info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'grant_date': '22nd of August, 2019', 'grant_month': 8, 'cpc_codes': ['F02M59/102', 'F02M55/04', 'F02M55/04', 'F02M59/102', 'F02M59/44', 'F02M59/06', 'F04B53/001', 'F02M59/368', 'F04B53/001', 'F02M59/44', 'F02M59/368', 'F02M59/06'], 'title': 'Pulsationsdämpfer und Hochdruckkraftstoffpumpe', 'publication_date': 'on August 22nd, 2019'}]}, 'var_functions.query_db:18': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0'}, {'symbol': 'B99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0'}, {'symbol': 'B29', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL', 'level': '4.0'}, {'symbol': 'B33', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY', 'level': '4.0'}, {'symbol': 'C22', 'titleFull': 'METALLURGY; FERROUS OR NON-FERROUS ALLOYS; TREATMENT OF ALLOYS OR NON-FERROUS METALS', 'level': '4.0'}, {'symbol': 'D99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0'}], 'var_functions.execute_python:22': {'total_german_patents_all': 68, 'german_patents_h2_2019': 34, 'years_available': [2019], 'sample_patents': [{'patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'grant_month': 11, 'grant_year': 2019, 'cpc_codes': ['B41F21/102', 'B41F22/00', 'B41F21/00'], 'title': 'Trommel zum Fördern eines Bogens'}, {'patents_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'grant_date': '5th of December, 2019', 'grant_month': 12, 'grant_year': 2019, 'cpc_codes': ['F02D41/3005', 'F02D41/20', 'F02M65/005', 'F02D41/00', 'F02D41/20', 'F02D41/20'], 'title': 'Ermittlung des Öffnungszeitpunkts eines Steuerventils eines indirekt angetriebenen Kraftstoffinjektors'}, {'patents_info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'grant_date': '22nd of August, 2019', 'grant_month': 8, 'grant_year': 2019, 'cpc_codes': ['F02M59/102', 'F02M55/04', 'F02M55/04', 'F02M59/102', 'F02M59/44', 'F02M59/06', 'F04B53/001', 'F02M59/368', 'F04B53/001', 'F02M59/44', 'F02M59/368', 'F02M59/06'], 'title': 'Pulsationsdämpfer und Hochdruckkraftstoffpumpe'}]}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
