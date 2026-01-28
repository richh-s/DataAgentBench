code = """import json, re

# Load the civic docs query result stored in the file path variable
path = var_call_CXyxXVPH2gGXd2Rsb1S2p8Td
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

spring_patterns = [r"Spring\s*,?\s*2022", r"2022\s*-?\s*Spring", r"March\s+2022", r"April\s+2022", r"May\s+2022", r"2022-March", r"2022-April", r"2022-May", r"2022-03", r"2022-04", r"2022-05", r"\bMar\b\s*2022", r"\bApr\b\s*2022", r"\bMay\b\s*2022"]
pattern = re.compile("(" + ")|(".join(spring_patterns) + ")", re.IGNORECASE)

candidates = []

for doc in docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if pattern.search(line):
            # walk upwards to find a plausible project title
            for j in range(i-1, max(i-20, -1), -1):
                prev = lines[j].strip()
                if not prev:
                    continue
                low = prev.lower()
                # skip lines that are clearly not titles
                if any(k in low for k in ['updates', 'project schedule', 'cid', 'item', 'page', 'agenda', 'meeting', 'date', 'recommended action', 'discussion', 'to:','subject', 'prepared by', 'approved by']):
                    continue
                if ':' in prev:
                    # often lines with ':' are headers, skip
                    continue
                # length heuristic
                if len(prev) > 200:
                    continue
                # avoid lines that look like paragraphs (contain many spaces and lowercase)
                # allow Title Case lines
                candidates.append(prev)
                break

# de-duplicate preserving order
seen = set()
projects = []
for p in candidates:
    key = p.strip()
    if key and key not in seen:
        seen.add(key)
        projects.append(key)

# Output results as JSON-serializable list
result = json.dumps(projects)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_BT53iOXDUlKYiILn447GjfpJ': [], 'var_call_dqgmrJKK5TBMw3nz65PRF9uh': ['civic_docs'], 'var_call_CXyxXVPH2gGXd2Rsb1S2p8Td': 'file_storage/call_CXyxXVPH2gGXd2Rsb1S2p8Td.json'}

exec(code, env_args)
