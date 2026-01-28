code = """import json, re, pandas as pd

def load_maybe_path(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

mongo_recs = load_maybe_path(var_call_KQ8qR60jRVAbmpSDNbSLUa2L)
cit_recs = load_maybe_path(var_call_Gcy9OwZ4BPgbXR3BKg8KmU3S)

cit_df = pd.DataFrame(cit_recs)
cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)
cit_map = dict(zip(cit_df['title'], cit_df['total_citations']))

# Determine domain via contains 'Physical Activity' in Author Keywords or general text; already physical activity domain implied by prompt

def is_physical_activity_domain(text):
    # simple heuristic: author keywords line includes Physical Activity, or repeated mentions.
    if re.search(r'(?i)Author Keywords[\s\S]{0,300}Physical\s+Activity', text):
        return True
    # otherwise count occurrences
    return len(re.findall(r'(?i)physical activity', text))>=2

rows=[]
for r in mongo_recs:
    title = r.get('filename','')
    if title.lower().endswith('.txt'):
        title = title[:-4]
    text = r.get('text','') or ''
    if not is_physical_activity_domain(text):
        continue
    rows.append({'title': title, 'total_citations': int(cit_map.get(title,0))})

out_df=pd.DataFrame(rows).drop_duplicates()
out_df=out_df.sort_values(['total_citations','title'], ascending=[False,True])
print('__RESULT__:')
print(json.dumps(out_df.to_dict(orient='records'), ensure_ascii=False))"""

env_args = {'var_call_8AQzsnVK3pjf8qv96fVixUDd': 'file_storage/call_8AQzsnVK3pjf8qv96fVixUDd.json', 'var_call_Gcy9OwZ4BPgbXR3BKg8KmU3S': 'file_storage/call_Gcy9OwZ4BPgbXR3BKg8KmU3S.json', 'var_call_CuwislDkhq3PJKeBDgFmstlY': [], 'var_call_sTOTPpLvdzZRAbkte2NRypwi': 'file_storage/call_sTOTPpLvdzZRAbkte2NRypwi.json', 'var_call_53iSUuuy40M0TesDhNqEkEr4': [{'cid': '0', 'name': 'id', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '1'}, {'cid': '1', 'name': 'title', 'type': 'TEXT', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'citation_count', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'citation_year', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}], 'var_call_jqJR2YFJJb1Bd6RAubD6yT4q': {'columns': ['title', 'total_citations'], 'head': [{'title': '"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'total_citations': '53'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'total_citations': '313'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'total_citations': '390'}]}, 'var_call_2jGdLUt8wHG962Eew14Dzpti': [], 'var_call_LCWTbFQgTxLUup36TYI5p8XP': 'file_storage/call_LCWTbFQgTxLUup36TYI5p8XP.json', 'var_call_KXiA4ED2Hu0tvNUxJlqiDPS2': {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'years_in_head': [], 'head_snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-tracking data can motivate the user towards\nconstructive self-reﬂection. One powerful form of narrative\nthat engages audience across various culture and age groups\nis animated movies. We collected a week of self-reported\nmood and behavior data from each user and created in Unity a\npersonalized animation based on their data. We evaluated the\nimpact of their video in a randomized control trial with a non-\npersonalized animated video as control. We found that person-\nalized videos tend to be more emotionally engaging, encourag-\ning greater and lengthier writing that indicated self-reﬂection\nabout moods and behaviors, compared to non-personalized\ncontrol videos.\n\nACM Classiﬁcation Keywords\nH.5.1'}, 'var_call_KQ8qR60jRVAbmpSDNbSLUa2L': 'file_storage/call_KQ8qR60jRVAbmpSDNbSLUa2L.json'}

exec(code, env_args)
