code = """import json
symbols = [r['Symbol'] for r in var_call_PxcmhVLGvHgoLPAHzeAHHgxC]

# Build UNION ALL query to count days in 2019 with (High-Low) > 0.2*Low (and Low>0)
parts = []
for s in symbols:
    ident = '"' + s.replace('"','""') + '"'
    parts.append(
        f"SELECT '{s}' AS Symbol, COUNT(*) AS days_exceed_20pct FROM {ident} "
        "WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' "
        "AND Low IS NOT NULL AND High IS NOT NULL AND Low > 0 "
        "AND (High - Low) > 0.2 * Low"
    )
query = " UNION ALL ".join(parts) + " ORDER BY days_exceed_20pct DESC, Symbol ASC LIMIT 5;"

print('__RESULT__:')
print(json.dumps({'sql': query, 'n_symbols': len(symbols)}))"""

env_args = {'var_call_kAC0K9TV4dAzsdbJNSCCsokM': 'file_storage/call_kAC0K9TV4dAzsdbJNSCCsokM.json', 'var_call_ZX1PzK6u0ZGnFSK4F7JAjOvY': {'symbols_total': 86, 'symbols_sql': "SELECT table_name AS Symbol FROM information_schema.tables WHERE table_schema = 'main' AND table_type = 'BASE TABLE' AND table_name IN ('AGMH','ALACU','AMHC','ANDA','APEX','BCLI','BHAT','BIOC','BKYI','BLFS','BOSC','BOTJ','BWEN','CBAT','CCCL','CDMOP','CEMI','CFBK','CFFA','CLRB','CORV','CPAAU','CPAH','CUBA','CVV','DZSI','ELSE','EXPC','EYEG','FAMI','FNCB','FSBW','FTFT','GDYN','GLG','GRNVU','GTEC','HCCOU','HNNA','HQI','HRTX','IDEX','IGIC','IOTS','ISNS','ITI','LACQ','MBCN','MBNKP','MCEP','MLND','MMAC','MNCLU','MNPR','NVEE','NXTD','OPOF','OPTT','ORGO','ORSNU','OTEL','PBFS','PBTS','PCSB','PECK','PEIX','PFIE','PLIN','POPE','QRHC','SES','SHSP','SNSS','SSNT','STKS','TGLS','TMSR','VERB','VMD','VRRM','VTIQW','VVPR','WHLM','WHLR','XBIOW','XPEL');"}, 'var_call_PxcmhVLGvHgoLPAHzeAHHgxC': [{'Symbol': 'AGMH'}, {'Symbol': 'ALACU'}, {'Symbol': 'AMHC'}, {'Symbol': 'ANDA'}, {'Symbol': 'APEX'}, {'Symbol': 'BCLI'}, {'Symbol': 'BHAT'}, {'Symbol': 'BIOC'}, {'Symbol': 'BKYI'}, {'Symbol': 'BLFS'}, {'Symbol': 'BOSC'}, {'Symbol': 'BOTJ'}, {'Symbol': 'BWEN'}, {'Symbol': 'CBAT'}, {'Symbol': 'CCCL'}, {'Symbol': 'CDMOP'}, {'Symbol': 'CEMI'}, {'Symbol': 'CFBK'}, {'Symbol': 'CFFA'}, {'Symbol': 'CLRB'}, {'Symbol': 'CORV'}, {'Symbol': 'CPAAU'}, {'Symbol': 'CPAH'}, {'Symbol': 'CUBA'}, {'Symbol': 'CVV'}, {'Symbol': 'DZSI'}, {'Symbol': 'ELSE'}, {'Symbol': 'EXPC'}, {'Symbol': 'EYEG'}, {'Symbol': 'FAMI'}, {'Symbol': 'FNCB'}, {'Symbol': 'FSBW'}, {'Symbol': 'FTFT'}, {'Symbol': 'GDYN'}, {'Symbol': 'GLG'}, {'Symbol': 'GRNVU'}, {'Symbol': 'GTEC'}, {'Symbol': 'HCCOU'}, {'Symbol': 'HNNA'}, {'Symbol': 'HQI'}, {'Symbol': 'HRTX'}, {'Symbol': 'IDEX'}, {'Symbol': 'IGIC'}, {'Symbol': 'IOTS'}, {'Symbol': 'ISNS'}, {'Symbol': 'ITI'}, {'Symbol': 'LACQ'}, {'Symbol': 'MBCN'}, {'Symbol': 'MBNKP'}, {'Symbol': 'MCEP'}, {'Symbol': 'MLND'}, {'Symbol': 'MMAC'}, {'Symbol': 'MNCLU'}, {'Symbol': 'MNPR'}, {'Symbol': 'NVEE'}, {'Symbol': 'NXTD'}, {'Symbol': 'OPOF'}, {'Symbol': 'OPTT'}, {'Symbol': 'ORGO'}, {'Symbol': 'ORSNU'}, {'Symbol': 'OTEL'}, {'Symbol': 'PBFS'}, {'Symbol': 'PBTS'}, {'Symbol': 'PCSB'}, {'Symbol': 'PECK'}, {'Symbol': 'PEIX'}, {'Symbol': 'PFIE'}, {'Symbol': 'PLIN'}, {'Symbol': 'POPE'}, {'Symbol': 'QRHC'}, {'Symbol': 'SES'}, {'Symbol': 'SHSP'}, {'Symbol': 'SNSS'}, {'Symbol': 'SSNT'}, {'Symbol': 'STKS'}, {'Symbol': 'TGLS'}, {'Symbol': 'TMSR'}, {'Symbol': 'VERB'}, {'Symbol': 'VMD'}, {'Symbol': 'VRRM'}, {'Symbol': 'VTIQW'}, {'Symbol': 'VVPR'}, {'Symbol': 'WHLM'}, {'Symbol': 'WHLR'}, {'Symbol': 'XBIOW'}, {'Symbol': 'XPEL'}]}

exec(code, env_args)
