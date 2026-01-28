code = """import json, os
# var_call_mtKLCwOcIYLgbsvlEjhWkC5B may be a filepath (string) to a JSON file or a list
# var_call_3QOxOb7OmNcSvlYbShRQeJqr from previous execute_python is a list of titles

# Load citations
cit_var = var_call_mtKLCwOcIYLgbsvlEjhWkC5B
if isinstance(cit_var, str) and os.path.exists(cit_var):
    with open(cit_var, 'r', encoding='utf-8') as f:
        citations = json.load(f)
else:
    citations = cit_var

# Load titles (this variable should be a list)
titles = var_call_3QOxOb7OmNcSvlYbShRQeJqr

# Build citation map
cit_map = {}
for rec in citations:
    # ensure title string
    title = rec.get('title')
    # citation counts might be strings, convert safely
    try:
        cnt = int(rec.get('total_citations'))
    except Exception:
        try:
            cnt = int(rec.get('citation_count'))
        except Exception:
            cnt = None
    cit_map[title] = cnt

results = []
total = 0
for t in titles:
    cit = cit_map.get(t)
    if cit is None:
        # try normalized match: strip, collapse spaces
        t_norm = ' '.join(str(t).split())
        cit = cit_map.get(t_norm)
    if cit is None:
        # try matching ignoring punctuation quotes
        import re
        def norm(s):
            return re.sub(r"[^A-Za-z0-9 ]+", "", s).strip().lower()
        t_key = norm(t)
        found = None
        for k,v in cit_map.items():
            if k is None:
                continue
            if norm(k) == t_key:
                found = v
                break
        cit = found
    results.append({'title': t, 'citations': cit})
    if cit is not None:
        total += cit

out = {'papers': results, 'total_citations_for_food_domain': total}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_y7sTqMxz8v6UcMHattxaO0rs': 'file_storage/call_y7sTqMxz8v6UcMHattxaO0rs.json', 'var_call_3QOxOb7OmNcSvlYbShRQeJqr': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use'], 'var_call_mtKLCwOcIYLgbsvlEjhWkC5B': 'file_storage/call_mtKLCwOcIYLgbsvlEjhWkC5B.json'}

exec(code, env_args)
