code = """import json, pandas as pd

cases = pd.DataFrame(var_call_XpPw4sKwo7C21mLArbfjnlOv)

# load accounts full from file path
path = var_call_ILcjjdVpeBGs9NCvybjxFcd4
with open(path, 'r') as f:
    accounts = pd.DataFrame(json.load(f))

# clean ids
cases['account_clean'] = cases['accountid'].astype(str).str.replace('#','', regex=False).str.strip()
accounts['account_clean'] = accounts['account_id'].astype(str).str.replace('#','', regex=False).str.strip()

# clean state
accounts['state'] = accounts['shipping_state'].astype(str).str.strip()

# join
m = cases.merge(accounts[['account_clean','state']], on='account_clean', how='left')

# coerce closure_days
m['closure_days'] = pd.to_numeric(m['closure_days'], errors='coerce')

# keep valid 2-letter states
m = m[m['state'].notna()]
m['state'] = m['state'].astype(str).str.strip()
m = m[m['state'].str.fullmatch(r'[A-Z]{2}')]

# compute average closure days per state
agg = (m.groupby('state', as_index=False)
         .agg(avg_closure_days=('closure_days','mean'), n_cases=('case_id','count'))
      )

# pick min avg, tie-breaker: higher n_cases then alpha
agg = agg.sort_values(['avg_closure_days','n_cases','state'], ascending=[True, False, True])
best_state = agg.iloc[0]['state'] if len(agg) else None

print('__RESULT__:')
print(json.dumps({'best_state': best_state}))"""

env_args = {'var_call_ILcjjdVpeBGs9NCvybjxFcd4': 'file_storage/call_ILcjjdVpeBGs9NCvybjxFcd4.json', 'var_call_xgsUH6X5N7vur80o3qtM4liW': [{'accountid': '#001Wt00000PHVvRIAX'}, {'accountid': '#001Wt00000PGXrLIAX'}, {'accountid': '#001Wt00000PGaZDIA1'}, {'accountid': '#001Wt00000PFsjOIAT'}, {'accountid': '001Wt00000PH9ITIA1'}], 'var_call_uuav2ynzN3jxX9GNe6qf5MZa': [{'ShippingState': 'FL'}, {'ShippingState': 'TX'}, {'ShippingState': 'AZ'}, {'ShippingState': 'CA'}, {'ShippingState': 'MO'}, {'ShippingState': 'OH'}, {'ShippingState': 'NY'}, {'ShippingState': 'CO'}, {'ShippingState': 'MI'}, {'ShippingState': 'NV'}, {'ShippingState': 'MN'}, {'ShippingState': 'MA'}, {'ShippingState': 'WA'}, {'ShippingState': 'IA'}, {'ShippingState': 'OR'}, {'ShippingState': 'UT'}, {'ShippingState': 'GA'}, {'ShippingState': 'VA'}, {'ShippingState': 'IL'}, {'ShippingState': 'NJ'}], 'var_call_XpPw4sKwo7C21mLArbfjnlOv': [{'case_id': '500Wt00000DDPIsIAP', 'accountid': '#001Wt00000PGRnYIAX', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'closure_days': '0.00662037037037037'}, {'case_id': '#500Wt00000DDTERIA5', 'accountid': '001Wt00000PGzSaIAL', 'createddate': '2022-03-10T09:30:00.000+0000', 'closeddate': '2022-03-13T09:45:27.000+0000', 'closure_days': '3.0107291666666667'}, {'case_id': '#500Wt00000DDYdwIAH', 'accountid': '001Wt00000PFj4zIAD', 'createddate': '2022-02-03T14:30:00.000+0000', 'closeddate': '2022-02-03T14:46:56.000+0000', 'closure_days': '0.01175925925925926'}, {'case_id': '#500Wt00000DDYpHIAX', 'accountid': '#001Wt00000PHHXXIA5', 'createddate': '2022-09-05T11:15:00.000+0000', 'closeddate': '2022-09-05T11:42:09.000+0000', 'closure_days': '0.01885416666666667'}, {'case_id': '#500Wt00000DDet1IAD', 'accountid': '001Wt00000PGzSbIAL', 'createddate': '2021-09-07T23:48:00.000+0000', 'closeddate': '2021-09-08T03:11:32.000+0000', 'closure_days': '0.1413425925925926'}, {'case_id': '500Wt00000DDg1yIAD', 'accountid': '#001Wt00000PHVnNIAX', 'createddate': '2022-02-08T06:22:00.000+0000', 'closeddate': '2022-02-08T06:43:35.000+0000', 'closure_days': '0.014988425925925926'}, {'case_id': '500Wt00000DDg1zIAD', 'accountid': '001Wt00000PGdzxIAD', 'createddate': '2022-04-17T14:20:00.000+0000', 'closeddate': '2022-04-17T14:37:58.000+0000', 'closure_days': '0.012476851851851852'}, {'case_id': '500Wt00000DDg8RIAT', 'accountid': '001Wt00000PGZZoIAP', 'createddate': '2022-05-10T11:30:00.000+0000', 'closeddate': '2022-05-10T17:02:48.000+0000', 'closure_days': '0.2311111111111111'}, {'case_id': '500Wt00000DDgLLIA1', 'accountid': '#001Wt00000PGZZoIAP', 'createddate': '2022-05-12T14:45:00.000+0000', 'closeddate': '2022-05-12T14:54:10.000+0000', 'closure_days': '0.00636574074074074'}, {'case_id': '500Wt00000DDsKuIAL', 'accountid': '#001Wt00000PHVvRIAX', 'createddate': '2022-07-23T07:37:00.000+0000', 'closeddate': '2022-07-23T07:47:37.000+0000', 'closure_days': '0.007372685185185185'}, {'case_id': '500Wt00000DDxVqIAL', 'accountid': '001Wt00000PHVvRIAX', 'createddate': '2021-09-15T09:10:00.000+0000', 'closeddate': '2021-09-15T09:50:35.000+0000', 'closure_days': '0.028182870370370372'}, {'case_id': '500Wt00000DDxZ4IAL', 'accountid': '001Wt00000PGtmwIAD', 'createddate': '2021-06-19T21:19:00.000+0000', 'closeddate': '2021-06-19T21:32:46.000+0000', 'closure_days': '0.009560185185185185'}, {'case_id': '500Wt00000DDzSnIAL', 'accountid': '001Wt00000PGaZCIA1', 'createddate': '2021-10-15T11:15:00.000+0000', 'closeddate': '2021-10-15T20:15:55.000+0000', 'closure_days': '0.3756365740740741'}, {'case_id': '#500Wt00000DDzSoIAL', 'accountid': '001Wt00000PHR8gIAH', 'createddate': '2022-07-26T12:38:00.000+0000', 'closeddate': '2022-07-26T13:40:22.000+0000', 'closure_days': '0.04331018518518519'}, {'case_id': '#500Wt00000DDzZFIA1', 'accountid': '001Wt00000PGoAaIAL', 'createddate': '2021-07-15T10:30:00.000+0000', 'closeddate': '2021-07-15T13:32:47.000+0000', 'closure_days': '0.12693287037037038'}, {'case_id': '500Wt00000DDzarIAD', 'accountid': '#001Wt00000PGoAaIAL', 'createddate': '2021-10-08T08:07:00.000+0000', 'closeddate': '2021-10-08T08:43:11.000+0000', 'closure_days': '0.025127314814814814'}, {'case_id': '500Wt00000DDzcTIAT', 'accountid': '001Wt00000PGRnYIAX', 'createddate': '2022-08-01T10:15:00.000+0000', 'closeddate': '2022-08-01T14:45:37.000+0000', 'closure_days': '0.18792824074074074'}, {'case_id': '500Wt00000DDzfhIAD', 'accountid': '001Wt00000PGzM9IAL', 'createddate': '2022-03-04T09:45:00.000+0000', 'closeddate': '2022-03-05T10:25:32.000+0000', 'closure_days': '1.0281481481481483'}, {'case_id': '#500Wt00000DDzuDIAT', 'accountid': '#001Wt00000PGtmwIAD', 'createddate': '2021-06-17T18:18:00.000+0000', 'closeddate': '2021-06-17T21:37:59.000+0000', 'closure_days': '0.13887731481481483'}, {'case_id': '#500Wt00000DE077IAD', 'accountid': '001Wt00000PGZmfIAH', 'createddate': '2021-07-22T09:45:00.000+0000', 'closeddate': '2021-07-22T10:00:58.000+0000', 'closure_days': '0.011087962962962963'}, {'case_id': '500Wt00000DE08jIAD', 'accountid': '001Wt00000PGSwYIAX', 'createddate': '2021-09-16T11:00:00.000+0000', 'closeddate': '2021-09-16T11:14:27.000+0000', 'closure_days': '0.010034722222222223'}, {'case_id': '#500Wt00000DE0FCIA1', 'accountid': '001Wt00000PHVvRIAX', 'createddate': '2021-09-05T11:15:00.000+0000', 'closeddate': '2021-09-05T11:25:45.000+0000', 'closure_days': '0.007465277777777778'}, {'case_id': '500Wt00000DE0IPIA1', 'accountid': '001Wt00000PHVtpIAH', 'createddate': '2022-08-10T09:30:00.000+0000', 'closeddate': '2022-08-10T13:59:01.000+0000', 'closure_days': '0.18681712962962962'}, {'case_id': '500Wt00000DE0QTIA1', 'accountid': '001Wt00000PFt7TIAT', 'createddate': '2022-02-02T15:30:45.000+0000', 'closeddate': '2022-02-03T10:17:46.000+0000', 'closure_days': '0.7826504629629629'}, {'case_id': '500Wt00000DE0S5IAL', 'accountid': '001Wt00000PFt7TIAT', 'createddate': '2022-03-05T11:20:30.000+0000', 'closeddate': '2022-03-05T11:34:08.000+0000', 'closure_days': '0.009467592592592593'}, {'case_id': '#500Wt00000DE0ThIAL', 'accountid': '#001Wt00000PGXrLIAX', 'createddate': '2021-10-02T10:30:00.000+0000', 'closeddate': '2021-10-03T13:27:49.000+0000', 'closure_days': '1.1234837962962962'}, {'case_id': '500Wt00000DE0YXIA1', 'accountid': '#001Wt00000PGaZDIA1', 'createddate': '2022-02-24T19:20:00.000+0000', 'closeddate': '2022-02-25T04:35:46.000+0000', 'closure_days': '0.3859490740740741'}]}

exec(code, env_args)
