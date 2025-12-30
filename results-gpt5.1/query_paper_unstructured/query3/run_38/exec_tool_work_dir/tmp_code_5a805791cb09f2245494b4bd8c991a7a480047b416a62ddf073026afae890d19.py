code = """import json, pandas as pd, re

# Load full Mongo result
path_p = var_call_SsZCeNF82c6ql85sKJbtvAAq
with open(path_p, 'r') as f:
    papers = json.load(f)

records = []
for doc in papers:
    if not isinstance(doc, dict):
        continue
    filename = doc.get('filename','')
    if not filename:
        continue
    title = re.sub(r"\.txt$","", filename)
    text = doc.get('text','') or ''
    years = re.findall(r"20[0-3][0-9]", text)
    year = None
    for y in years:
        yi = int(y)
        if 2000 <= yi <= 2030:
            year = yi
            break
    if year is None or year <= 2016:
        continue
    if 'empirical' not in text.lower():
        continue
    records.append({'title': title, 'year': year})

papers_df = pd.DataFrame(records).drop_duplicates(subset=['title'])

# Load citations aggregation result
path_c = var_call_3RdIKm8ph6IZ0OYZ2XeC4Znf
with open(path_c, 'r') as f:
    cites = json.load(f)

cites_df = pd.DataFrame(cites)

cites_df['total_citations'] = cites_df['total_citations'].astype(int)

merged = pd.merge(papers_df, cites_df, on='title', how='left')

result = merged[['title','total_citations']].sort_values('title').to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_call_SsZCeNF82c6ql85sKJbtvAAq': 'file_storage/call_SsZCeNF82c6ql85sKJbtvAAq.json', 'var_call_3RdIKm8ph6IZ0OYZ2XeC4Znf': 'file_storage/call_3RdIKm8ph6IZ0OYZ2XeC4Znf.json', 'var_call_xhshLshjc26OoLWmohkevP6Z': {'papers_example': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}, {'title': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'year': 2018}, {'title': 'Communicating Uncertainty in Fertility Prognosis', 'year': 2019}, {'title': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'year': 2018}], 'cites_example': 'file_'}, 'var_call_rNl06dU6uRhAR9mZDartgGtX': {'cols': ['title', 'total_citations'], 'head': [{'title': '"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'total_citations': '53'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'total_citations': '313'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'total_citations': '390'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'total_citations': '368'}, {'title': 'A Situated Exploration of Designing for Personal Health Ecosystems Through Data-enabled Design', 'total_citations': '277'}]}}

exec(code, env_args)
