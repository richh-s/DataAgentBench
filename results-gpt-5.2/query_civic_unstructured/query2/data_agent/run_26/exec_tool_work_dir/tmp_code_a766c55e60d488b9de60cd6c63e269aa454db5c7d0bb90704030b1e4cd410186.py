code = """import json, pandas as pd

def load_tool_result(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x,'r',encoding='utf-8') as f:
            return json.load(f)
    return x

fund=load_tool_result(var_call_QZtCO6cQtvO8QTD4wdb2dF3L)
fund_df=pd.DataFrame(fund)
fund_df['total_amount']=pd.to_numeric(fund_df['total_amount'])
name='Bluffs Park Shade Structure'
amount=int(fund_df.loc[fund_df.Project_Name==name,'total_amount'].sum())
print('__RESULT__:')
print(json.dumps({'project':name,'amount':amount}))"""

env_args = {'var_call_hXf50YBfCrrwm4VISQMICNsZ': ['Funding'], 'var_call_SxtnxuThncsmTRlN1JT8h0Dx': ['civic_docs'], 'var_call_UCJq4gDEzfiZVQPH44VuWTPI': 'file_storage/call_UCJq4gDEzfiZVQPH44VuWTPI.json', 'var_call_QZtCO6cQtvO8QTD4wdb2dF3L': 'file_storage/call_QZtCO6cQtvO8QTD4wdb2dF3L.json', 'var_call_daScurDCWm3lCH5Z7VUW1soU': {'projects_completed_2022_park': [], 'matched_projects': [], 'total_funding': 0}, 'var_call_jx825yvGj5t1RO9j1r5BxfCm': [{'i': 137, 'line': '(cid:131) Plans and specifications have been completed', 'context': ['(cid:190) Updates:', '', '(cid:131) Plans and specifications have been completed', '(cid:131) Awaiting final FEMA/CalOES approval for scope modification', '']}, {'i': 149, 'line': '(cid:131) Field data collection has been completed and storm drain inventory has', 'context': ['(cid:190) Updates:', '', '(cid:131) Field data collection has been completed and storm drain inventory has', '', 'been finalized and incorporated into GIS.']}, {'i': 314, 'line': '(cid:190) Updates: Construction was completed November 2022. Notice of completion', 'context': ['Bluffs Park Shade Structure', '', '(cid:190) Updates: Construction was completed November 2022. Notice of completion', '', 'filed January 2023']}, {'i': 335, 'line': '(cid:131) Construction was completed, January 2023', 'context': ['(cid:190) Updates:', '', '(cid:131) Construction was completed, January 2023', '(cid:131) Scheduled for Council acceptance on April 24, 2023', '']}, {'i': 342, 'line': '(cid:131) Construction was completed, November 2022', 'context': ['(cid:190) Updates:', '', '(cid:131) Construction was completed, November 2022', '(cid:131) Notice of completion filed January 2023', '']}, {'i': 348, 'line': '(cid:131) Construction was completed, November 2022', 'context': ['(cid:190) Updates:', '', '(cid:131) Construction was completed, November 2022', '(cid:131) Notice of completion filed January 2023', '']}], 'var_call_SW73zavkufIUTTcjJF3JGvZs': {'projects': [], 'total_funding': 0, 'matched': []}, 'var_call_EzTxSsaG4wvDCAsUvus10f6V': {'name': 'Bluffs Park Shade Structure', 'window': '(cid:190) Project Schedule:  (cid:131) Begin construction: Summer 2023 (cid:131) Complete Construction: Summer 2023  Bluffs Park Shade Structure  (cid:190) Updates: Construction was completed November 2022. Notice of completion  filed January 2023  Page 4 of 6'}, 'var_call_W8M2vGAPzhZmp7KIynKuxOlQ': {'line': '(cid:190) Updates: Construction was completed November 2022. Notice of completion', 'match_construction_completed': True, 'has_2022': True}, 'var_call_inJ7MiXtDSTK3UCekRGgNQny': [], 'var_call_m4WvobkweONLXd77kftGyIeV': [], 'var_call_oQUfbh6uhKnEusRElU9lLdVb': {'has_Bluffs': True, 'sample': 'Bluffs Park South Walkway Repairs\n\n(cid:190) Updates:\n\n(cid:'}, 'var_call_nBkMLp4idDO8kShaq5qrAB1c': [[169, 'Trancas Canyon Park Upper and Lower Slopes Repair'], [195, 'Permanent Skate Park'], [228, 'Malibu Bluffs Park South Walkway Repairs'], [250, 'Trancas Canyon Park Playground'], [312, 'Bluffs Park Shade Structure']], 'var_call_2mdHauMeJxrJy4w8kaU4kZLG': ['Bluffs Park Shade Structure']}

exec(code, env_args)
