code = """import json, re
# load the stored query results
fp_latest = var_call_odEChWwbyx3ZSKtoFlIj7SPR
fp_pp = var_call_eQzyT8z7ifD8VFtKdZCFk1cg
fp_info = var_call_f9EegKMFs4uCCzbPvb1PZAYw
with open(fp_latest) as f:
    latest = json.load(f)
with open(fp_pp) as f:
    pp = json.load(f)
with open(fp_info) as f:
    infos = json.load(f)
# build mapping from (Name,Version) to project names (GITHUB)
from collections import defaultdict
pv_map = defaultdict(set)
for r in pp:
    if r.get('System')!='NPM':
        continue
    name = r.get('Name')
    version = r.get('Version')
    ptype = r.get('ProjectType')
    pname = r.get('ProjectName')
    if name and version and pname and ptype and ptype.upper()=='GITHUB':
        pv_map[(name,version)].add(pname)
# build list of latest unique (Name,Version)
pairs = []
seen = set()
for r in latest:
    if r.get('System')!='NPM':
        continue
    name = r.get('Name')
    version = r.get('Version')
    if not name or not version:
        continue
    if (name,version) in seen:
        continue
    seen.add((name,version))
    pairs.append((name,version))
# prepare info texts
info_texts = [ (i.get('Project_Information') or '', i) for i in infos ]

# regex to find stars
star_re = re.compile(r'([0-9][0-9,]*)\s*(?:stars|star)', re.I)
# helper to extract stars from text
def extract_stars(text):
    if not text:
        return None
    m = star_re.search(text)
    if not m:
        return None
    s = m.group(1).replace(',','')
    try:
        return int(s)
    except:
        return None

results = []
for name, version in pairs:
    projects = pv_map.get((name,version), [])
    best = {'project': None, 'stars': 0}
    # if no project mapping, skip
    if not projects:
        # we may still try to find any info that mentions the package name? but skip
        results.append({'package': name, 'version': version, 'stars': 0, 'project': None})
        continue
    for proj in projects:
        proj_lower = proj.lower()
        # find matching info entries where Project_Information contains proj
        matched = []
        for txt, row in info_texts:
            if not txt:
                continue
            if proj_lower in txt.lower():
                matched.append((txt,row))
        # if no matched, still attempt to parse infos where repo appears differently? skip
        max_stars_for_proj = None
        for txt,row in matched:
            s = extract_stars(txt)
            if s is not None:
                if max_stars_for_proj is None or s>max_stars_for_proj:
                    max_stars_for_proj = s
        if max_stars_for_proj is None:
            # try to parse any numbers in matched text even if pattern different
            for txt,row in matched:
                # look for 'has a total of X stars' pattern
                m2 = re.search(r'([0-9][0-9,]*)', txt)
                if m2:
                    try:
                        s2 = int(m2.group(1).replace(',',''))
                        max_stars_for_proj = s2
                        break
                    except:
                        pass
        if max_stars_for_proj is None:
            stars_val = 0
        else:
            stars_val = max_stars_for_proj
        if stars_val > best['stars']:
            best['stars'] = stars_val
            best['project'] = proj
    results.append({'package': name, 'version': version, 'stars': best['stars'], 'project': best['project']})
# sort by stars desc
results_sorted = sorted(results, key=lambda x: (x['stars'] if x['stars'] is not None else 0), reverse=True)
# pick top 5
top5 = results_sorted[:5]
# ensure JSON serializable and convert None -> null handled by json
out = json.dumps(top5)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_odEChWwbyx3ZSKtoFlIj7SPR': 'file_storage/call_odEChWwbyx3ZSKtoFlIj7SPR.json', 'var_call_cX7ZObtVcMBUYFPZ5bTHIOB4': 'file_storage/call_cX7ZObtVcMBUYFPZ5bTHIOB4.json', 'var_call_eQzyT8z7ifD8VFtKdZCFk1cg': 'file_storage/call_eQzyT8z7ifD8VFtKdZCFk1cg.json', 'var_call_f9EegKMFs4uCCzbPvb1PZAYw': 'file_storage/call_f9EegKMFs4uCCzbPvb1PZAYw.json'}

exec(code, env_args)
