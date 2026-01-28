code = """import json

mongo_hits = var_call_1Yk2X8kGmtofmKZ73W6fxgv6
citations = var_call_zTc3llUeuL9uBEwIIqC7tbW0

# Extract titles from filenames (strip .txt)
titles = [d['filename'][:-4] if d['filename'].endswith('.txt') else d['filename'] for d in mongo_hits]

# Sum citation totals for matching titles
total = 0
for rec in citations:
    title = rec.get('title')
    if title in titles:
        total += int(rec.get('total_citations'))

print("__RESULT__:")
print(json.dumps(total))"""

env_args = {'var_call_1Yk2X8kGmtofmKZ73W6fxgv6': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}], 'var_call_zTc3llUeuL9uBEwIIqC7tbW0': [{'title': 'A Lived Informatics Model of Personal Informatics', 'total_citations': '390'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'total_citations': '220'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': '266'}, {'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'total_citations': '270'}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'total_citations': '636'}]}

exec(code, env_args)
