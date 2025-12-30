code = """import re, json, pandas as pd
path_docs = var_call_DqHoZrSWtJtolhom1wQSxjma
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)
funding_records = var_call_GXPG9ngCVTr5LORjiPJxxwne
texts = [d.get('text','') for d in civic_docs]
pattern = re.compile(r'^(?P<name>.+?)(?:\n|\r)(?:\(cid:190\) Updates:|\(cid:190\) Project Description:)', re.MULTILINE)
projects = []
for txt in texts:
    for m in pattern.finditer(txt):
        name = m.group('name').strip()
        projects.append(name)
project_info = {}
for name in projects:
    lower = name.lower()
    topic = []
    if 'park' in lower:
        topic.append('park')
    if 'playground' in lower:
        topic.append('playground')
    if 'road' in lower or 'highway' in lower or 'bridge' in lower or 'pch' in lower:
        topic.append('road')
    topics = ','.join(sorted(set(topic))) if topic else ''
    status = ''
    st = ''
    et = ''
    for txt in texts:
        if name in txt:
            window_start = max(0, txt.find(name))
            window = txt[window_start:window_start+800]
            m_completed = re.search(r'Construction was completed,? ([A-Za-z]+ )?2022', window)
            if m_completed:
                status = 'completed'
                et = '2022'
            break
    project_info[name] = {'Project_Name': name, 'topic': topics, 'status': status, 'st': st, 'et': et}
funding_df = pd.DataFrame(funding_records)
funding_df['Amount'] = funding_df['Amount'].astype(int)
proj_df = pd.DataFrame(project_info.values())
merged = funding_df.merge(proj_df, on='Project_Name', how='left')
mask_park = merged['topic'].str.contains('park', case=False, na=False)
mask_completed_2022 = (merged['status'] == 'completed') & merged['et'].str.contains('2022', na=False)
result_amount = int(merged[mask_park & mask_completed_2022]['Amount'].sum())
out = json.dumps(result_amount)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_DqHoZrSWtJtolhom1wQSxjma': 'file_storage/call_DqHoZrSWtJtolhom1wQSxjma.json', 'var_call_GXPG9ngCVTr5LORjiPJxxwne': 'file_storage/call_GXPG9ngCVTr5LORjiPJxxwne.json'}

exec(code, env_args)
