code = """import json
res = var_call_RoX66CPtmqtCfZ9Edn3f7c1z
cand = res['candidate_tickers'] if isinstance(res, dict) else json.loads(res)['candidate_tickers']

parts = []
for t in cand:
    parts.append(
        f"SELECT '{t}' AS Symbol, CAST(COUNT(*) AS BIGINT) AS days_count FROM ("
        f"SELECT Date, High, Low FROM \"{t}\" "
        f"WHERE Date >= '2019-01-01' AND Date < '2020-01-01' "
        f"AND Low IS NOT NULL AND Low > 0 AND High IS NOT NULL "
        f"AND (High - Low) / Low > 0.2"
        f") s"
    )

union_query = " UNION ALL ".join(parts) + " ORDER BY days_count DESC, Symbol ASC LIMIT 5;"

print('__RESULT__:')
print(json.dumps({'sql': union_query}))"""

env_args = {'var_call_pDpILRLzxzoT5P1Kosgioq0m': 'file_storage/call_pDpILRLzxzoT5P1Kosgioq0m.json', 'var_call_MCUnaKaEKzfS0pL4YmqLF0EK': 'file_storage/call_MCUnaKaEKzfS0pL4YmqLF0EK.json', 'var_call_RoX66CPtmqtCfZ9Edn3f7c1z': {'candidate_tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'n': 86}, 'var_call_7o3COXjG6E8N9Fp3QgIcfpmp': 'file_storage/call_7o3COXjG6E8N9Fp3QgIcfpmp.json'}

exec(code, env_args)
