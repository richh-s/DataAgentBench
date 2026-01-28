code = """import json

with open(var_call_WPw67wgXaskTYVaZBay2hrci, 'r', encoding='utf-8') as f:
    docs = json.load(f)

venues = ['chi', 'cscw', 'ubicomp', 'dis', 'pervasivehealth', 'www', 'iui', 'ozchi', 'tei', 'ah']

years_to_check = list(range(2017, 2031))

count_docs = len(docs)
count_empirical = 0
count_year_after_2016 = 0
count_both = 0

candidates = []

for d in docs:
    fn = d.get('filename') or ''
    text = d.get('text') or ''
    if not fn or not text:
        continue
    head = text[:8000]
    lines = head.split('\n')[:120]
    # Detect year
    year_found = None
    # Venue lines
    for line in lines:
        low = line.lower()
        if any(v in low for v in venues):
            for y in years_to_check:
                ys = str(y)
                if ys in line:
                    year_found = y
                    break
        if year_found is not None:
            break
    if year_found is None:
        # Try copyright lines
        for line in lines:
            low = line.lower()
            if ('copyright' in low) or ('©' in line) or ('(c)' in low):
                for y in years_to_check:
                    ys = str(y)
                    if ys in line:
                        year_found = y
                        break
            if year_found is not None:
                break
    if year_found is None:
        # Fallback: search any line for a year
        for line in lines:
            for y in years_to_check:
                if str(y) in line:
                    year_found = y
                    break
            if year_found is not None:
                break
    has_emp = ('empirical' in text.lower())
    if has_emp:
        count_empirical += 1
    if (year_found is not None) and (year_found > 2016):
        count_year_after_2016 += 1
    if has_emp and (year_found is not None) and (year_found > 2016):
        count_both += 1
        title = fn
        if title.lower().endswith('.txt'):
            title = title[:-4]
        candidates.append({'title': title, 'year': year_found})

summary = {
    'total_docs': count_docs,
    'empirical_docs': count_empirical,
    'docs_after_2016': count_year_after_2016,
    'empirical_after_2016': count_both,
    'sample_candidates': candidates[:10]
}

print('__RESULT__:')
print(json.dumps(summary))"""

env_args = {'var_call_WPw67wgXaskTYVaZBay2hrci': 'file_storage/call_WPw67wgXaskTYVaZBay2hrci.json', 'var_call_1ntqvKIgCKBFjh2PBN0ocFX8': 'file_storage/call_1ntqvKIgCKBFjh2PBN0ocFX8.json', 'var_call_mYMhTkK3uSl7cJInG6UsluoL': [], 'var_call_lk7wSCfnHF8Qhr71426NHQZw': [], 'var_call_B6tTsBXqGYIrbqBYA3iowVR1': [], 'var_call_rHchAtTQ45xNOeRMELsaL42l': [], 'var_call_A4dO1XSE2oNscPIdA44yQl9j': 'file_storage/call_A4dO1XSE2oNscPIdA44yQl9j.json', 'var_call_VW5B9dNmtzlCsNOr6Fo9Ij2M': [], 'var_call_ga3ePrln9Ysiub3S5PuqOLiz': [], 'var_call_B8hRX2vJ43xrKIyp30Wa77Xx': {'titles': ['An Empirical Exploration of Mindfulness Design Using Solo Travel Domain', 'Understanding the Adoption of Quantified Self-tracking Wearable Devices in the Organization Environment: An Empirical Case Study'], 'filenames': ['An Empirical Exploration of Mindfulness Design Using Solo Travel Domain.txt', 'Understanding the Adoption of Quantified Self-tracking Wearable Devices in the Organization Environment: An Empirical Case Study.txt'], 'citation_map': {'An Empirical Exploration of Mindfulness Design Using Solo Travel Domain': 352, 'Understanding the Adoption of Quantified Self-tracking Wearable Devices in the Organization Environment: An Empirical Case Study': 231}}, 'var_call_quEk3CTzjHSBBZtAGo3SHuyU': []}

exec(code, env_args)
