code = """import json, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

fund = load_records(var_call_9cXbeBzbNaOXIHYfXpfQYeX9)
fund_df = pd.DataFrame(fund)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

# Disaster-related projects: use naming convention with FEMA/CalOES/CalJPIA/FEMA Project
mask = fund_df['Project_Name'].str.contains('FEMA|CalOES|CalJPIA', case=False, na=False)
# Projects that started in 2022: use name contains '2022'
mask2 = fund_df['Project_Name'].str.contains('2022', na=False)

total = int(fund_df[mask & mask2]['total_amount'].sum())
projects = fund_df[mask & mask2][['Project_Name','total_amount']].sort_values('Project_Name').to_dict('records')

out={'total_funding': total, 'projects': projects}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_WforWNGckDLZNcgvbG8AKAU6': ['Funding'], 'var_call_QfAvDZ3qPtBCuw0ojwVBpNT6': ['civic_docs'], 'var_call_pvJShtqIdgjHoyyWmysUP8iU': 'file_storage/call_pvJShtqIdgjHoyyWmysUP8iU.json', 'var_call_9cXbeBzbNaOXIHYfXpfQYeX9': 'file_storage/call_9cXbeBzbNaOXIHYfXpfQYeX9.json', 'var_call_SQoTkmoTWIbOJzh1MoSBeDNQ': [], 'var_call_GJsuDFVB0bTNRESDDnW2BAs3': {'filename': 'malibucity_agenda_03222023-2060.txt', 'has_phrase': True, 'snippet': 'Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current and\nupcoming Capital Improvement Projects and Disaster Recovery Projects.\n\nDISCUSSION: Staff will provide a status update on the following active projects in the\nFiscal Year 2022-2023 Capital Improvement Program:\n\nCapital Improvement Projects (Design)\n\n2022 Morning View Resurfacing & Storm Drain Improvements\n\n(cid:190) Updates:\n\n(cid:131) Staff is working with the consultant '}, 'var_call_kQDJ26XM3UOfI1mNEVk016On': ['malibucity_agenda__06282023-2116.txt', 'malibucity_agenda__09272023-2155.txt'], 'var_call_Jj4tPnpovouE2ChvMBrqC3OC': 'file_storage/call_Jj4tPnpovouE2ChvMBrqC3OC.json'}

exec(code, env_args)
