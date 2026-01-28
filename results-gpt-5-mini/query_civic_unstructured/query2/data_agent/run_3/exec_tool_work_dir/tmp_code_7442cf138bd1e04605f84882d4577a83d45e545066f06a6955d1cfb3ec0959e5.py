code = """import json, re
# var_call_lGT6WoCuyWvDkZO6yDO1wveb is a string path to the JSON result file
p = var_call_lGT6WoCuyWvDkZO6yDO1wveb
with open(p, 'r', encoding='utf-8') as f:
    docs = json.load(f)

found = []
for doc in docs:
    text = doc.get('text','')
    # Pattern 1: heading then (cid:...) Updates and somewhere 'completed' with 2022
    for m in re.finditer(r"([^
]{1,200})\n\n\(cid:[0-9]+\) Updates:.*?(?:completed|Construction was completed).*?2022", text, flags=re.I|re.S):
        name = m.group(1).strip()
        # filter out generic headings
        if len(name)>0 and len(name)<200:
            found.append(name)
    # Pattern 2: look for 'Construction was completed' and take prior non-empty line up to 5 lines above
    for m in re.finditer(r"Construction was completed.*?2022", text, flags=re.I|re.S):
        start = m.start()
        segment = text[:start]
        lines = segment.splitlines()
        # find last non-empty line that isn't 'Updates:' or 'Project Schedule:' etc
        for ln in reversed(lines[-10:]):
            ln_strip = ln.strip()
            if not ln_strip:
                continue
            if re.search(r'Updates:|Project Schedule:|Agenda Item', ln_strip, flags=re.I):
                continue
            # take this as name if reasonably short
            if len(ln_strip)<200:
                found.append(ln_strip)
                break
    # Pattern 3: direct headings with Park keyword that are near 'completed' in same paragraph
    paragraphs = re.split(r"\n\n+", text)
    for para in paragraphs:
        if re.search(r'completed.*2022', para, flags=re.I) and re.search(r'park|playground|walkway|shade', para, flags=re.I):
            # take first line as name
            first = para.strip().splitlines()[0].strip()
            if first:
                found.append(first)

# post-process: keep only those that contain park-related keywords or 'Walkway' or 'Playground' or 'Shade' or 'Bluffs' or 'Point Dume'
keywords = re.compile(r'park|playground|walkway|shade|bluffs|point dume|trancas', flags=re.I)
names = []
for n in found:
    if keywords.search(n):
        # clean trailing words like 'Project' or colons
        n2 = re.sub(r'\s*-?\s*Project$','', n, flags=re.I).strip()
        n2 = n2.replace('\r','')
        names.append(n2)

# unique preserving order
seen = set()
unique = []
for n in names:
    if n not in seen:
        seen.add(n)
        unique.append(n)

result = unique
import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_lGT6WoCuyWvDkZO6yDO1wveb': 'file_storage/call_lGT6WoCuyWvDkZO6yDO1wveb.json'}

exec(code, env_args)
