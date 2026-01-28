code = """import json
# Load all query results keys from the parallel call stored keys
keys = [
 'var_call_0R6ltubXBBFWQ1waC2Z8VD6N','var_call_qsdxYqddv0uqN52CsMm6m92r','var_call_xI7wNXKIRjQXk18VxTveQ33i',
 'var_call_i4vJxMzerxXbLSSUp0jM06Ra','var_call_GpUNVqeSfdabKPRmhgEgTf47','var_call_KIZ7jDQku2idlIOovH9h1kBZ',
 'var_call_6ly55qgMCNhPXSVEZGSRRrqq','var_call_kLuUHWdrxtAiVMD16MVUYScS','var_call_kVjoBDDwBptb5Bxc4mPTxrqM',
 'var_call_HQ2i3EHDnMloHcfdbS2mLpSY','var_call_KupRW8EVhuK751O6ZcpcKXGZ','var_call_ITkKKcm97aS1Ij67iwJTHGvN',
 'var_call_AH3fOFOaLNwy1Fwf6Kr9pAcY','var_call_5bzJSPHdS0jqwofOWICBk9l8','var_call_yrVl2UCvlDErP9mIqk59Fin0',
 'var_call_rv86kr5Sm2lLDESGr06hK2WT','var_call_FZmbkseVjkxNDRi1NERh30J0','var_call_PxIIg0ppFiU2c2dHvnBRoUMs',
 'var_call_pxKFhgnPM9sRe0K0KpWV2P46','var_call_sQ1h14SakFzQ6fX2HjsuqO3f','var_call_STK1nOyJwrk5eMV8vUos8va0',
 'var_call_qmMynxogglXbcGk0hKAOoL5L','var_call_YsJRg5JwExmgpXYilaW5tPlR','var_call_ezFgVmtMB6nZxVJsv4EsihvN',
 'var_call_Lq5VGkQJ9PP6PcoroGbzhQym','var_call_I5c91O8fvUdMv3vsGapoW4Xh','var_call_J2nYk12WL1fD66kfwO529yHR',
 'var_call_q5TOc8thtNia7UaddtNy3uNk','var_call_gOHCfFOtj7wSbMt20tXVtuvY','var_call_SyLAQnF4KsrOL2A0YnpjZVvX',
 'var_call_7h3rIhgTs8dA601EOrs7Omie','var_call_C90Q3P5piU8NhtoJf2gOTEjU','var_call_bSE6kELWNN7Aha6VDhJqMbta',
 'var_call_h9ev6QBI80mcQb727XX8oZfV','var_call_mX7ngWc8G26WCxIM1v2lDMEf','var_call_P5LwaNyyQjwrM0YX3frdfLwc',
 'var_call_DW2hKlblpZcE2hK1FwUEC3jX','var_call_gTrNpFMXGrgSvphrZza3Biyb','var_call_xvmS85QskxcpqGinTvpWXfvL',
 'var_call_HmrEZiU6TZZt2YPDKBNYxsZl','var_call_1LZe6HTibnCwuQOqZMBT6oZv','var_call_Xu1kqp0fYBTsb14fGYNoZVm7',
 'var_call_p1SEQwrhtBRBPswifrVfVORt','var_call_0ipqepRlsqwAU9ViC1QRis4O','var_call_mJBFCGLIrTf47xXqbhrJU7Wm',
 'var_call_Qt91HOjXojtyqoxs5R0Hg2KL','var_call_LthTMA3UTvQe3f3NeCerPUKA','var_call_zNNPx5xkDVIKHS9RtMcV9lPD',
 'var_call_DFGqCPhca9A1wFd71t2aKQj6','var_call_0MmFCMdMmupbv0x6EuYK4Cw1'
]
all_rows = []
for k in keys:
    with open(k, 'r') as f:
        txt = f.read()
    # the file contains the JSON list directly
    data = json.loads(txt)
    # data is a list e.g. [{"Symbol": "AGMH", "cnt": "13.0"}]
    for row in data:
        sym = row['Symbol']
        # cnt might be 'nan' string
        cnt = row['cnt']
        try:
            cntv = float(cnt)
            if cntv != cntv: # nan check
                cntv = 0.0
        except:
            cntv = 0.0
        all_rows.append({'Symbol': sym, 'cnt': int(cntv)})
# sort by cnt desc then symbol
all_rows_sorted = sorted(all_rows, key=lambda r: (-r['cnt'], r['Symbol']))
# take top 5
top5 = all_rows_sorted[:5]
print('__RESULT__:')
print(json.dumps({'top5_symbols': top5, 'all_count': len(all_rows_sorted)}))"""

env_args = {'var_call_PPqOo48KnLzN7VZUluh7p1Pf': 'file_storage/call_PPqOo48KnLzN7VZUluh7p1Pf.json', 'var_call_MxbtFlCKNvwOOD1Kk6AOFzDM': 'file_storage/call_MxbtFlCKNvwOOD1Kk6AOFzDM.json', 'var_call_t3UInuKPgfoZduflOJPGqTNT': {'num_stockinfo_S': 86, 'num_trade_tables': 2753, 'num_intersection': 86, 'intersection_sample': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP'], 'intersection_all_count': 86}, 'var_call_0R6ltubXBBFWQ1waC2Z8VD6N': [{'Symbol': 'AGMH', 'cnt': '13.0'}], 'var_call_qsdxYqddv0uqN52CsMm6m92r': [{'Symbol': 'ALACU', 'cnt': '0.0'}], 'var_call_xI7wNXKIRjQXk18VxTveQ33i': [{'Symbol': 'AMHC', 'cnt': 'nan'}], 'var_call_i4vJxMzerxXbLSSUp0jM06Ra': [{'Symbol': 'ANDA', 'cnt': '0.0'}], 'var_call_GpUNVqeSfdabKPRmhgEgTf47': [{'Symbol': 'APEX', 'cnt': '15.0'}], 'var_call_KIZ7jDQku2idlIOovH9h1kBZ': [{'Symbol': 'BCLI', 'cnt': '0.0'}], 'var_call_6ly55qgMCNhPXSVEZGSRRrqq': [{'Symbol': 'BHAT', 'cnt': '10.0'}], 'var_call_kLuUHWdrxtAiVMD16MVUYScS': [{'Symbol': 'BIOC', 'cnt': '21.0'}], 'var_call_kVjoBDDwBptb5Bxc4mPTxrqM': [{'Symbol': 'BKYI', 'cnt': '16.0'}], 'var_call_HQ2i3EHDnMloHcfdbS2mLpSY': [{'Symbol': 'BLFS', 'cnt': '0.0'}], 'var_call_KupRW8EVhuK751O6ZcpcKXGZ': [{'Symbol': 'BOSC', 'cnt': '3.0'}], 'var_call_ITkKKcm97aS1Ij67iwJTHGvN': [{'Symbol': 'BOTJ', 'cnt': '0.0'}], 'var_call_AH3fOFOaLNwy1Fwf6Kr9pAcY': [{'Symbol': 'BWEN', 'cnt': '5.0'}], 'var_call_5bzJSPHdS0jqwofOWICBk9l8': [{'Symbol': 'CBAT', 'cnt': '23.0'}], 'var_call_yrVl2UCvlDErP9mIqk59Fin0': [{'Symbol': 'CCCL', 'cnt': '13.0'}], 'var_call_rv86kr5Sm2lLDESGr06hK2WT': [{'Symbol': 'CDMOP', 'cnt': '0.0'}], 'var_call_FZmbkseVjkxNDRi1NERh30J0': [{'Symbol': 'CEMI', 'cnt': '3.0'}], 'var_call_PxIIg0ppFiU2c2dHvnBRoUMs': [{'Symbol': 'CFBK', 'cnt': '0.0'}], 'var_call_pxKFhgnPM9sRe0K0KpWV2P46': [{'Symbol': 'CFFA', 'cnt': '0.0'}], 'var_call_sQ1h14SakFzQ6fX2HjsuqO3f': [{'Symbol': 'CLRB', 'cnt': '14.0'}], 'var_call_STK1nOyJwrk5eMV8vUos8va0': [{'Symbol': 'CORV', 'cnt': '10.0'}], 'var_call_qmMynxogglXbcGk0hKAOoL5L': [{'Symbol': 'CPAAU', 'cnt': '0.0'}], 'var_call_YsJRg5JwExmgpXYilaW5tPlR': [{'Symbol': 'CPAH', 'cnt': '16.0'}], 'var_call_ezFgVmtMB6nZxVJsv4EsihvN': [{'Symbol': 'CUBA', 'cnt': '0.0'}], 'var_call_Lq5VGkQJ9PP6PcoroGbzhQym': [{'Symbol': 'CVV', 'cnt': '0.0'}], 'var_call_I5c91O8fvUdMv3vsGapoW4Xh': [{'Symbol': 'DZSI', 'cnt': '1.0'}], 'var_call_J2nYk12WL1fD66kfwO529yHR': [{'Symbol': 'ELSE', 'cnt': '0.0'}], 'var_call_q5TOc8thtNia7UaddtNy3uNk': [{'Symbol': 'EXPC', 'cnt': '0.0'}], 'var_call_gOHCfFOtj7wSbMt20tXVtuvY': [{'Symbol': 'EYEG', 'cnt': '18.0'}], 'var_call_SyLAQnF4KsrOL2A0YnpjZVvX': [{'Symbol': 'FAMI', 'cnt': '23.0'}], 'var_call_7h3rIhgTs8dA601EOrs7Omie': [{'Symbol': 'FNCB', 'cnt': '1.0'}], 'var_call_C90Q3P5piU8NhtoJf2gOTEjU': [{'Symbol': 'FSBW', 'cnt': '0.0'}], 'var_call_bSE6kELWNN7Aha6VDhJqMbta': [{'Symbol': 'FTFT', 'cnt': '21.0'}], 'var_call_h9ev6QBI80mcQb727XX8oZfV': [{'Symbol': 'GDYN', 'cnt': '0.0'}], 'var_call_mX7ngWc8G26WCxIM1v2lDMEf': [{'Symbol': 'GLG', 'cnt': '42.0'}], 'var_call_P5LwaNyyQjwrM0YX3frdfLwc': [{'Symbol': 'GRNVU', 'cnt': '0.0'}], 'var_call_DW2hKlblpZcE2hK1FwUEC3jX': [{'Symbol': 'GTEC', 'cnt': '0.0'}], 'var_call_gTrNpFMXGrgSvphrZza3Biyb': [{'Symbol': 'HCCOU', 'cnt': '0.0'}], 'var_call_xvmS85QskxcpqGinTvpWXfvL': [{'Symbol': 'HNNA', 'cnt': '0.0'}], 'var_call_HmrEZiU6TZZt2YPDKBNYxsZl': [{'Symbol': 'HQI', 'cnt': '2.0'}], 'var_call_1LZe6HTibnCwuQOqZMBT6oZv': [{'Symbol': 'HRTX', 'cnt': '1.0'}], 'var_call_Xu1kqp0fYBTsb14fGYNoZVm7': [{'Symbol': 'IDEX', 'cnt': '15.0'}], 'var_call_p1SEQwrhtBRBPswifrVfVORt': [{'Symbol': 'IGIC', 'cnt': '0.0'}], 'var_call_0ipqepRlsqwAU9ViC1QRis4O': [{'Symbol': 'IOTS', 'cnt': '1.0'}], 'var_call_mJBFCGLIrTf47xXqbhrJU7Wm': [{'Symbol': 'ISNS', 'cnt': '0.0'}], 'var_call_Qt91HOjXojtyqoxs5R0Hg2KL': [{'Symbol': 'ITI', 'cnt': '0.0'}], 'var_call_LthTMA3UTvQe3f3NeCerPUKA': [{'Symbol': 'LACQ', 'cnt': '0.0'}], 'var_call_zNNPx5xkDVIKHS9RtMcV9lPD': [{'Symbol': 'MBCN', 'cnt': '0.0'}], 'var_call_DFGqCPhca9A1wFd71t2aKQj6': [{'Symbol': 'MBNKP', 'cnt': '0.0'}], 'var_call_0MmFCMdMmupbv0x6EuYK4Cw1': [{'Symbol': 'MCEP', 'cnt': '14.0'}]}

exec(code, env_args)
