code = """import pandas as pd
import json

# Load data
order_items = locals()['var_function-call-455465860512101407']
emails = locals()['var_function-call-3675204781101789071']
chats = locals()['var_function-call-3675204781101785204']
cases_file = locals()['var_function-call-5122639424377830665']

with open(cases_file, 'r') as f:
    cases = json.load(f)

def clean_id(x):
    if not isinstance(x, str):
        return None
    x = x.strip()
    if x.startswith('#'):
        return x[1:]
    return x

valid_ois = set()
for item in order_items:
    oid = clean_id(item['Id'])
    if oid:
        valid_ois.add(oid)

valid_case_ids_text = set()
for e in emails:
    pid = clean_id(e.get('parentid'))
    if pid and pid != 'None':
        valid_case_ids_text.add(pid)
for c in chats:
    cid = clean_id(c.get('caseid'))
    if cid and cid != 'None':
        valid_case_ids_text.add(cid)

relevant_cases = []
for c in cases:
    c_id = clean_id(c.get('id'))
    c_oid = clean_id(c.get('orderitemid__c'))
    
    is_linked_oi = c_oid in valid_ois
    is_linked_text_id = c_id in valid_case_ids_text
    
    sub_desc = (str(c.get('subject', '')) + " " + str(c.get('description', ''))).lower()
    has_sa_text = "secureanalytics" in sub_desc
    
    if is_linked_oi or is_linked_text_id or has_sa_text:
        relevant_cases.append(c)

df = pd.DataFrame(relevant_cases)

if not df.empty:
    df['createddate'] = pd.to_datetime(df['createddate'])
    start_date = pd.Timestamp("2020-06-10").tz_localize('UTC')
    end_date = pd.Timestamp("2021-04-10").tz_localize('UTC')
    
    mask = (df['createddate'] >= start_date) & (df['createddate'] <= end_date)
    df_filtered = df[mask].copy()
    
    if not df_filtered.empty:
        df_filtered['month_year'] = df_filtered['createddate'].dt.to_period('M')
        # Use total counts
        counts = df_filtered['month_year'].value_counts().sort_index()
        result = {str(k): int(v) for k, v in counts.items()}
        print("__RESULT__:")
        print(json.dumps(result))
    else:
        print("__RESULT__:")
        print(json.dumps({}))
else:
    print("__RESULT__:")
    print(json.dumps({}))"""

env_args = {'var_function-call-2501921911844964614': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-2501921911844962647': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-455465860512101407': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-2577931855183809706': 'file_storage/function-call-2577931855183809706.json', 'var_function-call-8123939596398534791': {'2020-09': 1, '2020-11': 2, '2021-01': 1, '2021-03': 1}, 'var_function-call-7821128947417071662': [{'Name': 'SecureAnalytics Pro'}], 'var_function-call-14362444106178238778': 'file_storage/function-call-14362444106178238778.json', 'var_function-call-14267522873611632795': {'2020-09': 1, '2020-11': 2, '2021-01': 1, '2021-03': 1}, 'var_function-call-7644003844626233942': [{'id': 'a03Wt00000JqhItIAJ', 'name': 'Software Installation Error', 'description__c': 'Users report encountering errors during the initial installation process, which hinders the setup of TechPulse solutions.'}, {'id': '#a03Wt00000JqmLvIAJ', 'name': 'Billing Discrepancy', 'description__c': 'Some clients encounter unexpected charges on their billing statements, leading to confusion and dissatisfaction.'}, {'id': 'a03Wt00000JqmX6IAJ', 'name': 'Customizability Limitation   ', 'description__c': 'Despite customization options, some users find it challenging to tailor solutions to fit extremely niche industry needs.'}, {'id': 'a03Wt00000JqnHwIAJ', 'name': 'User Interface Bug', 'description__c': "A segment of users face occasional glitches in the software's user interface, affecting their overall usability experience."}, {'id': '#a03Wt00000JqtOtIAJ', 'name': 'Support Response Delay', 'description__c': 'Some users face delays in getting timely responses from the TechPulse support team during peak times.'}, {'id': 'a03Wt00000JqvLsIAJ', 'name': 'License Renewal Confusion', 'description__c': 'Clients find the license renewal process unclear, causing unexpected service disruptions.'}, {'id': '#a03Wt00000JqvNUIAZ', 'name': 'Training Module Access   ', 'description__c': 'Customers report occasional technical difficulties accessing online training modules crucial for product adoption.'}, {'id': 'a03Wt00000JqvvOIAR', 'name': 'Data Loss Incident', 'description__c': 'In rare cases, clients experience unanticipated data loss during software updates, causing significant operational setbacks.'}, {'id': '#a03Wt00000JqxVjIAJ', 'name': 'AI Feature Malfunction', 'description__c': 'Some AI-powered features intermittently fail to operate, resulting in reduced efficiency and user frustration.'}, {'id': '#a03Wt00000JqxtvIAB', 'name': 'Scalability Issue', 'description__c': 'Some enterprises report difficulties in scaling TechPulse solutions to meet increasing demands, impacting their expansion efforts.'}, {'id': 'a03Wt00000JqzKcIAJ', 'name': 'Data Integration Error', 'description__c': 'Users experience challenges when integrating TechPulse solutions with specific third-party software, leading to workflow disruptions.'}, {'id': 'a03Wt00000JqzPSIAZ', 'name': 'Security Compliance Query', 'description__c': 'Clients have concerns about understanding and adhering to the evolving security compliance standards set by TechPulse Solutions.'}, {'id': 'a03Wt00000JqzR3IAJ', 'name': 'Workflow Integration Lag', 'description__c': 'Certain clients experience latency issues when deploying TechPulse solutions within complex existing workflows.'}, {'id': 'a03Wt00000JqzSfIAJ', 'name': 'Feature Update Notification', 'description__c': "Customers are not consistently notified of new feature updates, leading to underutilization of the software's full capabilities."}, {'id': '#a03Wt00000JqzUHIAZ', 'name': 'ROI Assessment Discrepancy', 'description__c': 'A few customers need assistance reconciling their expected ROI with performance metrics delivered by the solutions.'}], 'var_function-call-11110855418657005330': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}], 'var_function-call-3675204781101789071': [{'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': '500Wt00000DE00gIAD'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': '500Wt00000DDxnbIAD'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': '500Wt00000DE0NFIA1'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': '500Wt00000DDzsbIAD'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': '500Wt00000DDzsbIAD'}, {'parentid': '500Wt00000DDzsbIAD'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': '500Wt00000DE00gIAD'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': '500Wt00000DE0AMIA1'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': '500Wt00000DE00gIAD'}, {'parentid': '500Wt00000DE0NFIA1'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': '500Wt00000DDzsbIAD'}, {'parentid': '500Wt00000DDzsbIAD'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': '500Wt00000DDxnbIAD'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': '500Wt00000DDxnbIAD'}, {'parentid': '500Wt00000DE0AMIA1'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': '500Wt00000DDxnbIAD'}, {'parentid': 'None'}, {'parentid': '500Wt00000DE0AMIA1'}, {'parentid': '500Wt00000DE00gIAD'}, {'parentid': '500Wt00000DE00gIAD'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': '500Wt00000DE0NFIA1'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': '500Wt00000DE0NFIA1'}, {'parentid': '500Wt00000DE0AMIA1'}, {'parentid': '500Wt00000DE0AMIA1'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}, {'parentid': 'None'}], 'var_function-call-3675204781101785204': [{'caseid': '500Wt00000DDy8bIAD'}], 'var_function-call-5122639424377830665': 'file_storage/function-call-5122639424377830665.json', 'var_function-call-4099277827117764107': {'2020-09': 1, '2020-11': 2, '2021-01': 1, '2021-03': 1}}

exec(code, env_args)
