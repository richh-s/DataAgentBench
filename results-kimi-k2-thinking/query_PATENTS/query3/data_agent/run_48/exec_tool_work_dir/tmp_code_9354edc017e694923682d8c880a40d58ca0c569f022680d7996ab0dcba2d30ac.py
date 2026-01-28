code = """import json
import re

# Read the UNIV CALIFORNIA patents data
usc_file = locals()['var_functions.query_db:12']

with open(usc_file, 'r') as f:
    usc_patents = json.load(f)

print('Total UNIV CALIFORNIA patents found:', len(usc_patents))

# Extract publication numbers from UNIV CALIFORNIA patents
usc_pub_numbers = set()
usc_app_numbers = set()

# Pattern to match patent numbers like: US-2022074631-A1, TW-201925402-A, etc.
patent_pattern = re.compile(r'([A-Z]{2})\-\d+\-[A-Z]\d*')

for patent in usc_patents:
    patents_info = patent.get('Patents_info', '')
    
    # Look for publication numbers (most reliable for matching citations)
    if 'pub. number' in patents_info or 'publication number' in patents_info or 'publication no' in patents_info:
        # Extract all patent number patterns after "pub" keywords
        pub_section = patents_info
        if 'pub. number' in patents_info:
            pub_section = patents_info.split('pub. number')[1]
        elif 'publication number' in patents_info:
            pub_section = patents_info.split('publication number')[1]
        elif 'publication no' in patents_info:
            pub_section = patents_info.split('publication no')[1]
        
        pub_matches = patent_pattern.findall(pub_section)
        for match in pub_matches:
            usc_pub_numbers.add(f"{match[0]}-{match[1]}-{match[2]}")
    
    # Also extract application numbers as fallback
    if 'app. number' in patents_info or 'application number' in patents_info:
        app_section = patents_info
        if 'app. number' in patents_info:
            app_section = patents_info.split('app. number')[1]
        elif 'application number' in patents_info:
            app_section = patents_info.split('application number')[1]
        
        app_matches = patent_pattern.findall(app_section)
        for match in app_matches:
            usc_app_numbers.add(f"{match[0]}-{match[1]}-{match[2]}")

# Some manual extraction from the known patterns
for patent in usc_patents[:20]:  # Check first 20 to see patterns
    patents_info = patent.get('Patents_info', '')
    print('\nSample patent info:', patents_info[:150])

result_summary = {
    'usc_patent_count': len(usc_patents),
    'usc_pub_numbers_found': len(usc_pub_numbers),
    'usc_app_numbers_found': len(usc_app_numbers),
    'sample_pub_numbers': list(usc_pub_numbers)[:20],
    'sample_app_numbers': list(usc_app_numbers)[:20]
}

print('__RESULT__:')
print(json.dumps(result_summary))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'total_california_patents': 169, 'total_citations_found': 1308, 'unique_cpc_subclasses': 436, 'sample_cpc_codes': ['Y10S436', 'B01D53', 'B64G1', 'Y02E60', 'C07K1', 'C12Q2600', 'C07D323', 'C12M21', 'A23V2002', 'A61N5'], 'sample_citations': [{'cited_patent_number': 'US-4599677-A', 'california_patent_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'cited_patent_number': 'US-2015129765-A1', 'california_patent_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'cited_patent_number': 'FR-3105380-A1', 'california_patent_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}]}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:24': {'total_citing_patents_processed': 1, 'unique_citing_assignees': 0, 'university_patents_cited': 0, 'sample_citations': {}}, 'var_functions.query_db:28': [], 'var_functions.query_db:30': [{'symbol': 'B01D53/047', 'titleFull': 'Pressure swing adsorption'}, {'symbol': 'B01D53/0407', 'titleFull': 'Constructional details of adsorbing systems'}, {'symbol': 'B01D53/0462', 'titleFull': 'Temperature swing adsorption'}, {'symbol': 'B01D53/0454', 'titleFull': 'Controlling adsorption'}, {'symbol': 'B01D53/08', 'titleFull': 'Separation of gases or vapours; Recovering vapours of volatile solvents from gases; Chemical or biological purification of waste gases, e.g. engine exhaust gases, smoke, fumes, flue gases, aerosols by adsorption, e.g. preparative gas chromatography with moving adsorbents, e.g. rotating beds according to the "moving bed" method'}], 'var_functions.execute_python:32': {'usc_patent_count': 169, 'usc_publication_numbers': 0, 'sample_usc_pubs': []}}

exec(code, env_args)
