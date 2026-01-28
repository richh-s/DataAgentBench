code = """import json
import re

# Load all patents data
file_path = locals()['var_functions.query_db:18']

with open(file_path, 'r', encoding='utf-8') as f:
    all_patents = json.load(f)

# Find a few patents that cite UNIV CALIFORNIA to see the format
sample_citing_patents = []

# Find UNIV CALIFORNIA publication numbers first
california_pub_numbers = set()
for patent in all_patents:
    if 'UNIV CALIFORNIA' in patent['Patents_info']:
        # Extract publication numbers
        patterns = [r'pub\.?\s*(?:number|no\.)?\s*([A-Z]{2}-[A-Z0-9-]+)']
        for pattern in patterns:
            matches = re.findall(pattern, patent['Patents_info'], re.IGNORECASE)
            for match in matches:
                california_pub_numbers.add(match)

# Find citing patents
for patent in all_patents[:2000]:  # Check first 2000 patents
    if 'UNIV CALIFORNIA' in patent['Patents_info']:
        continue
    
    citation_data = patent.get('citation', '[]')
    if citation_data and citation_data != '[]':
        try:
            citations = json.loads(citation_data)
            if isinstance(citations, list):
                for citation in citations:
                    pub_num = citation.get('publication_number', '')
                    if pub_num and pub_num in california_pub_numbers:
                        sample_citing_patents.append(patent['Patents_info'])
                        if len(sample_citing_patents) >= 3:
                            break
        except:
            pass
    if len(sample_citing_patents) >= 3:
        break

result = {
    'sample_citing_patents': sample_citing_patents,
    'california_pub_numbers_sample': list(california_pub_numbers)[:10]
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:10': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:32': {'total_california_patents': 169, 'total_citing_assignees': 2, 'total_citations': 4, 'citing_assignees': ['T', 'S']}, 'var_functions.execute_python:34': {'total_california_patents': 169, 'total_citing_assignees': 4, 'total_citations': 4, 'citing_assignees': {'CAL': 1, 'BLO': 1, 'CRY': 1, 'SCHOWALTER LEO J': 1}}, 'var_functions.execute_python:36': {'total_california_patents': 169, 'total_california_pub_numbers': 262, 'total_citing_patents': 4, 'unique_citing_assignees': 4, 'assignees_with_citations': {'CAL': {'citation_count': 1, 'cpc_codes': ['G01V1/01', 'G01M7/00']}, 'BLO': {'citation_count': 1, 'cpc_codes': ['H01M2008/1293', 'Y02P70/56', 'H01M4/8657', 'H01M4/861', 'H01M4/9066', 'H01M2004/8684', 'H01M4/9016', 'Y02E60/50', 'H01M8/1253', 'H01M4/8642', 'H01M8/2425', 'H01M4/8885', 'H01M4/8663', 'Y02P70/50', 'H01M8/2457', 'H01M4/8652', 'Y02E60/525']}, 'CRY': {'citation_count': 1, 'cpc_codes': ['H01L21/02458', 'H01L21/02634', 'H01L29/2003', 'H01L29/66462', 'C30B25/16', 'H01L29/32', 'C30B25/20', 'C30B25/14', 'C30B29/403', 'H01L2924/0002', 'H01L29/205', 'H01L21/02389', 'H01L29/0657', 'H01L21/0254', 'C30B23/00', 'C30B11/003', 'C30B23/025', 'Y10T428/21', 'H01L33/325', 'H01L29/04', 'H01L33/025', 'H01L33/12', 'H01L29/7787', 'C30B25/10', 'H01L33/0075']}, 'SCHOWALTER LEO J': {'citation_count': 1, 'cpc_codes': ['H01L21/0262', 'H01L33/12', 'H01L21/02389', 'H01L21/02458', 'H01L21/02433', 'H01L21/0243', 'H01L33/08', 'H01L21/0251', 'H01L21/0254']}}}}

exec(code, env_args)
