code = """import json
import re

# Load data
with open(locals()['var_function-call-105374427897259333'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-105374427897260990'], 'r') as f:
    civic_docs = json.load(f)

project_amounts = {}
for row in funding_data:
    project_amounts[row['Project_Name']] = row['Amount']

project_names = list(project_amounts.keys())
project_names.sort(key=len, reverse=True)

matched_projects = set()

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
    
    # Handle overlaps
    by_start = {}
    for idx, name in found_indices:
        if idx not in by_start:
            by_start[idx] = []
        by_start[idx].append(name)
        
    sorted_starts = sorted(by_start.keys())
    final_segments = []
    last_end = -1
    
    for start in sorted_starts:
        if start < last_end:
            continue
        names = by_start[start]
        longest_name = max(names, key=len)
        end = start + len(longest_name)
        final_segments.append((start, longest_name))
        last_end = end
        
    for i in range(len(final_segments)):
        idx, p_name = final_segments[i]
        if i + 1 < len(final_segments):
            next_idx = final_segments[i+1][0]
            segment_text = text[idx:next_idx]
        else:
            segment_text = text[idx:]
        
        lower_seg = segment_text.lower()
        lower_name = p_name.lower()
        
        # Check Park
        is_park = False
        if "park" in lower_name or "playground" in lower_name:
            is_park = True
        elif re.search(r'\\bpark\\b', lower_seg) or re.search(r'\\bplayground\\b', lower_seg):
            is_park = True
            
        # Check Completed 2022
        is_completed_2022 = False
        if "2022" in lower_seg:
            lines = segment_text.split('\\n')
            for line in lines:
                l_line = line.lower()
                if "2022" in l_line:
                    # Check for completion
                    if "construction was completed" in l_line:
                        is_completed_2022 = True
                    elif ("completed" in l_line or "complete" in l_line) and "design" not in l_line:
                         if "construction" in l_line or "project" in l_line or "updates" in l_line:
                             is_completed_2022 = True

        if is_park and is_completed_2022:
            matched_projects.add(p_name)

total_funding = 0
for p in matched_projects:
    total_funding += int(project_amounts[p])

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "matched_projects": list(matched_projects)}))"""

env_args = {'var_function-call-105374427897260990': 'file_storage/function-call-105374427897260990.json', 'var_function-call-105374427897259333': 'file_storage/function-call-105374427897259333.json'}

exec(code, env_args)
