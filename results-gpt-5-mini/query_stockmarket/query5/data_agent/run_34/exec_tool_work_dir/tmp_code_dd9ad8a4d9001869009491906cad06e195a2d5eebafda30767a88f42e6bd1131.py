code = """import json
with open(var_call_pv35gldVJD8ASrqFZ76kYpsg, 'r') as f:
    symbols = json.load(f)
# Build SQL that unions counts per symbol
parts = []
for s in symbols:
    part = f"SELECT '{s}' AS Symbol, COUNT(*) AS cnt FROM \"{s}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > 0.2 * Low"
    parts.append(part)
sql = '\nUNION ALL\n'.join(parts) + '\nORDER BY cnt DESC, Symbol LIMIT 100;'
print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_Ew9OW2P4eOTHwsKbf4bvzLXN': 'file_storage/call_Ew9OW2P4eOTHwsKbf4bvzLXN.json', 'var_call_rnjSRrb2z06qGhayW5e8MrpQ': 'file_storage/call_rnjSRrb2z06qGhayW5e8MrpQ.json', 'var_call_pv35gldVJD8ASrqFZ76kYpsg': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}

exec(code, env_args)
