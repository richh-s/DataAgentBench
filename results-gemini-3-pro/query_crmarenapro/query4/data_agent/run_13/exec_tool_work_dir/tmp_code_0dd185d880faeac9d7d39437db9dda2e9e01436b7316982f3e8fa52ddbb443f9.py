code = """import json
from datetime import datetime

accounts_list = locals()['var_function-call-10993183544063601097']
cases_file = locals()['var_function-call-12245447546558012541']

with open(cases_file, 'r') as f:
    cases = json.load(f)

def clean_id(val):
    if not val:
        return ""
    s = str(val).strip()
    if s.startswith("#"):
        s = s[1:]
    return s

target_account_ids = set()
for a in accounts_list:
    aid = clean_id(a.get("AccountId"))
    if aid:
        target_account_ids.add(aid)

print(f"Target Accounts: {len(target_account_ids)}")

start_date = datetime(2020, 6, 10)
end_date = datetime(2021, 4, 10, 23, 59, 59)

monthly_counts = {}
subject_match_monthly_counts = {}

for c in cases:
    # Check Account
    c_aid = clean_id(c.get("accountid"))
    if c_aid not in target_account_ids:
        continue
        
    c_date_str = c.get("createddate")
    if not c_date_str:
        continue
    
    try:
        dt = datetime.strptime(c_date_str[:19], "%Y-%m-%dT%H:%M:%S")
        if start_date <= dt <= end_date:
            m_key = dt.strftime("%Y-%m")
            monthly_counts[m_key] = monthly_counts.get(m_key, 0) + 1
            
            subj = (c.get("subject") or "").lower()
            if "secureanalytics" in subj:
                subject_match_monthly_counts[m_key] = subject_match_monthly_counts.get(m_key, 0) + 1
    except:
        pass

print("__RESULT__:")
print(json.dumps({"all_cases_by_account": monthly_counts, "secureanalytics_subject_cases": subject_match_monthly_counts}))"""

env_args = {'var_function-call-10888803579691069025': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-10888803579691066634': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-2174225455058142858': 'file_storage/function-call-2174225455058142858.json', 'var_function-call-9786930371562019834': {'2021-01': 1, '2020-11': 2, '2020-09': 1, '2021-03': 1}, 'var_function-call-10845506614740905067': {'target_order_item_count': 19, 'total_case_matches': 6, 'matches_per_month': {'2021-01': 1, '2020-11': 2, '2023-06': 1, '2020-09': 1, '2021-03': 1}}, 'var_function-call-11203846788282099093': [], 'var_function-call-11203846788282101496': [{'id': 'a03Wt00000JqhItIAJ', 'name': 'Software Installation Error', 'description__c': 'Users report encountering errors during the initial installation process, which hinders the setup of TechPulse solutions.'}, {'id': '#a03Wt00000JqmLvIAJ', 'name': 'Billing Discrepancy', 'description__c': 'Some clients encounter unexpected charges on their billing statements, leading to confusion and dissatisfaction.'}, {'id': 'a03Wt00000JqmX6IAJ', 'name': 'Customizability Limitation   ', 'description__c': 'Despite customization options, some users find it challenging to tailor solutions to fit extremely niche industry needs.'}, {'id': 'a03Wt00000JqnHwIAJ', 'name': 'User Interface Bug', 'description__c': "A segment of users face occasional glitches in the software's user interface, affecting their overall usability experience."}, {'id': '#a03Wt00000JqtOtIAJ', 'name': 'Support Response Delay', 'description__c': 'Some users face delays in getting timely responses from the TechPulse support team during peak times.'}], 'var_function-call-11203846788282099803': [{'count': '5'}], 'var_function-call-3812414058627869613': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}], 'var_function-call-13430628881636285503': [{'id': '#500Wt00000DDxnbIAD', 'orderitemid__c': '802Wt00000799o1IAA', 'subject': 'ROI Metrics Clarification  ', 'description': 'I am experiencing difficulty aligning the performance metrics provided by SecureAnalytics Pro with our expected ROI, and need assistance to reconcile these discrepancies.', 'createddate': '2021-01-25T09:30:00.000+0000'}, {'id': '500Wt00000DDy8bIAD', 'orderitemid__c': '802Wt00000796qFIAQ', 'subject': 'Update Alerts Absent', 'description': "The system does not alert me to the new features added to SecureAnalytics Pro, leading to underutilization of its updates as I'm unaware of them.", 'createddate': '2020-11-05T08:19:00.000+0000'}, {'id': '500Wt00000DE00gIAD', 'orderitemid__c': '802Wt00000796bfIAA', 'subject': 'SecureAnalytics Compliance Concern', 'description': "I need clarification on SecureAnalytics Pro's adherence to security compliance standards.", 'createddate': '2020-09-29T01:59:00.000+0000'}, {'id': '500Wt00000DE0AMIA1', 'orderitemid__c': '802Wt00000796qFIAQ', 'subject': 'No Feature Update Notices', 'description': 'I am consistently not getting notified about feature updates for SecureAnalytics Pro, which means I am unable to take advantage of improvements and enhancements.', 'createddate': '2021-03-07T11:25:00.000+0000'}, {'id': '500Wt00000DE0NFIA1', 'orderitemid__c': '802Wt00000796qFIAQ', 'subject': 'Missing Feature Notifications', 'description': 'I have not been receiving notifications about new features in SecureAnalytics Pro, causing me to miss out on utilizing the full capabilities of the platform.', 'createddate': '2020-11-09T19:02:00.000+0000'}], 'var_function-call-10993183544063601097': [{'AccountId': '#001Wt00000PGHsyIAH'}, {'AccountId': '001Wt00000PGSwYIAX'}, {'AccountId': '001Wt00000PHVkAIAX'}, {'AccountId': '001Wt00000PHVllIAH'}, {'AccountId': '001Wt00000PFsjOIAT'}, {'AccountId': '001Wt00000PHVtpIAH'}, {'AccountId': '001Wt00000PGtdJIAT'}, {'AccountId': '#001Wt00000PHR8gIAH'}, {'AccountId': '001Wt00000PGovMIAT'}, {'AccountId': '001Wt00000PGR63IAH'}, {'AccountId': '#001Wt00000PGGTuIAP'}, {'AccountId': '001Wt00000PGSwZIAX'}, {'AccountId': '001Wt00000PHW0HIAX'}], 'var_function-call-12245447546558012541': 'file_storage/function-call-12245447546558012541.json'}

exec(code, env_args)
