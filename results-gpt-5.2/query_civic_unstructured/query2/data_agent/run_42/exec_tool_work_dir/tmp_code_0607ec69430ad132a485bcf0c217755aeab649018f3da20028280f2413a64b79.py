code = """import json, re, pandas as pd

def load_records(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

civic = load_records(var_call_bHJGX4GoXn1vhcFVCm4sfVaJ)
fund = load_records(var_call_ysrpGoZ8cOuONtjxyV4hE5mC)

fund_df = pd.DataFrame(fund)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

text_all = "\n".join([d.get('text','') for d in civic])

parts = re.split(r"Capital Improvement Projects \(Completed\)", text_all, flags=re.I)
completed_text = parts[1] if len(parts) > 1 else text_all
completed_text = re.split(r"\n\s*Disaster Projects\b|\n\s*Capital Improvement Projects \(", completed_text, flags=re.I)[0]

park_kw = re.compile(r"\b(park|playground)\b", re.I)
fund_parks = fund_df[fund_df['Project_Name'].str.contains(park_kw, na=False)].copy()

completed_names = []
for name in fund_parks['Project_Name'].unique().tolist():
    if re.search(re.escape(name), completed_text, flags=re.I):
        completed_names.append(name)

completed_fund = fund_parks[fund_parks['Project_Name'].isin(completed_names)]

total = int(completed_fund['total_amount'].sum())

out = {
    'total_funding_usd': total,
    'completed_2022_park_projects_matched': completed_names,
    'matched_count': len(completed_names)
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_6JOmnlla3B3fVc8WUhQBuDT2': ['Funding'], 'var_call_VQqz1Q931QqJtlfAxctSfc45': ['civic_docs'], 'var_call_bHJGX4GoXn1vhcFVCm4sfVaJ': 'file_storage/call_bHJGX4GoXn1vhcFVCm4sfVaJ.json', 'var_call_ysrpGoZ8cOuONtjxyV4hE5mC': 'file_storage/call_ysrpGoZ8cOuONtjxyV4hE5mC.json'}

exec(code, env_args)
