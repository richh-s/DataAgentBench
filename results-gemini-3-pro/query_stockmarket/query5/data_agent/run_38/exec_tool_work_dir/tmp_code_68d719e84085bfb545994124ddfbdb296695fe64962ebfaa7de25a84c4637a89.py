code = """import json

symbols = ["VRRM", "LACQ", "IGIC", "BLFS", "VTIQW", "MNCLU", "CVV", "HRTX", "MLND", "CEMI", "OPOF", "SES", "VMD", "MNPR", "OPTT", "PBTS", "ORGO", "SHSP", "HNNA", "CCCL", "ITI", "MBCN", "HQI", "BHAT", "GRNVU", "AGMH", "CDMOP", "MCEP", "ISNS", "ALACU", "MBNKP", "CORV", "DZSI", "SSNT", "BOSC", "CPAAU", "VERB", "BKYI", "ORSNU", "AMHC", "PBFS", "PLIN", "FSBW", "BIOC", "BOTJ", "CFBK", "GTEC", "GLG", "XPEL", "EXPC", "WHLR", "FTFT", "QRHC", "NVEE", "ANDA", "TGLS", "PECK", "SNSS", "VVPR", "XBIOW", "POPE", "FNCB", "STKS", "EYEG", "TMSR", "IOTS", "CFFA", "ELSE", "GDYN", "APEX", "PCSB", "OTEL", "PEIX", "CBAT", "NXTD", "HCCOU", "PFIE", "BWEN", "CLRB", "WHLM", "MMAC", "BCLI", "CUBA", "CPAH", "IDEX", "FAMI"]

mid = len(symbols) // 2
batch1 = symbols[:mid]
batch2 = symbols[mid:]

def build_query(syms):
    qs = []
    for s in syms:
        # Construct query without double quotes if possible, or careful escaping
        # Using single quotes for Python string, double quotes for SQL table name
        # We need to escape the double quote inside the single quoted string
        qs.append('SELECT \'' + s + '\' as Symbol, COUNT(*) as DaysCount FROM "' + s + '" WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\' AND (High - Low) > (0.2 * Low)')
    return ' UNION ALL '.join(qs)

q1 = build_query(batch1)
q2 = build_query(batch2)

print("__RESULT__:")
print(json.dumps([q1, q2]))"""

env_args = {'var_function-call-403440647070611719': 'file_storage/function-call-403440647070611719.json', 'var_function-call-403440647070612544': 'file_storage/function-call-403440647070612544.json', 'var_function-call-260576047833116338': 'file_storage/function-call-260576047833116338.json', 'var_function-call-10305514131646820460': 'file_storage/function-call-10305514131646820460.json', 'var_function-call-5618153105640558916': 'file_storage/function-call-5618153105640558916.json'}

exec(code, env_args)
