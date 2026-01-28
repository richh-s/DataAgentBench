code = """import json
pairs = var_call_4SDsaWkuzmbgalTzhLk14vQN['pairs']
rows = var_call_RQ1lzvb6LmHh9IC6Azrbxock
m = {r['symbol'].split('/')[0]: r['titleFull'] for r in rows}

result_rows = []
for assignee, subclass in pairs:
    result_rows.append({
        'citing_assignee': assignee,
        'cpc_subclass': subclass,
        'cpc_subclass_titleFull': m.get(subclass)
    })

print('__RESULT__:')
print(json.dumps(result_rows))"""

env_args = {'var_call_Tos0p1lnlN2ubDRTAIwKJNro': ['publicationinfo'], 'var_call_ZFmIV1fFavMFSIv2jon6hg0O': ['cpc_definition'], 'var_call_Cp4L2jTAkxznf31PFHsbbte3': [], 'var_call_HPGrAYsdLHl5CfJGN6CGzNQN': 'file_storage/call_HPGrAYsdLHl5CfJGN6CGzNQN.json', 'var_call_8eq7hQAWj63UVf3ywkN7mWF2': {'uc_pub_count': 59, 'sample_uc_pubs': ['AU-2003297741-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2019275518-B2', 'AU-6535890-A', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038-C', 'CN-100339724-C', 'CN-102067370-B', 'CN-102584712-A', 'CN-103189548-A', 'EP-0826155-A4', 'EP-1212462-A1', 'EP-4284234-A1', 'HK-1250569-A1', 'ID-23426-A', 'IL-244029-A0']}, 'var_call_oBhzxPHXHfPYMCD0FbUB7c5I': 'file_storage/call_oBhzxPHXHfPYMCD0FbUB7c5I.json', 'var_call_5ix4DJMKDrtYm1t2clwL1HDK': {'hit_publications_count': 1, 'unique_citing_assignees': 0, 'unique_pairs': 0, 'unique_subclasses': 0, 'pairs_sample': [], 'subclasses': []}, 'var_call_cHKmOhfiXOsGORlqkNoa92F1': ['The US patent application (no. US-201715785968-A) is held by BLOOM ENERGY CORP and has publication no. US-10615444-B2.'], 'var_call_nzE28pBC1oHzlfRJIQjuTZ39': {'assignee': 'BLOOM ENERGY CORP'}, 'var_call_4SDsaWkuzmbgalTzhLk14vQN': {'pairs': [['BLOOM ENERGY CORP', 'H01M4'], ['BLOOM ENERGY CORP', 'H01M8']], 'subclasses': ['H01M4', 'H01M8']}, 'var_call_T4N7BuXvAHPDc4OORzkXaWfZ': [], 'var_call_2T2WxcYEboUBYvGqu0JOi0hk': [{'symbol': 'H01M4/0471', 'titleFull': 'Processes of manufacture in general involving thermal treatment, e.g. firing, sintering, backing particulate active material, thermal decomposition, pyrolysis'}, {'symbol': 'H01M4/0473', 'titleFull': 'Filling tube-or pockets type electrodes; Applying active mass in cup-shaped terminals'}, {'symbol': 'H01M4/049', 'titleFull': 'Manufacturing of an active layer by chemical means'}, {'symbol': 'H01M4/0402', 'titleFull': 'Methods of deposition of the material'}, {'symbol': 'H01M4/0438', 'titleFull': 'Processes of manufacture in general by electrochemical processing'}], 'var_call_RQ1lzvb6LmHh9IC6Azrbxock': [{'symbol': 'H01M8/00', 'titleFull': 'Fuel cells; Manufacture thereof'}, {'symbol': 'H01M4/00', 'titleFull': 'Electrodes'}]}

exec(code, env_args)
