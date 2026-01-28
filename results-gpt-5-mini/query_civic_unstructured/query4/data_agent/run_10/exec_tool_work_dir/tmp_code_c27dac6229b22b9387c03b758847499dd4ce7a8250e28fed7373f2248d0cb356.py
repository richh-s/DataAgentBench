code = """import json
import re
from pathlib import Path

# Load data from storage-provided file paths
civic_path = Path(var_call_6ucBW9CpzEmskz35MPLVZQtx)
funding_path = Path(var_call_mMh9v7wutsXN4RBP52G2aHU6)

civic = json.loads(civic_path.read_text())
funding = json.loads(funding_path.read_text())

# normalize function
def norm(s):
    s = s.lower()
    s = re.sub(r"\(.*?\)", "", s)  # remove parenthetical suffixes
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

# season-year patterns to search for Spring 2022
patterns = [
    r"spring\s*,?\s*2022",
    r"2022\s*-\s*spring",
    r"march\s+2022",
    r"april\s+2022",
    r"may\s+2022",
    r"2022-03",
    r"2022-04",
    r"2022-05",
    r"03-2022",
    r"04-2022",
    r"05-2022",
    r"03/2022",
    r"04/2022",
    r"05/2022"
]
pattern_re = re.compile("(" + ")|(".join(patterns) + ")", re.IGNORECASE)

extracted_projects = []

for doc in civic:
    text = doc.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if pattern_re.search(line):
            # look backwards up to 10 lines to find a project title
            title = None
            for j in range(i-1, max(i-12, -1), -1):
                cand = lines[j].strip()
                if not cand:
                    continue
                # skip lines that look like headers or labels
                low = cand.lower()
                if any(low.startswith(x) for x in ['updates', 'project schedule', 'project description', 'project updates', 'estimated schedule', 'agenda item', 'page', 'subject', 'to:', 'prepared by', 'approved by', 'date prepared']):
                    continue
                # if line is short but contains letters, consider it a title
                if len(cand) > 3:
                    title = cand
                    break
            if title:
                extracted_projects.append(title)

# Deduplicate and clean
unique_projects = []
seen = set()
for p in extracted_projects:
    np = re.sub(r'\s+', ' ', p).strip()
    if np.lower() not in seen:
        seen.add(np.lower())
        unique_projects.append(np)

# Prepare funding records
for r in funding:
    # ensure Amount numeric
    try:
        r['Amount'] = int(r['Amount'])
    except:
        # if empty or bad, set 0
        r['Amount'] = 0

# Build token sets for funding names
def tokens(s):
    s2 = norm(s)
    return set(s2.split())

funding_tokens = [(r['Project_Name'], tokens(r['Project_Name']), r['Amount']) for r in funding]

matched_funding_rows = []
project_matches = {}

for proj in unique_projects:
    pnorm = norm(proj)
    ptoks = set(pnorm.split())
    matches = []
    for name, ftoks, amt in funding_tokens:
        # direct substring match
        if pnorm and pnorm in norm(name):
            matches.append((name, amt))
            continue
        # token overlap
        if ptoks and ftoks:
            inter = ptoks & ftoks
            union = ptoks | ftoks
            score = len(inter) / max(1, len(union))
            if score >= 0.4:
                matches.append((name, amt))
    # record
    project_matches[proj] = matches
    for m in matches:
        matched_funding_rows.append(m)

# Count projects that were identified as starting in Spring 2022
projects_count = len(unique_projects)

# Sum funding for matched funding rows, avoiding duplicate funding rows counted multiple times
# matched_funding_rows contains tuples (name, amt)
seen_rows = set()
total_funding = 0
for name, amt in matched_funding_rows:
    if name not in seen_rows:
        seen_rows.add(name)
        total_funding += amt

# Also include projects that had no matches: they contribute 0 funding

result = {
    'spring_2022_projects_count': projects_count,
    'total_funding': total_funding,
    'matched_projects': project_matches
}

# Prepare printable JSON string (ensure serializable)
out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_TqOXjmDcN9CqXType328F016': ['civic_docs'], 'var_call_waQ4ta3rrchXTbG69iUW6xYG': ['Funding'], 'var_call_6ucBW9CpzEmskz35MPLVZQtx': 'file_storage/call_6ucBW9CpzEmskz35MPLVZQtx.json', 'var_call_mMh9v7wutsXN4RBP52G2aHU6': 'file_storage/call_mMh9v7wutsXN4RBP52G2aHU6.json'}

exec(code, env_args)
