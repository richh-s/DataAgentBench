code = """import re, json, pandas as pd, os, textwrap

# Load full civic docs
path_docs = var_call_S1uCbQ3Q1qgxWhyN0WSmj7Ke
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

# Load funding table
path_funding = var_call_r9xiorIIwOVeePCbbMP7uFNM
with open(path_funding, 'r') as f:
    funding = json.load(f)

funding_df = pd.DataFrame(funding)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Very rough heuristic: extract project lines that look like titles, then infer topic and completion year
project_pattern = re.compile(r"^(?P<name>[^\n\r]{5,80})$")

projects = []
for doc in civic_docs:
    text = doc.get('text','')
    lines = [l.strip() for l in text.split('\n')]
    for i, line in enumerate(lines):
        if len(line) < 5 or len(line) > 120: continue
        # Identify project title heuristically by checking for keywords like 'Project', 'Park', 'Improvements', etc.
        if any(k in line for k in ['Project', 'Park', 'Improvements', 'Repairs', 'Playground', 'Shade Structure', 'Walkway']):
            name = line
            # Look ahead a few lines for status/completion info
            context = '\n'.join(lines[i:i+10])
            status = None
            if re.search(r'Construction was completed,?\s*(?P<date>[A-Za-z]+\s+\d{4}|\d{4})', context):
                status = 'completed'
                m = re.search(r'Construction was completed,?\s*(?P<date>[A-Za-z]+\s+\d{4}|\d{4})', context)
                et = m.group('date')
            elif re.search(r'Construction was completed\s*(?P<date>\w+\s+\d{4})', context):
                status = 'completed'
                et = re.search(r'Construction was completed\s*(?P<date>\w+\s+\d{4})', context).group('date')
            elif re.search(r'Construction was completed\.?\s*(?P<date>\w+\s+\d{4})', context):
                status = 'completed'
                et = re.search(r'Construction was completed\.?\s*(?P<date>\w+\s+\d{4})', context).group('date')
            else:
                et = ''
            # Topic heuristic
            topic_keywords = []
            lower_ctx = context.lower()
            for kw in ['park', 'playground', 'road', 'highway', 'bridge', 'storm drain', 'drainage', 'water', 'guardrail', 'emergency', 'warning']:
                if kw in lower_ctx:
                    topic_keywords.append(kw)
            topic = ','.join(sorted(set(topic_keywords))) if topic_keywords else ''
            projects.append({'Project_Name': name.strip(), 'status': status, 'et': et, 'topic': topic})

projects_df = pd.DataFrame(projects).drop_duplicates(subset=['Project_Name','status','et','topic'])

# Filter park-related completed in 2022
mask_park = projects_df['topic'].str.contains('park', case=False, na=False)
mask_completed = projects_df['status'] == 'completed'
mask_2022 = projects_df['et'].astype(str).str.contains('2022')
park_2022 = projects_df[mask_park & mask_completed & mask_2022]

# Join with funding on Project_Name using fuzzy/contains match: exact first
merged = funding_df.merge(park_2022, on='Project_Name', how='inner')

total_funding = int(merged['Amount'].sum()) if not merged.empty else 0

result = {
    'projects_2022_park_completed': park_2022.to_dict(orient='records'),
    'matched_funding_records': merged.to_dict(orient='records'),
    'total_funding': total_funding
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_S1uCbQ3Q1qgxWhyN0WSmj7Ke': 'file_storage/call_S1uCbQ3Q1qgxWhyN0WSmj7Ke.json', 'var_call_r9xiorIIwOVeePCbbMP7uFNM': 'file_storage/call_r9xiorIIwOVeePCbbMP7uFNM.json'}

exec(code, env_args)
