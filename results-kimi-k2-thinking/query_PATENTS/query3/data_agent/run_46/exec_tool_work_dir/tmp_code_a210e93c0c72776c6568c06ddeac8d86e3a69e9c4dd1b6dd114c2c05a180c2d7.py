code = """import json
import re

# Get UNIV CALIFORNIA patents and their citations
file_path = var_functions.query_db:18
with open(file_path, 'r') as f:
    uc_publications = json.load(f)

print('Total UNIV CALIFORNIA patents:', len(uc_publications))

# Extract publication numbers and their citations
uc_patents = {}
citation_numbers = set()

for pub in uc_publications:
    patents_info = pub.get('Patents_info', '')
    
    # Extract publication number
    pub_num_match = re.search(r'(US|WO|EP|JP|CN|TW|KR|DE|GB|FR)-[A-Z0-9-]+-A[0-9]*', patents_info)
    if pub_num_match:
        pub_num = pub_num_match.group(0)
        
        # Extract citations
        citations = json.loads(pub.get('citation', '[]'))
        citation_pubs = []
        for citation in citations:
            citation_pub = citation.get('publication_number', '')
            if citation_pub:
                citation_pubs.append(citation_pub)
                citation_numbers.add(citation_pub)
        
        uc_patents[pub_num] = {
            'patents_info': patents_info,
            'citations': citation_pubs,
            'cpc': json.loads(pub.get('cpc', '[]'))
        }

print('UC Patents extracted:', len(uc_patents))
print('Unique cited patents:', len(citation_numbers))

# Show some examples
sample_patent = list(uc_patents.keys())[0] if uc_patents else None
if sample_patent:
    print('\nSample UC patent:', sample_patent)
    print('Citations:', uc_patents[sample_patent]['citations'][:5])

print('__RESULT__:')
print(json.dumps({
    'uc_patent_count': len(uc_patents), 
    'unique_citations': len(citation_numbers),
    'sample_patent': sample_patent,
    'sample_citations': uc_patents[sample_patent]['citations'][:5] if sample_patent else []
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:10': 'test', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'uc_patent_count': 3}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
