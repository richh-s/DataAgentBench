code = """import json, re
# Get USC patents file path
usc_path_key = 'var_functions.query_db:12'
usc_file = locals()[usc_path_key]
with open(usc_file, 'r') as f:
    usc_patents = json.load(f)
print('USC patents total:', len(usc_patents))

# Look for patterns with "pub" to find publication numbers
usc_pub_numbers = set()
patent_num_pattern = re.compile(r'([A-Z]{2})\-(\d+)\-([A-Z]\d*)')

for patent in usc_patents[:20]:
    info = patent.get('Patents_info', '')
    print('\nPatent info:', info[:200])
    
    # Extract numbers after publication keywords
    if 'pub.' in info or 'publication' in info:
        sections = re.split(r'(pub\.|publication (?:number|no))', info, flags=re.IGNORECASE)
        if len(sections) > 2:
            pub_section = sections[-1]
            matches = patent_num_pattern.findall(pub_section)
            for match in matches:
                usc_pub_numbers.add(f"{match[0]}-{match[1]}-{match[2]}")

print('\nFound USC publication numbers:', len(usc_pub_numbers))
print('Sample:', list(usc_pub_numbers)[:10])"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'total_california_patents': 169, 'total_citations_found': 1308, 'unique_cpc_subclasses': 436, 'sample_cpc_codes': ['Y10S436', 'B01D53', 'B64G1', 'Y02E60', 'C07K1', 'C12Q2600', 'C07D323', 'C12M21', 'A23V2002', 'A61N5'], 'sample_citations': [{'cited_patent_number': 'US-4599677-A', 'california_patent_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'cited_patent_number': 'US-2015129765-A1', 'california_patent_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'cited_patent_number': 'FR-3105380-A1', 'california_patent_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}]}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:24': {'total_citing_patents_processed': 1, 'unique_citing_assignees': 0, 'university_patents_cited': 0, 'sample_citations': {}}, 'var_functions.query_db:28': [], 'var_functions.query_db:30': [{'symbol': 'B01D53/047', 'titleFull': 'Pressure swing adsorption'}, {'symbol': 'B01D53/0407', 'titleFull': 'Constructional details of adsorbing systems'}, {'symbol': 'B01D53/0462', 'titleFull': 'Temperature swing adsorption'}, {'symbol': 'B01D53/0454', 'titleFull': 'Controlling adsorption'}, {'symbol': 'B01D53/08', 'titleFull': 'Separation of gases or vapours; Recovering vapours of volatile solvents from gases; Chemical or biological purification of waste gases, e.g. engine exhaust gases, smoke, fumes, flue gases, aerosols by adsorption, e.g. preparative gas chromatography with moving adsorbents, e.g. rotating beds according to the "moving bed" method'}], 'var_functions.execute_python:32': {'usc_patent_count': 169, 'usc_publication_numbers': 0, 'sample_usc_pubs': []}}

exec(code, env_args)
