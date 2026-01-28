code = """import json
import re
import os

# Load USC publication numbers and CPC mapping
output_dir = './analysis_output'
usc_cpc_file = os.path.join(output_dir, 'usc_pub_to_cpc.json')
usc_pub_file = os.path.join(output_dir, 'usc_publication_numbers.json')

with open(usc_cpc_file, 'r') as f:
    usc_pub_to_cpc = json.load(f)

with open(usc_pub_file, 'r') as f:
    usc_publication_numbers = json.load(f)

usc_pub_set = set(usc_publication_numbers)
print('USC patents loaded:', len(usc_pub_set))

# Pattern to extract assignee from patent info
assignee_pattern = re.compile(r'(owned by|belongs to|assigned to|belonging to)\s+([^\.]+)', re.IGNORECASE)

# Pattern to extract patent numbers from text
patent_pattern = re.compile(r'([A-Z]{2}\-\d+\-[A-Z]\d*)')

# Load patents with citations data
citation_data_file = locals()['var_functions.query_db:76']
with open(citation_data_file, 'r') as f:
    citation_data = json.load(f)

print('Total patents to check for USC citations:', len(citation_data))

# Find citations to USC patents
citing_assignees_to_usc = {}  # citing_assignee -> list of (usc_patent, usc_cpc_codes)
usc_cited_by_count = {}  # USC patent -> list of citing assignees

for patent in citation_data:
    patents_info = patent.get('Patents_info', '')
    citation_json = patent.get('citation', '')
    
    # Skip if no citations
    if not citation_json or citation_json == '[]':
        continue
    
    # Extract assignee
    assignee_match = assignee_pattern.search(patents_info)
    if assignee_match:
        citing_assignee = assignee_match.group(2).strip()
        # Exclude UNIV CALIFORNIA citations
        if 'UNIV CALIFORNIA' in citing_assignee.upper():
            continue
    else:
        continue
    
    # Parse citations
    try:
        citations = json.loads(citation_json) if isinstance(citation_json, str) else citation_json
        for citation in citations:
            cited_patent = citation.get('publication_number', '')
            if cited_patent in usc_pub_set:
                # Found a citation to USC patent
                if citing_assignee not in citing_assignees_to_usc:
                    citing_assignees_to_usc[citing_assignee] = []
                
                # Get CPC codes for this USC patent
                usc_cpc_codes = usc_pub_to_cpc.get(cited_patent, [])
                
                citing_assignees_to_usc[citing_assignee].append({
                    'usc_patent': cited_patent,
                    'usc_cpc_codes': usc_cpc_codes
                })
                
                # Track which USC patents are cited by whom
                if cited_patent not in usc_cited_by_count:
                    usc_cited_by_count[cited_patent] = set()
                usc_cited_by_count[cited_patent].add(citing_assignee)
                
    except:
        continue

print('Found', len(citing_assignees_to_usc), 'assignees citing USC patents')
print('Found', len(usc_cited_by_count), 'USC patents cited')

# Save intermediate results
with open(os.path.join(output_dir, 'citing_assignees_to_usc.json'), 'w') as f:
    json.dump(citing_assignees_to_usc, f)

with open(os.path.join(output_dir, 'usc_cited_by_count.json'), 'w') as f:
    json.dump({k: list(v) for k, v in usc_cited_by_count.items()}, f)

result = {
    'unique_citing_assignees': len(citing_assignees_to_usc),
    'usc_patents_cited': len(usc_cited_by_count),
    'total_citations_found': sum(len(v) for v in citing_assignees_to_usc.values())
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'total_california_patents': 169, 'total_citations_found': 1308, 'unique_cpc_subclasses': 436, 'sample_cpc_codes': ['Y10S436', 'B01D53', 'B64G1', 'Y02E60', 'C07K1', 'C12Q2600', 'C07D323', 'C12M21', 'A23V2002', 'A61N5'], 'sample_citations': [{'cited_patent_number': 'US-4599677-A', 'california_patent_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'cited_patent_number': 'US-2015129765-A1', 'california_patent_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'cited_patent_number': 'FR-3105380-A1', 'california_patent_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}]}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:24': {'total_citing_patents_processed': 1, 'unique_citing_assignees': 0, 'university_patents_cited': 0, 'sample_citations': {}}, 'var_functions.query_db:28': [], 'var_functions.query_db:30': [{'symbol': 'B01D53/047', 'titleFull': 'Pressure swing adsorption'}, {'symbol': 'B01D53/0407', 'titleFull': 'Constructional details of adsorbing systems'}, {'symbol': 'B01D53/0462', 'titleFull': 'Temperature swing adsorption'}, {'symbol': 'B01D53/0454', 'titleFull': 'Controlling adsorption'}, {'symbol': 'B01D53/08', 'titleFull': 'Separation of gases or vapours; Recovering vapours of volatile solvents from gases; Chemical or biological purification of waste gases, e.g. engine exhaust gases, smoke, fumes, flue gases, aerosols by adsorption, e.g. preparative gas chromatography with moving adsorbents, e.g. rotating beds according to the "moving bed" method'}], 'var_functions.execute_python:32': {'usc_patent_count': 169, 'usc_publication_numbers': 0, 'sample_usc_pubs': []}, 'var_functions.execute_python:46': {'count': 169}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.execute_python:52': {'usc_patents_with_cpc': 70}, 'var_functions.execute_python:54': {'usc_patents': 169, 'usc_publications': 168, 'usc_with_cpc': 168, 'sample_usc': ['US-11445941-B2', 'US-12025581-B2', 'AU-5366398-A', 'US-2005234013-A1', 'AP-3334-A', 'US-2021282642-A1', 'US-9061071-B2', 'AU-3353000-A', 'BR-9610580-A', 'CA-2220674-A1']}, 'var_functions.query_db:56': [{'symbol': 'C01B35/1045', 'titleFull': 'Oxyacids'}, {'symbol': 'C01B35/1027', 'titleFull': 'Oxides'}, {'symbol': 'C07K16/1018', 'titleFull': 'Orthomyxoviridae, e.g. influenza virus'}, {'symbol': 'C08G69/14', 'titleFull': 'Lactams'}, {'symbol': 'C09K11/881', 'titleFull': 'Chalcogenides'}, {'symbol': 'C09K11/892', 'titleFull': 'Chalcogenides'}, {'symbol': 'C01B17/508', 'titleFull': 'Preparation of sulfur dioxide by oxidation of sulfur compounds'}, {'symbol': 'C10B43/12', 'titleFull': 'Burners'}, {'symbol': 'C01B11/068', 'titleFull': 'Stabilisation by additives other than oxides, hydroxides, carbonates of alkali or alkaline-earth metals; Coating of particles; Shaping; Granulation'}, {'symbol': 'C01B11/066', 'titleFull': 'Magnesium hypochlorite'}], 'var_functions.execute_python:60': {'count': 168, 'sample': ['US-11445941-B2', 'US-12025581-B2', 'AU-5366398-A', 'US-2005234013-A1', 'AP-3334-A']}, 'var_functions.query_db:62': [], 'var_functions.execute_python:64': {'usc_patents_processed': 169, 'usc_with_publication_numbers': 168, 'usc_with_cpc_codes': 168}, 'var_functions.query_db:66': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}], 'var_functions.execute_python:72': {'usc_patents': 168, 'usc_with_cpc': 168}, 'var_functions.query_db:74': [], 'var_functions.query_db:76': 'file_storage/functions.query_db:76.json'}

exec(code, env_args)
