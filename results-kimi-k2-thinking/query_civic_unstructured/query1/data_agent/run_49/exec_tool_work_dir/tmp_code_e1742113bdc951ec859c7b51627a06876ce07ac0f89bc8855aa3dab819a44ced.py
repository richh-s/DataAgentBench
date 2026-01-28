code = """import json
import re

# Access funding data
funding_key = 'var_functions.query_db:0'
funding_records = locals().get(funding_key, [])

# Debug info
print(f"Number of funding records: {len(funding_records)}")

# Access civic docs data
civic_key = 'var_functions.query_db:2'
civic_docs = locals().get(civic_key, [])

print(f"Number of civic documents: {len(civic_docs)}")

print('__RESULT__:')
print(json.dumps({
    "funding_count": len(funding_records),
    "civic_docs_count": len(civic_docs)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_found': 276, 'sample_projects': ['project_227', 'project_131', 'project_95', 'project_35', 'project_46', 'project_138', 'project_123', 'project_282', 'project_488', 'project_486']}}

exec(code, env_args)
