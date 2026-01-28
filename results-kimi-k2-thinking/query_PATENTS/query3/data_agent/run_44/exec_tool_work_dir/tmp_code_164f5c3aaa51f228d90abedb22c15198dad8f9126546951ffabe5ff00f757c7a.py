code = """import json
import pandas as pd

# Read the results from the previous query
uni_california_patents = locals().get('var_functions.query_db:5', '')

# Print a debug message
print(f"uni_california_patents type: {type(uni_california_patents)}")
print(f"uni_california_patents length: {len(str(uni_california_patents))}")

# Since the result is a string, parse it
if isinstance(uni_california_patents, str) and uni_california_patents.endswith('.json'):
    with open(uni_california_patents, 'r') as f:
        data = json.load(f)
else:
    data = uni_california_patents

# Extract first few records to inspect
if isinstance(data, list):
    print(f"Number of UNIV CALIFORNIA patents: {len(data)}")
    for i, record in enumerate(data[:3]):
        print(f"\nRecord {i}:")
        for key, value in record.items():
            print(f"  {key}: {str(value)[:200]}...")
else:
    print(f"Unexpected data type: {type(data)}")
    print(str(data)[:500])

# Extract basic info
if isinstance(data, list):
    patents_with_citations = []
    for record in data:
        patent_info = record.get('Patents_info', '')
        citations = record.get('citation', '[]')
        
        # Parse citations
        try:
            citation_list = json.loads(citations.replace('""', '"null"')) if citations else []
        except:
            citation_list = []
        
        patents_with_citations.append({
            'patent_info': patent_info,
            'citation_count': len(citation_list),
            'citations': citation_list
        })
    
    df = pd.DataFrame(patents_with_citations)
    print(f"\nTotal UNIV CALIFORNIA patents: {len(df)}")
    print(f"Patents with citations: {len(df[df['citation_count'] > 0])}")

# Save the actual JSON data for the next step
import os
result_file = '/tmp/uc_patents.json'
if isinstance(data, list):
    with open(result_file, 'w') as f:
        json.dump(data, f)

__RESULT__:
json.dumps(result_file)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
