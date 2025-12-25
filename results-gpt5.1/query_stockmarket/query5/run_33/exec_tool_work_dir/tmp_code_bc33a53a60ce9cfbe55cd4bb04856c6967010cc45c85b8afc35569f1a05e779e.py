code = """import pandas as pd
agg1 = var_call_yHr4I2UeyIyjGJx56A7X4qe2
agg2 = var_call_RYAXfBLVYIORcPMrg5wZxr2s
all_rows = agg1 + agg2
df = pd.DataFrame(all_rows)
df = df.sort_values('days_over_20pct', ascending=False).head(5)
res = df.to_json(orient='records')
print("__RESULT__:")
print(res)"""

env_args = {'var_call_yAwZzrWyQVMkKPkWYf9G6yca': 'file_storage/call_yAwZzrWyQVMkKPkWYf9G6yca.json', 'var_call_wjDF1reXZ8tTsle6jzEeVTds': 'file_storage/call_wjDF1reXZ8tTsle6jzEeVTds.json', 'var_call_rlaiVj6cHnvIQ9KR84KFROXd': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_dVhE8qSckQds9jAQviWsPWCV': 'file_storage/call_dVhE8qSckQds9jAQviWsPWCV.json', 'var_call_yHr4I2UeyIyjGJx56A7X4qe2': [{'Symbol': 'AGMH', 'days_over_20pct': 13}, {'Symbol': 'ALACU', 'days_over_20pct': 0}], 'var_call_ECfokJ0zVzxydeO1oKZavxBX': 'file_storage/call_ECfokJ0zVzxydeO1oKZavxBX.json', 'var_call_qxbtcHz3cVD4PbAYpgkulodt': 'file_storage/call_qxbtcHz3cVD4PbAYpgkulodt.json', 'var_call_RYAXfBLVYIORcPMrg5wZxr2s': [{'Symbol': 'CBAT', 'days_over_20pct': 23}, {'Symbol': 'BIOC', 'days_over_20pct': 21}, {'Symbol': 'BKYI', 'days_over_20pct': 16}, {'Symbol': 'APEX', 'days_over_20pct': 15}, {'Symbol': 'CCCL', 'days_over_20pct': 13}, {'Symbol': 'BHAT', 'days_over_20pct': 10}, {'Symbol': 'BWEN', 'days_over_20pct': 5}, {'Symbol': 'CEMI', 'days_over_20pct': 3}, {'Symbol': 'BOSC', 'days_over_20pct': 3}, {'Symbol': 'ANDA', 'days_over_20pct': 0}, {'Symbol': 'BCLI', 'days_over_20pct': 0}, {'Symbol': 'BLFS', 'days_over_20pct': 0}, {'Symbol': 'BOTJ', 'days_over_20pct': 0}, {'Symbol': 'CDMOP', 'days_over_20pct': 0}, {'Symbol': 'CFBK', 'days_over_20pct': 0}]}

exec(code, env_args)
