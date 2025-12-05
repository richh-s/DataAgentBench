code = """import json
import pandas as pd
syms = json.loads(var_call_rlaiVj6cHnvIQ9KR84KFROXd)
import duckdb
con = duckdb.connect(database='stocktrade_database', read_only=True)
rows = []
for s in syms:
    try:
        df = con.execute(f"SELECT Date, High, Low FROM '{s}' WHERE Date >= '2019-01-01' AND Date <= '2019-12-31'").fetchdf()
    except Exception:
        continue
    if df.empty:
        continue
    df['range_pct'] = (df['High'] - df['Low']) / df['Low']
    cnt = int((df['range_pct'] > 0.2).sum())
    rows.append({'Symbol': s, 'days_over_20pct': cnt})
con.close()
res_df = pd.DataFrame(rows)
res_df = res_df.sort_values('days_over_20pct', ascending=False).head(5)
result = res_df.to_json(orient='records')
print("__RESULT__:")
print(result)"""

env_args = {'var_call_yAwZzrWyQVMkKPkWYf9G6yca': 'file_storage/call_yAwZzrWyQVMkKPkWYf9G6yca.json', 'var_call_wjDF1reXZ8tTsle6jzEeVTds': 'file_storage/call_wjDF1reXZ8tTsle6jzEeVTds.json', 'var_call_rlaiVj6cHnvIQ9KR84KFROXd': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}

exec(code, env_args)
