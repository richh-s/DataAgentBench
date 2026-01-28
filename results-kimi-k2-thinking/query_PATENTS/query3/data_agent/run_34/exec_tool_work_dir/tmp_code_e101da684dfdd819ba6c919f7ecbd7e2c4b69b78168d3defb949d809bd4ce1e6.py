code = """import json
import sqlite3
import pandas as pd

# Read the result file
result_path = locals()['var_functions.query_db:16']
print('Reading from: ' + str(result_path))

with open(result_path, 'r') as f:
    patents_data = json.load(f)

print('Total patents with citations: ' + str(len(patents_data)))

# Process the data to extract citations and CPC codes
citations_list = []
cpc_codes_list = []

for patent in patents_data:
    patents_info = patent['Patents_info']
    
    # Parse citations
    try:
        citations = json.loads(patent['citation'])
    except:
        citations = []
    
    # Parse CPC codes
    try:
        cpc_data = json.loads(patent['cpc'])
        cpc_codes = [cpc['code'] for cpc in cpc_data if 'code' in cpc]
    except:
        cpc_codes = []
    
    citations_list.append({
        'patents_info': patents_info,
        'citations': citations,
        'cpc_codes': cpc_codes
    })

# Collect all publication numbers that need to be checked for assignees
all_pub_numbers = []
for item in citations_list:
    for citation in item['citations']:
        if 'publication_number' in citation and citation['publication_number']:
            all_pub_numbers.append(citation['publication_number'])

print('Total citation publication numbers to check: ' + str(len(set(all_pub_numbers))))

# Show first few records
for i, item in enumerate(citations_list[:2]):
    print('\n' + str(i+1) + '. Patent: ' + item['patents_info'][:80])
    print('   CPC codes: ' + str(item['cpc_codes'][:3]) + '...')
    print('   Citations count: ' + str(len(item['citations'])))
    if item['citations']:
        print('   First citation: ' + str(item['citations'][0].get('publication_number', 'N/A')))

result = {'status': 'processed', 'total_patents': len(citations_list), 'total_citations': len(set(all_pub_numbers))}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': [{'total': '169'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
