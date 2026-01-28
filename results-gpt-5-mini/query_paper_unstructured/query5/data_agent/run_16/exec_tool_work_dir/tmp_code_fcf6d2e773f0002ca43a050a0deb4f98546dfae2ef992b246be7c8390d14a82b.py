code = """import json
# Load the citations data (2020) and CHI paper filenames
with open(var_call_mALohj97VQIHLtJCzMrobCxP, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_gS9FjovkeX8vVLVyMkvIOCen, 'r', encoding='utf-8') as f:
    chi_files = json.load(f)
# Extract CHI titles (filename without .txt)
chi_titles = set()
for rec in chi_files:
    fn = rec.get('filename', '')
    if fn.lower().endswith('.txt'):
        title = fn[:-4]
    else:
        title = fn
    chi_titles.add(title)
# Find citations records whose title is in CHI titles
matched = []
total = 0
for rec in citations:
    title = rec.get('title')
    # citation_count may be string; convert
    try:
        count = int(rec.get('citation_count', 0))
    except:
        try:
            count = int(float(rec.get('citation_count', 0)))
        except:
            count = 0
    if title in chi_titles:
        matched.append({'title': title, 'citation_count': count})
        total += count
# Sort matched by citation_count desc
matched.sort(key=lambda x: x['citation_count'], reverse=True)
result = {'papers': matched, 'total_citations_2020': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_mALohj97VQIHLtJCzMrobCxP': 'file_storage/call_mALohj97VQIHLtJCzMrobCxP.json', 'var_call_dBdXXP4YxJcrzw7ffnEyjiT0': 'file_storage/call_dBdXXP4YxJcrzw7ffnEyjiT0.json', 'var_call_gS9FjovkeX8vVLVyMkvIOCen': 'file_storage/call_gS9FjovkeX8vVLVyMkvIOCen.json'}

exec(code, env_args)
