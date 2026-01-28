code = """import pandas as pd
import json
from datetime import datetime

# load data from previous query
records = var_call_e9QEeWpgoHEGPsunabqeKgP5

df = pd.DataFrame(records)
if df.empty:
    result = None
else:
    # parse datetimes
    df['createddate'] = pd.to_datetime(df['createddate'], utc=True)
    # define the 10-month window
    start = pd.to_datetime('2020-06-10T00:00:00+0000')
    end = pd.to_datetime('2021-04-10T00:00:00+0000')
    # ensure filtering
    df = df[(df['createddate'] >= start) & (df['createddate'] < end)]
    # build month buckets from June 2020 through March 2021 (10 months)
    month_starts = pd.date_range(start=pd.to_datetime('2020-06-01T00:00:00+0000'), periods=10, freq='MS', tz='UTC')
    month_labels = [d.strftime('%B') for d in month_starts]
    counts = []
    for d in month_starts:
        next_d = (d + pd.offsets.MonthBegin(1))
        cnt = int(((df['createddate'] >= d) & (df['createddate'] < next_d)).sum())
        counts.append(cnt)
    s = pd.Series(counts, index=month_labels)
    mean = float(s.mean())
    std = float(s.std(ddof=0))
    threshold = mean + 2 * std
    # find months exceeding threshold
    significant = s[s > threshold]
    if len(significant) == 0:
        result = None
    else:
        # choose the month with highest count (if tie, first)
        result = significant.idxmax()

# print result as JSON-serializable string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_AX6zRp3w4sxFJHhOKjUing1s': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}], 'var_call_e9QEeWpgoHEGPsunabqeKgP5': [{'id': '#500Wt00000DDxnbIAD', 'subject': 'roi metrics clarification', 'description': 'i am experiencing difficulty aligning the performance metrics provided by secureanalytics pro with our expected roi, and need assistance to reconcile these discrepancies.', 'createddate': '2021-01-25T09:30:00.000+0000'}, {'id': '500Wt00000DDy8bIAD', 'subject': 'update alerts absent', 'description': "the system does not alert me to the new features added to secureanalytics pro, leading to underutilization of its updates as i'm unaware of them.", 'createddate': '2020-11-05T08:19:00.000+0000'}, {'id': '500Wt00000DE00gIAD', 'subject': 'secureanalytics compliance concern', 'description': "i need clarification on secureanalytics pro's adherence to security compliance standards.", 'createddate': '2020-09-29T01:59:00.000+0000'}, {'id': '500Wt00000DE0AMIA1', 'subject': 'no feature update notices', 'description': 'i am consistently not getting notified about feature updates for secureanalytics pro, which means i am unable to take advantage of improvements and enhancements.', 'createddate': '2021-03-07T11:25:00.000+0000'}, {'id': '500Wt00000DE0NFIA1', 'subject': 'missing feature notifications', 'description': 'i have not been receiving notifications about new features in secureanalytics pro, causing me to miss out on utilizing the full capabilities of the platform.', 'createddate': '2020-11-09T19:02:00.000+0000'}], 'var_call_AnkeLQYbrl7N9lHX4p3IgFsy': [{'Id': '#802Wt0000078yuGIAQ', 'OrderId': '801Wt00000PGdVHIA1', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '8.0', 'UnitPrice': '617.4905'}, {'Id': '802Wt00000790mOIAQ', 'OrderId': '#801Wt00000PHQuGIAX', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '30.0', 'UnitPrice': '552.4915'}, {'Id': '802Wt00000790zGIAQ', 'OrderId': '#801Wt00000PGc9QIAT', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '6.0', 'UnitPrice': '617.4905'}, {'Id': '802Wt00000794F2IAI', 'OrderId': '801Wt00000PHLzOIAX', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '2.0', 'UnitPrice': '649.99'}, {'Id': '802Wt000007968eIAA', 'OrderId': '801Wt00000PH4FLIA1', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '2.0', 'UnitPrice': '649.99'}, {'Id': '802Wt00000796bfIAA', 'OrderId': '801Wt00000PGRh3IAH', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '3.0', 'UnitPrice': '649.99'}, {'Id': '802Wt00000796qFIAQ', 'OrderId': '801Wt00000PHRdKIAX', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '7.0', 'UnitPrice': '617.4905'}, {'Id': '802Wt0000079734IAA', 'OrderId': '#801Wt00000PGu6KIAT', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '1.0', 'UnitPrice': '649.99'}, {'Id': '802Wt00000797W5IAI', 'OrderId': '801Wt00000PHWZlIAP', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '20.0', 'UnitPrice': '552.4915'}, {'Id': '802Wt00000797awIAA', 'OrderId': '801Wt00000PGdVGIA1', 'Product2Id': '#01tWt000006hVJdIAM', 'Quantity': '10.0', 'UnitPrice': '584.991'}, {'Id': '802Wt00000797z7IAA', 'OrderId': '801Wt00000PGos9IAD', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '1.0', 'UnitPrice': '649.99'}, {'Id': '#802Wt00000798VPIAY', 'OrderId': '#801Wt00000PGdjoIAD', 'Product2Id': '#01tWt000006hVJdIAM', 'Quantity': '10.0', 'UnitPrice': '584.991'}, {'Id': '802Wt00000798YdIAI', 'OrderId': '801Wt00000PH8yvIAD', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '30.0', 'UnitPrice': '552.4915'}, {'Id': '802Wt00000798okIAA', 'OrderId': '#801Wt00000PGVJJIA5', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '1.0', 'UnitPrice': '649.99'}, {'Id': '#802Wt00000799o1IAA', 'OrderId': '#801Wt00000PGoc0IAD', 'Product2Id': '#01tWt000006hVJdIAM', 'Quantity': '19.0', 'UnitPrice': '584.991'}, {'Id': '802Wt0000079A2bIAE', 'OrderId': '801Wt00000PGe00IAD', 'Product2Id': '#01tWt000006hVJdIAM', 'Quantity': '12.0', 'UnitPrice': '584.991'}, {'Id': '802Wt0000079ACGIA2', 'OrderId': '#801Wt00000PGSYIIA5', 'Product2Id': '#01tWt000006hVJdIAM', 'Quantity': '20.0', 'UnitPrice': '552.4915'}, {'Id': '802Wt0000079B0EIAU', 'OrderId': '801Wt00000PHHMIIA5', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '6.0', 'UnitPrice': '617.4905'}, {'Id': '802Wt0000079B6gIAE', 'OrderId': '#801Wt00000PHQz1IAH', 'Product2Id': '#01tWt000006hVJdIAM', 'Quantity': '4.0', 'UnitPrice': '649.99'}], 'var_call_u4qVUoelDuK7Gudv5jeUO4AN': [{'id': '#500Wt00000DDxnbIAD', 'subject': 'roi metrics clarification', 'description': 'i am experiencing difficulty aligning the performance metrics provided by secureanalytics pro with our expected roi, and need assistance to reconcile these discrepancies.', 'createddate': '2021-01-25T09:30:00.000+0000', 'orderitemid__c': '802Wt00000799o1IAA'}, {'id': '500Wt00000DDy8bIAD', 'subject': 'update alerts absent', 'description': "the system does not alert me to the new features added to secureanalytics pro, leading to underutilization of its updates as i'm unaware of them.", 'createddate': '2020-11-05T08:19:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE00gIAD', 'subject': 'secureanalytics compliance concern', 'description': "i need clarification on secureanalytics pro's adherence to security compliance standards.", 'createddate': '2020-09-29T01:59:00.000+0000', 'orderitemid__c': '802Wt00000796bfIAA'}, {'id': '500Wt00000DE0AMIA1', 'subject': 'no feature update notices', 'description': 'i am consistently not getting notified about feature updates for secureanalytics pro, which means i am unable to take advantage of improvements and enhancements.', 'createddate': '2021-03-07T11:25:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0NFIA1', 'subject': 'missing feature notifications', 'description': 'i have not been receiving notifications about new features in secureanalytics pro, causing me to miss out on utilizing the full capabilities of the platform.', 'createddate': '2020-11-09T19:02:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}]}

exec(code, env_args)
