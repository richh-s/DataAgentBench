code = """import json
symbols = var_call_ViohjA2g7kDqYXIDjjz3qdWZ['symbols']

parts = []
for s in symbols:
    parts.append(
        "SELECT '"+s+"' AS Symbol, COUNT(*) AS cnt FROM \""+s+"\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) / Low > 0.2"
    )
q = " UNION ALL ".join(parts)
sql = "SELECT Symbol, cnt FROM ("+q+") ORDER BY cnt DESC, Symbol ASC LIMIT 5;"

print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_DqrJ20Dt6kRZ0Xf4cm1RtXQg': 'file_storage/call_DqrJ20Dt6kRZ0Xf4cm1RtXQg.json', 'var_call_ViohjA2g7kDqYXIDjjz3qdWZ': {'n_total': 86, 'n_common': 86, 'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}, 'var_call_AREtt9xxwb8L8HlhehNmyqYW': 'file_storage/call_AREtt9xxwb8L8HlhehNmyqYW.json', 'var_call_hnx1eRDETSlVjqPpzvEPm2bU': {'n_symbols': 86, 'n_in_trade_db': 86, 'missing': []}}

exec(code, env_args)
