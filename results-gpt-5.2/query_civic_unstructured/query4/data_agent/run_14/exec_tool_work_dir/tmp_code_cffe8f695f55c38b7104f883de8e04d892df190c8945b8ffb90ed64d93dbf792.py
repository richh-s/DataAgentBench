code = """import json, re

path = var_call_RrmAuwXmqg52X8TuT8IIP0jf
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

projects = set()

# capture blocks where a project name is a standalone line followed later by 'Begin Construction: Spring 2022'
pat_begin = re.compile(r'Begin\s+Construction\s*:\s*Spring\s+2022\b', re.IGNORECASE)

for d in docs:
    lines = [ln.strip() for ln in d.get('text','').splitlines()]
    for i, ln in enumerate(lines):
        if ln and pat_begin.search("\n".join(lines[i:i+20])):
            # search backwards for nearest plausible project title within previous 15 lines
            title = None
            for j in range(i-1, max(-1, i-20), -1):
                cand = lines[j].strip()
                if not cand:
                    continue
                if ':' in cand:
                    continue
                if cand.startswith(('(cid', '•', '-', '–')):
                    continue
                if len(cand) < 4 or len(cand) > 120:
                    continue
                # stop if reach section headers
                low = cand.lower()
                if 'project schedule' in low or 'estimated schedule' in low or low.startswith('capital improvement projects') or low.startswith('disaster projects'):
                    continue
                # accept as title
                title = cand
                break
            if title:
                projects.add(title)

print('__RESULT__:')
print(json.dumps(sorted(projects)))"""

env_args = {'var_call_GU7TOrWp60QnSxcfBDDbjJb3': ['civic_docs'], 'var_call_oT345mwgQj4Nim0YXkOkj7b9': ['Funding'], 'var_call_4kyFbfoBMGRtUpextA1f4p3h': 'file_storage/call_4kyFbfoBMGRtUpextA1f4p3h.json', 'var_call_RrmAuwXmqg52X8TuT8IIP0jf': 'file_storage/call_RrmAuwXmqg52X8TuT8IIP0jf.json'}

exec(code, env_args)
