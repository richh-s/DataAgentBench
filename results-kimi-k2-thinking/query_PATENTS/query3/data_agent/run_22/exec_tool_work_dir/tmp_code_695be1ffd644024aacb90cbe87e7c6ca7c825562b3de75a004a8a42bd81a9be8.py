code = """import json
import re

# Load all patents data
file_path = locals()['var_functions.query_db:18']

with open(file_path, 'r', encoding='utf-8') as f:
    all_patents = json.load(f)

# Find UNIV CALIFORNIA patents and extract their publication numbers
california_patents = []
california_pub_numbers = set()

for patent in all_patents:
    patents_info = patent['Patents_info']
    if 'UNIV CALIFORNIA' in patents_info:
        california_patents.append(patent)
        # Extract publication number from patents_info
        pattern = r'(US|WO|EP|JP|CN|TW|DE|GB|FR|KR|CA|AU)-([A-Z0-9-]+)'
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
                        # Extract assignee name more carefully
                        # Look for patterns like "COMPANY NAME holds", "is owned by COMPANY", etc.
                        assignee = ''
                        
                        # Try various patterns
                        patterns = [
                            r'^([A-Z][A-Z\s&\.-]+?[A-Z])\s+(?:holds|holds the|is|assigned|belonging to|owned by)',
                            r'(?:is owned by|is assigned to|belongs to|held by)\s+([A-Z][A-Z\s&\.-]+?[A-Z])',
                            r'^([A-Z][A-Z\s&\.-]+?[A-Z])\b'
                        ]
                        
                        for pattern in patterns:
                            match = re.search(pattern, patents_info, re.IGNORECASE)
                            if match:
                                assignee = match.group(1).strip()
                                # Clean up the assignee name
                                assignee = re.sub(r'\s+(?:holds|holds the|is|assigned|belonging to|owned by)\b.*', '', assignee, flags=re.IGNORECASE)
                                assignee = assignee.strip()
                                break
                        
                        if assignee and assignee != 'UNIV CALIFORNIA' and len(assignee) > 2:
                            if assignee not in citing_assignees:
                                citing_assignees[assignee] = 0
                            citing_assignees[assignee] += 1
                        break
        except:
            pass

# Sort by number of citations
citing_assignees_sorted = dict(sorted(citing_assignees.items(), key=lambda x: x[1], reverse=True))

result = {
    'total_california_patents': len(california_patents),
    'total_citing_assignees': len(citing_assignees_sorted),
    'total_citations': sum(citing_assignees_sorted.values()),
    'citing_assignees': citing_assignees_sorted
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:10': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:32': {'total_california_patents': 169, 'total_citing_assignees': 2, 'total_citations': 4, 'citing_assignees': ['T', 'S']}}

exec(code, env_args)
