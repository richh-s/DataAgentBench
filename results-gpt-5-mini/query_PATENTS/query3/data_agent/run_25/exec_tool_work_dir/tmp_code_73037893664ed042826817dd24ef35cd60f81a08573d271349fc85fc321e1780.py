code = """import json, re
path = var_call_l3Wv2stVqubRXfB59zoHvWq0
with open(path,'r') as f:
    data = json.load(f)
# build map of publication number -> record
pub_map = {}
# regexes
pubnum_regexes = [
    re.compile(r"pub(?:lication)?(?:\.\s)?number\s*[:]?\s*([A-Z]{1,3}-[0-9A-Z\-]+)", re.IGNORECASE),
    re.compile(r"publication number\s*[:]?\s*([A-Z]{1,3}-[0-9A-Z\-]+)", re.IGNORECASE),
    re.compile(r"(US-\d{5,}-[A-Z0-9]+)", re.IGNORECASE),
    re.compile(r"([A-Z]{2,3}-\d{4,}-[A-Z0-9]+)", re.IGNORECASE),
    re.compile(r"([A-Z]{2,3}-\d{6,})", re.IGNORECASE)
]
# helper to extract pubnum from Patents_info
for rec in data:
    pi = rec.get('Patents_info','')
    found = None
    for rx in pubnum_regexes:
        m = rx.search(pi)
        if m:
            found = m.group(1).strip()
            break
    if found:
        pub_map[found] = rec
# Now iterate all records and parse their citation field
citing = {}  # assignee -> set of primary cpc codes
cpc_codes_set = set()
for rec in data:
    # parse citation
    cit_field = rec.get('citation','')
    try:
        cit_list = json.loads(cit_field) if cit_field and cit_field.strip().startswith('[') else []
    except Exception:
        cit_list = []
    # collect cited publication numbers
    cited_pubnums = [c.get('publication_number') for c in cit_list if isinstance(c,dict) and c.get('publication_number')]
    # check if any cited pubnum maps to a UNIV CALIFORNIA record
    cites_uc = False
    for cp in cited_pubnums:
        if cp in pub_map:
            if 'UNIV CALIFORNIA' in pub_map[cp].get('Patents_info',''):
                cites_uc = True
                break
    if cites_uc:
        # extract assignee from this rec Patents_info
        pi = rec.get('Patents_info','')
        assignee = None
        # common separators
        for sep in [' holds ', ' is owned by ', ' is assigned to ', ' assigned to ', ' owns ', ' held by ', ' holds the '] :
            if sep in pi:
                assignee = pi.split(sep)[0].strip()
                break
        if not assignee:
            # fallback: take initial uppercase words before a verb
            m = re.match(r"^([A-Z0-9 &,.\-]+?)\s+(?:holds|owns|is|has|with)", pi)
            if m:
                assignee = m.group(1).strip()
            else:
                # take first 6 words
                assignee = ' '.join(pi.split()[:6])
        # normalize
        assignee = assignee.strip().strip('.,')
        if assignee.upper() == 'UNIV CALIFORNIA':
            continue
        # parse cpc primary codes
        cpc_field = rec.get('cpc','')
        try:
            cpc_list = json.loads(cpc_field) if cpc_field and cpc_field.strip().startswith('[') else []
        except Exception:
            cpc_list = []
        primary_codes = []
        for c in cpc_list:
            if isinstance(c, dict) and c.get('first'):
                code = c.get('code')
                if code:
                    primary_codes.append(code)
        # if none marked first, take first code entries codes
        if not primary_codes and cpc_list:
            for c in cpc_list:
                if isinstance(c, dict) and c.get('code'):
                    primary_codes.append(c.get('code'))
                    break
        if not primary_codes:
            primary_codes = []
        if primary_codes:
            if assignee not in citing:
                citing[assignee] = set()
            for pc in primary_codes:
                citing[assignee].add(pc)
                cpc_codes_set.add(pc)
# prepare output
out = {'assignee_to_cpcs': {k: sorted(list(v)) for k,v in citing.items()}, 'cpc_codes': sorted(list(cpc_codes_set)), 'num_pub_with_identified_pubnum': len(pub_map)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_6s5RpImgm3iTcGaGq8ohXGZr': 'file_storage/call_6s5RpImgm3iTcGaGq8ohXGZr.json', 'var_call_gG2899rItsLZOgaJaeMhanfU': [], 'var_call_l3Wv2stVqubRXfB59zoHvWq0': 'file_storage/call_l3Wv2stVqubRXfB59zoHvWq0.json'}

exec(code, env_args)
