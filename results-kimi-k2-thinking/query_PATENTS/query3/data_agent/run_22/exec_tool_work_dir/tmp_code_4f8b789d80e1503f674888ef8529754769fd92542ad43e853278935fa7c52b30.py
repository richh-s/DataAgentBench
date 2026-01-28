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
        # Extract publication number - look for pub number patterns
        patterns = [
            r'pub\.?\s*(?:number|no\.)?\s*([A-Z]{2}-[A-Z0-9-]+)',
            r'publication\s*(?:number|no\.)?\s*([A-Z]{2}-[A-Z0-9-]+)',
            r'([A-Z]{2}-[0-9]{6,10}-[A-Z][0-9]?)'  # General pattern
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, patents_info, re.IGNORECASE)
            for match in matches:
                if isinstance(match, tuple):
                    pub_num = match[0]
                else:
                    pub_num = match
                california_pub_numbers.add(pub_num)

# Find patents that cite UNIV CALIFORNIA patents and collect CPC codes
citing_data = []

for patent in all_patents:
    patents_info = patent['Patents_info']
    
    # Skip UNIV CALIFORNIA patents
    if 'UNIV CALIFORNIA' in patents_info:
        continue
    
    citation_data = patent.get('citation', '[]')
    cpc_data = patent.get('cpc', '[]')
    
    # Check if this patent cites any UNIV CALIFORNIA patent
    cited_california_patents = []
    if citation_data and citation_data != '[]':
        try:
            citations = json.loads(citation_data)
            if isinstance(citations, list):
                for citation in citations:
                    pub_num = citation.get('publication_number', '')
                    if pub_num and pub_num in california_pub_numbers:
                        cited_california_patents.append(pub_num)
        except:
            pass
    
    if cited_california_patents:
        # Extract assignee name - look for the first entity mentioned
        assignee = ''
        
        # Pattern 1: "COMPANY NAME holds the..."
        match = re.match(r'^([A-Z][A-Z0-9\s&\.,\-]+?[A-Z0-9])\s+(?:holds|holds the|is|assigned|belonging to|owned by|assigned to|patent filing)', patents_info)
        if match:
            assignee = match.group(1).strip()
        else:
            # Pattern 2: "In US, the patent... is owned by COMPANY"
            match = re.search(r'(?:is owned by|is assigned to|belongs to|held by|assigned to)\s+([A-Z][A-Z0-9\s&\.,\-]+?[A-Z0-9])', patents_info)
            if match:
                assignee = match.group(1).strip()
            else:
                # Pattern 3: "Patent filing... from US, belonging to COMPANY"
                match = re.search(r'(?:patent filing|application|patent application)[^,]+?(?:held by|assigned to|belonging to|owned by)\s+([A-Z][A-Z0-9\s&\.,\-]+?[A-Z0-9])', patents_info, re.IGNORECASE)
                if match:
                    assignee = match.group(1).strip()
        
        # Clean assignee name
        if assignee:
            assignee = re.sub(r'\s+(?:holds|holds the|is|assigned|belonging to|owned by|assigned to|patent filing|the patent|application|from US,).*', '', assignee, flags=re.IGNORECASE)
            assignee = assignee.strip()
        
        # Extract CPC codes
        cpc_codes = []
        if cpc_data and cpc_data != '[]':
            try:
                cpc_entries = json.loads(cpc_data)
                if isinstance(cpc_entries, list):
                    for entry in cpc_entries:
                        code = entry.get('code', '')
                        if code:
                            cpc_codes.append(code)
            except:
                pass
        
        citing_data.append({
            'assignee': assignee,
            'cited_california_patents': cited_california_patents,
            'cpc_codes': list(set(cpc_codes)),  # Remove duplicates
            'patent_info': patents_info[:200] + '...' if len(patents_info) > 200 else patents_info
        })

# Process and count unique assignees
assignee_citations = {}
for data in citing_data:
    assignee = data['assignee']
    if assignee and assignee != 'UNIV CALIFORNIA':
        if assignee not in assignee_citations:
            assignee_citations[assignee] = {
                'citation_count': 0,
                'cpc_codes': set()
            }
        assignee_citations[assignee]['citation_count'] += len(data['cited_california_patents'])
        assignee_citations[assignee]['cpc_codes'].update(data['cpc_codes'])

# Convert sets to lists for JSON serialization
for assignee in assignee_citations:
    assignee_citations[assignee]['cpc_codes'] = list(assignee_citations[assignee]['cpc_codes'])

result = {
    'total_california_patents': len(california_patents),
    'total_california_pub_numbers': len(california_pub_numbers),
    'total_citing_patents': len(citing_data),
    'unique_citing_assignees': len(assignee_citations),
    'assignees_with_citations': assignee_citations
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:10': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:32': {'total_california_patents': 169, 'total_citing_assignees': 2, 'total_citations': 4, 'citing_assignees': ['T', 'S']}, 'var_functions.execute_python:34': {'total_california_patents': 169, 'total_citing_assignees': 4, 'total_citations': 4, 'citing_assignees': {'CAL': 1, 'BLO': 1, 'CRY': 1, 'SCHOWALTER LEO J': 1}}}

exec(code, env_args)
