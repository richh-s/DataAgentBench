code = """import json
import pandas as pd
import re

# Load the data from the previous query
data_file = locals()['var_functions.query_db:0']
with open(data_file, 'r') as f:
    all_patents = json.load(f)

print(f"Total patents in raw data: {len(all_patents)}")
print("\nFirst few entries:")
for i, patent in enumerate(all_patents[:3]):
    print(f"\n{i+1}. Patents_info: {patent['Patents_info']}")
    print(f"   Grant_date: {patent['grant_date']}")
    print(f"   CPC: {patent['cpc'][:100]}...")

# Let's look for patterns to identify German patents
print("\n\nLooking for German patent patterns...")
german_patterns = []
for patent in all_patents[:20]:
    patents_info = patent['Patents_info']
    if 'from DE' in patents_info or 'Germany' in patents_info:
        german_patterns.append(patent)

print(f"Found {len(german_patterns)} potential German patents in first 20 entries")
for i, patent in enumerate(german_patterns[:5]):
    print(f"\n{i+1}. {patent['Patents_info']}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
