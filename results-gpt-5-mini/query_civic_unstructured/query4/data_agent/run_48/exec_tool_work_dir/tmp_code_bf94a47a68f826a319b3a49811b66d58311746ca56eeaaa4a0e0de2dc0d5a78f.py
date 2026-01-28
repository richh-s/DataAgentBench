code = """import json, re
# Load the civic docs query result JSON file path from storage variable
path = var_call_BbHlkOS5ptYiDuPuA4GtohCC
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

patterns = [r"\bSpring\s*2022\b", r"\b2022[-\s]*Spring\b", r"\bMarch\s*2022\b", r"\bApril\s*2022\b", r"\bMay\s*2022\b", r"\bMar\.?\s*2022\b", r"\bApr\.?\s*2022\b", r"\bMay\.?\s*2022\b", r"2022-03", r"2022-04", r"2022-05"]
pattern = re.compile("(?:" + ")|(?:".join(patterns) + ")", re.IGNORECASE)

found_projects = []

for doc in docs:
    text = doc.get('text', '')
    for m in pattern.finditer(text):
        start = m.start()
        # look backwards up to 800 chars to find preceding lines
        window_start = max(0, start-800)
        snippet = text[window_start:start]
        lines = snippet.splitlines()
        # iterate backwards to find a candidate title
        candidate = None
        for line in reversed(lines[-12:]):
            s = line.strip()
            if not s:
                continue
            low = s.lower()
            # skip common labels and meta lines
            if any(tok in low for tok in ['updates', 'project schedule', 'project description', 'page', 'agenda', 'item', 'approved by', 'date prepared', 'meeting date', 'recommended action', 'discussion', 'subject']):
                continue
            if s.startswith('(') or s.startswith('cid:'):
                continue
            # skip short noise lines
            if len(s) < 4:
                continue
            # prefer lines containing 'Project' or keywords
            if 'project' in low or any(k in low for k in ['park', 'road', 'repair', 'improvements', 'retaining wall', 'playground', 'water', 'drain', 'storm', 'median', 'skate', 'walkway', 'slope', 'traffic', 'signal', 'shade']):
                candidate = s
                break
            # otherwise pick a reasonably long capitalized line
            words = s.split()
            cap_words = sum(1 for w in words if w and w[0].isupper())
            if len(s) > 20 and cap_words >= max(2, len(words)//2):
                candidate = s
                break
        if not candidate:
            # fallback: nearest non-empty line
            for line in reversed(lines[-12:]):
                s = line.strip()
                if s and not s.startswith('('):
                    candidate = s
                    break
        if candidate:
            # clean candidate
            candidate = candidate.rstrip(':').strip()
            # filter out lines that are clearly not project names
            if len(candidate) > 2 and not candidate.lower().startswith('page'):
                found_projects.append(candidate)

# deduplicate while preserving order
seen = set()
proj_list = []
for p in found_projects:
    if p not in seen:
        seen.add(p)
        proj_list.append(p)

# Prepare JSON-serializable output
out = json.dumps(proj_list)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_BbHlkOS5ptYiDuPuA4GtohCC': 'file_storage/call_BbHlkOS5ptYiDuPuA4GtohCC.json'}

exec(code, env_args)
