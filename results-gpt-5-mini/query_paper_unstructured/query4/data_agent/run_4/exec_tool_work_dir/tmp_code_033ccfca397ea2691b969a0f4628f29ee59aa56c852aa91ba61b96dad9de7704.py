code = """import json, re
p = var_call_40G8suqyORvGvH2VqbbBEhkO
with open(p, 'r', encoding='utf-8') as f:
    data = json.load(f)

out = []
for rec in data:
    filename = rec.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = rec.get('text','')
    has_pa = 'physical activity' in text.lower() or 'physical activity' in title.lower()
    occs = []
    for m in re.finditer(r"(.{0,40}2016.{0,40})", text):
        occs.append(m.group(0))
    # also look for venue-year patterns like 'CHI 2016' or 'CHI 2016,'
    venue_matches = re.findall(r"\b(CHI|Ubicomp|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*[,\-]?(\s*)2016\b", text, re.I)
    out.append({'title': title, 'has_physical_activity': has_pa, 'year_mentions_count': len(occs), 'year_snippets': occs[:5], 'venue_2016_matches': venue_matches})

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_UeAwGvyL4BRgCq5TsBDxPehn': 'file_storage/call_UeAwGvyL4BRgCq5TsBDxPehn.json', 'var_call_dtnwJdFJIovt8fdBMoCOC9Z5': [], 'var_call_40G8suqyORvGvH2VqbbBEhkO': 'file_storage/call_40G8suqyORvGvH2VqbbBEhkO.json', 'var_call_jokn9ejj3SySQh0YVLoqQrID': [], 'var_call_GCWkR1OFB2vPEOsJxlXZD4wx': [], 'var_call_On7oCux1AjpCpaT2jkfydY5j': 'file_storage/call_On7oCux1AjpCpaT2jkfydY5j.json', 'var_call_z3BmMZCV2zNwBJd3OBhZLJql': ['paper_docs'], 'var_call_9PGGGyYeJkpVGL7Mt4nLr2dm': ['Citations', 'sqlite_sequence'], 'var_call_BQYWUevYFUky85OvPZGvHJRC': 'file_storage/call_BQYWUevYFUky85OvPZGvHJRC.json', 'var_call_xQdYTsepG8F9TC14yLse3ody': 'file_storage/call_xQdYTsepG8F9TC14yLse3ody.json', 'var_call_k69zPsARtimNXJyEpFOK96WM': [{'title': 'A Lived Informatics Model of Personal Informatics', 'total_citations': 390}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'total_citations': 220}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': 265}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': 266}, {'title': 'Barriers to Engagement with a Personal Informatics Productivity Tool', 'total_citations': 306}], 'var_call_AVDKSVvM8kKfNzpAO5OLq1AT': {'candidates_count': 5, 'c2016_count': 0, 'c2016': [], 'matches': []}}

exec(code, env_args)
