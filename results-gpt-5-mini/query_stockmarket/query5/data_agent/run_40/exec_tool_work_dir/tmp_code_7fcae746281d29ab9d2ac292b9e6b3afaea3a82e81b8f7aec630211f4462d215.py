code = """import json
with open(var_call_PPqOo48KnLzN7VZUluh7p1Pf, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_MxbtFlCKNvwOOD1Kk6AOFzDM, 'r') as f:
    trade_tables = json.load(f)
symbols_s = [r['Symbol'] for r in stockinfo]
trade_set = set(trade_tables)
symbols = sorted([s for s in symbols_s if s in trade_set])
parts = []
for s in symbols:
    part = (
        "SELECT '" + s + "' AS Symbol, SUM(CASE WHEN (\"High\" - \"Low\") > 0.2 * \"Low\" THEN 1 ELSE 0 END) AS cnt "
        "FROM \"" + s + "\" "
        "WHERE \"Date\" >= '2019-01-01' AND \"Date\" <= '2019-12-31'"
    )
    parts.append(part)
union_sql = "\nUNION ALL\n".join(parts)
final_sql = "WITH t AS (\n" + union_sql + "\n)\nSELECT Symbol, cnt FROM t ORDER BY cnt DESC, Symbol ASC LIMIT 5;"
output = {'num_symbols': len(symbols), 'final_sql_start': final_sql[:1000]}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_PPqOo48KnLzN7VZUluh7p1Pf': 'file_storage/call_PPqOo48KnLzN7VZUluh7p1Pf.json', 'var_call_MxbtFlCKNvwOOD1Kk6AOFzDM': 'file_storage/call_MxbtFlCKNvwOOD1Kk6AOFzDM.json', 'var_call_t3UInuKPgfoZduflOJPGqTNT': {'num_stockinfo_S': 86, 'num_trade_tables': 2753, 'num_intersection': 86, 'intersection_sample': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP'], 'intersection_all_count': 86}}

exec(code, env_args)
