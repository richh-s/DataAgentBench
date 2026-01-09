code = """import json, re, pandas as pd

def load_maybe_path(x):
    if isinstance(x, str):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

papers = load_maybe_path(var_call_mQ4MR4okAGVk8rRwsPEjOnVV)

df = pd.DataFrame(papers)
df['title'] = df['filename'].str.replace(r'\\.txt$', '', regex=True)

def pub_year(txt):
    if not isinstance(txt, str):
        return None
    m = re.search(r"\b(?:CHI|UbiComp|CSCW|DIS|IUI|WWW|TEI|OzCHI|PervasiveHealth|AH)\s*'?\s*(\d{2})\b", txt)
    if m:
        yy = int(m.group(1))
        return 2000+yy if yy<=30 else 1900+yy
    m2 = re.search(r"\b(20\d{2})\b", txt)
    if m2:
        # use first occurrence
        return int(m2.group(1))
    return None

df['pub_year'] = [pub_year(t) for t in df['text'].tolist()]

out = df[['title','pub_year']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_8fMaorK3TSrjojq1oPQfLpMO': 'file_storage/call_8fMaorK3TSrjojq1oPQfLpMO.json', 'var_call_SfMGEro4SDvnESWaKsJVlOAm': 'file_storage/call_SfMGEro4SDvnESWaKsJVlOAm.json', 'var_call_WfAIsipV2AOM0gr51VowBVz5': [], 'var_call_fZH1JE6HGdaqiEJxAXKMPqqa': 'file_storage/call_fZH1JE6HGdaqiEJxAXKMPqqa.json', 'var_call_f4Se9vGAKiFrCQA1SPqzI8QA': [], 'var_call_wXnobs1oEQBdN7QGVYFNzkem': [{'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure", 'total_citations': '542'}, {'title': 'SweatAtoms: Materializing Physical Activity', 'total_citations': '428'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity', 'total_citations': '358'}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'total_citations': '349'}, {'title': 'Low Sampling Rate for Physical Activity Recognition', 'total_citations': '348'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'total_citations': '335'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'total_citations': '278'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'total_citations': '259'}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'total_citations': '221'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity', 'total_citations': '180'}, {'title': 'Move into Another World of Happy: Insights for Designing Affect-based Physical Activity Interventions', 'total_citations': '107'}, {'title': 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach', 'total_citations': '98'}, {'title': 'Understanding Physical Activity Through 3D Printed Material Artifacts', 'total_citations': '46'}, {'title': 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity', 'total_citations': '12'}], 'var_call_mQ4MR4okAGVk8rRwsPEjOnVV': 'file_storage/call_mQ4MR4okAGVk8rRwsPEjOnVV.json'}

exec(code, env_args)
