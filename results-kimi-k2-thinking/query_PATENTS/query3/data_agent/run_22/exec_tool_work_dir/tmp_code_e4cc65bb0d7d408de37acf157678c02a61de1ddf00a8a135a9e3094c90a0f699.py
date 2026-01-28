code = """import json
import re

# Load all patents data
file_path = locals()['var_functions.query_db:18']

with open(file_path, 'r', encoding='utf-8') as f:
    all_patents = json.load(f)

# Find UNIV CALIFORNIA patents
california_patents = []
for patent in all_patents:
    if 'UNIV CALIFORNIA' in patent['Patents_info']:
        california_patents.append(patent)

# Extract publication numbers from UNIV CALIFORNIA patents using regex
california_pub_numbers = set()
for patent in california_patents:
    patents_info = patent['Patents_info']
    # Look for patterns like US-2022074631-A1, TW-201925402-A, etc.
    pattern = r'(US|WO|EP|JP|CN|TW|DE|GB|FR|KR|CA|AU|IN|BR|MX|RU|IT|ES|NL|SE|DK|NO|FI|BE|AT|CH|IE|PT|NZ|PL|CZ|HU|TR|GR|IL|ZA|SG|MY|TH|PH|ID|VN|AR|CL|CO|PE|EC|UY|VE|BO|PY|HN|SV|GT|CR|PA|DO|NI|PR|KW|SA|AE|BH|OM|QA|JO|LB|EG|MA|TN|DZ|LY|SD|ET|KE|TZ|UG|RW|BI|DJ|ER|SO|YE|IR|IQ|AF|BD|BT|MV|LK|NP|PH|TW)-([A-Z0-9-]+)'
    matches = re.findall(pattern, patents_info)
    for match in matches:
        pub_num = match[0] + '-' + match[1]
        california_pub_numbers.add(pub_num)

# Find patents from other assignees that cite UNIV CALIFORNIA patents
citing_assignees = {}

for patent in all_patents:
    patents_info = patent['Patents_info']
    # Skip UNIV CALIFORNIA patents
    if 'UNIV CALIFORNIA' in patents_info:
        continue
    
    citation_data = patent.get('citation', '[]')
    if citation_data and citation_data != '[]':
        try:
            citations = json.loads(citation_data)
            if isinstance(citations, list):
                for citation in citations:
                    pub_num = citation.get('publication_number', '')
                    if pub_num and pub_num in california_pub_numbers:
                        # Extract assignee name
                        assignee_match = re.match(r'^([^,]+?)(?: holds| holds the| is| assigned| belonging to| owned by)?', patents_info)
                        if assignee_match:
                            assignee = assignee_match.group(1).strip()
                            if assignee != 'UNIV CALIFORNIA' and not assignee.startswith('In US, the application'):
                                if assignee not in citing_assignees:
                                    citing_assignees[assignee] = []
                                citing_assignees[assignee].append({
                                    'cited_patent': pub_num,
                                    'citing_patent_info': patents_info
                                })
                        break
        except:
            pass

result = {
    'total_california_patents': len(california_patents),
    'total_citing_assignees': len(citing_assignees),
    'total_citations': sum(len(citations) for citations in citing_assignees.values()),
    'citing_assignees': list(citing_assignees.keys())
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:10': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
