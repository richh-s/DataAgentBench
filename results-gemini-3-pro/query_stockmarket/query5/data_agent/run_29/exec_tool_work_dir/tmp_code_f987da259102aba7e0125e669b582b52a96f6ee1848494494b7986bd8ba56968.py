code = """s_str = "AGMH ALACU AMHC ANDA APEX BCLI BHAT BIOC BKYI BLFS BOSC BOTJ BWEN CBAT CCCL CDMOP CEMI CFBK CFFA CLRB CORV CPAAU CPAH CUBA CVV DZSI ELSE EXPC EYEG FAMI FNCB FSBW FTFT GDYN GLG GRNVU GTEC HCCOU HNNA HQI HRTX IDEX IGIC IOTS ISNS ITI LACQ MBCN MBNKP MCEP MLND MMAC MNCLU MNPR NVEE NXTD OPOF OPTT ORGO ORSNU OTEL PBFS PBTS PCSB PECK PEIX PFIE PLIN POPE QRHC SES SHSP SNSS SSNT STKS TGLS TMSR VERB VMD VRRM VTIQW VVPR WHLM WHLR XBIOW XPEL"
symbols = s_str.split()
parts = []
for sym in symbols:
    parts.append("SELECT '" + sym + "' as Symbol, COUNT(*) as Days FROM \"" + sym + "\" WHERE Date LIKE '2019-%' AND (High - Low) > 0.2 * Low")
full_query = " UNION ALL ".join(parts) + " ORDER BY Days DESC LIMIT 5"
print("__RESULT__:")
print(full_query)"""

env_args = {'var_function-call-6864036421110469424': 'file_storage/function-call-6864036421110469424.json', 'var_function-call-17804377391217170707': 'file_storage/function-call-17804377391217170707.json', 'var_function-call-376996191395007665': {'count': 86, 'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}, 'var_function-call-1901555800846452131': 'debug', 'var_function-call-5138997391997677328': [{'Symbol': 'AGMH', 'Days': '13'}]}

exec(code, env_args)
