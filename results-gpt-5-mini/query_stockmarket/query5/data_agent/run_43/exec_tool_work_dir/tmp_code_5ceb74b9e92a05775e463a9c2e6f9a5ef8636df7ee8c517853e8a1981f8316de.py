code = """import json, os
symbols = var_call_C4BA4GDA4Eo9SkcmJjPoDB4I

selects = []
for s in symbols:
    sel = ("SELECT '" + s + "' AS Symbol, COALESCE(SUM(CASE WHEN (\"High\" - \"Low\") > 0.2 * NULLIF(\"Low\",0) THEN 1 ELSE 0 END),0) AS cnt "
           "FROM \"" + s + "\" WHERE \"Date\" >= '2019-01-01' AND \"Date\" <= '2019-12-31'")
    selects.append(sel)

sql = " UNION ALL ".join(selects) + " ORDER BY cnt DESC LIMIT 5;"
print('__RESULT__:')
print(json.dumps({'sql': sql}))"""

env_args = {'var_call_WieKl7aHdSZW9WQUOPcwhEKt': 'file_storage/call_WieKl7aHdSZW9WQUOPcwhEKt.json', 'var_call_VgonKm8xOr3QKnin3IPr4pvT': 'file_storage/call_VgonKm8xOr3QKnin3IPr4pvT.json', 'var_call_9kEodSYCb5yj1kZ4zEVqvNCc': {'type_stockinfo': 'list', 'len_stockinfo': 86, 'type_trade_tables': 'list', 'len_trade_tables': 2753}, 'var_call_7L41ZFTbZeAqvr48T0bE1vD2': 'file_storage/call_7L41ZFTbZeAqvr48T0bE1vD2.json', 'var_call_C4BA4GDA4Eo9SkcmJjPoDB4I': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}

exec(code, env_args)
