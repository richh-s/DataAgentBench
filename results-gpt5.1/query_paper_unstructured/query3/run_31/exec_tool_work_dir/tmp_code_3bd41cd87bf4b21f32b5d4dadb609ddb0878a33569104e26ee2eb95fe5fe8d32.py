code = """import re, json, pandas as pd
import json as js

with open(var_call_fQom8adI882atG1Z9SpR4GSk, 'r') as f:
    mongo_records = js.load(f)

empirical_docs = []
for doc in mongo_records:
    text = doc.get('text','').lower()
    if 'empirical' in text:
        years = re.findall(r'20[0-9]{2}', text)
        years = [int(y) for y in years]
        pub_year = min(years) if years else None
        if pub_year and pub_year >= 2017:
            title = doc.get('filename','').rsplit('.txt',1)[0]
            empirical_docs.append({'title': title, 'year': pub_year})

with open(var_call_bCLQtbyLXZoPE0OHwtZcVuCJ, 'r') as f:
    cit_records = js.load(f)

cit_df = pd.DataFrame(cit_records)
cit_df['title_clean'] = cit_df['title'].str.replace('^"|"$', '', regex=True)

emp_df = pd.DataFrame(empirical_docs)

merged = emp_df.merge(cit_df, left_on='title', right_on='title_clean', how='left')

result = merged[['title','total_citations']].to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_fQom8adI882atG1Z9SpR4GSk': 'file_storage/call_fQom8adI882atG1Z9SpR4GSk.json', 'var_call_bCLQtbyLXZoPE0OHwtZcVuCJ': 'file_storage/call_bCLQtbyLXZoPE0OHwtZcVuCJ.json', 'var_call_TodI2PcnmfqKoLuXfup6UTch': {'keys': ['title', 'total_citations']}}

exec(code, env_args)
