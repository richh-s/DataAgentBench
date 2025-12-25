code = """import json
import re
import pandas as pd

# Load previous extracted data if possible? No, variables are local to the execution block unless printed.
# I have to reload.

with open(locals()['var_function-call-2797324583492744393'], 'r') as f:
    filings_data = json.load(f)

def extract_year(date_str):
    if not date_str:
        return None
    match = re.search(r'\b(19|20)\d{2}\b', str(date_str))
    if match:
        return int(match.group(0))
    return None

years = []
for entry in filings_data:
    y = extract_year(entry.get('filing_date'))
    if y:
        years.append(y)

df = pd.DataFrame(years, columns=['year'])
print("Year distribution:")
print(df['year'].value_counts().sort_index().tail(10))"""

env_args = {'var_function-call-11252670295542494115': 'file_storage/function-call-11252670295542494115.json', 'var_function-call-11252670295542493418': 'file_storage/function-call-11252670295542493418.json', 'var_function-call-1816704933838744903': [{'count(*)': '277813'}], 'var_function-call-3705720165070456970': [{'level': '4.0', 'symbol': 'B04', 'parents': '[\n  "B"\n]'}, {'level': '4.0', 'symbol': 'B23', 'parents': '[\n  "B"\n]'}, {'level': '4.0', 'symbol': 'B30', 'parents': '[\n  "B"\n]'}, {'level': '4.0', 'symbol': 'B21', 'parents': '[\n  "B"\n]'}, {'level': '4.0', 'symbol': 'B25', 'parents': '[\n  "B"\n]'}], 'var_function-call-2797324583492744393': 'file_storage/function-call-2797324583492744393.json', 'var_function-call-4024176117624834020': []}

exec(code, env_args)
