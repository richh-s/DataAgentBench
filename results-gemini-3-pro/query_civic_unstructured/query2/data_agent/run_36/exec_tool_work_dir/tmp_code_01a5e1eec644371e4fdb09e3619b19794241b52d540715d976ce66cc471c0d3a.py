code = """import json

with open(locals()['var_function-call-105374427897259333'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-105374427897260990'], 'r') as f:
    civic_docs = json.load(f)

project_names = [r['Project_Name'] for r in funding_data]
project_names.sort(key=len, reverse=True)

results = []

for doc in civic_docs:
    text = doc['text']
    found_indices = []
    for p_name in project_names:
        start = 0
        while True:
            idx = text.lower().find(p_name.lower(), start)
            if idx == -1:
                break
            found_indices.append((idx, p_name))
            start = idx + len(p_name)
    found_indices.sort(key=lambda x: x[0])
    
    by_start = {}
    for idx, name in found_indices:
        if idx not in by_start:
            by_start[idx] = []
        by_start[idx].append(name)
    
    sorted_starts = sorted(by_start.keys())
    final_segments = []
    last_end = -1
    for start in sorted_starts:
        if start < last_end: continue
        longest_name = max(by_start[start], key=len)
        end = start + len(longest_name)
        final_segments.append((start, longest_name))
        last_end = end

    for i in range(len(final_segments)):
        idx, p_name = final_segments[i]
        if "park" in p_name.lower() or "playground" in p_name.lower():
            if i + 1 < len(final_segments):
                seg_text = text[idx:final_segments[i+1][0]]
            else:
                seg_text = text[idx:]
            
            clean_seg = seg_text.replace('\\n', ' ')[:300]
            results.append({"project": p_name, "preview": clean_seg})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-105374427897260990': 'file_storage/function-call-105374427897260990.json', 'var_function-call-105374427897259333': 'file_storage/function-call-105374427897259333.json', 'var_function-call-14205364589829705343': {'total_funding': 21000, 'matched_projects': ['Bluffs Park Shade Structure']}}

exec(code, env_args)
