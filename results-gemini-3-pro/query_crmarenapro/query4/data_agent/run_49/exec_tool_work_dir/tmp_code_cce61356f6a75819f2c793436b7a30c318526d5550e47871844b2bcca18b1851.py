code = """import json
from datetime import datetime

# Load OrderItems
with open(locals()['var_function-call-15276008645661363926'], 'r') as f:
    order_items_list = json.load(f)

oi_to_prod = {}
for item in order_items_list:
    oid = item['Id']
    pid = item['Product2Id']
    if oid.startswith('#'): oid = oid[1:]
    if pid.startswith('#'): pid = pid[1:]
    oi_to_prod[oid] = pid

# Load Cases
with open(locals()['var_function-call-708752942025156642'], 'r') as f:
    cases = json.load(f)

product_counts = {}
cutoff_date = datetime(2020, 6, 1)
today = datetime(2021, 4, 10)

for case in cases:
    oid = case.get('orderitemid__c')
    if not oid: continue
    if oid.startswith('#'): oid = oid[1:]
    
    if oid in oi_to_prod:
        pid = oi_to_prod[oid]
        cdate_str = case.get('createddate')
        if cdate_str:
            try:
                cdate = datetime.strptime(cdate_str[:10], "%Y-%m-%d")
                if cdate >= cutoff_date and cdate <= today:
                    if pid not in product_counts:
                        product_counts[pid] = 0
                    product_counts[pid] += 1
            except:
                pass

print("__RESULT__:")
print(json.dumps(product_counts))"""

env_args = {'var_function-call-10023800480704351753': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-13331700831189368373': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-708752942025156642': 'file_storage/function-call-708752942025156642.json', 'var_function-call-9034528603292838690': {'2021-01': 1, '2020-11': 2, '2020-09': 1, '2021-03': 1}, 'var_function-call-6207247607094848795': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro', 'Description': 'Data analytics platform with enhanced focus on security and compliance.', 'IsActive': '1', 'External_ID__c': 'Data Analytics Platforms,Security and Compliance Modules_13'}], 'var_function-call-11919922663904100365': [{'createddate': '2021-01-25T09:30:00.000+0000'}, {'createddate': '2020-11-05T08:19:00.000+0000'}, {'createddate': '2020-09-29T01:59:00.000+0000'}, {'createddate': '2021-03-07T11:25:00.000+0000'}, {'createddate': '2020-11-09T19:02:00.000+0000'}], 'var_function-call-12950532305396451246': [{'id': 'a03Wt00000JqhItIAJ', 'name': 'Software Installation Error', 'description__c': 'Users report encountering errors during the initial installation process, which hinders the setup of TechPulse solutions.'}, {'id': '#a03Wt00000JqmLvIAJ', 'name': 'Billing Discrepancy', 'description__c': 'Some clients encounter unexpected charges on their billing statements, leading to confusion and dissatisfaction.'}, {'id': 'a03Wt00000JqmX6IAJ', 'name': 'Customizability Limitation   ', 'description__c': 'Despite customization options, some users find it challenging to tailor solutions to fit extremely niche industry needs.'}, {'id': 'a03Wt00000JqnHwIAJ', 'name': 'User Interface Bug', 'description__c': "A segment of users face occasional glitches in the software's user interface, affecting their overall usability experience."}, {'id': '#a03Wt00000JqtOtIAJ', 'name': 'Support Response Delay', 'description__c': 'Some users face delays in getting timely responses from the TechPulse support team during peak times.'}, {'id': 'a03Wt00000JqvLsIAJ', 'name': 'License Renewal Confusion', 'description__c': 'Clients find the license renewal process unclear, causing unexpected service disruptions.'}, {'id': '#a03Wt00000JqvNUIAZ', 'name': 'Training Module Access   ', 'description__c': 'Customers report occasional technical difficulties accessing online training modules crucial for product adoption.'}, {'id': 'a03Wt00000JqvvOIAR', 'name': 'Data Loss Incident', 'description__c': 'In rare cases, clients experience unanticipated data loss during software updates, causing significant operational setbacks.'}, {'id': '#a03Wt00000JqxVjIAJ', 'name': 'AI Feature Malfunction', 'description__c': 'Some AI-powered features intermittently fail to operate, resulting in reduced efficiency and user frustration.'}, {'id': '#a03Wt00000JqxtvIAB', 'name': 'Scalability Issue', 'description__c': 'Some enterprises report difficulties in scaling TechPulse solutions to meet increasing demands, impacting their expansion efforts.'}], 'var_function-call-3623755885902086858': [{'total': '153', 'with_oi': '153'}], 'var_function-call-12251568129199960270': [{'Product2Id': '#01tWt000006hVTJIA2'}, {'Product2Id': '01tWt000006hVDBIA2'}, {'Product2Id': '01tWt000006hV8LIAU'}, {'Product2Id': '01tWt000006hVMrIAM'}, {'Product2Id': '#01tWt000006hVebIAE'}, {'Product2Id': '01tWt000006hVQ5IAM'}, {'Product2Id': '01tWt000006hVEnIAM'}, {'Product2Id': '01tWt000006hUgwIAE'}, {'Product2Id': '01tWt000006hV58IAE'}, {'Product2Id': '01tWt000006hVjRIAU'}, {'Product2Id': '#01tWt000006hV8LIAU'}, {'Product2Id': '01tWt000006hVBZIA2'}, {'Product2Id': '01tWt000006hVoHIAU'}, {'Product2Id': '01tWt000006hV6jIAE'}, {'Product2Id': '01tWt000006hTUkIAM'}, {'Product2Id': '01tWt000006hVhpIAE'}, {'Product2Id': '01tWt000006hVczIAE'}, {'Product2Id': '01tWt000006hVGPIA2'}, {'Product2Id': '01tWt000006hVJdIAM'}, {'Product2Id': '01tWt000006hVebIAE'}, {'Product2Id': '#01tWt000006hV58IAE'}, {'Product2Id': '#01tWt000006hVEnIAM'}, {'Product2Id': '01tWt000006hVwLIAU'}, {'Product2Id': '01tWt000006hVLFIA2'}, {'Product2Id': '#01tWt000006hV6jIAE'}, {'Product2Id': '01tWt000006hV9xIAE'}, {'Product2Id': '#01tWt000006hUgwIAE'}, {'Product2Id': '#01tWt000006hTUkIAM'}, {'Product2Id': '01tWt000006hVZlIAM'}, {'Product2Id': '#01tWt000006hVmfIAE'}, {'Product2Id': '01tWt000006hV57IAE'}, {'Product2Id': '#01tWt000006hVhpIAE'}, {'Product2Id': '01tWt000006hPffIAE'}, {'Product2Id': '#01tWt000006hV0IIAU'}, {'Product2Id': '01tWt000006hUKMIA2'}, {'Product2Id': '01tWt000006hVQ6IAM'}, {'Product2Id': '#01tWt000006hV57IAE'}, {'Product2Id': '#01tWt000006hVMrIAM'}, {'Product2Id': '#01tWt000006hVBZIA2'}, {'Product2Id': '01tWt000006hVptIAE'}, {'Product2Id': '#01tWt000006hVZlIAM'}, {'Product2Id': '#01tWt000006hV9xIAE'}, {'Product2Id': '01tWt000006hUtqIAE'}, {'Product2Id': '01tWt000006hVUvIAM'}, {'Product2Id': '#01tWt000006hVDBIA2'}, {'Product2Id': '01tWt000006hV0IIAU'}, {'Product2Id': '#01tWt000006hVI1IAM'}, {'Product2Id': '01tWt000006hVmfIAE'}, {'Product2Id': '#01tWt000006hVGPIA2'}, {'Product2Id': '01tWt000006hVI1IAM'}, {'Product2Id': '#01tWt000006hVLFIA2'}, {'Product2Id': '#01tWt000006hUsEIAU'}, {'Product2Id': '#01tWt000006hVQ6IAM'}, {'Product2Id': '01tWt000006hVgDIAU'}, {'Product2Id': '#01tWt000006hVrWIAU'}, {'Product2Id': '01tWt000006hVY9IAM'}, {'Product2Id': '#01tWt000006hVjRIAU'}, {'Product2Id': '#01tWt000006hVY9IAM'}, {'Product2Id': '#01tWt000006hVUvIAM'}, {'Product2Id': '#01tWt000006hUtqIAE'}, {'Product2Id': '01tWt000006hVTJIA2'}, {'Product2Id': '01tWt000006hVRhIAM'}, {'Product2Id': '#01tWt000006hVQ5IAM'}, {'Product2Id': '01tWt000006hVJeIAM'}, {'Product2Id': '#01tWt000006hVoHIAU'}, {'Product2Id': '#01tWt000006hPffIAE'}, {'Product2Id': '#01tWt000006hVJdIAM'}, {'Product2Id': '#01tWt000006hVwLIAU'}, {'Product2Id': '01tWt000006hPfgIAE'}, {'Product2Id': '#01tWt000006hVczIAE'}, {'Product2Id': '#01tWt000006hVptIAE'}], 'var_function-call-7179611796588648358': [{'orderitemid__c': '802Wt00000797r4IAA'}, {'orderitemid__c': '802Wt00000798aDIAQ'}, {'orderitemid__c': '802Wt00000792tiIAA'}, {'orderitemid__c': '802Wt00000797r3IAA'}, {'orderitemid__c': '802Wt00000797r5IAA'}, {'orderitemid__c': '802Wt00000792tiIAA'}, {'orderitemid__c': '802Wt0000078xAFIAY'}, {'orderitemid__c': '802Wt0000079ATyIAM'}, {'orderitemid__c': '802Wt00000794bXIAQ'}, {'orderitemid__c': '802Wt00000796yFIAQ'}, {'orderitemid__c': '802Wt000007988nIAA'}, {'orderitemid__c': '802Wt00000797axIAA'}, {'orderitemid__c': '802Wt00000797r5IAA'}, {'orderitemid__c': '802Wt0000079As9IAE'}, {'orderitemid__c': '802Wt000007983xIAA'}, {'orderitemid__c': '802Wt0000079ADpIAM'}, {'orderitemid__c': '802Wt000007928FIAQ'}, {'orderitemid__c': '802Wt0000079ATxIAM'}, {'orderitemid__c': '802Wt00000799EZIAY'}, {'orderitemid__c': '802Wt0000079ATxIAM'}], 'var_function-call-12052341154570949748': [{'count(*)': '689'}], 'var_function-call-15276008645661363926': 'file_storage/function-call-15276008645661363926.json', 'var_function-call-1464354546213212185': {'matches': 6, 'monthly_counts': {'2021-01': 1, '2020-11': 2, '2020-09': 1, '2021-03': 1}}}

exec(code, env_args)
