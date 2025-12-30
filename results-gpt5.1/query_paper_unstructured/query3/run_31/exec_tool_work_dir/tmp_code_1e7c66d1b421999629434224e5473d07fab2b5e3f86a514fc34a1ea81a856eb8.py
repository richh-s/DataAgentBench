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

emp_df = pd.DataFrame(empirical_docs)

# perform manual join
results = []
for e in empirical_docs:
    title = e['title']
    # clean quotes in citation titles
    matches = [r for r in cit_records if r['title'].strip('"') == title]
    total = matches[0]['total_citations'] if matches else None
    results.append({'title': title, 'total_citations': total})

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_fQom8adI882atG1Z9SpR4GSk': 'file_storage/call_fQom8adI882atG1Z9SpR4GSk.json', 'var_call_bCLQtbyLXZoPE0OHwtZcVuCJ': 'file_storage/call_bCLQtbyLXZoPE0OHwtZcVuCJ.json', 'var_call_TodI2PcnmfqKoLuXfup6UTch': {'keys': ['title', 'total_citations']}, 'var_call_Ms6hzApAq5Cv9eiaKTN1EjEi': {'columns': ['title', 'total_citations'], 'sample': [{'title': '"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'total_citations': '53'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'total_citations': '313'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'total_citations': '390'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'total_citations': '368'}, {'title': 'A Situated Exploration of Designing for Personal Health Ecosystems Through Data-enabled Design', 'total_citations': '277'}]}}

exec(code, env_args)
