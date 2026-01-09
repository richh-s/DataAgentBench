code = """import json, re
import pandas as pd

# load mongo docs (may be a file path)
raw = var_call_fXcE8gcML1dtHYH4pToQFkoT
if isinstance(raw, str):
    with open(raw, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = raw

spring_patterns = [
    r"\bSpring\s*2022\b",
    r"\b2022\s*[-–]\s*Spring\b",
    r"\b2022\s*Spring\b",
]
month_pat = re.compile(r"\b(March|April|May)\s+2022\b", re.IGNORECASE)

# capture 'Project Schedule' blocks with lines like 'Begin Construction: Fall 2023'
# We'll treat a project as started in Spring 2022 if within its nearby schedule block there is a line containing 'Begin' or 'Start' with Spring 2022.

project_start_spring2022 = set()

# heuristic: find headings (project names) as standalone lines (no colon) followed by optional blocks until next blank line and next heading.
for d in docs:
    text = d.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]

    current_project = None
    buffer = []

    def flush():
        nonlocal current_project, buffer
        if current_project and buffer:
            blk = "\n".join(buffer)
            if re.search(r"\b(Begin|Start)(?:\s+\w+){0,3}\s*:\s*Spring\s+2022\b", blk, re.IGNORECASE) or \
               re.search(r"\b(Begin|Start)(?:\s+\w+){0,3}\s*:\s*2022\s*[-–]?\s*Spring\b", blk, re.IGNORECASE) or \
               re.search(r"\b(Begin|Start)(?:\s+\w+){0,3}\s*:\s*(March|April|May)\s+2022\b", blk, re.IGNORECASE):
                project_start_spring2022.add(current_project)
        current_project = None
        buffer = []

    for ln in lines:
        # detect project name line: non-empty, no leading bullets, not 'Project Schedule' etc, and followed by later 'Updates:' in buffer.
        if ln and (':' not in ln) and not ln.startswith(('(', 'cid', 'Page', 'Agenda', 'Public', 'To', 'Prepared', 'Approved', 'Date', 'Meeting', 'Subject', 'RECOMMENDED', 'DISCUSSION', 'Capital Improvement', 'Disaster Recovery', 'Project Description', 'Project Updates', 'Project Schedule', 'Estimated Schedule')):
            # Many non-project lines exist; add extra heuristic: title case and length < 80
            if len(ln) < 80 and re.search(r"[A-Za-z]", ln):
                # start new project; flush previous
                flush()
                current_project = ln
                buffer = []
                continue
        if current_project:
            buffer.append(ln)
    flush()

# If none found via begin/start lines, fall back to any block containing 'Spring 2022' near a project schedule label.
if not project_start_spring2022:
    for d in docs:
        text = d.get('text','')
        if 'Spring 2022' not in text and '2022-Spring' not in text and '2022 Spring' not in text:
            continue
        # naive: capture previous non-empty line as project
        for m in re.finditer(r"Spring\s+2022|2022\s*[-–]\s*Spring|2022\s+Spring|(?:March|April|May)\s+2022", text, re.IGNORECASE):
            before = text[:m.start()].splitlines()
            cand = ''
            for ln in reversed(before):
                ln=ln.strip()
                if ln and ':' not in ln and len(ln)<80:
                    cand=ln
                    break
            if cand:
                project_start_spring2022.add(cand)

projects = sorted(project_start_spring2022)

print('__RESULT__:')
print(json.dumps({'projects': projects, 'count': len(projects)}))"""

env_args = {'var_call_TlI74jLg2bFHKmzFuVk7AJqM': ['Funding'], 'var_call_5wzrwfkZwg9a9BZl1um4J4FU': ['civic_docs'], 'var_call_fXcE8gcML1dtHYH4pToQFkoT': 'file_storage/call_fXcE8gcML1dtHYH4pToQFkoT.json'}

exec(code, env_args)
