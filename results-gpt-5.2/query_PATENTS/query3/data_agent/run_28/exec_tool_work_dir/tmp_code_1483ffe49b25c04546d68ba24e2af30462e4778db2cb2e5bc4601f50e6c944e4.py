code = """import re, json
rows = var_call_mFi1XwcigCl8ELkuSiPTntvu

def extract(p):
    m = re.search(r'pub\. number\s+([A-Z]{2}-[0-9]+[A-Z0-9-]*?)\b', p)
    if m:
        return m.group(1)
    m = re.search(r'publication number\s+([A-Z]{2}-[0-9]+[A-Z0-9-]*?)\b', p)
    if m:
        return m.group(1)
    m = re.search(r'publication no\.\s+([A-Z]{2}-[0-9]+[A-Z0-9-]*?)\b', p)
    if m:
        return m.group(1)
    return None

out = [{'Patents_info': r['Patents_info'], 'pub': extract(r['Patents_info'])} for r in rows]
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_1qqHLHChxvaoBiBUSDt8j9Xn': ['publicationinfo'], 'var_call_ebIZYTH9V4k3B9k7wzQIfopr': ['cpc_definition'], 'var_call_xLB0RW8rsY3zUFgZ6QoQjcQn': [], 'var_call_2XMXyBFfZI8aURDPjg9UvGT6': 'file_storage/call_2XMXyBFfZI8aURDPjg9UvGT6.json', 'var_call_TF4QLhwEB4e1iDj6aPCUEz1G': {'uc_publication_numbers_count': 0, 'sql_queries_total': 0, 'first_query': None}, 'var_call_mFi1XwcigCl8ELkuSiPTntvu': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}]}

exec(code, env_args)
