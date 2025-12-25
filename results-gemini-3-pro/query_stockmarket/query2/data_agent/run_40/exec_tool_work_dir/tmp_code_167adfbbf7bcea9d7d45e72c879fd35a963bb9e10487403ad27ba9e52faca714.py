code = """import json

k1 = 'var_function-call-8651100051121965824'
k2 = 'var_function-call-10552792860447953947'
with open(locals()[k1], 'r') as f:
    etf_data = json.load(f)

print("__RESULT__:")
print(json.dumps("test"))"""

env_args = {'var_function-call-8651100051121965824': 'file_storage/function-call-8651100051121965824.json', 'var_function-call-10552792860447953947': 'file_storage/function-call-10552792860447953947.json', 'var_function-call-4775747613018573872': {'count': 1435, 'first_50': ['LQDH', 'FLMB', 'IQIN', 'SLX', 'JPSE', 'VIDI', 'ULVM', 'EWP', 'EWM', 'JOYY', 'GII', 'DIV', 'AFK', 'FLIY', 'EMQQ', 'XMHQ', 'USTB', 'EFAX', 'IWP', 'EUSA', 'CNXT', 'VIXY', 'GSJY', 'EWZ', 'LCR', 'TFLO', 'IBDL', 'PFFD', 'IG', 'ZJPN', 'FXG', 'JHMS', 'GEM', 'ZHOK', 'AAAU', 'LRGF', 'SSPY', 'EWY', 'DMRS', 'PULS', 'AOK', 'SPHQ', 'MMIT', 'EMNT', 'EUMV', 'REET', 'VPL', 'SRVR', 'SLV', 'SGDJ']}}

exec(code, env_args)
