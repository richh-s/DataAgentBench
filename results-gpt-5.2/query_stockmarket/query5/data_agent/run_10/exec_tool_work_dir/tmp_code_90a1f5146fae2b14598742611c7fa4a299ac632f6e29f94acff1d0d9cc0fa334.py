code = """import json
avail = var_call_uX9H0f26HGrJIoXaQ5RXITxp['available']
# quote table names that are reserved/need quoting
reserved = {'ELSE'}
qs=[]
for t in avail:
    tbl = f'"{t}"' if t in reserved else t
    qs.append("SELECT '{}' AS Symbol, COUNT(*) AS days FROM {} WHERE Date >= '2019-01-01' AND Date < '2020-01-01' AND Low > 0 AND (High - Low) / Low > 0.2".format(t, tbl))
query = "SELECT Symbol, days FROM (" + " UNION ALL ".join(qs) + ") t ORDER BY days DESC, Symbol ASC LIMIT 5;"
print('__RESULT__:')
print(json.dumps(query))"""

env_args = {'var_call_ekORxxxLuAnrlnsBk9tLaxAt': 'file_storage/call_ekORxxxLuAnrlnsBk9tLaxAt.json', 'var_call_CoBpvddZUSoNvkGdnTFxoyeR': {'tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'n': 86}, 'var_call_ER5VEOVIeqnubCN98QtGcoRg': 'file_storage/call_ER5VEOVIeqnubCN98QtGcoRg.json', 'var_call_uX9H0f26HGrJIoXaQ5RXITxp': {'available': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'missing': [], 'n_available': 86, 'n_missing': 0}, 'var_call_TT1yaAdbRFq5NBGPqjj9OMjt': 'file_storage/call_TT1yaAdbRFq5NBGPqjj9OMjt.json', 'var_call_FoIZDmdoA1w5QRs4habDRUhV': 'file_storage/call_FoIZDmdoA1w5QRs4habDRUhV.json'}

exec(code, env_args)
