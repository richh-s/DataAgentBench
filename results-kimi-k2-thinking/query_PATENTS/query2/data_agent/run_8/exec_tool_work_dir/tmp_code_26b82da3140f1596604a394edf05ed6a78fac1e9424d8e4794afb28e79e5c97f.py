code = """import json
import pandas as pd
import re
from datetime import datetime

# Load the full results from the query
with open(var_functions.query_db:2, 'r') as f:
    patents_2019 = json.load(f)

print(f"Total patents granted in 2019: {len(patents_2019)}")

# Display first few records to understand structure
for i, record in enumerate(patents_2019[:3]):
    print(f"\nRecord {i+1}:")
    print(f"Patents_info: {record['Patents_info']}")
    print(f"Grant date: {record['grant_date']}")
    print(f"CPC codes: {record['cpc'][:100]}...")

# Let's convert to a DataFrame for easier processing
df = pd.DataFrame(patents_2019)
print(f"\nDataFrame shape: {df.shape}")
print(df.head())

# Output the result as JSON string for confirmation
result = {
    'total_patents_2019': len(patents_2019),
    'sample_records': patents_2019[:3]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
