code = """import json
import re

# Load query results from storage variables
# These variables may be file paths (strings) if large; handle both cases.

def load_var(v):
    if isinstance(v, str):
        # assume it's a file path
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

funding = load_var(var_call_SdeIzpwHWXTGbiSgCGNZzY8M)
docs = load_var(var_call_fJ8zcOtfuMJb3QVTDXZxf5ZV)

# Extract funding project names (these records already filtered Amount > 50000)
fund_names = [rec.get('Project_Name','').strip() for rec in funding]

# Normalization helper
import string

def normalize(s):
    s = s.lower()
    # replace punctuation with spaces
    s = re.sub(r"[^a-z0-9]+", ' ', s)
    s = re.sub(r"\s+", ' ', s).strip()
    return s

norm_fund = [normalize(n) for n in fund_names]

# Function to extract project titles from a 'Capital Improvement Projects (Design)' section

def extract_design_titles(text):
    titles = []
    lc = text.lower()
    marker = 'capital improvement projects (design)'
    idx = lc.find(marker)
    if idx == -1:
        return titles
    # find end of section: look for common following headings
    end_markers = ['capital improvement projects (construction)', 'capital improvement projects (not started)', '\n\ncapital improvement projects (construction)', '\n\ncapital improvement projects (not started)']
    end_idx = None
    for em in end_markers:
        j = lc.find(em, idx+len(marker))
        if j != -1:
            if end_idx is None or j < end_idx:
                end_idx = j
    section = text[idx + len(marker): end_idx].strip() if end_idx else text[idx + len(marker):].strip()

    # Find occurrences of 'Updates:' and 'Project Description:' and treat the preceding non-empty line as title
    for m in re.finditer(r'Updates:|Project Description:|Project Updates:|Project Description', section, flags=re.IGNORECASE):
        start = m.start()
        prefix = section[:start].rstrip()
        # get last non-empty line
        lines = prefix.splitlines()
        # walk back to find a candidate title
        for ln in range(len(lines)-1, -1, -1):
            line = lines[ln].strip()
            # skip short or page markers or lines that look like bullets
            if not line:
                continue
            if re.match(r'page \d+ of', line.lower()):
                continue
            if len(line) < 4:
                continue
            # Exclude lines that are clearly section labels
            if re.search(r'project schedule|complete design|advertise|begin construction|updates|agenda item|recommended action|discussion|public works', line, re.IGNORECASE):
                continue
            # Found a candidate
            titles.append(line)
            break

    # Also try to capture titles that appear as standalone headings separated by blank lines before 'Project Schedule' or 'Estimated Schedule'
    for m in re.finditer(r'Project Schedule:|Estimated Schedule:|Project Updates:', section, flags=re.IGNORECASE):
        start = m.start()
        prefix = section[:start].rstrip()
        lines = prefix.splitlines()
        for ln in range(len(lines)-1, -1, -1):
            line = lines[ln].strip()
            if not line or len(line) < 4:
                continue
            if re.search(r'page \d+ of', line.lower()):
                continue
            if re.search(r'updates|project schedule|estimated schedule', line, re.IGNORECASE):
                continue
            titles.append(line)
            break

    # Clean titles: remove repeated header fragments, bullets markers
    clean_titles = []
    for t in titles:
        t2 = t
        # sometimes titles include numbering or item labels; remove leading non-alphanumeric
        t2 = re.sub(r'^[-\d\.\)\s]+', '', t2)
        t2 = re.sub(r'\s+', ' ', t2).strip()
        if t2 and t2.lower() not in [ct.lower() for ct in clean_titles]:
            clean_titles.append(t2)

    return clean_titles

# Aggregate titles from all documents
all_titles = []
for doc in docs:
    text = doc.get('text','')
    titles = extract_design_titles(text)
    all_titles.extend(titles)

# Deduplicate and normalize titles
unique_titles = []
seen = set()
for t in all_titles:
    nt = t.strip()
    if not nt:
        continue
    if nt.lower() in seen:
        continue
    seen.add(nt.lower())
    unique_titles.append(nt)

# If no titles found by heuristics, try a fallback: look for lines under the header separated by double newlines until next header
if not unique_titles:
    for doc in docs:
        text = doc.get('text','')
        lc = text.lower()
        marker = 'capital improvement projects (design)'
        idx = lc.find(marker)
        if idx == -1:
            continue
        section = text[idx+len(marker):]
        # split by double newlines and take lines that look like titles (short)
        parts = [p.strip() for p in section.split('\n\n') if p.strip()]
        for p in parts[:30]:
            # stop if we hit another major heading
            if re.search(r'capital improvement projects \(|capital improvement projects \(|capital improvement projects \(', p, re.IGNORECASE):
                break
            # take first line of p
            line = p.splitlines()[0].strip()
            if len(line) > 4 and len(line) < 200:
                unique_titles.append(line)

# Prepare normalized tokens for matching

def tokens(s):
    return [w for w in normalize(s).split() if w]

norm_fund_list = norm_fund
fund_tok_list = [set(tokens(n)) for n in fund_names]

matched_titles = set()

for title in unique_titles:
    ntitle = normalize(title)
    t_tokens = set(tokens(title))
    for fn, nfn in zip(fund_names, norm_fund_list):
        # direct substring match
        if ntitle in nfn or nfn in ntitle:
            matched_titles.add(title)
            break
        # token overlap
        f_tokens = set(tokens(fn))
        if not t_tokens or not f_tokens:
            continue
        inter = t_tokens.intersection(f_tokens)
        # overlap ratio relative to smaller set
        ratio = len(inter) / min(len(t_tokens), len(f_tokens))
        if ratio >= 0.6:
            matched_titles.add(title)
            break

result_count = len(matched_titles)

# For debugging, you might want to include matched items, but we will only output the count as required.

print("__RESULT__:")
print(json.dumps(result_count))"""

env_args = {'var_call_SdeIzpwHWXTGbiSgCGNZzY8M': 'file_storage/call_SdeIzpwHWXTGbiSgCGNZzY8M.json', 'var_call_fJ8zcOtfuMJb3QVTDXZxf5ZV': 'file_storage/call_fJ8zcOtfuMJb3QVTDXZxf5ZV.json'}

exec(code, env_args)
