code = """import json
import pandas as pd
import re

# Load funding data
with open('/tmp/tmp8opjs8_m.json', 'r') as f:
    funding_data = json.load(f)

# Load civic documents data
with open('/tmp/tmpg5k2n9mq.json', 'r') as f:
    civic_docs_data = json.load(f)

# Convert funding data to DataFrame
funding_df = pd.DataFrame(funding_data)
print(f"Total funding records: {len(funding_df)}")

# Sample of funding data
print("\nSample funding data:")
print(funding_df.head())

# Sample of civic docs
print(f"\nTotal civic documents: {len(civic_docs_data)}")
print("\nSample civic doc:")
print(json.dumps(civic_docs_data[0], indent=2)[:2000] + "...")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
