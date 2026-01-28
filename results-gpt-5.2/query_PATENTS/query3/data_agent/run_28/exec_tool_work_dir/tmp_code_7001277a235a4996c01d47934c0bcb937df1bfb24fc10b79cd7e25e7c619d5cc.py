code = """import json, re
rec = var_call_2XMXyBFfZI8aURDPjg9UvGT6
if isinstance(rec, str):
    with open(rec, 'r', encoding='utf-8') as f:
        rec = json.load(f)

def extract_pub_number(patents_info: str):
    if not patents_info:
        return None
    for pat in [r'pub\. number\s+([^\s]+)', r'publication number\s+([^\s]+)', r'publication no\.\s+([^\s]+)']:
        m = re.search(pat, patents_info, flags=re.IGNORECASE)
        if m:
            return m.group(1).strip().rstrip('.,;')
    return None

uc_pubs = sorted({extract_pub_number(r.get('Patents_info','')) for r in rec if extract_pub_number(r.get('Patents_info',''))})

chunks = [uc_pubs[i:i+60] for i in range(0, len(uc_pubs), 60)]
queries=[]
for ch in chunks:
    ors = ' OR '.join([f"citation LIKE '%\\\"publication_number\\\": \\\"{pn}\\\"%'" for pn in ch])
    queries.append("SELECT Patents_info, cpc, citation, title_localized FROM publicationinfo WHERE ("+ors+");")

print('__RESULT__:')
print(json.dumps({'uc_pubs_count':len(uc_pubs),'chunks':len(chunks),'queries':queries}))"""

env_args = {'var_call_1qqHLHChxvaoBiBUSDt8j9Xn': ['publicationinfo'], 'var_call_ebIZYTH9V4k3B9k7wzQIfopr': ['cpc_definition'], 'var_call_xLB0RW8rsY3zUFgZ6QoQjcQn': [], 'var_call_2XMXyBFfZI8aURDPjg9UvGT6': 'file_storage/call_2XMXyBFfZI8aURDPjg9UvGT6.json', 'var_call_TF4QLhwEB4e1iDj6aPCUEz1G': {'uc_publication_numbers_count': 0, 'sql_queries_total': 0, 'first_query': None}, 'var_call_mFi1XwcigCl8ELkuSiPTntvu': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}], 'var_call_T7uu1VT7Xx7p60t9lfCVPX00': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'pub': None}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.', 'pub': None}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.', 'pub': None}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.', 'pub': None}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.', 'pub': None}], 'var_call_IjjCaIFHcXkhW8ASaStW0JSP': {'s': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'matches': [['pub\\. number\\s+([^\\s]+)', 'US-2022074631-A1.'], ['publication number\\s+([^\\s]+)', None], ['publication no\\.\\s+([^\\s]+)', None]]}, 'var_call_e6f3Knwls8CUdA2PSpQQqnMp': {'uc_publication_numbers_count': 180, 'sample': ['AP-3334-A', 'AU-2001257114-A1', 'AU-2001296493-B2', 'AU-2002254753-B2', 'AU-2003247814-A1', 'AU-2003297741-A1', 'AU-2004253879-A1', 'AU-2005269556-A1', 'AU-2007297661-A1', 'AU-2008329628-B2']}, 'var_call_WGr48sqJ4J4jrjY7WgW2k7P5': {'note': 'need full uc_pubs list in python from previous call var_call_e6f3... not available; will recompute in next step'}}

exec(code, env_args)
