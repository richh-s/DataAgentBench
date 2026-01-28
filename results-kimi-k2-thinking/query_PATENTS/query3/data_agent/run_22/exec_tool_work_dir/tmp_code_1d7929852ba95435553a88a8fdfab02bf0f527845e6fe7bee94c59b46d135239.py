code = """import json
import re

# Load all patents data
file_path = var_functions.query_db:18

with open(file_path, 'r', encoding='utf-8') as f:
    all_patents = json.load(f)

# Find UNIV CALIFORNIA patents
california_patents = []
for patent in all_patents:
    if 'UNIV CALIFORNIA' in patent['Patents_info']:
        california_patents.append(patent)

# Extract publication numbers
california_pub_numbers = set()
for patent in california_patents:
    patents_info = patent['Patents_info']
    # Extract pub number using regex
    pattern = r'(US|WO|EP|JP|CN|TW|DE|GB|FR|KR|CA)-([A-Z0-9-]+)'
    matches = re.findall(pattern, patents_info)
    for match in matches:
        pub_num = match[0] + '-' + match[1]
        california_pub_numbers.add(pub_num)

# Count citations that cite UNIV CALIFORNIA patents
citations_count = 0
citing_assignees = set()

california_citations = []
for patent in all_patents:
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
                        citations_count += 1
                        # Extract assignee
                        assignee_match = re.search(r'^([^,]+?)(?: holds| holds the| is| assigned| belonging to| owned by)?', patent['Patents_info'])
                        if assignee_match:
                            assignee = assignee_match.group(1).strip()
                            if assignee != 'UNIV CALIFORNIA':
                                citing_assignees.add(assignee)
                        california_citations.append({
                            'citing_patent': patent['Patents_info'],
                            'cited_california_patent': pub_num,
                            'citation': citation
                        })
                        break
        except:
            pass

result = {
    'total_california_patents': len(california_patents),
    'total_citations_from_other_assignees': citations_count,
    'unique_citing_assignees': len(citing_assignees),
    'california_pub_numbers_count': len(california_pub_numbers),
    'citing_assignees_list': list(citing_assignees)[:20]  # First 20 for preview
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:10': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
