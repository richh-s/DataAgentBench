code = """import json
import re
import pandas as pd

with open(locals()['var_function-call-2797324583492744393'], 'r') as f:
    filings_data = json.load(f)

print(f"Total entries: {len(filings_data)}")

def extract_year(date_str):
    if not date_str:
        return None
    match = re.search(r'\b(19|20)\d{2}\b', str(date_str))
    if match:
        return int(match.group(0))
    return None

years = []
for i, entry in enumerate(filings_data):
    y = extract_year(entry.get('filing_date'))
    if y:
        years.append(y)
    if i < 5:
        print(f"Sample date: {entry.get('filing_date')} -> {y}")

if not years:
    print("No years extracted.")
    print("__RESULT__:")
    print("[]")
else:
    df = pd.DataFrame(years, columns=['year'])
    print(f"Min year: {df['year'].min()}, Max year: {df['year'].max()}")
    print("Year counts tail:")
    print(df['year'].value_counts().sort_index().tail(10))
    
    print("__RESULT__:")
    print(json.dumps("Done"))"""

env_args = {'var_function-call-11252670295542494115': 'file_storage/function-call-11252670295542494115.json', 'var_function-call-11252670295542493418': 'file_storage/function-call-11252670295542493418.json', 'var_function-call-1816704933838744903': [{'count(*)': '277813'}], 'var_function-call-3705720165070456970': [{'level': '4.0', 'symbol': 'B04', 'parents': '[\n  "B"\n]'}, {'level': '4.0', 'symbol': 'B23', 'parents': '[\n  "B"\n]'}, {'level': '4.0', 'symbol': 'B30', 'parents': '[\n  "B"\n]'}, {'level': '4.0', 'symbol': 'B21', 'parents': '[\n  "B"\n]'}, {'level': '4.0', 'symbol': 'B25', 'parents': '[\n  "B"\n]'}], 'var_function-call-2797324583492744393': 'file_storage/function-call-2797324583492744393.json', 'var_function-call-4024176117624834020': [], 'var_function-call-7163784566198070492': {}}

exec(code, env_args)
