code = """import json, re
# Load data from storage-provided file paths
with open(var_call_O4nkGAb8V0cu2IJL0DJFErKf, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(var_call_dhOgPAH5yYQRj271OIlkZkX7, 'r', encoding='utf-8') as f:
    cites = json.load(f)

# Build set of titles for papers presented at CHI (detect 'CHI' as a whole word in text)
chi_titles = set()
for d in docs:
    filename = d.get('filename', '')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = d.get('text', '') or ''
    if re.search(r"\bCHI\b", text, re.IGNORECASE):
        chi_titles.add(title)

# Filter citation records for 2020 (already queried) that match CHI titles
matched = []
for r in cites:
    t = r.get('title')
    cc = r.get('citation_count')
    try:
        cc_int = int(cc)
    except:
        try:
            cc_int = int(float(cc))
        except:
            cc_int = 0
    if t in chi_titles:
        matched.append({'title': t, 'citation_count': cc_int})

# Compute total citations across matched CHI papers
total = sum(x['citation_count'] for x in matched)
# Sort matched list by citation_count descending
matched_sorted = sorted(matched, key=lambda x: x['citation_count'], reverse=True)

result = {'total_citations_2020_for_CHI_papers': total, 'papers': matched_sorted}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_dhOgPAH5yYQRj271OIlkZkX7': 'file_storage/call_dhOgPAH5yYQRj271OIlkZkX7.json', 'var_call_O4nkGAb8V0cu2IJL0DJFErKf': 'file_storage/call_O4nkGAb8V0cu2IJL0DJFErKf.json'}

exec(code, env_args)
