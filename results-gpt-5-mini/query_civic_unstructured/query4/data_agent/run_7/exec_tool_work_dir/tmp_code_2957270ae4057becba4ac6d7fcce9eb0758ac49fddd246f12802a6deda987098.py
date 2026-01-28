code = """import json, re
# Read the Mongo query result stored in var_call_BM51I30oAu2S3Iytx6gDIzK1
with open(var_call_BM51I30oAu2S3Iytx6gDIzK1, 'r', encoding='utf-8') as f:
    docs = json.load(f)

project_names = []
for doc in docs:
    text = doc.get('text', '')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        # Look for lines that indicate a start in Spring 2022
        if re.search(r'(?i)begin\b.*\b(Spring(?:/Summer)?\s*2022|Spring\s*2022|March\s*2022|April\s*2022|May\s*2022)', line):
            # search backwards for a candidate project name
            for k in range(1, 8):
                idx = i - k
                if idx < 0:
                    break
                cand = lines[idx].strip()
                if not cand:
                    continue
                # filter out generic lines
                if re.search(r'(?i)project (?:schedule|description)|updates|agenda|item|page|\(', cand):
                    continue
                # ignore short headers like 'Updates:' or 'Estimated Schedule:'
                if len(cand) > 3 and len(cand) < 150:
                    # normalize whitespace
                    cand_norm = re.sub(r'\s+', ' ', cand)
                    project_names.append(cand_norm)
                    break
        else:
            # also handle lines like 'Complete Final Design: Spring 2022' followed by 'Begin Construction: Spring 2022' captured above
            pass

# deduplicate while preserving order
seen = set()
unique_projects = []
for p in project_names:
    if p not in seen:
        seen.add(p)
        unique_projects.append(p)

# As a fallback, also look for explicit 'Begin Design: Spring 2022' etc. but already covered

# Prepare JSON serializable output
output = unique_projects

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_BM51I30oAu2S3Iytx6gDIzK1': 'file_storage/call_BM51I30oAu2S3Iytx6gDIzK1.json'}

exec(code, env_args)
