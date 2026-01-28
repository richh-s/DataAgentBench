code = """import json, re, os
# load variables (handle either direct data or file path)
def load_var(v):
    if isinstance(v, str) and v.endswith('.json') and os.path.exists(v):
        with open(v, 'r') as f:
            return json.load(f)
    return v

var_mapping = load_var(var_call_Zgu0dlOfqao34ryZI7bLTHJA)
var_projinfo = load_var(var_call_iEEmLfxD9Rf5lxvvk0JlBkg4)

mapping = var_mapping.get('mapping') if isinstance(var_mapping, dict) else var_mapping
projinfo = var_projinfo

# build repo -> stars mapping
repo_stars = {}
num_parsed = 0
for entry in projinfo:
    pi = entry.get('Project_Information') or ''
    # find repo pattern owner/repo
    m = re.search(r'([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)', pi)
    if not m:
        continue
    repo = m.group(1)
    # find stars number
    stars = None
    # patterns to match numbers with commas
    patterns = [r'has (?:garnered a total of |a total of |currently has |)([0-9,]+) stars',
                r'stars count of ([0-9,]+)',
                r'([0-9,]+) stars',
                r'has a total of ([0-9,]+) stars',
                r'currently has [0-9,]+ open issues, ([0-9,]+) stars',
                r'currently has [0-9,]+ open issues, ([0-9,]+) stars']
    for pat in patterns:
        mm = re.search(pat, pi)
        if mm:
            try:
                stars = int(mm.group(1).replace(',',''))
                break
            except:
                continue
    if stars is None:
        # try alternate 'with an impressive 10,249 stars' capture numbers before 'stars'
        mm = re.search(r'([0-9,]+)\s+stars', pi)
        if mm:
            try:
                stars = int(mm.group(1).replace(',',''))
            except:
                stars = None
    if stars is None:
        # could be '0 stars' etc
        mm = re.search(r'0\s+stars', pi)
        if mm:
            stars = 0
    if stars is None:
        continue
    # store maximum if duplicates
    if repo in repo_stars:
        repo_stars[repo] = max(repo_stars[repo], stars)
    else:
        repo_stars[repo] = stars
    num_parsed += 1

# associate mapping entries with stars
records = []
for m in mapping:
    repo = m.get('ProjectName')
    if not repo:
        continue
    stars = repo_stars.get(repo)
    if stars is None:
        continue
    records.append({'Name': m.get('Name'), 'Version': m.get('Version'), 'ProjectName': repo, 'Stars': stars})

# deduplicate by package name keeping unique (there should be one per latest)
# sort by stars desc
records_sorted = sorted(records, key=lambda x: x['Stars'], reverse=True)
# take top 5
top5 = records_sorted[:5]

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_wTx4WUlrMN0IMwtp8pOPhILg': 'file_storage/call_wTx4WUlrMN0IMwtp8pOPhILg.json', 'var_call_dFPubGgWvKq7qBzs9pPNNtw9': 'file_storage/call_dFPubGgWvKq7qBzs9pPNNtw9.json', 'var_call_Zgu0dlOfqao34ryZI7bLTHJA': 'file_storage/call_Zgu0dlOfqao34ryZI7bLTHJA.json', 'var_call_iEEmLfxD9Rf5lxvvk0JlBkg4': 'file_storage/call_iEEmLfxD9Rf5lxvvk0JlBkg4.json'}

exec(code, env_args)
