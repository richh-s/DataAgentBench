code = """import json, pandas as pd
paths = {
 'AGMH': var_call_jkID5uPdJmGAp0joXw7iidP0,
 'ALACU': var_call_wcuoPAyMnSkqC4aMxxs0XoYZ,
 'ANDA': var_call_823PfdLSv3RJU3aWveEABchz,
 'APEX': var_call_uUCxhFyaQXmPp0mSDUrDgyx9,
 'BCLI': var_call_HaE3BYRQ5bZKKYO2Pph8nHGL,
 'BHAT': var_call_sjckutrv0OjH7PiXCbucjQYw,
 'BIOC': var_call_U42SAVxVZiewr5FTCFZpkXBs,
 'BKYI': var_call_FrieFN22pGgDYHScfv3fXQyv,
 'BLFS': var_call_I68L2TYwedwhTpLcjQP55CLC,
 'BOSC': var_call_8IY0ul8xSyjYJzB8oxf4UP2Y,
 'BOTJ': var_call_8HR83d5JyWQmWIfcKiOoIufz,
 'BWEN': var_call_T0F5CKrih5nWzO4cLNqPnc8m,
 'CBAT': var_call_8MvKs2adpUu06RgStjlq19L0,
 'CCCL': var_call_iShugSkouqrMhrnlGr55ZyPh,
 'CDMOP': var_call_fUN3dtxuA8HFRSb2oEQBJ1Y3
}
frames = []
for sym, path in paths.items():
    if isinstance(path, str):
        with open(path, 'r') as f:
            data = json.load(f)
    else:
        data = path
    if not data:
        continue
    df = pd.DataFrame(data)
    df['High'] = pd.to_numeric(df['High'])
    df['Low'] = pd.to_numeric(df['Low'])
    df['range_pct'] = (df['High'] - df['Low']) / df['Low']
    count = (df['range_pct'] > 0.2).sum()
    frames.append({'Symbol': sym, 'DaysOver20Pct': int(count)})
res = pd.DataFrame(frames).sort_values('DaysOver20Pct', ascending=False)
print('__RESULT__:')
print(res.to_json(orient='records'))"""

env_args = {'var_call_l2OZI76iNWq57oZUH6RuuG4P': 'file_storage/call_l2OZI76iNWq57oZUH6RuuG4P.json', 'var_call_XutlXI7WfJsJZQTGrY7FduU5': 'file_storage/call_XutlXI7WfJsJZQTGrY7FduU5.json', 'var_call_mkPncQr6Sp6JEiGH5tjo5Mwj': [['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']], 'var_call_jkID5uPdJmGAp0joXw7iidP0': 'file_storage/call_jkID5uPdJmGAp0joXw7iidP0.json', 'var_call_wcuoPAyMnSkqC4aMxxs0XoYZ': 'file_storage/call_wcuoPAyMnSkqC4aMxxs0XoYZ.json', 'var_call_zwFv3SDOkQf7roCCws1bYgNJ': [], 'var_call_823PfdLSv3RJU3aWveEABchz': 'file_storage/call_823PfdLSv3RJU3aWveEABchz.json', 'var_call_uUCxhFyaQXmPp0mSDUrDgyx9': 'file_storage/call_uUCxhFyaQXmPp0mSDUrDgyx9.json', 'var_call_HaE3BYRQ5bZKKYO2Pph8nHGL': 'file_storage/call_HaE3BYRQ5bZKKYO2Pph8nHGL.json', 'var_call_sjckutrv0OjH7PiXCbucjQYw': 'file_storage/call_sjckutrv0OjH7PiXCbucjQYw.json', 'var_call_U42SAVxVZiewr5FTCFZpkXBs': 'file_storage/call_U42SAVxVZiewr5FTCFZpkXBs.json', 'var_call_FrieFN22pGgDYHScfv3fXQyv': 'file_storage/call_FrieFN22pGgDYHScfv3fXQyv.json', 'var_call_I68L2TYwedwhTpLcjQP55CLC': 'file_storage/call_I68L2TYwedwhTpLcjQP55CLC.json', 'var_call_8IY0ul8xSyjYJzB8oxf4UP2Y': 'file_storage/call_8IY0ul8xSyjYJzB8oxf4UP2Y.json', 'var_call_8HR83d5JyWQmWIfcKiOoIufz': 'file_storage/call_8HR83d5JyWQmWIfcKiOoIufz.json', 'var_call_T0F5CKrih5nWzO4cLNqPnc8m': 'file_storage/call_T0F5CKrih5nWzO4cLNqPnc8m.json', 'var_call_8MvKs2adpUu06RgStjlq19L0': 'file_storage/call_8MvKs2adpUu06RgStjlq19L0.json', 'var_call_iShugSkouqrMhrnlGr55ZyPh': 'file_storage/call_iShugSkouqrMhrnlGr55ZyPh.json', 'var_call_fUN3dtxuA8HFRSb2oEQBJ1Y3': 'file_storage/call_fUN3dtxuA8HFRSb2oEQBJ1Y3.json'}

exec(code, env_args)
