code = """import json
path = var_call_mtKLCwOcIYLgbsvlEjhWkC5B
with open(path, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build a dict for quick lookup of total citations by title
cit_map = {rec['title']: int(rec['total_citations']) for rec in citations}

# Load the titles from previous mongo query storage
titles_path = var_call_3QOxOb7OmNcSvlYbShRQeJqr
with open(titles_path, 'r', encoding='utf-8') as f:
    titles = json.load(f)

# For domain 'food', find papers whose title suggests domain or filename search already filtered to include 'food' in text.
# Use the titles we extracted from the paper_docs result (these documents had 'food' in their text).
results = []
total = 0
for t in titles:
    # Some titles in citations may match exactly; try exact match first
    cit = cit_map.get(t)
    if cit is None:
        # try variations: remove extra punctuation, normalize spaces
        t_norm = ' '.join(t.split())
        cit = cit_map.get(t_norm)
    if cit is not None:
        results.append({'title': t, 'citations': cit})
        total += cit
    else:
        results.append({'title': t, 'citations': None})

out = {'papers': results, 'total_citations_for_food_domain': total}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_y7sTqMxz8v6UcMHattxaO0rs': 'file_storage/call_y7sTqMxz8v6UcMHattxaO0rs.json', 'var_call_3QOxOb7OmNcSvlYbShRQeJqr': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use'], 'var_call_mtKLCwOcIYLgbsvlEjhWkC5B': 'file_storage/call_mtKLCwOcIYLgbsvlEjhWkC5B.json'}

exec(code, env_args)
