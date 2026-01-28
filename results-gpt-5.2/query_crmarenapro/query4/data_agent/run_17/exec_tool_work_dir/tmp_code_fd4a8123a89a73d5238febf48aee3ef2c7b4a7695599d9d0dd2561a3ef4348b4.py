code = """import json, pandas as pd
rows = var_call_rVfl3lDNW1SJG067LveStELF
# past 10 months relative to 2021-04-10 are Jun 2020 through Mar 2021 (inclusive)
df = pd.DataFrame(rows)
df['month_start'] = pd.to_datetime(df['month_start'])
df['month'] = df['month_start'].dt.strftime('%B')
df['cnt'] = df['opp_lineitems'].astype(int)
# identify a month that significantly exceeds others: use z-score > 1.5 if possible else max
mean = df['cnt'].mean()
std = df['cnt'].std(ddof=0)
if std == 0:
    pick = df.loc[df['cnt'].idxmax(), 'month']
else:
    df['z'] = (df['cnt']-mean)/std
    sig = df[df['z']>1.5]
    if len(sig)>0:
        pick = sig.sort_values(['z','cnt'], ascending=False).iloc[0]['month']
    else:
        pick = df.loc[df['cnt'].idxmax(), 'month']
print('__RESULT__:')
print(json.dumps(pick))"""

env_args = {'var_call_6FgyddAAGHXicbVMqfsvqSdM': [], 'var_call_um4R0DlZNitXcSZibnoSz2F2': [], 'var_call_yutKFmM8KZ0lgje7vNBkEter': [{'orderitemid__c': '802Wt00000792zUIAQ', 'cnt': '4'}, {'orderitemid__c': '802Wt0000078ypPIAQ', 'cnt': '3'}, {'orderitemid__c': '802Wt0000078xAFIAY', 'cnt': '3'}, {'orderitemid__c': '802Wt00000798aDIAQ', 'cnt': '3'}, {'orderitemid__c': '802Wt00000797CjIAI', 'cnt': '3'}, {'orderitemid__c': '802Wt00000796qFIAQ', 'cnt': '3'}, {'orderitemid__c': '802Wt00000799EZIAY', 'cnt': '3'}, {'orderitemid__c': '802Wt00000797r5IAA', 'cnt': '3'}, {'orderitemid__c': '802Wt0000079A2ZIAU', 'cnt': '3'}, {'orderitemid__c': '802Wt00000798S9IAI', 'cnt': '3'}, {'orderitemid__c': '802Wt000007928FIAQ', 'cnt': '3'}, {'orderitemid__c': '802Wt00000792tiIAA', 'cnt': '3'}, {'orderitemid__c': '802Wt00000798olIAA', 'cnt': '3'}, {'orderitemid__c': '802Wt00000796jiIAA', 'cnt': '2'}, {'orderitemid__c': '802Wt00000798iIIAQ', 'cnt': '2'}, {'orderitemid__c': '802Wt00000798NMIAY', 'cnt': '2'}, {'orderitemid__c': '802Wt00000797foIAA', 'cnt': '2'}, {'orderitemid__c': '802Wt00000797pRIAQ', 'cnt': '2'}, {'orderitemid__c': '802Wt00000798dRIAQ', 'cnt': '2'}, {'orderitemid__c': '802Wt00000799UfIAI', 'cnt': '2'}], 'var_call_9rJVd9IPAO88jnIgpydg6kVd': [], 'var_call_jYObvCDU7bMjV12yZzVm5IeY': [{'cnt': '126'}], 'var_call_rVfl3lDNW1SJG067LveStELF': [{'month_start': '2020-06-01 00:00:00', 'opp_lineitems': '2'}, {'month_start': '2020-07-01 00:00:00', 'opp_lineitems': '4'}, {'month_start': '2020-08-01 00:00:00', 'opp_lineitems': '1'}, {'month_start': '2020-09-01 00:00:00', 'opp_lineitems': '1'}, {'month_start': '2020-10-01 00:00:00', 'opp_lineitems': '3'}, {'month_start': '2020-11-01 00:00:00', 'opp_lineitems': '2'}, {'month_start': '2020-12-01 00:00:00', 'opp_lineitems': '1'}, {'month_start': '2021-01-01 00:00:00', 'opp_lineitems': '4'}, {'month_start': '2021-02-01 00:00:00', 'opp_lineitems': '1'}, {'month_start': '2021-03-01 00:00:00', 'opp_lineitems': '1'}]}

exec(code, env_args)
