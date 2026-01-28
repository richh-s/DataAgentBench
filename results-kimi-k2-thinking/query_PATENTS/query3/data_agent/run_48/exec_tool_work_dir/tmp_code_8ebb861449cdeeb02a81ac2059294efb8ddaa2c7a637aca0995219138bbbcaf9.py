code = """import json

# Get USC patents file path
usc_patents_file = locals()['var_functions.query_db:12']

# Load USC patents data
with open(usc_patents_file, 'r') as f:
    usc_patents = json.load(f)

# Create a mapping from publication number to CPC codes
usc_pub_to_cpc = {}
patent_pattern = 'US-\\d+-[A-Z]\\d*'

for patent in usc_patents:
    patents_info = patent.get('Patents_info', '')
    cpc_json = patent.get('cpc', '')
    
    # Find publication number
    import re
    pub_match = None
    if 'pub. number' in patents_info:
        pub_part = patents_info.split('pub. number')[1]
        pub_match = re.search(patent_pattern, pub_part)
    elif 'publication number' in patents_info:
        pub_part = patents_info.split('publication number')[1]
        pub_match = re.search(patent_pattern, pub_part)
    elif 'publication no' in patents_info:
        pub_part = patents_info.split('publication no')[1]
        pub_match = re.search(patent_pattern, pub_part)
    
    if pub_match:
        pub_num = pub_match.group()
        # Parse CPC codes
        try:
            if cpc_json and cpc_json != '[]':
                if isinstance(cpc_json, str):
                    cpc_list = json.loads(cpc_json)
                else:
                    cpc_list = cpc_json
                
                cpc_codes = [item.get('code', '') for item in cpc_list if item.get('code')]
                if cpc_codes:
                    usc_pub_to_cpc[pub_num] = cpc_codes
        except:
            pass

print('USC publication numbers with CPC codes:', len(usc_pub_to_cpc))
print('Sample mapping:', {k: usc_pub_to_cpc[k][:3] for k in list(usc_pub_to_cpc)[:3]})

# Save for later
import os
output_dir = './analysis_output'
os.makedirs(output_dir, exist_ok=True)

with open(os.path.join(output_dir, 'usc_pub_to_cpc.json'), 'w') as f:
    json.dump(usc_pub_to_cpc, f)

result = {'usc_patents_with_cpc': len(usc_pub_to_cpc)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'total_california_patents': 169, 'total_citations_found': 1308, 'unique_cpc_subclasses': 436, 'sample_cpc_codes': ['Y10S436', 'B01D53', 'B64G1', 'Y02E60', 'C07K1', 'C12Q2600', 'C07D323', 'C12M21', 'A23V2002', 'A61N5'], 'sample_citations': [{'cited_patent_number': 'US-4599677-A', 'california_patent_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'cited_patent_number': 'US-2015129765-A1', 'california_patent_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'cited_patent_number': 'FR-3105380-A1', 'california_patent_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}]}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:24': {'total_citing_patents_processed': 1, 'unique_citing_assignees': 0, 'university_patents_cited': 0, 'sample_citations': {}}, 'var_functions.query_db:28': [], 'var_functions.query_db:30': [{'symbol': 'B01D53/047', 'titleFull': 'Pressure swing adsorption'}, {'symbol': 'B01D53/0407', 'titleFull': 'Constructional details of adsorbing systems'}, {'symbol': 'B01D53/0462', 'titleFull': 'Temperature swing adsorption'}, {'symbol': 'B01D53/0454', 'titleFull': 'Controlling adsorption'}, {'symbol': 'B01D53/08', 'titleFull': 'Separation of gases or vapours; Recovering vapours of volatile solvents from gases; Chemical or biological purification of waste gases, e.g. engine exhaust gases, smoke, fumes, flue gases, aerosols by adsorption, e.g. preparative gas chromatography with moving adsorbents, e.g. rotating beds according to the "moving bed" method'}], 'var_functions.execute_python:32': {'usc_patent_count': 169, 'usc_publication_numbers': 0, 'sample_usc_pubs': []}, 'var_functions.execute_python:46': {'count': 169}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
