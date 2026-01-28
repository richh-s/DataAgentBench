code = """import json
var_univ = var_call_cc68Z6aX2MXH8DgcWXYV034B
if isinstance(var_univ, str):
    with open(var_univ, 'r', encoding='utf-8') as f:
        univ_records = json.load(f)
else:
    univ_records = var_univ

pis = [r.get('Patents_info','') for r in univ_records][:50]
print('__RESULT__:')
print(json.dumps(pis))"""

env_args = {'var_call_cc68Z6aX2MXH8DgcWXYV034B': 'file_storage/call_cc68Z6aX2MXH8DgcWXYV034B.json', 'var_call_r1rLlChnwgV9fpjtfBZ4FUB9': [], 'var_call_gpK3xriqZczE4HtoLAE6feqr': ['In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.', 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.', 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.', 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.', 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.', 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.', 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.', 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.', 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.'], 'var_call_aImyVbUV9Z2hMgiWtgSxfFfT': 'file_storage/call_aImyVbUV9Z2hMgiWtgSxfFfT.json', 'var_call_eiXMVRbHEswgJ2rp1nTqEsy4': 'file_storage/call_eiXMVRbHEswgJ2rp1nTqEsy4.json', 'var_call_Ss5g2DXt2Jt33OTnaUSJGorR': {'assignees': [], 'cpc_codes': [], 'num_univ_pubs': 0}}

exec(code, env_args)
