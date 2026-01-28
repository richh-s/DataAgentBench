code = """import json

# Load assignee data from previous step
assignee_file = locals()['var_functions.execute_python:58']
assignee_data = assignee_file['assignee_data']

# Load CPC definitions
cpc_file = locals()['var_functions.query_db:60']
cpc_definitions = {item['symbol']: item['titleFull'] for item in cpc_file}

# Compile final results
results = []

for assignee, data in assignee_data.items():
    cpc_codes = data['cpc_codes']
    for cpc_code in cpc_codes:
        if cpc_code in cpc_definitions:
            results.append({
                'assignee': assignee,
                'cpc_code': cpc_code,
                'cpc_title': cpc_definitions[cpc_code]
            })
        else:
            # Try to get the subclass symbol by taking before the last slash
            if '/' in cpc_code:
                parts = cpc_code.split('/')
                if len(parts) > 1:
                    subclass_symbol = '/'.join(parts[:-1])
                    if subclass_symbol in cpc_definitions:
                        results.append({
                            'assignee': assignee,
                            'cpc_code': cpc_code,
                            'cpc_title': cpc_definitions[subclass_symbol]
                        })

print('Final results to present:')
for r in results:
    print(f"Assignee: {r['assignee']}")
    print(f"CPC: {r['cpc_code']} - {r['cpc_title']}")
    print()

# Store final answer data
final_answer = results

print('__RESULT__:')
print(json.dumps(final_answer))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:34': {'total_univ_calif_patents': 169, 'total_extracted_pubs': 114, 'sample_pubs': ['US-2006292670-A1.', 'WO-2020055916-A9.', 'WO-2010045542-A3.', 'WO-2017214343-A1.', 'US-6980295-B2.', 'KR-20160119166-A.', 'CA-3161617-A1.', 'AU-2015364602-B2.', 'IL-274176-A.', 'US-2004115131-A1.']}, 'var_functions.execute_python:36': {'total_univ_calif_patents': 169, 'unique_cited_publications': 1112, 'citations_with_pub_numbers': 1112}, 'var_functions.execute_python:38': {'total_cited_by_univ_calif': 1112, 'total_univ_calif_publications': 114, 'sample_univ_calif_pubs': ['US-11421276-B2.', 'EP-3668487-A4.', 'KR-20050085437-A.', 'US-2020283856-A1.', 'EP-0826155-A4.', 'WO-2021102420-A1.', 'US-2009031436-A1.', 'JP-2009260386-A.', 'US-11014955-B2.', 'PT-2970346-T.']}, 'var_functions.execute_python:42': {'total_patents': 277813, 'univ_calif_patents': 169, 'sample_pubs': ['US-2003112494-A1', 'KR-100228821-B1', 'IL-274176-A', 'US-2020025859-A1', 'US-2021000566-A1', 'US-6750960-B2', 'WO-2024112568-A1', 'AU-2015364602-B2', 'PE-20130764-A1', 'EP-3668487-A4']}, 'var_functions.execute_python:44': {'total_university_california_pubs': 114, 'citing_patents_found': 4, 'sample_citing_patent': {'patent_info': 'The US patent filing (application number US-4007205-A) is assigned to CALIFORNIA INST OF TECHN and has publication number US-2005165588-A1.', 'cites': 'US-6237292-B1', 'cpc': '[\n  {\n    "code": "G01M7/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01M7/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01V1/01",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01V1/01",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}}, 'var_functions.execute_python:46': {'total_citing_patents': 1, 'unique_assignees': 1, 'sample_assignees': ['BLOOM ENERGY CORP and has publication no. US-10615444-B2.'], 'cpc_codes_to_lookup': ['H01M2008/1293', 'H01M2004/8684', 'H01M8/2457', 'H01M8/1253', 'H01M4/8657', 'H01M4/8652', 'Y02E60/525', 'Y02E60/50', 'H01M4/8642', 'H01M4/8663', 'H01M4/861', 'H01M4/9066', 'H01M8/2425', 'H01M4/8885', 'H01M4/9016', 'Y02P70/56', 'Y02P70/50']}, 'var_functions.execute_python:48': {'total_citing_patents': 1, 'unique_assignees': 1, 'assignees': ['BLOOM ENERGY CORP']}, 'var_functions.execute_python:50': {'total_citing_assignees': 3, 'total_cpc_codes_to_lookup': 44, 'assignees': ['CALIFORNIA INST OF TECHN', 'BLOOM ENERGY CORP', 'CRYSTAL IS INC'], 'cpc_codes': ['H01M8/2425', 'Y10T428/21', 'H01M2008/1293', 'H01L29/205', 'H01M4/8652', 'H01L21/02458', 'C30B11/003', 'H01M8/2457', 'H01L33/0075', 'H01M4/9016', 'H01L29/7787', 'H01M4/861', 'H01L29/04', 'H01L29/66462', 'C30B25/16', 'H01M8/1253', 'Y02E60/525', 'C30B25/10', 'H01L29/32', 'H01M4/9066', 'H01M4/8642', 'H01L21/02389', 'H01L33/025', 'H01M4/8657', 'H01M2004/8684', 'H01L29/0657', 'H01L21/02634', 'C30B25/14', 'C30B29/403', 'H01L33/12', 'H01L33/325', 'C30B23/00', 'H01L2924/0002', 'Y02E60/50', 'H01M4/8885', 'H01L21/0254', 'Y02P70/56', 'G01M7/00', 'H01L29/2003', 'H01M4/8663', 'Y02P70/50', 'C30B23/025', 'G01V1/01', 'C30B25/20']}, 'var_functions.query_db:56': [{'symbol': 'C30B', 'titleFull': 'SINGLE-CRYSTAL GROWTH; UNIDIRECTIONAL SOLIDIFICATION OF EUTECTIC MATERIAL OR UNIDIRECTIONAL DEMIXING OF EUTECTOID MATERIAL; REFINING BY ZONE-MELTING OF MATERIAL; PRODUCTION OF A HOMOGENEOUS POLYCRYSTALLINE MATERIAL WITH DEFINED STRUCTURE; SINGLE CRYSTALS OR HOMOGENEOUS POLYCRYSTALLINE MATERIAL WITH DEFINED STRUCTURE; AFTER-TREATMENT OF SINGLE CRYSTALS OR A HOMOGENEOUS POLYCRYSTALLINE MATERIAL WITH DEFINED STRUCTURE; APPARATUS THEREFOR'}, {'symbol': 'G01V', 'titleFull': 'GEOPHYSICS; GRAVITATIONAL MEASUREMENTS; DETECTING MASSES OR OBJECTS; TAGS'}, {'symbol': 'G01M', 'titleFull': 'TESTING STATIC OR DYNAMIC BALANCE OF MACHINES OR STRUCTURES; TESTING OF STRUCTURES OR APPARATUS, NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'H01L', 'titleFull': 'SEMICONDUCTOR DEVICES NOT COVERED BY CLASS H10'}, {'symbol': 'Y02E', 'titleFull': 'REDUCTION OF GREENHOUSE GAS [GHG] EMISSIONS, RELATED TO ENERGY GENERATION, TRANSMISSION OR DISTRIBUTION'}, {'symbol': 'Y02P', 'titleFull': 'CLIMATE CHANGE MITIGATION TECHNOLOGIES IN THE PRODUCTION OR PROCESSING OF GOODS'}, {'symbol': 'Y10T', 'titleFull': 'TECHNICAL SUBJECTS COVERED BY FORMER US CLASSIFICATION'}], 'var_functions.execute_python:58': {'assignee_data': {'BLOOM ENERGY CORP': {'citation_count': 1, 'cpc_codes': ['H01M4/9066', 'H01M8/2425']}}, 'all_cpc_codes': ['H01M4/9066', 'H01M8/2425']}, 'var_functions.query_db:60': [{'symbol': 'H01M8/2425', 'titleFull': 'High-temperature cells with solid electrolytes'}, {'symbol': 'H01M4/9066', 'titleFull': 'Metals or alloys specially used in fuel cell operating at high temperature, e.g. SOFC of metal-ceramic composites or mixtures, e.g. cermets'}]}

exec(code, env_args)
