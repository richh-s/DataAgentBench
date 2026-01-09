code = """import json
from pathlib import Path

syms = var_call_bhE6541bgevvOr8lfSccB8Gr['symbols']
trade_tables = json.loads(Path(var_call_boQEBkvLs65ZZL3FG2HbHPlT).read_text())
trade_set = set(trade_tables)
syms_avail = [s for s in syms if s in trade_set]

parts = []
for s in syms_avail:
    parts.append("SELECT '" + s + "' AS Symbol, COUNT(*) AS days_cnt FROM \"" + s + "\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) / Low > 0.2")

union_query = "\nUNION ALL\n".join(parts)
final_query = "SELECT Symbol, days_cnt FROM (" + union_query + ") t ORDER BY days_cnt DESC, Symbol ASC LIMIT 5;"

print('__RESULT__:')
print(json.dumps({'query': final_query, 'n_syms_avail': len(syms_avail)}))"""

env_args = {'var_call_qVJ7lfNYWj3RHEQQqgzN2tRe': 'file_storage/call_qVJ7lfNYWj3RHEQQqgzN2tRe.json', 'var_call_bhE6541bgevvOr8lfSccB8Gr': {'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'n': 86}, 'var_call_boQEBkvLs65ZZL3FG2HbHPlT': 'file_storage/call_boQEBkvLs65ZZL3FG2HbHPlT.json'}

exec(code, env_args)
