code = """import json, pandas as pd
symbols = json.load(open(var_call_MevG3IYwsWxPXQTHgjGFzBtQ))
chunk = symbols  # all symbols
queries = []
for sym in chunk:
    q = f"SELECT Date, High, Low FROM '{sym}' WHERE Date >= '2019-01-01' AND Date <= '2019-12-31';"
    queries.append({"symbol": sym, "query": q})
result = json.dumps(queries)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_wsLlo5WL8oajUAP335Xuj82G': 'file_storage/call_wsLlo5WL8oajUAP335Xuj82G.json', 'var_call_jRSW6QeUSSMM8v5ABpxKRewW': 'file_storage/call_jRSW6QeUSSMM8v5ABpxKRewW.json', 'var_call_JQu5ol25ysfGqUF3masWUnuO': 'file_storage/call_JQu5ol25ysfGqUF3masWUnuO.json', 'var_call_MevG3IYwsWxPXQTHgjGFzBtQ': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}

exec(code, env_args)
