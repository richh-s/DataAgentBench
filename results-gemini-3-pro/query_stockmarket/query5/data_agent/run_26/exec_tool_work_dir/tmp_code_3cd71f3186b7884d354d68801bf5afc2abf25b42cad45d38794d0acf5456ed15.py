code = """import json

relevant_symbols = locals()['var_function-call-2958366835203944472']
dq = chr(34)

queries = []
for sym in relevant_symbols:
    q = f"SELECT '{sym}' as Symbol, COUNT(*) as Days FROM {dq}{sym}{dq} WHERE Date LIKE '2019-%' AND (High - Low) > 0.2 * Low"
    queries.append(q)

full_query = " UNION ALL ".join(queries)
final_query = full_query + " ORDER BY Days DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-441098270662308992': 'file_storage/function-call-441098270662308992.json', 'var_function-call-10433719829515190866': 'file_storage/function-call-10433719829515190866.json', 'var_function-call-2958366835203944472': ['BOSC', 'BWEN', 'MBNKP', 'GTEC', 'XPEL', 'CFBK', 'PECK', 'PCSB', 'CBAT', 'FTFT', 'IDEX', 'SSNT', 'NXTD', 'IOTS', 'STKS', 'CCCL', 'FNCB', 'PFIE', 'POPE', 'GLG', 'CVV', 'GRNVU', 'MMAC', 'OPOF', 'BIOC', 'MLND', 'BKYI', 'MNPR', 'FSBW', 'CLRB', 'ANDA', 'VMD', 'TGLS', 'ISNS', 'CUBA', 'BHAT', 'CPAH', 'PLIN', 'BOTJ', 'AGMH', 'HCCOU', 'VVPR', 'BLFS', 'HRTX', 'VERB', 'NVEE', 'CORV', 'AMHC', 'ALACU', 'DZSI', 'PBFS', 'TMSR', 'ORGO', 'WHLM', 'GDYN', 'OPTT', 'XBIOW', 'PEIX', 'HQI', 'APEX', 'CEMI', 'MNCLU', 'ORSNU', 'PBTS', 'CPAAU', 'EYEG', 'HNNA', 'CDMOP', 'EXPC', 'WHLR', 'SNSS', 'ELSE', 'SHSP', 'IGIC', 'MCEP', 'OTEL', 'BCLI', 'MBCN', 'SES', 'CFFA', 'VTIQW', 'VRRM', 'QRHC', 'LACQ', 'FAMI', 'ITI']}

exec(code, env_args)
