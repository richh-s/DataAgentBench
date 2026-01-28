code = """import json
import pandas as pd

# The result file path from the query
result_file = var_functions.query_db:12

# Read and parse the JSON data
with open(result_file, 'r') as f:
    patents_data = json.load(f)

print(f'Total UNIV CALIFORNIA patents found: {len(patents_data)}')

# Initialize data collector
citations_data = []
cpc_codes = set()

# Process each patent record
for patent in patents_data:
    try:
        # Parse patent info to extract publication/application numbers
        patent_info_str = patent['Patents_info']
        
        # Parse citation JSON
        citation_json = patent['citation']
        if citation_json and citation_json != '[]' and citation_json != '':
            try:
                if isinstance(citation_json, str):
                    citations = json.loads(citation_json)
                else:
                    citations = citation_json
                    
                for citation in citations:
                    pub_num = citation.get('publication_number', '')
                    if pub_num:
                        citations_data.append({
                            'california_patent_info': patent_info_str,
                            'cited_patent_number': pub_num
                        })
            except json.JSONDecodeError:
                pass
        
        # Parse CPC codes
        cpc_json = patent['cpc']
        if cpc_json and cpc_json != '[]' and cpc_json != '':
            try:
                if isinstance(cpc_json, str):
                    cpc_list = json.loads(cpc_json)
                else:
                    cpc_list = cpc_json
                    
                for cpc_item in cpc_list:
                    cpc_code = cpc_item.get('code', '')
                    if cpc_code:
                        # Extract primary subclass (format: Section/Class/Subclass)
                        parts = cpc_code.split('/')
                        if len(parts) >= 2:
                            # Get the subclass group (before first slash, then take first 4 chars for subclass)
                            subclass = cpc_code.split('/')[0][:4]
                            cpc_codes.add(subclass)
            except json.JSONDecodeError:
                pass
    except Exception as e:
        continue

print(f'Source patents: {len(patent)}')
print(f'Citations found: {len(citations_data)}')
print(f'Unique CPC subclasses: {len(cpc_codes)}')
print(f'First few CPC codes: {list(cpc_codes)[:10]}')

# Save filtered data for next steps
import os
output_dir = './query_results'
os.makedirs(output_dir, exist_ok=True)

# Save citations data
citations_file = os.path.join(output_dir, 'california_citations.json')
with open(citations_file, 'w') as f:
    json.dump(citations_data, f)

# Save CPC codes
cpc_file = os.path.join(output_dir, 'california_cpc_codes.json')
with open(cpc_file, 'w') as f:
    json.dump(list(cpc_codes), f)

print('Data saved to query_results/')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
