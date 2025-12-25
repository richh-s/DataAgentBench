code = """import json
from datetime import datetime

with open(locals()['var_function-call-8702892083309368303'], 'r') as f:
    cases = json.load(f)

text_matches_counts = {}
text_matches = []

for case in cases:
    # Check text
    subj = case.get('subject', '') or ''
    desc = case.get('description', '') or ''
    combined = (subj + " " + desc).lower()
    
    if "secureanalytics pro" in combined:
        c_date_str = case.get('createddate')
        try:
            c_date = datetime.strptime(c_date_str, "%Y-%m-%dT%H:%M:%S.%f%z")
            month_key = c_date.strftime("%B")
            text_matches_counts[month_key] = text_matches_counts.get(month_key, 0) + 1
            text_matches.append(case)
        except ValueError:
             try:
                c_date = datetime.strptime(c_date_str, "%Y-%m-%dT%H:%M:%S%z")
                month_key = c_date.strftime("%B")
                text_matches_counts[month_key] = text_matches_counts.get(month_key, 0) + 1
                text_matches.append(case)
             except:
                pass

print("__RESULT__:")
print(json.dumps({
    "text_matches_counts": text_matches_counts,
    "total_text_matches": len(text_matches)
}))"""

env_args = {'var_function-call-16064184842318411823': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-8702892083309368303': 'file_storage/function-call-8702892083309368303.json', 'var_function-call-7519533941935195638': {'January 2021': 1, 'November 2020': 2, 'September 2020': 1, 'March 2021': 1}, 'var_function-call-2303119916940098335': {'num_order_items': 19, 'total_matches': 6, 'all_month_counts': {'January 2021': 1, 'November 2020': 2, 'June 2023': 1, 'September 2020': 1, 'March 2021': 1}}, 'var_function-call-3892015857153050438': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}], 'var_function-call-14753483501253137550': [], 'var_function-call-6369002579201554899': [{'id': '500Wt00000DE00gIAD', 'priority': 'High', 'subject': 'SecureAnalytics Compliance Concern', 'description': "I need clarification on SecureAnalytics Pro's adherence to security compliance standards.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqscWIAR', 'createddate': '2020-09-29T01:59:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000796bfIAA', 'issueid__c': 'a03Wt00000JqzPSIAZ', 'accountid': '#001Wt00000PFsjOIAT', 'ownerid': '005Wt000003NJWTIA4'}], 'var_function-call-4190302696212677617': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-2251203383370484797': {'total_cases': 153, 'num_populated_oid': 153, 'sample_oids': ['802Wt00000797r4IAA', '802Wt00000798aDIAQ', '802Wt00000792tiIAA', '802Wt00000797r3IAA', '802Wt00000797r5IAA', '802Wt00000792tiIAA', '802Wt0000078xAFIAY', '802Wt0000079ATyIAM', '802Wt00000794bXIAQ', '802Wt00000796yFIAQ'], 'num_matches': 6, 'unique_matches': ['802Wt00000798YdIAI', '802Wt00000796bfIAA', '802Wt00000796qFIAQ', '802Wt00000799o1IAA'], 'valid_ids_sample': ['802Wt0000078yuGIAQ', '802Wt00000790mOIAQ', '802Wt00000790zGIAQ', '802Wt00000794F2IAI', '802Wt000007968eIAA']}, 'var_function-call-2757038605895839176': [], 'var_function-call-6439198860382598056': [{'id': '#500Wt00000DDxnbIAD', 'priority': 'Medium', 'subject': 'ROI Metrics Clarification  ', 'description': 'I am experiencing difficulty aligning the performance metrics provided by SecureAnalytics Pro with our expected ROI, and need assistance to reconcile these discrepancies.', 'status': 'Closed', 'contactid': '003Wt00000Jqy8QIAR', 'createddate': '2021-01-25T09:30:00.000+0000', 'closeddate': '2021-01-25T15:27:34.000+0000', 'orderitemid__c': '802Wt00000799o1IAA', 'issueid__c': 'a03Wt00000JqzUHIAZ', 'accountid': '001Wt00000PGGTuIAP', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '500Wt00000DDy8bIAD', 'priority': 'Low', 'subject': 'Update Alerts Absent', 'description': "The system does not alert me to the new features added to SecureAnalytics Pro, leading to underutilization of its updates as I'm unaware of them.", 'status': 'Closed', 'contactid': '#003Wt00000Jqp0NIAR', 'createddate': '2020-11-05T08:19:00.000+0000', 'closeddate': '2020-11-05T08:50:10.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVtpIAH', 'ownerid': '005Wt000003NI5mIAG'}, {'id': '500Wt00000DE00gIAD', 'priority': 'High', 'subject': 'SecureAnalytics Compliance Concern', 'description': "I need clarification on SecureAnalytics Pro's adherence to security compliance standards.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqscWIAR', 'createddate': '2020-09-29T01:59:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000796bfIAA', 'issueid__c': 'a03Wt00000JqzPSIAZ', 'accountid': '#001Wt00000PFsjOIAT', 'ownerid': '005Wt000003NJWTIA4'}, {'id': '500Wt00000DE0AMIA1', 'priority': 'High', 'subject': 'No Feature Update Notices', 'description': 'I am consistently not getting notified about feature updates for SecureAnalytics Pro, which means I am unable to take advantage of improvements and enhancements.', 'status': 'Closed', 'contactid': '003Wt00000Jqp0NIAR', 'createddate': '2021-03-07T11:25:00.000+0000', 'closeddate': '2021-03-07T17:46:52.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVtpIAH', 'ownerid': '005Wt000003NJeXIAW'}, {'id': '500Wt00000DE0NFIA1', 'priority': 'Medium', 'subject': 'Missing Feature Notifications', 'description': 'I have not been receiving notifications about new features in SecureAnalytics Pro, causing me to miss out on utilizing the full capabilities of the platform.', 'status': 'Closed', 'contactid': '#003Wt00000Jqp0NIAR', 'createddate': '2020-11-09T19:02:00.000+0000', 'closeddate': '2020-11-10T09:47:54.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVtpIAH', 'ownerid': '005Wt000003NDu7IAG'}]}

exec(code, env_args)
