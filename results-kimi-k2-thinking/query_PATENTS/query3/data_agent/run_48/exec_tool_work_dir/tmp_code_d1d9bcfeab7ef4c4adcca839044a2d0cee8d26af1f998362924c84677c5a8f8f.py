code = """import json
import os

# Get the result file from previous query
result_file_key = 'var_functions.query_db:12'
result_file_path = locals()[result_file_key]

# Read the patents data
with open(result_file_path, 'r') as f:
    patents_data = json.load(f)

# Initialize data structures
citations_list = []
cpc_subclasses = set()

# Process each patent record
for patent in patents_data:
    # Parse citation information
    citation_json = patent.get('citation', '')
    if citation_json and citation_json != '[]':
        try:
            citations = json.loads(citation_json) if isinstance(citation_json, str) else citation_json
            for citation in citations:
                pub_num = citation.get('publication_number', '')
                if pub_num:
                    citations_list.append({
                        'cited_patent_number': pub_num,
                        'california_patent_info': patent.get('Patents_info', '')
                    })
        except:
            continue
    
    # Parse CPC codes
    cpc_json = patent.get('cpc', '')
    if cpc_json and cpc_json != '[]':
        try:
            cpc_list = json.loads(cpc_json) if isinstance(cpc_json, str) else cpc_json
            for cpc_item in cpc_list:
                cpc_code = cpc_item.get('code', '')
                if cpc_code:
                    # Extract primary subclass group
                    main_group = cpc_code.split('/')[0]
                    cpc_subclasses.add(main_group)
        except:
            continue

# Create results summary
result_summary = {
    'total_california_patents': len(patents_data),
    'total_citations_found': len(citations_list),
    'unique_cpc_subclasses': len(cpc_subclasses),
    'sample_cpc_codes': list(cpc_subclasses)[:10],
    'sample_citations': citations_list[:3]
}

# Prepare output directory
output_dir = './analysis_output'
os.makedirs(output_dir, exist_ok=True)

# Save data for next steps
citations_file = os.path.join(output_dir, 'california_citations.json')
with open(citations_file, 'w') as f:
    json.dump(citations_list, f)

cpc_file = os.path.join(output_dir, 'california_cpc_codes.json')
with open(cpc_file, 'w') as f:
    json.dump(list(cpc_subclasses), f)

print('__RESULT__:')
print(json.dumps(result_summary))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
