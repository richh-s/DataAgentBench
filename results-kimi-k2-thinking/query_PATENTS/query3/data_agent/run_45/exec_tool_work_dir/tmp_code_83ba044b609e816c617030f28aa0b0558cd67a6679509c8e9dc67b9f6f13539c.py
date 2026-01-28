code = """import json
import re

# Get UNIV CALIFORNIA patents from storage
uc_patents = var_functions.query_db:8

# Extract publication numbers
uc_pub_numbers = set()
for patent in uc_patents:
    info = patent['Patents_info']
    # Find publication number pattern
    match = re.search(r'pub\. number ([A-Z0-9-]+)', info)
    if match:
        pub_num = match.group(1)
        uc_pub_numbers.add(pub_num)

print(f'Total UNIV CALIFORNIA patents: {len(uc_patents)}')
print(f'Extracted publication numbers: {len(uc_pub_numbers)}')
print(f'Sample: {list(uc_pub_numbers)[:5]}')

# Now let's examine the citation structure to understand how to search
# Get sample patents to see how citations are stored
sample_patents = var_functions.query_db:22

print(f'\nSample patents to examine: {len(sample_patents)}')

# Check if any of these sample patents cite UNIV CALIFORNIA patents
citing_patents_sample = []
for patent in sample_patents:
    citation_data = patent.get('citation', '[]')
    if citation_data and citation_data != '[]':
        try:
            citations = json.loads(citation_data)
            for cite in citations:
                if cite.get('publication_number') in uc_pub_numbers:
                    citing_patents_sample.append({
                        'Patents_info': patent['Patents_info'],
                        'cites': cite['publication_number']
                    })
        except:
            pass

print(f'Found {len(citing_patents_sample)} sample patents citing UC')

print('__RESULT__:')
print(json.dumps({
    'uc_patents_count': len(uc_patents),
    'uc_pub_numbers_count': len(uc_pub_numbers),
    'citing_sample_count': len(citing_patents_sample),
    'sample_citations': citing_patents_sample[:3] if citing_patents_sample else 'None'
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'B', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING'}, {'symbol': 'C', 'titleFull': 'CHEMISTRY; METALLURGY'}]}

exec(code, env_args)
