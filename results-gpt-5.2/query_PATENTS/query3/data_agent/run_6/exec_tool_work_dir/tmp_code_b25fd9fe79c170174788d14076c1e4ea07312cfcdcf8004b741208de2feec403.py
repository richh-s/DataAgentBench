code = """import json, re

# load UC assigned rows
with open(var_call_eiOZ6mu6Fp62QgEmh27Olb79, 'r', encoding='utf-8') as f:
    uc_rows = json.load(f)

uc_pubnums = set()
for r in uc_rows:
    pi = r.get('Patents_info') or ''
    m = re.search(r'pub\.? number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', pi)
    if m:
        uc_pubnums.add(m.group(1))

# citing rows
with open(var_call_xMfWqfhDClhUS1zR9axrOYJP, 'r', encoding='utf-8') as f:
    citing_rows = json.load(f)

# parse citing assignee and primary CPC code (first==true) and check if it cites any UC pubnum
pairs = []  # (assignee, subclass)
for r in citing_rows:
    pi = r.get('Patents_info') or ''
    # extract assignee
    m = re.search(r'(?:owned by|is owned by|assigned to|is assigned to|held by)\s+([^.,]+)', pi)
    if not m:
        continue
    assignee = m.group(1).strip()
    if 'UNIV CALIFORNIA' in assignee:
        continue

    cit = r.get('citation') or '[]'
    try:
        cit_list = json.loads(cit)
    except Exception:
        continue
    cited_pubs = {c.get('publication_number') for c in cit_list if isinstance(c, dict)}
    if not (cited_pubs & uc_pubnums):
        continue

    cpc = r.get('cpc') or '[]'
    try:
        cpc_list = json.loads(cpc)
    except Exception:
        cpc_list = []
    primary_codes = [d.get('code') for d in cpc_list if isinstance(d, dict) and d.get('first') is True and d.get('code')]
    # derive primary subclass: 4 chars + /00? Actually subclass like A61K. Use first 4 chars.
    for code in primary_codes[:1]:
        subclass = code[:4]
        pairs.append((assignee, subclass))

# unique pairs
pairs = sorted(set(pairs))
subclasses = sorted({s for _, s in pairs})

print('__RESULT__:')
print(json.dumps({'pairs': pairs, 'subclasses': subclasses, 'n_pairs': len(pairs), 'n_subclasses': len(subclasses)}))"""

env_args = {'var_call_iM799Cm624tRs8ZUZbXDWbwz': ['publicationinfo'], 'var_call_rBpbCGpvxezpdzQIOB6hxBNV': ['cpc_definition'], 'var_call_9s7Mnh5BPOggS0UNRTFgPRjn': [], 'var_call_eiOZ6mu6Fp62QgEmh27Olb79': 'file_storage/call_eiOZ6mu6Fp62QgEmh27Olb79.json', 'var_call_GnypOtugLW7pWagsqCLJ7yAc': {'uc_pubnums_count': 59, 'query': "SELECT Patents_info, cpc, citation FROM publicationinfo WHERE citation IS NOT NULL AND citation <> '[]' AND (citation LIKE '%0826155%' OR citation LIKE '%100339724%' OR citation LIKE '%102067370%' OR citation LIKE '%102584712%' OR citation LIKE '%103189548%' OR citation LIKE '%11376346%' OR citation LIKE '%11546022%' OR citation LIKE '%11667770%' OR citation LIKE '%1212462%' OR citation LIKE '%1250569%' OR citation LIKE '%2003297741%' OR citation LIKE '%2006051790%' OR citation LIKE '%2006292670%' OR citation LIKE '%2007297661%' OR citation LIKE '%2008349842%' OR citation LIKE '%2010045542%' OR citation LIKE '%2010214112%' OR citation LIKE '%2012162563%' OR citation LIKE '%2013002850%' OR citation LIKE '%2014224156%' OR citation LIKE '%2015364602%' OR citation LIKE '%2017145219%' OR citation LIKE '%2017214343%' OR citation LIKE '%2017281687%' OR citation LIKE '%2018026404%' OR citation LIKE '%2018243924%' OR citation LIKE '%201925402%' OR citation LIKE '%2019275518%' OR citation LIKE '%2019328740%' OR citation LIKE '%20200041324%' OR citation LIKE '%2020025859%' OR citation LIKE '%2020055916%' OR citation LIKE '%2021000566%' OR citation LIKE '%2021101879%' OR citation LIKE '%2021102420%' OR citation LIKE '%2022018060%' OR citation LIKE '%2022074631%' OR citation LIKE '%2023155090%' OR citation LIKE '%2023171142%' OR citation LIKE '%2023225482%' OR citation LIKE '%2023279470%' OR citation LIKE '%2023321419%' OR citation LIKE '%2024044766%' OR citation LIKE '%2024112568%' OR citation LIKE '%2298540%' OR citation LIKE '%23426%' OR citation LIKE '%244029%' OR citation LIKE '%2550552%' OR citation LIKE '%2562038%' OR citation LIKE '%274176%' OR citation LIKE '%4284234%' OR citation LIKE '%5304932%' OR citation LIKE '%5547866%' OR citation LIKE '%6535890%' OR citation LIKE '%6750960%' OR citation LIKE '%6767662%' OR citation LIKE '%70061%' OR citation LIKE '%9061071%' OR citation LIKE '%S6163700%');"}, 'var_call_xMfWqfhDClhUS1zR9axrOYJP': 'file_storage/call_xMfWqfhDClhUS1zR9axrOYJP.json'}

exec(code, env_args)
