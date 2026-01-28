code = """import json, re

def load(v):
    if isinstance(v, str):
        with open(v,'r',encoding='utf-8') as f:
            return json.load(f)
    return v

r2 = load(var_call_FVa9JgU0Reg8z2C8uZsObNC7)
r3 = load(var_call_r7VU2xINQ5M7CWpKGbXheKAT)
rows = r2 + r3

# parse assignee from Patents_info: 'owned by X' or 'assigned to X' or 'held by X'
assignee_patterns = [r'owned by ([^\.]+?) and', r'assigned to ([^\.]+?) and', r'held by ([^\.]+?) and']

def get_assignee(pi):
    if not pi:
        return None
    for pat in assignee_patterns:
        m=re.search(pat, pi, flags=re.IGNORECASE)
        if m:
            return m.group(1).strip()
    return None

# primary CPC subclasses: take cpc entries with first==true; then truncate to subclass (first 4 chars like H01L)

def parse_cpc_list(s):
    if not s:
        return []
    try:
        lst=json.loads(s)
        return lst if isinstance(lst,list) else []
    except Exception:
        return []

def primary_subclasses(cpc_s):
    lst=parse_cpc_list(cpc_s)
    out=[]
    for e in lst:
        if isinstance(e,dict) and e.get('first')==True and isinstance(e.get('code'),str):
            code=e['code']
            subclass=code[:4]
            if re.match(r'^[A-HY][0-9]{2}[A-Z]$', subclass):
                out.append(subclass)
    return sorted(set(out))

pairs=set()
for r in rows:
    ass=get_assignee(r.get('Patents_info'))
    if not ass:
        continue
    if 'UNIV CALIFORNIA' in ass.upper() or 'UNIVERSITY OF CALIFORNIA' in ass.upper():
        continue
    for sc in primary_subclasses(r.get('cpc')):
        pairs.add((ass, sc))

pairs=sorted(pairs)
subclasses=sorted({sc for _,sc in pairs})

print('__RESULT__:')
print(json.dumps({'n_citing_records':len(rows),'n_pairs':len(pairs),'n_unique_subclasses':len(subclasses),'pairs_sample':pairs[:20],'subclasses':subclasses}))"""

env_args = {'var_call_1qqHLHChxvaoBiBUSDt8j9Xn': ['publicationinfo'], 'var_call_ebIZYTH9V4k3B9k7wzQIfopr': ['cpc_definition'], 'var_call_xLB0RW8rsY3zUFgZ6QoQjcQn': [], 'var_call_2XMXyBFfZI8aURDPjg9UvGT6': 'file_storage/call_2XMXyBFfZI8aURDPjg9UvGT6.json', 'var_call_TF4QLhwEB4e1iDj6aPCUEz1G': {'uc_publication_numbers_count': 0, 'sql_queries_total': 0, 'first_query': None}, 'var_call_mFi1XwcigCl8ELkuSiPTntvu': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}], 'var_call_T7uu1VT7Xx7p60t9lfCVPX00': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'pub': None}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.', 'pub': None}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.', 'pub': None}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.', 'pub': None}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.', 'pub': None}], 'var_call_IjjCaIFHcXkhW8ASaStW0JSP': {'s': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'matches': [['pub\\. number\\s+([^\\s]+)', 'US-2022074631-A1.'], ['publication number\\s+([^\\s]+)', None], ['publication no\\.\\s+([^\\s]+)', None]]}, 'var_call_e6f3Knwls8CUdA2PSpQQqnMp': {'uc_publication_numbers_count': 180, 'sample': ['AP-3334-A', 'AU-2001257114-A1', 'AU-2001296493-B2', 'AU-2002254753-B2', 'AU-2003247814-A1', 'AU-2003297741-A1', 'AU-2004253879-A1', 'AU-2005269556-A1', 'AU-2007297661-A1', 'AU-2008329628-B2']}, 'var_call_WGr48sqJ4J4jrjY7WgW2k7P5': {'note': 'need full uc_pubs list in python from previous call var_call_e6f3... not available; will recompute in next step'}, 'var_call_wBXei7D2ILqUC9Li0hD2I9OP': 'file_storage/call_wBXei7D2ILqUC9Li0hD2I9OP.json', 'var_call_hl0hngBMzsscFFJTe9a7eOaJ': {'n_queries': 3}, 'var_call_BWV2XRTSpZkA8KeshAKU1hNx': [], 'var_call_FVa9JgU0Reg8z2C8uZsObNC7': 'file_storage/call_FVa9JgU0Reg8z2C8uZsObNC7.json', 'var_call_r7VU2xINQ5M7CWpKGbXheKAT': 'file_storage/call_r7VU2xINQ5M7CWpKGbXheKAT.json'}

exec(code, env_args)
