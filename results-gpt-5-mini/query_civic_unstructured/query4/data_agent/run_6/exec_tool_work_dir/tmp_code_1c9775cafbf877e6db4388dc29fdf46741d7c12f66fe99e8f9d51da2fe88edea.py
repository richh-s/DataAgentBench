code = """import json
# Load the civic docs query result saved to a file path
path = var_call_WQOnz4h2kKRYxFLRC3s88Esu
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

keywords = ['project','repair','improvements','improvement','study','plan','park','water','road','drain','playground','slope','resurfacing']
projects = set()

for doc in docs:
    text = doc.get('text','')
    lower = text.lower()
    # search for occurrences of 'spring' near '2022'
    idx = 0
    while True:
        i = lower.find('spring', idx)
        if i == -1:
            break
        # check if '2022' occurs within 80 chars after or before
        window_start = max(0, i-200)
        window_end = min(len(lower), i+200)
        window = lower[window_start:window_end]
        if '2022' in window or '2022' in lower[window_start:window_end]:
            # find previous non-empty line
            prev_segment = text[window_start:i]
            lines = prev_segment.strip().splitlines()
            if lines:
                candidate = lines[-1].strip()
                if 3 < len(candidate) < 200 and any(k in candidate.lower() for k in keywords):
                    projects.add(candidate)
        idx = i+6
    # search for months March/April/May with 2022
    for month in ['march','april','may']:
        idx = 0
        while True:
            i = lower.find(month, idx)
            if i == -1:
                break
            window_start = max(0, i-200)
            window = lower[window_start:i+200]
            if '2022' in window:
                prev_segment = text[window_start:i]
                lines = prev_segment.strip().splitlines()
                if lines:
                    candidate = lines[-1].strip()
                    if 3 < len(candidate) < 200 and any(k in candidate.lower() for k in keywords):
                        projects.add(candidate)
            idx = i+len(month)
    # also look for lines that contain 'Project' and within next 200 chars mention spring and 2022
    lines = text.splitlines()
    for idx_line, line in enumerate(lines):
        if 'project' in line.lower() or any(k in line.lower() for k in ['repair','improvements','improvement','study','slope','resurfacing']):
            # look ahead few lines
            ahead = '\n'.join(lines[idx_line:idx_line+6]).lower()
            if 'spring' in ahead and '2022' in ahead:
                candidate = line.strip()
                if 3 < len(candidate) < 200:
                    projects.add(candidate)

projects_list = sorted(projects)
import json
out = json.dumps({"projects": projects_list})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_hSIn0HXpIysBJLncOq2LulYt': ['civic_docs'], 'var_call_6f74mMKpIuCBNIwpLg5yIUV5': ['Funding'], 'var_call_WQOnz4h2kKRYxFLRC3s88Esu': 'file_storage/call_WQOnz4h2kKRYxFLRC3s88Esu.json'}

exec(code, env_args)
