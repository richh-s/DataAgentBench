code = """import json
p1 = var_call_M0U5buiAvISz429MtqwKvqqA
p2 = var_call_4e328mmHfSVOI68hPDqpaEt8
with open(p1, 'r') as f:
    data1 = json.load(f)
with open(p2, 'r') as f:
    data2 = json.load(f)
symbol_to_company = {rec['Symbol']: rec.get('Company Description','') for rec in data1}
tables = set(data2)
common = [s for s in symbol_to_company.keys() if s in tables]
# Build SQL
selects = []
for s in sorted(common):
    comp = symbol_to_company[s].replace("'", "''")
    sel = "SELECT '{sym}' AS symbol, '{comp}' AS company, SUM(CASE WHEN (\"High\" - \"Low\") > 0.2 * \"Low\" AND \"Date\" >= '2019-01-01' AND \"Date\" <= '2019-12-31' THEN 1 ELSE 0 END) AS cnt FROM \"{sym}\"".format(sym=s, comp=comp)
    selects.append(sel)
union_sql = ' UNION ALL '.join(selects)
final_sql = 'SELECT symbol, company, cnt FROM ( ' + union_sql + ' ) ORDER BY cnt DESC LIMIT 5;'
out = {'sql': final_sql, 'num_symbols': len(common)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_M0U5buiAvISz429MtqwKvqqA': 'file_storage/call_M0U5buiAvISz429MtqwKvqqA.json', 'var_call_4e328mmHfSVOI68hPDqpaEt8': 'file_storage/call_4e328mmHfSVOI68hPDqpaEt8.json', 'var_call_ieif7E55M9zu0rRuxqr9BMXT': {'count': 86, 'symbols_sample': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}}

exec(code, env_args)
