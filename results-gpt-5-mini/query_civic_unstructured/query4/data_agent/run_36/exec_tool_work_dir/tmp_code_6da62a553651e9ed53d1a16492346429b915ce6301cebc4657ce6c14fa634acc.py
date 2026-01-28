code = """import json
import re
import pandas as pd

# Load data from storage variables (file paths)
with open(var_call_3fClD2OAoi2MtPThexPA0RaP, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)

with open(var_call_K77CorqWc0g2MRMwJSb68Q4U, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Create DataFrame for funding
fund_df = pd.DataFrame(funding_records)
# Ensure Amount is numeric
def to_int(x):
    try:
        return int(str(x).replace(',', '').strip())
    except:
        try:
            return int(float(str(x)))
        except:
            return 0

fund_df['Amount'] = fund_df['Amount'].apply(to_int)

# Prepare pattern to detect Spring 2022 (March-May 2022)
pattern = re.compile(r'(spring[\s,.-]*2022|2022[\s,.-]*spring|(?:march|mar|april|apr|may)[\s,.-]*2022|2022[\s,.-]*(?:march|mar|april|apr|may)|2022-0?3|2022-0?4|2022-0?5)', re.I)

# Lowercase texts for searching
docs_texts = [d.get('text','').lower() for d in civic_docs]

matched_projects = set()

for idx, row in fund_df.iterrows():
    pname = str(row['Project_Name']).lower()
    if not pname or pname.strip() == '':
        continue
    found = False
    for text in docs_texts:
        start = 0
        while True:
            i = text.find(pname, start)
            if i == -1:
                break
            # define window around occurrence to search for spring 2022 indicators
            window_start = max(0, i - 200)
            window_end = min(len(text), i + len(pname) + 1000)
            window = text[window_start:window_end]
            if pattern.search(window):
                matched_projects.add(row['Project_Name'])
                found = True
                break
            start = i + 1
        if found:
            break

# Compute count and total funding
matched_list = sorted(list(matched_projects))
count = len(matched_list)
# Sum amounts for matched projects (match exact Project_Name in fund_df)
matched_funds = fund_df[fund_df['Project_Name'].isin(matched_list)]['Amount'].sum()

result = {
    'count': count,
    'total_funding': int(matched_funds),
    'projects': matched_list
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_p78B03ub9bqHqjZnpymqtWmt': ['civic_docs'], 'var_call_vVNH7vMG67yKNrJVIxjeXHvV': ['Funding'], 'var_call_K77CorqWc0g2MRMwJSb68Q4U': 'file_storage/call_K77CorqWc0g2MRMwJSb68Q4U.json', 'var_call_3fClD2OAoi2MtPThexPA0RaP': 'file_storage/call_3fClD2OAoi2MtPThexPA0RaP.json'}

exec(code, env_args)
