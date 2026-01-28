code = """import json
import pandas as pd

# Load the full dataset
with open('/tmp/tmp0q5j9s0s.json', 'r') as f:
    full_data = json.load(f)

# Load the UNIV CALIFORNIA subset
with open('/tmp/tmpk2i1u7_p.json', 'r') as f:
    uc_data = json.load(f)

print(f"Total records in full dataset: {len(full_data)}")
print(f"Records with UNIV CALIFORNIA: {len(uc_data)}")

# Let's examine the structure of Patents_info and citation fields
print("\nSample Patents_info from UC data:")
print(uc_data[0]['Patents_info'])

print("\nSample citation from UC data:")
print(uc_data[0]['citation'][:500] + "..." if len(uc_data[0]['citation']) > 500 else uc_data[0]['citation'])

# Let's also check if there's CPC data
print("\nSample CPC data:")
print(uc_data[0].get('cpc', 'No CPC field')[:500] if isinstance(uc_data[0].get('cpc'), str) else uc_data[0].get('cpc', 'No CPC field'))

print('__RESULT__:')
print(json.dumps({
    "full_count": len(full_data),
    "uc_count": len(uc_data),
    "sample_structure": "examined"
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
