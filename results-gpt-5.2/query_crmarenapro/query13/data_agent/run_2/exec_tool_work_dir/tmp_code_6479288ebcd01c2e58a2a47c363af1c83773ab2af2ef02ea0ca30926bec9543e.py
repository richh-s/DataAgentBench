code = """import json, pandas as pd
from datetime import date

def load(var):
    if isinstance(var, str):
        with open(var, 'r') as f:
            return json.load(f)
    return var

o = load(var_call_5LnoUhiZEBjNFXL15aHTUdej)
c = load(var_call_40TxtrDdh6a1o1tPpifKv6Iu)
oi = load(var_call_pHzjgPjtivWAVqaiC6nHwRk8)

df_o = pd.DataFrame(o)
df_c = pd.DataFrame(c)
df_oi = pd.DataFrame(oi)

# normalize ids: strip, remove leading '#', treat 'None' as null
for df, col in [(df_o,'ContractID__c'), (df_o,'OwnerId'), (df_c,'Id'), (df_oi,'OwnerId')]:
    if col in df.columns:
        s = df[col].astype('string')
        s = s.str.strip()
        s = s.where(~s.isin(['None','nan','NaN','']), None)
        s = s.str.lstrip('#')
        df[col] = s

# filter contracts in past 5 months relative to 2022-11-25 => from 2022-06-25 inclusive
start = pd.Timestamp('2022-06-25')
end = pd.Timestamp('2022-11-25')
df_c['CompanySignedDate'] = pd.to_datetime(df_c['CompanySignedDate'], errors='coerce')
elig_contracts = set(df_c.loc[(df_c['CompanySignedDate']>=start) & (df_c['CompanySignedDate']<=end), 'Id'].dropna())

# eligible opportunities by contract
eligible_owners = df_o.loc[df_o['ContractID__c'].isin(list(elig_contracts)), 'OwnerId'].dropna().unique().tolist()

# compute sales totals from orders by owner (orderitems have ownerId)
df_oi['Quantity'] = pd.to_numeric(df_oi['Quantity'], errors='coerce')
df_oi['UnitPrice'] = pd.to_numeric(df_oi['UnitPrice'], errors='coerce')
df_oi['Sales'] = df_oi['Quantity'] * df_oi['UnitPrice']

df_sales = df_oi[df_oi['OwnerId'].isin(eligible_owners)].groupby('OwnerId', as_index=False)['Sales'].sum()
if df_sales.empty:
    top_id = None
else:
    top_id = df_sales.sort_values(['Sales','OwnerId'], ascending=[False, True]).iloc[0]['OwnerId']

print('__RESULT__:')
print(json.dumps(top_id))"""

env_args = {'var_call_5LnoUhiZEBjNFXL15aHTUdej': 'file_storage/call_5LnoUhiZEBjNFXL15aHTUdej.json', 'var_call_40TxtrDdh6a1o1tPpifKv6Iu': 'file_storage/call_40TxtrDdh6a1o1tPpifKv6Iu.json', 'var_call_pHzjgPjtivWAVqaiC6nHwRk8': 'file_storage/call_pHzjgPjtivWAVqaiC6nHwRk8.json'}

exec(code, env_args)
