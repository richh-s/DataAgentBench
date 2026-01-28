code = """import json
import re

# Load data from the stored file paths
funding_path = locals()['var_functions.query_db:5']
civic_docs_path = locals()['var_functions.query_db:8']

# Read and parse funding data
funding_file = open(funding_path)
funding_records = json.load(funding_file)
funding_file.close()

# Read and parse civic docs data
civic_file = open(civic_docs_path)
civic_docs = json.load(civic_file)
civic_file.close()

# Create summary of loaded data
result_summary = {
    'funding_count': len(funding_records),
    'civic_docs_count': len(civic_docs),
    'sample_funding': funding_records[0],
    'sample_civic_keys': list(civic_docs[0].keys())[:5],
    'sample_text_preview': civic_docs[0]['text'][:300]
}

print('__RESULT__:')
print(json.dumps(result_summary))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
