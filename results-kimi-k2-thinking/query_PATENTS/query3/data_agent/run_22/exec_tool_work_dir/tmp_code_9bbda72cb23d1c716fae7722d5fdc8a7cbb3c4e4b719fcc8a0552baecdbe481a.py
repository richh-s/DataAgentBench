code = """import json

# The citing assignees and their CPC codes from previous analysis
citing_assignees_data = [
    {"assignee": "CAL", "citation_count": 1, "cpc_codes": ["G01V", "G01M"]},
    {"assignee": "BLO", "citation_count": 1, "cpc_codes": ["H01M", "Y02P", "Y02E"]},
    {"assignee": "CRY", "citation_count": 1, "cpc_codes": ["C30B", "H01L", "Y10T"]},
    {"assignee": "SCHOWALTER LEO J", "citation_count": 1, "cpc_codes": ["H01L"]}
]

# CPC titles from the database query
cpc_titles = {
    "G01M": "TESTING STATIC OR DYNAMIC BALANCE OF MACHINES OR STRUCTURES; TESTING OF STRUCTURES OR APPARATUS, NOT OTHERWISE PROVIDED FOR",
    "G01V": "GEOPHYSICS; GRAVITATIONAL MEASUREMENTS; DETECTING MASSES OR OBJECTS; TAGS",
    "H01L": "SEMICONDUCTOR DEVICES NOT COVERED BY CLASS H10",
    "H01M": "PROCESSES OR MEANS, e.g. BATTERIES, FOR THE DIRECT CONVERSION OF CHEMICAL ENERGY INTO ELECTRICAL ENERGY",
    "Y02E": "REDUCTION OF GREENHOUSE GAS [GHG] EMISSIONS, RELATED TO ENERGY GENERATION, TRANSMISSION OR DISTRIBUTION",
    "Y02P": "CLIMATE CHANGE MITIGATION TECHNOLOGIES IN THE PRODUCTION OR PROCESSING OF GOODS",
    "Y10T": "TECHNICAL SUBJECTS COVERED BY FORMER US CLASSIFICATION",
    "C30B": "SINGLE-CRYSTAL GROWTH; UNIDIRECTIONAL SOLIDIFICATION OF EUTECTIC MATERIAL OR UNIDIRECTIONAL DEMIXING OF EUTECTOID MATERIAL"
}

# Create the final formatted result
final_results = []

for data in citing_assignees_data:
    assignee = data["assignee"]
    cpc_codes = data["cpc_codes"]
    
    for cpc_code in cpc_codes:
        title = cpc_titles.get(cpc_code, "Title not found")
        final_results.append({
            "citing_assignee": assignee,
            "cpc_subclass": cpc_code,
            "cpc_subclass_title": title
        })

text_result = "Citing Assignees and CPC Subclass Titles:

"
for result in final_results:
    text_result += f"Assignee: {result['citing_assignee']}\n"
    text_result += f"CPC Subclass: {result['cpc_subclass']}\n"
    text_result += f"Title: {result['cpc_subclass_title']}\n"
    text_result += "-" * 80 + "\n"

print('__RESULT__:')
print(text_result)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:10': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:32': {'total_california_patents': 169, 'total_citing_assignees': 2, 'total_citations': 4, 'citing_assignees': ['T', 'S']}, 'var_functions.execute_python:34': {'total_california_patents': 169, 'total_citing_assignees': 4, 'total_citations': 4, 'citing_assignees': {'CAL': 1, 'BLO': 1, 'CRY': 1, 'SCHOWALTER LEO J': 1}}, 'var_functions.execute_python:36': {'total_california_patents': 169, 'total_california_pub_numbers': 262, 'total_citing_patents': 4, 'unique_citing_assignees': 4, 'assignees_with_citations': {'CAL': {'citation_count': 1, 'cpc_codes': ['G01V1/01', 'G01M7/00']}, 'BLO': {'citation_count': 1, 'cpc_codes': ['H01M2008/1293', 'Y02P70/56', 'H01M4/8657', 'H01M4/861', 'H01M4/9066', 'H01M2004/8684', 'H01M4/9016', 'Y02E60/50', 'H01M8/1253', 'H01M4/8642', 'H01M8/2425', 'H01M4/8885', 'H01M4/8663', 'Y02P70/50', 'H01M8/2457', 'H01M4/8652', 'Y02E60/525']}, 'CRY': {'citation_count': 1, 'cpc_codes': ['H01L21/02458', 'H01L21/02634', 'H01L29/2003', 'H01L29/66462', 'C30B25/16', 'H01L29/32', 'C30B25/20', 'C30B25/14', 'C30B29/403', 'H01L2924/0002', 'H01L29/205', 'H01L21/02389', 'H01L29/0657', 'H01L21/0254', 'C30B23/00', 'C30B11/003', 'C30B23/025', 'Y10T428/21', 'H01L33/325', 'H01L29/04', 'H01L33/025', 'H01L33/12', 'H01L29/7787', 'C30B25/10', 'H01L33/0075']}, 'SCHOWALTER LEO J': {'citation_count': 1, 'cpc_codes': ['H01L21/0262', 'H01L33/12', 'H01L21/02389', 'H01L21/02458', 'H01L21/02433', 'H01L21/0243', 'H01L33/08', 'H01L21/0251', 'H01L21/0254']}}}, 'var_functions.execute_python:38': {'sample_citing_patents': [], 'california_pub_numbers_sample': ['IL-244029-A0', 'US-2017145219-A1', 'US-2023155090-A1', 'WO-2024112568-A1', 'US-2006292670-A1', 'HK-1250569-A1', 'CN-103189548-A', 'US-2018243924-A1', 'ID-23426-A', 'US-2021101879-A1']}, 'var_functions.execute_python:40': {'total_patents': 277813}, 'var_functions.execute_python:42': {'california_patents': 169, 'california_pub_numbers': 225, 'citing_patents': 4}, 'var_functions.execute_python:44': {'total_citing_assignees': 4, 'total_citations': 4, 'citing_assignees': [{'assignee': 'CAL', 'citation_count': 1, 'cpc_codes': ['G01V', 'G01M']}, {'assignee': 'BLO', 'citation_count': 1, 'cpc_codes': ['H01M', 'Y02P', 'Y02E']}, {'assignee': 'CRY', 'citation_count': 1, 'cpc_codes': ['Y10T', 'H01L', 'C30B']}, {'assignee': 'SCHOWALTER LEO J', 'citation_count': 1, 'cpc_codes': ['H01L']}]}, 'var_functions.execute_python:46': {'citing_assignees': [{'assignee': 'CAL', 'citation_count': 1, 'cpc_codes': ['G01V', 'G01M']}, {'assignee': 'BLO', 'citation_count': 1, 'cpc_codes': ['Y02P', 'H01M', 'Y02E']}, {'assignee': 'CRY', 'citation_count': 1, 'cpc_codes': ['C30B', 'H01L', 'Y10T']}, {'assignee': 'SCHOWALTER LEO J', 'citation_count': 1, 'cpc_codes': ['H01L']}], 'cpc_subclasses_to_lookup': ['G01M', 'G01V', 'C30B', 'Y10T', 'H01M', 'Y02P', 'H01L', 'Y02E']}, 'var_functions.execute_python:48': {'california_pub_numbers_sample': ['US-10744347-B2', 'US-202016780659-A', 'CA-3225295-A1', 'US-201715625819-A', 'US-11248107-B2', 'PE-20130764-A1', 'US-2010025717-A1', 'US-2023024482-W', 'WO-2018026404-A3', 'AU-2003247814-A', 'KR-20200084864-A', 'AU-2007297661-A', 'CA-2718348-C', 'US-3666017D-A', 'KR-20087016723-A'], 'citing_patents_found': 4, 'sample_citing_patents': ['The US patent filing (application number US-4007205-A) is assigned to CALIFORNIA INST OF TECHN and has publication number US-2005165588-A1.', 'The US patent application (no. US-201715785968-A) is held by BLOOM ENERGY CORP and has publication no. US-10615444-B2.', 'The US application (ID US-201414520615-A) is owned by CRYSTAL IS INC and has publication no. US-9447521-B2.', 'SCHOWALTER LEO J holds the US application (number US-2000608-A), with publication number US-9437430-B2.']}, 'var_functions.query_db:52': [{'symbol': 'G01M', 'titleFull': 'TESTING STATIC OR DYNAMIC BALANCE OF MACHINES OR STRUCTURES; TESTING OF STRUCTURES OR APPARATUS, NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'H01L', 'titleFull': 'SEMICONDUCTOR DEVICES NOT COVERED BY CLASS H10'}, {'symbol': 'H01M', 'titleFull': 'PROCESSES OR MEANS, e.g. BATTERIES, FOR THE DIRECT CONVERSION OF CHEMICAL ENERGY INTO ELECTRICAL ENERGY'}, {'symbol': 'Y02E', 'titleFull': 'REDUCTION OF GREENHOUSE GAS [GHG] EMISSIONS, RELATED TO ENERGY GENERATION, TRANSMISSION OR DISTRIBUTION'}, {'symbol': 'Y02P', 'titleFull': 'CLIMATE CHANGE MITIGATION TECHNOLOGIES IN THE PRODUCTION OR PROCESSING OF GOODS'}, {'symbol': 'Y10T', 'titleFull': 'TECHNICAL SUBJECTS COVERED BY FORMER US CLASSIFICATION'}, {'symbol': 'C30B', 'titleFull': 'SINGLE-CRYSTAL GROWTH; UNIDIRECTIONAL SOLIDIFICATION OF EUTECTIC MATERIAL OR UNIDIRECTIONAL DEMIXING OF EUTECTOID MATERIAL; REFINING BY ZONE-MELTING OF MATERIAL; PRODUCTION OF A HOMOGENEOUS POLYCRYSTALLINE MATERIAL WITH DEFINED STRUCTURE; SINGLE CRYSTALS OR HOMOGENEOUS POLYCRYSTALLINE MATERIAL WITH DEFINED STRUCTURE; AFTER-TREATMENT OF SINGLE CRYSTALS OR A HOMOGENEOUS POLYCRYSTALLINE MATERIAL WITH DEFINED STRUCTURE; APPARATUS THEREFOR'}, {'symbol': 'G01V', 'titleFull': 'GEOPHYSICS; GRAVITATIONAL MEASUREMENTS; DETECTING MASSES OR OBJECTS; TAGS'}]}

exec(code, env_args)
