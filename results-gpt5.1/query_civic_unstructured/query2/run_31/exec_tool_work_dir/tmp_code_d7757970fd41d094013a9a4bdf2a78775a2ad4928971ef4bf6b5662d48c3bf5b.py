code = """import re, json, pandas as pd

# Load civic docs
path_docs = var_call_LtTuW4LYMQtDhMRejOKBXVO4
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)
texts = [d['text'] for d in civic_docs]
full_text = "\n".join(texts)

# Heuristic: build project records from funding names, then look for them in civic text with context lines
path_fund = var_call_yCa6dDjhzQsHWVyY74DHCaIE
with open(path_fund, 'r') as f:
    funding = json.load(f)

fund_df = pd.DataFrame(funding)

projects = []
for name in fund_df['Project_Name']:
    # Quick park-topic heuristic by name
    lname = name.lower()
    is_park_topic = 'park' in lname or 'playground' in lname or 'skate' in lname
    projects.append({'Project_Name': name, 'is_park_topic_name': is_park_topic})

proj_df = pd.DataFrame(projects)

# For each project, search in text for completion info and years
results = []
for proj in projects:
    name = proj['Project_Name']
    pattern = re.escape(name)
    matches = list(re.finditer(pattern, full_text))
    completed_2022 = False
    any_park_context = proj['is_park_topic_name']
    for m in matches:
        start = max(0, m.start()-300)
        end = min(len(full_text), m.end()+300)
        ctx = full_text[start:end].lower()
        if 'park' in ctx or 'playground' in ctx or 'skate' in ctx:
            any_park_context = True
        if 'construction was completed' in ctx or 'construction was completed,' in ctx or 'construction was completed ' in ctx or 'was completed' in ctx or 'construction completed' in ctx:
            # check year 2022 in same context
            if '2022' in ctx:
                completed_2022 = True
    results.append({'Project_Name': name, 'park_topic': any_park_context, 'completed_2022': completed_2022})

res_df = pd.DataFrame(results)

# Join back to funding and filter
fund_df['Amount'] = fund_df['Amount'].astype(int)
merged = fund_df.merge(res_df, on='Project_Name', how='left')
filtered = merged[(merged['park_topic'] == True) & (merged['completed_2022'] == True)]

answer = {
    'projects': filtered[['Project_Name','Amount']].to_dict(orient='records'),
    'total_amount': int(filtered['Amount'].sum())
}

out = json.dumps(answer)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_LtTuW4LYMQtDhMRejOKBXVO4': 'file_storage/call_LtTuW4LYMQtDhMRejOKBXVO4.json', 'var_call_yCa6dDjhzQsHWVyY74DHCaIE': 'file_storage/call_yCa6dDjhzQsHWVyY74DHCaIE.json'}

exec(code, env_args)
