code = """import re, json, pandas as pd, os, textwrap

# Load full civic docs
path_docs = var_call_uAVRSBcehtbSQDZ1WQdvQPUW
with open(path_docs, 'r') as f:
    docs = json.load(f)

texts = [d['text'] for d in docs]

# Very heuristic extraction: split on double newlines, treat lines that look like project titles
projects = []
for text in texts:
    for line in text.split('\n'):
        s = line.strip()
        if not s:
            continue
        # consider as potential project line if it has 'Park' in name or 'playground' etc.
        if re.search(r"park|Playground", s, re.IGNORECASE):
            # try to capture completion info nearby (look ahead few lines)
            snippet = textwrap.shorten(s, width=200)
            projects.append({"Project_Name": s})

# Deduplicate names
unique_names = sorted(set(p['Project_Name'] for p in projects))

# Now, we specifically search for park-related projects completed in 2022 in text to get names
park_2022_completed = set()
for text in texts:
    # simple window search
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if re.search(r"completed", line, re.IGNORECASE) and '2022' in line:
            # look backwards for a line mentioning Park
            for j in range(max(0, i-5), i):
                if re.search(r"park", lines[j], re.IGNORECASE):
                    name = lines[j].strip()
                    if len(name) > 3:
                        park_2022_completed.add(name)

park_2022_completed = sorted(park_2022_completed)

result = {"park_2022_completed_projects": park_2022_completed}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_uAVRSBcehtbSQDZ1WQdvQPUW': 'file_storage/call_uAVRSBcehtbSQDZ1WQdvQPUW.json', 'var_call_6LzlQsqgli9cEEFoQlzFdqo8': 'file_storage/call_6LzlQsqgli9cEEFoQlzFdqo8.json', 'var_call_DNEn2Q6SiNqGrClNN258hjkD': ['civic_docs'], 'var_call_iUQqUdxYJQoU6mCLQL9w7hGu': ['Funding']}

exec(code, env_args)
