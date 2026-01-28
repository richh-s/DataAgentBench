code = """import json
import re
import os

# Get UNIV CALIFORNIA patents from previous query
usc_patents_file = locals()['var_functions.query_db:12']

with open(usc_patents_file, 'r') as f:
    usc_patents = json.load(f)

# Extract publication numbers from USC patents
usc_publication_numbers = set()
pub_num_pattern = re.compile(r'(US|WO|EP|JP|CN|KR|GB|DE|FR|TW)\-\d+[A-Z]?\-\d+[A-Z]?[A-Z]?')

for patent in usc_patents:
    patents_info = patent['Patents_info']
    matches = pub_num_pattern.findall(patents_info)
    
    # Look for "pub. number" or similar patterns
    if 'pub. number' in patents_info:
        pub_part = patents_info.split('pub. number')[1]
        pub_num_match = pub_num_pattern.search(pub_part)
        if pub_num_match:
            usc_publication_numbers.add(pub_num_match.group())
    elif 'publication number' in patents_info:
        pub_part = patents_info.split('publication number')[1]
        pub_num_match = pub_num_pattern.search(pub_part)
        if pub_num_match:
            usc_publication_numbers.add(pub_num_match.group())
    elif 'publication no' in patents_info:
        pub_part = patents_info.split('publication no')[1]
        pub_num_match = pub_num_pattern.search(pub_part)
        if pub_num_match:
            usc_publication_numbers.add(pub_num_match.group())

print(f'Found {len(usc_publication_numbers)} USC publication numbers')
print('Sample USC patents:', list(usc_publication_numbers)[:10])

# Save USC patent numbers for follow-up queries
output_dir = './analysis_output'
os.makedirs(output_dir, exist_ok=True)

usc_patents_file = os.path.join(output_dir, 'usc_publication_numbers.json')
with open(usc_patents_file, 'w') as f:
    json.dump(list(usc_publication_numbers), f)

summary = {
    'usc_patent_count': len(usc_patents),
    'usc_publication_numbers': len(usc_publication_numbers),
    'sample_usc_pubs': list(usc_publication_numbers)[:15]
}

print('__RESULT__:')
print(json.dumps(summary))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'total_california_patents': 169, 'total_citations_found': 1308, 'unique_cpc_subclasses': 436, 'sample_cpc_codes': ['Y10S436', 'B01D53', 'B64G1', 'Y02E60', 'C07K1', 'C12Q2600', 'C07D323', 'C12M21', 'A23V2002', 'A61N5'], 'sample_citations': [{'cited_patent_number': 'US-4599677-A', 'california_patent_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'cited_patent_number': 'US-2015129765-A1', 'california_patent_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'cited_patent_number': 'FR-3105380-A1', 'california_patent_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}]}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:24': {'total_citing_patents_processed': 1, 'unique_citing_assignees': 0, 'university_patents_cited': 0, 'sample_citations': {}}, 'var_functions.query_db:28': [], 'var_functions.query_db:30': [{'symbol': 'B01D53/047', 'titleFull': 'Pressure swing adsorption'}, {'symbol': 'B01D53/0407', 'titleFull': 'Constructional details of adsorbing systems'}, {'symbol': 'B01D53/0462', 'titleFull': 'Temperature swing adsorption'}, {'symbol': 'B01D53/0454', 'titleFull': 'Controlling adsorption'}, {'symbol': 'B01D53/08', 'titleFull': 'Separation of gases or vapours; Recovering vapours of volatile solvents from gases; Chemical or biological purification of waste gases, e.g. engine exhaust gases, smoke, fumes, flue gases, aerosols by adsorption, e.g. preparative gas chromatography with moving adsorbents, e.g. rotating beds according to the "moving bed" method'}]}

exec(code, env_args)
