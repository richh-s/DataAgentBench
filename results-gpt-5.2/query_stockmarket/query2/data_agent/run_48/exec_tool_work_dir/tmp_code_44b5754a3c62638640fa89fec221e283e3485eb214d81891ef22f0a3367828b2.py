code = """import json
path_etfs = var_call_FUvH3fPlMC7f1SsXJdXrJGAD
with open(path_etfs,'r') as f:
    etfs=json.load(f)
syms=set([r['symbol'] for r in etfs])
# sample some known high-price ETFs
cands=[s for s in ['IVV','SPY','QQQ','IWM','DIA','IYR','TLT','GLD','IAU','VTI','VOO','SCHB','XLF','XLK','XLY','XLP','XLE','XLI','XLV','XLU','FXI','EEM'] if s in syms]
print('__RESULT__:')
print(json.dumps({'candidates_in_arca_etf_list':cands}))"""

env_args = {'var_call_FUvH3fPlMC7f1SsXJdXrJGAD': 'file_storage/call_FUvH3fPlMC7f1SsXJdXrJGAD.json', 'var_call_IHbpJReSGBxSJZJQN1U6OsBu': 'file_storage/call_IHbpJReSGBxSJZJQN1U6OsBu.json', 'var_call_EudNuCiFmivVPNUZK0QYnx03': {'n_symbols': 1435, 'first10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_call_YIWQMj4d6w1vmxx46152IgAh': []}

exec(code, env_args)
