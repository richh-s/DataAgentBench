code = """import json, pandas as pd

def norm_id(x):
    if x is None:
        return None
    return str(x).strip().lstrip('#')

cases = pd.DataFrame(var_call_vtP11mjgor6oY3cGsuW1UTO0)
cases['orderitem_norm'] = cases['orderitemid__c'].map(norm_id)
cases['created_dt'] = pd.to_datetime(cases['createddate'], utc=True, errors='coerce')

path = var_call_WL0Pxw2c20UOffU2OdAZABXM
with open(path, 'r') as f:
    oi_records = json.load(f)
ois = pd.DataFrame(oi_records)
ois['orderitem_norm'] = ois['orderitem_id'].map(norm_id)
ois['product_norm'] = ois['Product2Id'].map(norm_id)

target = norm_id('01tWt000006hVJdIAM')

df = cases.merge(ois[['orderitem_norm','product_norm']], on='orderitem_norm', how='left')
df = df[df['product_norm'] == target].copy()

df['month_start'] = df['created_dt'].dt.to_period('M').dt.to_timestamp()
counts = df.groupby('month_start').size().sort_index()

if len(counts)==0:
    out = None
else:
    mean = float(counts.mean())
    std = float(counts.std(ddof=0))
    if std == 0:
        out = counts.idxmax().strftime('%B')
    else:
        z = (counts - mean) / std
        sig = z[z > 1.5]
        out = (sig.idxmax() if len(sig)>0 else counts.idxmax()).strftime('%B')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_WL0Pxw2c20UOffU2OdAZABXM': 'file_storage/call_WL0Pxw2c20UOffU2OdAZABXM.json', 'var_call_vtP11mjgor6oY3cGsuW1UTO0': [{'createddate': '2020-12-29T08:36:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'createddate': '2020-09-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'createddate': '2021-01-10T09:30:00.000+0000', 'orderitemid__c': '802Wt00000797axIAA'}, {'createddate': '2020-09-05T09:15:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'createddate': '2021-03-31T11:41:00.000+0000', 'orderitemid__c': '802Wt00000798OvIAI'}, {'createddate': '2020-07-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000795XwIAI'}, {'createddate': '2020-07-01T15:30:00.000+0000', 'orderitemid__c': '802Wt00000794bTIAQ'}, {'createddate': '2021-03-24T18:04:00.000+0000', 'orderitemid__c': '802Wt00000796dGIAQ'}, {'createddate': '2021-03-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'createddate': '2020-11-05T11:00:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'createddate': '2021-02-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}, {'createddate': '2021-01-25T09:30:00.000+0000', 'orderitemid__c': '802Wt00000799o1IAA'}, {'createddate': '2020-11-05T08:19:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'createddate': '2020-10-01T14:30:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'createddate': '2020-09-03T14:45:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'createddate': '2020-10-22T03:55:00.000+0000', 'orderitemid__c': '802Wt00000796JtIAI'}, {'createddate': '2021-02-20T14:30:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'createddate': '2020-09-29T01:59:00.000+0000', 'orderitemid__c': '802Wt00000796bfIAA'}, {'createddate': '2021-01-03T15:30:00.000+0000', 'orderitemid__c': '802Wt00000799b7IAA'}, {'createddate': '2021-03-07T11:25:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'createddate': '2020-11-10T22:14:00.000+0000', 'orderitemid__c': '802Wt00000799uTIAQ'}, {'createddate': '2020-11-09T19:02:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'createddate': '2021-03-10T15:45:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}]}

exec(code, env_args)
