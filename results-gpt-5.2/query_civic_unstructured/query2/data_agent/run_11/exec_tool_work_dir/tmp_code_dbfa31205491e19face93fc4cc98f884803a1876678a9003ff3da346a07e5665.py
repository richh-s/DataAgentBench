code = """import json

# total funding for park-related projects completed in 2022 based on civic doc evidence:
# From docs, 'Bluffs Park Shade Structure' has construction completed Nov 2022.
# Compute funding total from Funding table: already queried as 21000.

res = {'total_funding': 21000, 'projects': [{'Project_Name':'Bluffs Park Shade Structure','Total_Amount':21000}]}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_YVr6YsGg98GUbY989wj39zDB': ['Funding'], 'var_call_44cSXvBgDbGLbNPd4odSmpfZ': ['civic_docs'], 'var_call_TUyzQDUuBNfMgCrDpx3Q4u3H': 'file_storage/call_TUyzQDUuBNfMgCrDpx3Q4u3H.json', 'var_call_Jmi8UhdfHAynqpxuKZ7QYJhT': 'file_storage/call_Jmi8UhdfHAynqpxuKZ7QYJhT.json', 'var_call_57OCdCDHjEqIiHyAkAgVDFue': {'path': 'file_storage/call_TUyzQDUuBNfMgCrDpx3Q4u3H.json'}, 'var_call_6NCPYwYlD3EbD0pv9R7J5NMR': {'total_funding_completed_2022_park_related': 0, 'projects': []}, 'var_call_mOKxHE05TXkEHHGnnt4Yx65a': 'file_storage/call_mOKxHE05TXkEHHGnnt4Yx65a.json', 'var_call_fS755rW5V5mjWOpcdl4bcOfa': {'total': 0, 'projects': []}, 'var_call_VRpTCVIDTxAvj2AKelmtbsaY': [{'total': '21000'}]}

exec(code, env_args)
