code = """import re, json
s = "The US patent application (no. US-201715785968-A) is held by BLOOM ENERGY CORP and has publication no. US-10615444-B2."
assignee=None
m=re.search(r'is held by\s+(.*?)\s+and has', s, re.IGNORECASE)
if m:
    assignee=m.group(1).strip()
print('__RESULT__:')
print(json.dumps({'assignee':assignee}))"""

env_args = {'var_call_Tos0p1lnlN2ubDRTAIwKJNro': ['publicationinfo'], 'var_call_ZFmIV1fFavMFSIv2jon6hg0O': ['cpc_definition'], 'var_call_Cp4L2jTAkxznf31PFHsbbte3': [], 'var_call_HPGrAYsdLHl5CfJGN6CGzNQN': 'file_storage/call_HPGrAYsdLHl5CfJGN6CGzNQN.json', 'var_call_8eq7hQAWj63UVf3ywkN7mWF2': {'uc_pub_count': 59, 'sample_uc_pubs': ['AU-2003297741-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2019275518-B2', 'AU-6535890-A', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038-C', 'CN-100339724-C', 'CN-102067370-B', 'CN-102584712-A', 'CN-103189548-A', 'EP-0826155-A4', 'EP-1212462-A1', 'EP-4284234-A1', 'HK-1250569-A1', 'ID-23426-A', 'IL-244029-A0']}, 'var_call_oBhzxPHXHfPYMCD0FbUB7c5I': 'file_storage/call_oBhzxPHXHfPYMCD0FbUB7c5I.json', 'var_call_5ix4DJMKDrtYm1t2clwL1HDK': {'hit_publications_count': 1, 'unique_citing_assignees': 0, 'unique_pairs': 0, 'unique_subclasses': 0, 'pairs_sample': [], 'subclasses': []}, 'var_call_cHKmOhfiXOsGORlqkNoa92F1': ['The US patent application (no. US-201715785968-A) is held by BLOOM ENERGY CORP and has publication no. US-10615444-B2.']}

exec(code, env_args)
