code = """import re, json, pandas as pd
from pathlib import Path

path_docs = Path(var_call_aixywG09ZxW0fTU72ubJwKpr)
records_docs = json.loads(path_docs.read_text())

path_fund = Path(var_call_8YeeR8BUKk3n7NloGyzVRMuW)
records_fund = json.loads(path_fund.read_text())

fund_df = pd.DataFrame(records_fund)

mask = fund_df['Project_Name'].str.contains('FEMA', case=False, na=False) | fund_df['Project_Name'].str.contains('emergency', case=False, na=False)
rel_fund = fund_df[mask].copy()

projects = []
for rec in records_docs:
    text = rec.get('text', '')
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    for i, line in enumerate(lines):
        pattern = r'(Project|Repairs|Improvements|Warning)'
        if re.search(pattern, line) and len(line.split()) <= 12:
            name = line.strip()
            context = ' '.join(lines[max(0, i-3):i+4])
            topic_parts = []
            if re.search('FEMA', context, re.I):
                topic_parts.append('FEMA')
            if re.search('emergency', context, re.I):
                topic_parts.append('emergency warning')
            if re.search('warning', context, re.I) and 'emergency warning' not in topic_parts:
                topic_parts.append('warning')
            if re.search('road', context, re.I):
                topic_parts.append('road')
            if re.search('park', context, re.I):
                topic_parts.append('park')
            if re.search('drain', context, re.I):
                topic_parts.append('drainage')

            topic = ', '.join(dict.fromkeys(topic_parts)) if topic_parts else None

            status = None
            if re.search('currently under construction|Begin Construction', context, re.I):
                status = 'design'
            if re.search('Construction was completed|completed November|completed,', context, re.I):
                status = 'completed'
            if re.search('Not Started', context, re.I):
                status = 'not started'

            projects.append({'Project_Name': name, 'topic': topic, 'status': status})

proj_df = pd.DataFrame(projects).drop_duplicates(subset=['Project_Name'])

merged = rel_fund.merge(proj_df, on='Project_Name', how='left')

out = merged[['Project_Name', 'Funding_Source', 'Amount', 'status']].to_dict(orient='records')

result = json.dumps(out)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_aixywG09ZxW0fTU72ubJwKpr': 'file_storage/call_aixywG09ZxW0fTU72ubJwKpr.json', 'var_call_8YeeR8BUKk3n7NloGyzVRMuW': 'file_storage/call_8YeeR8BUKk3n7NloGyzVRMuW.json'}

exec(code, env_args)
