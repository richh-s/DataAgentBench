code = """import json
import re

# Load the citing patents data from earlier step
file_path = locals()['var_functions.query_db:28']
with open(file_path, 'r') as f:
    all_patents = json.load(f)

# Rebuild UNIV CALIFORNIA publication numbers
univ_calif_pubs = set()
for rec in all_patents:
    if 'UNIV CALIFORNIA' in rec['Patents_info']:
        match = re.search(r'pub\. number\s+([A-Z]{2,3}-[^,\s\]]+)', rec['Patents_info'])
        if match:
            pub_num = match.group(1).rstrip('.')
            univ_calif_pubs.add(pub_num)

# Find patents that cite UNIV CALIFORNIA, grouped by assignee
assignee_data = {}

for rec in all_patents:
    if 'UNIV CALIFORNIA' in rec['Patents_info']:
        continue
    
    citations_str = rec['citation']
    if not citations_str or citations_str == '[]':
        continue
    
    try:
        citations = json.loads(citations_str)
        for cite in citations:
            pub_num = cite.get('publication_number', '')
            if pub_num and pub_num in univ_calif_pubs:
                # Extract assignee
                info = rec['Patents_info']
                assignee = None
                
                patterns = [
                    r'is assigned to\s+([^,]+?)(?:\s+and\s+has|\.|$)',
                    r'is owned by\s+([^,]+?)(?:\s+and\s+has|\.|$)',
                    r'held by\s+([^,]+?)(?:\s+and\s+has|\.|$)',
                    r'belonging to\s+([^,]+?)(?:\s+and\s+has|\.|$)'
                ]
                
                for pat in patterns:
                    match = re.search(pat, info)
                    if match:
                        assignee = match.group(1).strip()
                        break
                
                if not assignee or 'UNIV CALIFORNIA' in assignee:
                    continue
                
                # Get CPC codes with metadata
                primary_cpc = []
                if rec['cpc'] and rec['cpc'] != '[]':
                    try:
                        cpc_list = json.loads(rec['cpc'])
                        for item in cpc_list:
                            if item.get('inventive') and item.get('first'):
                                primary_cpc.append(item['code'])
                        
                        # If no first+inventive, take inventive ones
                        if not primary_cpc:
                            for item in cpc_list:
                                if item.get('inventive'):
                                    primary_cpc.append(item['code'])
                    except:
                        pass
                
                # Add to assignee data
                if assignee not in assignee_data:
                    assignee_data[assignee] = {
                        'citation_count': 0,
                        'cpc_codes': set()
                    }
                
                assignee_data[assignee]['citation_count'] += 1
                assignee_data[assignee]['cpc_codes'].update(primary_cpc)
                break
    except:
        pass

print('Assignees found:', len(assignee_data))
for assignee, data in assignee_data.items():
    print(f'{assignee}: {data["citation_count"]} citations, CPC codes: {list(data["cpc_codes"])}')

# Build query for CPC definitions - get unique primary CPC codes
all_primary_cpc = set()
for data in assignee_data.values():
    all_primary_cpc.update(data['cpc_codes'])

print('\\nUnique CPC codes to lookup:', len(all_primary_cpc))
print('Codes:', list(all_primary_cpc))

# Store results for next step
result = {
    'assignee_data': {k: {
        'citation_count': v['citation_count'],
        'cpc_codes': list(v['cpc_codes'])
    } for k, v in assignee_data.items()},
    'all_cpc_codes': list(all_primary_cpc)
}

print('\\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:34': {'total_univ_calif_patents': 169, 'total_extracted_pubs': 114, 'sample_pubs': ['US-2006292670-A1.', 'WO-2020055916-A9.', 'WO-2010045542-A3.', 'WO-2017214343-A1.', 'US-6980295-B2.', 'KR-20160119166-A.', 'CA-3161617-A1.', 'AU-2015364602-B2.', 'IL-274176-A.', 'US-2004115131-A1.']}, 'var_functions.execute_python:36': {'total_univ_calif_patents': 169, 'unique_cited_publications': 1112, 'citations_with_pub_numbers': 1112}, 'var_functions.execute_python:38': {'total_cited_by_univ_calif': 1112, 'total_univ_calif_publications': 114, 'sample_univ_calif_pubs': ['US-11421276-B2.', 'EP-3668487-A4.', 'KR-20050085437-A.', 'US-2020283856-A1.', 'EP-0826155-A4.', 'WO-2021102420-A1.', 'US-2009031436-A1.', 'JP-2009260386-A.', 'US-11014955-B2.', 'PT-2970346-T.']}, 'var_functions.execute_python:42': {'total_patents': 277813, 'univ_calif_patents': 169, 'sample_pubs': ['US-2003112494-A1', 'KR-100228821-B1', 'IL-274176-A', 'US-2020025859-A1', 'US-2021000566-A1', 'US-6750960-B2', 'WO-2024112568-A1', 'AU-2015364602-B2', 'PE-20130764-A1', 'EP-3668487-A4']}, 'var_functions.execute_python:44': {'total_university_california_pubs': 114, 'citing_patents_found': 4, 'sample_citing_patent': {'patent_info': 'The US patent filing (application number US-4007205-A) is assigned to CALIFORNIA INST OF TECHN and has publication number US-2005165588-A1.', 'cites': 'US-6237292-B1', 'cpc': '[\n  {\n    "code": "G01M7/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01M7/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01V1/01",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01V1/01",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}}, 'var_functions.execute_python:46': {'total_citing_patents': 1, 'unique_assignees': 1, 'sample_assignees': ['BLOOM ENERGY CORP and has publication no. US-10615444-B2.'], 'cpc_codes_to_lookup': ['H01M2008/1293', 'H01M2004/8684', 'H01M8/2457', 'H01M8/1253', 'H01M4/8657', 'H01M4/8652', 'Y02E60/525', 'Y02E60/50', 'H01M4/8642', 'H01M4/8663', 'H01M4/861', 'H01M4/9066', 'H01M8/2425', 'H01M4/8885', 'H01M4/9016', 'Y02P70/56', 'Y02P70/50']}, 'var_functions.execute_python:48': {'total_citing_patents': 1, 'unique_assignees': 1, 'assignees': ['BLOOM ENERGY CORP']}, 'var_functions.execute_python:50': {'total_citing_assignees': 3, 'total_cpc_codes_to_lookup': 44, 'assignees': ['CALIFORNIA INST OF TECHN', 'BLOOM ENERGY CORP', 'CRYSTAL IS INC'], 'cpc_codes': ['H01M8/2425', 'Y10T428/21', 'H01M2008/1293', 'H01L29/205', 'H01M4/8652', 'H01L21/02458', 'C30B11/003', 'H01M8/2457', 'H01L33/0075', 'H01M4/9016', 'H01L29/7787', 'H01M4/861', 'H01L29/04', 'H01L29/66462', 'C30B25/16', 'H01M8/1253', 'Y02E60/525', 'C30B25/10', 'H01L29/32', 'H01M4/9066', 'H01M4/8642', 'H01L21/02389', 'H01L33/025', 'H01M4/8657', 'H01M2004/8684', 'H01L29/0657', 'H01L21/02634', 'C30B25/14', 'C30B29/403', 'H01L33/12', 'H01L33/325', 'C30B23/00', 'H01L2924/0002', 'Y02E60/50', 'H01M4/8885', 'H01L21/0254', 'Y02P70/56', 'G01M7/00', 'H01L29/2003', 'H01M4/8663', 'Y02P70/50', 'C30B23/025', 'G01V1/01', 'C30B25/20']}, 'var_functions.query_db:56': [{'symbol': 'C30B', 'titleFull': 'SINGLE-CRYSTAL GROWTH; UNIDIRECTIONAL SOLIDIFICATION OF EUTECTIC MATERIAL OR UNIDIRECTIONAL DEMIXING OF EUTECTOID MATERIAL; REFINING BY ZONE-MELTING OF MATERIAL; PRODUCTION OF A HOMOGENEOUS POLYCRYSTALLINE MATERIAL WITH DEFINED STRUCTURE; SINGLE CRYSTALS OR HOMOGENEOUS POLYCRYSTALLINE MATERIAL WITH DEFINED STRUCTURE; AFTER-TREATMENT OF SINGLE CRYSTALS OR A HOMOGENEOUS POLYCRYSTALLINE MATERIAL WITH DEFINED STRUCTURE; APPARATUS THEREFOR'}, {'symbol': 'G01V', 'titleFull': 'GEOPHYSICS; GRAVITATIONAL MEASUREMENTS; DETECTING MASSES OR OBJECTS; TAGS'}, {'symbol': 'G01M', 'titleFull': 'TESTING STATIC OR DYNAMIC BALANCE OF MACHINES OR STRUCTURES; TESTING OF STRUCTURES OR APPARATUS, NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'H01L', 'titleFull': 'SEMICONDUCTOR DEVICES NOT COVERED BY CLASS H10'}, {'symbol': 'Y02E', 'titleFull': 'REDUCTION OF GREENHOUSE GAS [GHG] EMISSIONS, RELATED TO ENERGY GENERATION, TRANSMISSION OR DISTRIBUTION'}, {'symbol': 'Y02P', 'titleFull': 'CLIMATE CHANGE MITIGATION TECHNOLOGIES IN THE PRODUCTION OR PROCESSING OF GOODS'}, {'symbol': 'Y10T', 'titleFull': 'TECHNICAL SUBJECTS COVERED BY FORMER US CLASSIFICATION'}]}

exec(code, env_args)
