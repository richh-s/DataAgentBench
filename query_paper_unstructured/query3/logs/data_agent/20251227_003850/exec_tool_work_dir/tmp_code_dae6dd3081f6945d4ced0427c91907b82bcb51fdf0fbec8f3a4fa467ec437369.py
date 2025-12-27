code = """import json

# Load aggregated citation totals
with open(var_call_1ntqvKIgCKBFjh2PBN0ocFX8, 'r', encoding='utf-8') as f:
    citations = json.load(f)

empirical_titles = []
emp_citation_map = {}
for rec in citations:
    t = rec.get('title')
    tc = rec.get('total_citations')
    if isinstance(t, str) and ('empirical' in t.lower()):
        empirical_titles.append(t)
        try:
            emp_citation_map[t] = int(tc)
        except Exception:
            try:
                emp_citation_map[t] = int(float(tc))
            except Exception:
                emp_citation_map[t] = None

# Build filenames list (title + '.txt')
filenames = [t + '.txt' for t in empirical_titles]

result = {'titles': empirical_titles, 'filenames': filenames, 'citation_map': emp_citation_map}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_WPw67wgXaskTYVaZBay2hrci': 'file_storage/call_WPw67wgXaskTYVaZBay2hrci.json', 'var_call_1ntqvKIgCKBFjh2PBN0ocFX8': 'file_storage/call_1ntqvKIgCKBFjh2PBN0ocFX8.json', 'var_call_mYMhTkK3uSl7cJInG6UsluoL': [], 'var_call_lk7wSCfnHF8Qhr71426NHQZw': [], 'var_call_B6tTsBXqGYIrbqBYA3iowVR1': [], 'var_call_rHchAtTQ45xNOeRMELsaL42l': [], 'var_call_A4dO1XSE2oNscPIdA44yQl9j': 'file_storage/call_A4dO1XSE2oNscPIdA44yQl9j.json', 'var_call_VW5B9dNmtzlCsNOr6Fo9Ij2M': [], 'var_call_ga3ePrln9Ysiub3S5PuqOLiz': []}

exec(code, env_args)
