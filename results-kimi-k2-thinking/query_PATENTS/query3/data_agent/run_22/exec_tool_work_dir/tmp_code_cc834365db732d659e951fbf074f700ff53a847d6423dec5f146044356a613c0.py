code = """import json
import re

# Load all patents data
file_path = var_functions.query_db:18

with open(file_path, 'r', encoding='utf-8') as f:
    all_patents = json.load(f)

# Find UNIV CALIFORNIA patents and extract their publication numbers
univ_california_patents = []
univ_california_pub_numbers = set()

for patent in all_patents:
    patents_info = patent['Patents_info']
    if 'UNIV CALIFORNIA' in patents_info:
        univ_california_patents.append(patent)
        # Extract publication number
        match = re.search(r'(US|WO|EP|JP|CN|TW|DE|GB|FR|KR|CA|AU|IN|BR|MX|RU|IT|ES|NL|SE|DK|NO|FI|BE|AT|CH|IE|PT|NZ|PL|CZ|HU|TR|GR|IL|ZA|SG|MY|TH|PH|ID|VN|AR|CL|CO|PE|EC|UY|VE|BO|PY|HN|SV|GT|CR|PA|DO|NI|PR|KW|SA|AE|BH|OM|QA|JO|LB|EG|MA|TN|DZ|LY|SD|ET|KE|TZ|UG|RW|BI|DJ|ER|SO|YE|IR|IQ|AF|BD|BT|MV|LK|NP|PHTW)-([A-Z0-9-]+)', patents_info)
        if match:
            pub_num = match.group(1) + '-' + match.group(2)
            univ_california_pub_numbers.add(pub_num)

# Find patents that cite UNIV CALIFORNIA patents
citing_patents = []
for patent in all_patents:
    patents_info = patent['Patents_info']
    # Skip UNIV CALIFORNIA patents themselves
    if 'UNIV CALIFORNIA' in patents_info:
        continue
        
    citation_data = patent.get('citation', '[]')
    if citation_data and citation_data != '[]':
        try:
            citations = json.loads(citation_data)
            if isinstance(citations, list):
                for citation in citations:
                    pub_num = citation.get('publication_number', '')
                    if pub_num and pub_num in univ_california_pub_numbers:
                        citing_patents.append(patent)
                        break
        except:
            continue

print(f'Found {len(citing_patents)} patents that cite UNIV CALIFORNIA patents')
print(f'UNIV CALIFORNIA publication numbers: {len(univ_california_pub_numbers)}')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:10': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
