code = """import json
import pandas as pd

order_items = pd.DataFrame(var_call_MFRTK0Qr1o2gwN60euMBbEly)
order_items['Id_clean'] = order_items['Id'].str.lstrip('#')

cases = pd.DataFrame(var_call_hU83QmAvaVkX0kE2xW5hPan4)
cases['orderitemid__c_clean'] = cases['orderitemid__c'].str.lstrip('#')

merged = cases.merge(order_items, left_on='orderitemid__c_clean', right_on='Id_clean', how='inner')

merged['createddate'] = pd.to_datetime(merged['createddate'])
merged = merged[(merged['createddate'] >= '2020-06-10') & (merged['createddate'] < '2021-04-10')]

merged['month'] = merged['createddate'].dt.to_period('M').dt.to_timestamp()

monthly_counts = merged.groupby('month').size().reset_index(name='case_count').sort_values('month')

if monthly_counts.empty:
    result = None
else:
    max_count = monthly_counts['case_count'].max()
    second_max = monthly_counts[monthly_counts['case_count'] < max_count]['case_count'].max() if (monthly_counts['case_count'] < max_count).any() else 0
    # Define "significantly exceeds" as at least 50% more than the next highest month
    if max_count >= 1.5 * second_max and (monthly_counts['case_count'] == max_count).sum() == 1:
        peak_month = monthly_counts.loc[monthly_counts['case_count'] == max_count, 'month'].iloc[0]
        month_name = peak_month.strftime('%B')
        result = month_name
    else:
        result = None

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_kTA6VMKZrMczpF9tZemSjuXj': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_36czCjTHdozJWkYHcge8UUVB': [{'createddate': '2023-07-02T11:00:00.000+0000', 'orderitemid__c': '802Wt00000797r4IAA'}, {'createddate': '2020-12-29T08:36:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'createddate': '2023-09-30T11:30:00.000+0000', 'orderitemid__c': '802Wt00000792tiIAA'}, {'createddate': '2022-08-05T14:30:00.000+0000', 'orderitemid__c': '802Wt00000797r3IAA'}, {'createddate': '2020-09-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}], 'var_call_MFRTK0Qr1o2gwN60euMBbEly': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}], 'var_call_hU83QmAvaVkX0kE2xW5hPan4': [{'createddate': '2020-12-29T08:36:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'createddate': '2020-09-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'createddate': '2021-01-10T09:30:00.000+0000', 'orderitemid__c': '802Wt00000797axIAA'}, {'createddate': '2020-09-05T09:15:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'createddate': '2021-03-31T11:41:00.000+0000', 'orderitemid__c': '802Wt00000798OvIAI'}, {'createddate': '2020-07-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000795XwIAI'}, {'createddate': '2020-07-01T15:30:00.000+0000', 'orderitemid__c': '802Wt00000794bTIAQ'}, {'createddate': '2021-03-24T18:04:00.000+0000', 'orderitemid__c': '802Wt00000796dGIAQ'}, {'createddate': '2021-03-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'createddate': '2020-11-05T11:00:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'createddate': '2021-02-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}, {'createddate': '2021-01-25T09:30:00.000+0000', 'orderitemid__c': '802Wt00000799o1IAA'}, {'createddate': '2020-11-05T08:19:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'createddate': '2020-10-01T14:30:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'createddate': '2020-09-03T14:45:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'createddate': '2020-10-22T03:55:00.000+0000', 'orderitemid__c': '802Wt00000796JtIAI'}, {'createddate': '2021-02-20T14:30:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'createddate': '2020-09-29T01:59:00.000+0000', 'orderitemid__c': '802Wt00000796bfIAA'}, {'createddate': '2021-01-03T15:30:00.000+0000', 'orderitemid__c': '802Wt00000799b7IAA'}, {'createddate': '2021-03-07T11:25:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'createddate': '2020-11-10T22:14:00.000+0000', 'orderitemid__c': '802Wt00000799uTIAQ'}, {'createddate': '2020-11-09T19:02:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'createddate': '2021-03-10T15:45:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}]}

exec(code, env_args)
