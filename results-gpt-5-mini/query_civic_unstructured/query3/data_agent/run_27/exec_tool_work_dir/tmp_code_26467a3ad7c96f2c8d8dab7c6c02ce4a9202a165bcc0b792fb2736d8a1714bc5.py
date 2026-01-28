code = """import json

path = var_call_bnz5n8E8p3dgBfZPrwv4WgyV
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

found = []
seen = set()

for doc in docs:
    text = doc.get('text','')
    lowtext = text.lower()
    if 'fema' not in lowtext and 'emergency' not in lowtext:
        continue
    lines = text.splitlines()
    for idx, line in enumerate(lines):
        s = line.strip()
        if not s:
            continue
        if len(s) < 5 or len(s) > 200:
            continue
        low = s.lower()
        # candidate title heuristics
        if ('project' in low) or low.endswith('repairs') or low.endswith('improvements') or 'fema' in low or 'emergency' in low or 'disaster' in low:
            # ensure starts with uppercase letter or digit
            if not s[0].isalnum() and not s[0].isupper():
                # allow if first char is '(' or uppercase after
                pass
            # check surrounding context for status keywords
            start = max(0, idx-6)
            window = '\n'.join(lines[start: idx+7]).lower()
            status = None
            if 'completed' in window or 'construction was completed' in window or 'complete construction' in window:
                status = 'completed'
            elif 'design' in window or 'final design' in window or 'complete design' in window or 'preliminary design' in window:
                status = 'design'
            elif 'not started' in window or ('identified' in window and 'project' in window):
                status = 'not started'
            pname = ' '.join(s.split())
            if pname not in seen:
                seen.add(pname)
                found.append({'Project_Name': pname, 'Status': status})

# Also try to capture lines that explicitly mention '(FEMA Project)'
for doc in docs:
    text = doc.get('text','')
    lower = text.lower()
    pos = 0
    while True:
        i = lower.find('(fema project)', pos)
        if i == -1:
            break
        # find preceding line
        before = text[:i].rstrip('\n')
        parts = before.splitlines()
        if parts:
            candidate = parts[-1].strip()
            if candidate and len(candidate) < 200:
                pname = ' '.join(candidate.split())
                if pname not in seen:
                    # infer status from nearby
                    start = max(0, i-200)
                    window = text[start: i+200].lower()
                    status = None
                    if 'completed' in window:
                        status = 'completed'
                    elif 'design' in window:
                        status = 'design'
                    elif 'not started' in window:
                        status = 'not started'
                    seen.add(pname)
                    found.append({'Project_Name': pname, 'Status': status})
        pos = i+1

print("__RESULT__:")
print(json.dumps(found))"""

env_args = {'var_call_bnz5n8E8p3dgBfZPrwv4WgyV': 'file_storage/call_bnz5n8E8p3dgBfZPrwv4WgyV.json'}

exec(code, env_args)
