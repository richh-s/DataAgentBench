code = """import json, re, sys
# Retry with more efficient parsing: read file in streaming fashion
path = var_call_lSzGGgcV43Dols6dymGaHsSq
lang_map = {}
pattern = re.compile(r"([^,()]+?)\s*\(([\d,]+)\s*bytes\)")
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
    for entry in data:
        rn = entry.get('repo_name')
        desc = entry.get('language_description') or ''
        matches = pattern.findall(desc)
        if not matches:
            continue
        best_lang = None
        best_bytes = -1
        for m in matches:
            lang = m[0].strip()
            bytes_str = m[1].replace(',', '')
            try:
                b = int(bytes_str)
            except:
                b = 0
            if b > best_bytes:
                best_bytes = b
                best_lang = lang
        if best_lang:
            lang_map[rn] = best_lang

commits = var_call_DkgbLHaYHJmrmIRbXeKPKD9C
rows = []
for c in commits:
    rn = c.get('repo_name')
    cnt = c.get('commit_count')
    try:
        cnt_int = int(cnt)
    except:
        cnt_int = 0
    main_lang = lang_map.get(rn)
    if main_lang and main_lang.strip().lower() == 'python':
        continue
    if not main_lang:
        continue
    rows.append((rn, cnt_int, main_lang))

rows_sorted = sorted(rows, key=lambda x: x[1], reverse=True)[:5]
result = [r[0] for r in rows_sorted]
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_9MUDTBzI8iXiepI7mwBRRuh6': ['languages', 'repos', 'licenses'], 'var_call_LGHyHr7KzzVs0l56liOSaRFm': ['commits', 'contents', 'files'], 'var_call_lSzGGgcV43Dols6dymGaHsSq': 'file_storage/call_lSzGGgcV43Dols6dymGaHsSq.json', 'var_call_DkgbLHaYHJmrmIRbXeKPKD9C': [{'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'facebook/react', 'commit_count': '178'}]}

exec(code, env_args)
