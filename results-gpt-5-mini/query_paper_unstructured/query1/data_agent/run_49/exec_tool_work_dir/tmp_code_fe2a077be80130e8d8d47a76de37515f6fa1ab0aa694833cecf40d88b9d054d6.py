code = """import json
# Access previous query results stored in variables
docs = var_call_2K0XRPZ6niqRztbfaWbDumrf
citations = var_call_x9lIfbMLW4E5KoRs9sPrbnNn

# Build set of titles from filenames (strip .txt)
titles = set()
for d in docs:
    fn = d.get('filename','')
    if fn.lower().endswith('.txt'):
        titles.add(fn[:-4])
    else:
        titles.add(fn)

# Sum citation counts for matching titles
total = 0
matched = []
for c in citations:
    title = c.get('title')
    try:
        count = int(c.get('total_citations', 0))
    except Exception:
        # if it's not directly convertible, try float then int
        try:
            count = int(float(c.get('total_citations', 0)))
        except Exception:
            count = 0
    if title in titles:
        total += count
        matched.append({"title": title, "total_citations": count})

result = {
    "food_domain_titles": sorted(list(titles)),
    "matched_citations": matched,
    "total_citation_count": total
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_2K0XRPZ6niqRztbfaWbDumrf': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}], 'var_call_x9lIfbMLW4E5KoRs9sPrbnNn': [{'title': 'A Lived Informatics Model of Personal Informatics', 'total_citations': '390'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'total_citations': '220'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': '266'}, {'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'total_citations': '270'}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'total_citations': '636'}]}

exec(code, env_args)
