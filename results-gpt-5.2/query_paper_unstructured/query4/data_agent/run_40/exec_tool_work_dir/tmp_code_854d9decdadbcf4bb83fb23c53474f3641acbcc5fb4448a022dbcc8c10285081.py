code = """import json, re

def load_maybe_path(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

recs = load_maybe_path(var_call_LCWTbFQgTxLUup36TYI5p8XP)
text=recs[0]['text']
head=text[:1200]
years=re.findall(r'\b(19\d{2}|20\d{2})\b', head)
print('__RESULT__:')
print(json.dumps({'filename': recs[0]['filename'], 'years_in_head': years[:50], 'head_snippet': head}, ensure_ascii=False))"""

env_args = {'var_call_8AQzsnVK3pjf8qv96fVixUDd': 'file_storage/call_8AQzsnVK3pjf8qv96fVixUDd.json', 'var_call_Gcy9OwZ4BPgbXR3BKg8KmU3S': 'file_storage/call_Gcy9OwZ4BPgbXR3BKg8KmU3S.json', 'var_call_CuwislDkhq3PJKeBDgFmstlY': [], 'var_call_sTOTPpLvdzZRAbkte2NRypwi': 'file_storage/call_sTOTPpLvdzZRAbkte2NRypwi.json', 'var_call_53iSUuuy40M0TesDhNqEkEr4': [{'cid': '0', 'name': 'id', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '1'}, {'cid': '1', 'name': 'title', 'type': 'TEXT', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'citation_count', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'citation_year', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}], 'var_call_jqJR2YFJJb1Bd6RAubD6yT4q': {'columns': ['title', 'total_citations'], 'head': [{'title': '"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'total_citations': '53'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'total_citations': '313'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'total_citations': '390'}]}, 'var_call_2jGdLUt8wHG962Eew14Dzpti': [], 'var_call_LCWTbFQgTxLUup36TYI5p8XP': 'file_storage/call_LCWTbFQgTxLUup36TYI5p8XP.json'}

exec(code, env_args)
