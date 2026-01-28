code = """import json
from pathlib import Path

# Load the large query result from the MongoDB call stored in a file
file_path = var_call_QNAkirvfelitxdqwzf8u8zBY
with open(file_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Citations aggregation result variable
citations = var_call_hAVUT8lH4KFF1B8P88kvoweI

# Build title -> total_citations mapping
cit_map = {}
for r in citations:
    title = r.get('title')
    # convert to int safely
    try:
        tot = int(r.get('total_citations'))
    except Exception:
        try:
            tot = int(float(r.get('total_citations')))
        except Exception:
            tot = 0
    cit_map[title] = tot

# Heuristic to classify a document as 'food' domain
keywords = ['food', 'food journ', 'food diary', 'eat', 'eating', 'meal', 'diet', 'calorie', 'calories']

included_titles = []
for doc in docs:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','')
    text_l = text.lower()
    # check early part (abstract/keywords) and whole text for stronger signal
    early = text_l[:2000]
    is_food = False
    for kw in keywords:
        if kw in early:
            is_food = True
            break
    # also check for explicit phrase 'food journaling' anywhere
    if not is_food and 'food journ' in text_l:
        is_food = True
    # if still not decided, require at least 3 occurrences of 'food' in whole text
    if not is_food:
        if text_l.count('food') >= 3:
            is_food = True
    if is_food:
        included_titles.append(title)

# Sum citations for included titles
total = 0
details = []
for t in included_titles:
    c = cit_map.get(t, 0)
    total += c
    details.append({'title': t, 'citations': c})

result = {'total_citations': total, 'papers_counted': len(included_titles), 'papers': details}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_aPLhmEXjqZEiGbBg9mcRBhda': ['paper_docs'], 'var_call_nC6jGzrmWO3ydtXANgqeCPrD': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}], 'var_call_hAVUT8lH4KFF1B8P88kvoweI': [{'title': 'A Lived Informatics Model of Personal Informatics', 'total_citations': '390'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'total_citations': '220'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': '266'}, {'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'total_citations': '270'}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'total_citations': '636'}], 'var_call_QNAkirvfelitxdqwzf8u8zBY': 'file_storage/call_QNAkirvfelitxdqwzf8u8zBY.json'}

exec(code, env_args)
