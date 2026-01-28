code = """import json, re
import pandas as pd

# Load previous large query results from files (paths provided in storage variables)
with open(var_call_gUzOlgQil76xMCtN1O3cDFc1, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_q6cMbWTvgbRya0zFDqIILVc8, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Create dataframe for funding
fund_df = pd.DataFrame(funding)
# Normalize Amount to int
fund_df['Amount'] = fund_df['Amount'].astype(int)
# Lowercase project names for matching
fund_df['proj_lower'] = fund_df['Project_Name'].str.lower()

# Regex pattern for Spring 2022 (March-May 2022)
spring_pattern = re.compile(r"\b(Spring\s*2022|2022\s*[-/]?\s*Spring|March\s*2022|April\s*2022|May\s*2022|2022[- ]?03|2022[- ]?04|2022[- ]?05|2022-March|2022-April|2022-May)\b", re.I)

matched_projects = set()

# For each civic doc, if it mentions Spring 2022, look for any funding project names in the text
for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    if spring_pattern.search(text):
        text_lower = text.lower()
        for pname_lower, pname in zip(fund_df['proj_lower'], fund_df['Project_Name']):
            if pname_lower in text_lower:
                matched_projects.add(pname)

# Compute count and total funding (sum amounts for matching project names, include all funding rows matching those project names)
matched_projects_list = sorted(matched_projects)
if matched_projects_list:
    matched_rows = fund_df[fund_df['Project_Name'].isin(matched_projects_list)]
    total_funding = int(matched_rows['Amount'].sum())
else:
    total_funding = 0

result = {
    'projects_count': len(matched_projects_list),
    'total_funding': total_funding,
    'projects': matched_projects_list
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Rg2QBJNU5VZHFpvUVqq3gaAA': ['civic_docs'], 'var_call_jigmWJy2ZekNysELM9M1ORW1': [], 'var_call_gUzOlgQil76xMCtN1O3cDFc1': 'file_storage/call_gUzOlgQil76xMCtN1O3cDFc1.json', 'var_call_VSZzj9aZQ8YP4B5jH8pwEZEx': ['Funding'], 'var_call_q6cMbWTvgbRya0zFDqIILVc8': 'file_storage/call_q6cMbWTvgbRya0zFDqIILVc8.json'}

exec(code, env_args)
