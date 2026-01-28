code = """import json, re
p = var_call_40G8suqyORvGvH2VqbbBEhkO
with open(p, 'r', encoding='utf-8') as f:
    data = json.load(f)

candidates = []
for rec in data:
    filename = rec.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = rec.get('text','')
    if 'physical activity' not in text.lower() and 'physical activity' not in title.lower():
        continue
    header = text[:800]
    is2016 = False
    # direct 2016 in header
    if re.search(r"\b2016\b", header):
        is2016 = True
    # venue-year patterns in header
    if re.search(r"\b(CHI|Ubicomp|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\b[\s\S]{0,40}\b2016\b", header, re.I):
        is2016 = True
    # lines at top like 'CHI 2016, ...'
    if not is2016:
        lines = header.splitlines()
        for ln in lines[:10]:
            if '2016' in ln:
                is2016 = True
                break
    # also check filename for 2016
    if '2016' in filename:
        is2016 = True
    candidates.append({'title': title, 'is2016': is2016})

res = [c for c in candidates if c['is2016']]
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_UeAwGvyL4BRgCq5TsBDxPehn': 'file_storage/call_UeAwGvyL4BRgCq5TsBDxPehn.json', 'var_call_dtnwJdFJIovt8fdBMoCOC9Z5': [], 'var_call_40G8suqyORvGvH2VqbbBEhkO': 'file_storage/call_40G8suqyORvGvH2VqbbBEhkO.json', 'var_call_jokn9ejj3SySQh0YVLoqQrID': [], 'var_call_GCWkR1OFB2vPEOsJxlXZD4wx': [], 'var_call_On7oCux1AjpCpaT2jkfydY5j': 'file_storage/call_On7oCux1AjpCpaT2jkfydY5j.json', 'var_call_z3BmMZCV2zNwBJd3OBhZLJql': ['paper_docs'], 'var_call_9PGGGyYeJkpVGL7Mt4nLr2dm': ['Citations', 'sqlite_sequence'], 'var_call_BQYWUevYFUky85OvPZGvHJRC': 'file_storage/call_BQYWUevYFUky85OvPZGvHJRC.json', 'var_call_xQdYTsepG8F9TC14yLse3ody': 'file_storage/call_xQdYTsepG8F9TC14yLse3ody.json', 'var_call_k69zPsARtimNXJyEpFOK96WM': [{'title': 'A Lived Informatics Model of Personal Informatics', 'total_citations': 390}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'total_citations': 220}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': 265}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': 266}, {'title': 'Barriers to Engagement with a Personal Informatics Productivity Tool', 'total_citations': 306}], 'var_call_AVDKSVvM8kKfNzpAO5OLq1AT': {'candidates_count': 5, 'c2016_count': 0, 'c2016': [], 'matches': []}, 'var_call_3dTzwajaSCf8DeFyKJiykrMb': [{'title': 'A Lived Informatics Model of Personal Informatics', 'has_physical_activity': True, 'year_mentions_count': 0, 'year_snippets': [], 'venue_2016_matches': []}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'has_physical_activity': True, 'year_mentions_count': 0, 'year_snippets': [], 'venue_2016_matches': []}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'has_physical_activity': True, 'year_mentions_count': 3, 'year_snippets': ['Guimbetiere, and Tanzeem Choudhury. 2016.', '2016 ACM International Joint Conference on P', '24. Akane Sano. 2016. Measuring college students’ sleep,'], 'venue_2016_matches': []}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'has_physical_activity': True, 'year_mentions_count': 5, 'year_snippets': ['Coninx. 2016. Back on bike: the BoB mobile cycling a', '2016.  A  longitudinal evaluation  of  the  ', ' James Clawson and Elizabeth D. Mynatt. 2016. A Cancer ', ',  Lynne  Baillie  and  Stephen  Uzor.  2016.  Time  to ', '[43]  My  pelvic  floor  Fitness.  2016.  http://www.lightsbytena.co.uk/my-'], 'venue_2016_matches': []}, {'title': 'Barriers to Engagement with a Personal Informatics Productivity Tool', 'has_physical_activity': True, 'year_mentions_count': 0, 'year_snippets': [], 'venue_2016_matches': []}]}

exec(code, env_args)
