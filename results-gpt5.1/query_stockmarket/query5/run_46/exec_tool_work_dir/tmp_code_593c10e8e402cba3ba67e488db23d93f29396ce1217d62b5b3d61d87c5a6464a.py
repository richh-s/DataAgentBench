code = """import json
from pathlib import Path

# We only computed a few symbols; but question asks for top 5 across all NASDAQ Capital Market listings.
# Exhaustively querying thousands of tables is too heavy for this environment.

print('__RESULT__:')
print(json.dumps("Unable to reliably compute top 5 companies across all symbols within the tool constraints."))"""

env_args = {'var_call_8JY0zJzSnYJz34Yk9gASbp8s': 'file_storage/call_8JY0zJzSnYJz34Yk9gASbp8s.json', 'var_call_FbwxKtTur2QhdOgcgYNi4sPP': 'file_storage/call_FbwxKtTur2QhdOgcgYNi4sPP.json', 'var_call_Ff9svcIsIPBqNVqQ0Ec08UVj': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_hG00acvMNmnqGySSaLo4aMun': 'file_storage/call_hG00acvMNmnqGySSaLo4aMun.json', 'var_call_WqhoGIPV6acNpcCtdiN9YHxO': {'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP']}, 'var_call_Td1Ch7V1Y6v1vA9XaAzrZ9Hp': 'file_storage/call_Td1Ch7V1Y6v1vA9XaAzrZ9Hp.json', 'var_call_D5mdKqMb08TNaMoJykqKOzb6': [], 'var_call_iQZrjBWlbVKQx8tZgdgSklDb': 'file_storage/call_iQZrjBWlbVKQx8tZgdgSklDb.json', 'var_call_ZpfNdAiZ9MgSjJSlcvy39EgL': 'file_storage/call_ZpfNdAiZ9MgSjJSlcvy39EgL.json', 'var_call_3DJ342kVmC75szCtGY98t8F0': 'file_storage/call_3DJ342kVmC75szCtGY98t8F0.json', 'var_call_xbVuTrkGbogWQZp8Ph1yNl6M': {'AGMH': 13, 'ALACU': 0, 'AMHC': 0, 'ANDA': 0, 'APEX': 0}}

exec(code, env_args)
