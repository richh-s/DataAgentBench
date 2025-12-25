code = """import json

symbols = ["BOSC", "BWEN", "MBNKP", "GTEC", "XPEL", "CFBK", "PECK", "PCSB", "CBAT", "FTFT", "IDEX", "SSNT", "NXTD", "IOTS", "STKS", "CCCL", "FNCB", "PFIE", "POPE", "GLG", "CVV", "GRNVU", "MMAC", "OPOF", "BIOC", "MLND", "BKYI", "MNPR", "FSBW", "CLRB", "ANDA", "VMD", "TGLS", "ISNS", "CUBA", "BHAT", "CPAH", "PLIN", "BOTJ", "AGMH", "HCCOU", "VVPR", "BLFS", "HRTX", "VERB", "NVEE", "CORV", "AMHC", "ALACU", "DZSI", "PBFS", "TMSR", "ORGO", "WHLM", "GDYN", "OPTT", "XBIOW", "PEIX", "HQI", "APEX", "CEMI", "MNCLU", "ORSNU", "PBTS", "CPAAU", "EYEG", "HNNA", "CDMOP", "EXPC", "WHLR", "SNSS", "ELSE", "SHSP", "IGIC", "MCEP", "OTEL", "BCLI", "MBCN", "SES", "CFFA", "VTIQW", "VRRM", "QRHC", "LACQ", "FAMI", "ITI"]

batch1 = symbols[:43]
batch2 = symbols[43:]

dq = chr(34)

def make_query(batch):
    queries = []
    for sym in batch:
        q = f"SELECT '{sym}' as Symbol, COUNT(*) as Days FROM {dq}{sym}{dq} WHERE Date LIKE '2019-%' AND (High - Low) > 0.2 * Low"
        queries.append(q)
    return " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps([make_query(batch1), make_query(batch2)]))"""

env_args = {'var_function-call-441098270662308992': 'file_storage/function-call-441098270662308992.json', 'var_function-call-10433719829515190866': 'file_storage/function-call-10433719829515190866.json', 'var_function-call-2958366835203944472': ['BOSC', 'BWEN', 'MBNKP', 'GTEC', 'XPEL', 'CFBK', 'PECK', 'PCSB', 'CBAT', 'FTFT', 'IDEX', 'SSNT', 'NXTD', 'IOTS', 'STKS', 'CCCL', 'FNCB', 'PFIE', 'POPE', 'GLG', 'CVV', 'GRNVU', 'MMAC', 'OPOF', 'BIOC', 'MLND', 'BKYI', 'MNPR', 'FSBW', 'CLRB', 'ANDA', 'VMD', 'TGLS', 'ISNS', 'CUBA', 'BHAT', 'CPAH', 'PLIN', 'BOTJ', 'AGMH', 'HCCOU', 'VVPR', 'BLFS', 'HRTX', 'VERB', 'NVEE', 'CORV', 'AMHC', 'ALACU', 'DZSI', 'PBFS', 'TMSR', 'ORGO', 'WHLM', 'GDYN', 'OPTT', 'XBIOW', 'PEIX', 'HQI', 'APEX', 'CEMI', 'MNCLU', 'ORSNU', 'PBTS', 'CPAAU', 'EYEG', 'HNNA', 'CDMOP', 'EXPC', 'WHLR', 'SNSS', 'ELSE', 'SHSP', 'IGIC', 'MCEP', 'OTEL', 'BCLI', 'MBCN', 'SES', 'CFFA', 'VTIQW', 'VRRM', 'QRHC', 'LACQ', 'FAMI', 'ITI'], 'var_function-call-17333126425019614728': 'file_storage/function-call-17333126425019614728.json'}

exec(code, env_args)
