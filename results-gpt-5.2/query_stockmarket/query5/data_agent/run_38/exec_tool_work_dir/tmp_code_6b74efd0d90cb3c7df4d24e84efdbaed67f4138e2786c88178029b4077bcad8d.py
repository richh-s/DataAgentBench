code = """import json

tickers = var_call_S5t1p5RKaRddOoqE08d7y6ez['available']

selects = []
for t in tickers:
    sel = (
        f"SELECT '{t}' AS Symbol, CAST(COUNT(*) AS BIGINT) AS days "
        f"FROM \"{t}\" "
        + "WHERE Date >= '2019-01-01' AND Date < '2020-01-01' "
        + "AND Low IS NOT NULL AND Low > 0 AND High IS NOT NULL "
        + "AND (High - Low)/Low > 0.2"
    )
    selects.append(sel)

query = " UNION ALL ".join(selects) + " ORDER BY days DESC, Symbol ASC LIMIT 5;"

print('__RESULT__:')
print(json.dumps(query))"""

env_args = {'var_call_H2hcxVjddyl5n2L4MVpMNrjI': 'file_storage/call_H2hcxVjddyl5n2L4MVpMNrjI.json', 'var_call_QfZYyFBpPBlsKm8JbdZRunEq': {'tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'n': 86}, 'var_call_GIlC3qtu85xQNESV78Zcc4y7': 'file_storage/call_GIlC3qtu85xQNESV78Zcc4y7.json', 'var_call_S5t1p5RKaRddOoqE08d7y6ez': {'available': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'n_available': 86, 'n_missing': 0, 'missing_sample': []}, 'var_call_BfrRKswKFoaYnuPjl1oRU5st': 'file_storage/call_BfrRKswKFoaYnuPjl1oRU5st.json', 'var_call_gmuhGnwrFtL5YTcUsn5utLhu': 'file_storage/call_gmuhGnwrFtL5YTcUsn5utLhu.json'}

exec(code, env_args)
