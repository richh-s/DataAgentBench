code = """import json, textwrap

symbols_data = json.loads(var_call_vPGOtBLxkjHVzLaHmppQjjo4)
syms = symbols_data['symbols']

# build DuckDB SQL to count days per symbol in 2019 with (High-Low)/Low > 0.2
cases = []
for s in syms:
    cases.append(f"SELECT '{s}' AS Symbol, COUNT(*) AS cnt FROM '{s}' WHERE Date >= '2019-01-01' AND Date < '2020-01-01' AND (High - Low) / Low > 0.2")

union_sql = " UNION ALL ".join(cases)
full_sql = f"SELECT Symbol, cnt FROM ({union_sql}) ORDER BY cnt DESC LIMIT 5;"

result = json.dumps({'query': full_sql})
print('__RESULT__:')
print(result)"""

env_args = {'var_call_z0vUN3AiZB3aOsmYx8b60Vnr': 'file_storage/call_z0vUN3AiZB3aOsmYx8b60Vnr.json', 'var_call_VpDgoA7fXkQOcSnmZFJBToDI': 'file_storage/call_VpDgoA7fXkQOcSnmZFJBToDI.json', 'var_call_vPGOtBLxkjHVzLaHmppQjjo4': {'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}}

exec(code, env_args)
