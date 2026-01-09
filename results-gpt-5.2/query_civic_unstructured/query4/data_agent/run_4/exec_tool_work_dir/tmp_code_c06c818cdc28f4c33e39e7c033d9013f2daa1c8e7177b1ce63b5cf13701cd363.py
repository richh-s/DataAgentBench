code = """import json, re
raw = var_call_fXcE8gcML1dtHYH4pToQFkoT
if isinstance(raw, str):
    with open(raw, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = raw

project_start_spring2022 = set()

begin_pat = re.compile(r"\b(Begin|Start)(?:\s+\w+){0,4}\s*:\s*(Spring\s+2022|2022\s*[-–]?\s*Spring|(March|April|May)\s+2022)\b", re.IGNORECASE)
any_spring_pat = re.compile(r"(Spring\s+2022|2022\s*[-–]?\s*Spring|(March|April|May)\s+2022)", re.IGNORECASE)

skip_prefixes = ('(', 'cid', 'Page', 'Agenda', 'Public', 'To', 'Prepared', 'Approved', 'Date', 'Meeting', 'Subject', 'RECOMMENDED', 'DISCUSSION', 'Capital Improvement', 'Disaster Recovery', 'Project Description', 'Project Updates', 'Project Schedule', 'Estimated Schedule')

for d in docs:
    text = d.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    current_project = None
    buffer = []

    def flush():
        nonlocal current_project, buffer
        if current_project and buffer:
            blk = "\\n".join(buffer)
            if begin_pat.search(blk):
                project_start_spring2022.add(current_project)
        current_project = None
        buffer = []

    for ln in lines:
        is_title_candidate = (ln and (':' not in ln) and (not ln.startswith(skip_prefixes)) and len(ln) < 80 and re.search(r"[A-Za-z]", ln))
        if is_title_candidate:
            flush()
            current_project = ln
            buffer = []
            continue
        if current_project is not None:
            buffer.append(ln)
    flush()

if not project_start_spring2022:
    for d in docs:
        text = d.get('text','')
        if not any_spring_pat.search(text):
            continue
        for m in any_spring_pat.finditer(text):
            before_lines = text[:m.start()].splitlines()
            cand = None
            for ln in reversed(before_lines):
                t = ln.strip()
                if t and ':' not in t and len(t) < 80 and not t.startswith(skip_prefixes):
                    cand = t
                    break
            if cand:
                project_start_spring2022.add(cand)

projects = sorted(project_start_spring2022)

print('__RESULT__:')
print(json.dumps({'projects': projects, 'count': len(projects)}))"""

env_args = {'var_call_TlI74jLg2bFHKmzFuVk7AJqM': ['Funding'], 'var_call_5wzrwfkZwg9a9BZl1um4J4FU': ['civic_docs'], 'var_call_fXcE8gcML1dtHYH4pToQFkoT': 'file_storage/call_fXcE8gcML1dtHYH4pToQFkoT.json'}

exec(code, env_args)
