code = """import pandas as pd
import json

# Load Cases with subject/description
with open(locals()['var_function-call-14362444106178238778'], 'r') as f:
    cases = json.load(f)

df = pd.DataFrame(cases)

if df.empty:
    print("__RESULT__:")
    print(json.dumps({"error": "No cases"}))
else:
    df['createddate'] = pd.to_datetime(df['createddate'])
    
    # Filter Date
    start_date = pd.Timestamp("2020-06-10").tz_localize('UTC')
    end_date = pd.Timestamp("2021-04-10").tz_localize('UTC')
    mask = (df['createddate'] >= start_date) & (df['createddate'] <= end_date)
    df_filtered = df[mask].copy()
    
    # Filter by Text
    # Check subject and description for "SecureAnalytics Pro"
    def check_text(row):
        text = (str(row.get('subject', '')) + " " + str(row.get('description', ''))).lower()
        return "secureanalytics pro" in text

    df_filtered['match'] = df_filtered.apply(check_text, axis=1)
    df_matched = df_filtered[df_filtered['match']].copy()
    
    # Group by Month
    if not df_matched.empty:
        df_matched['month_year'] = df_matched['createddate'].dt.to_period('M')
        counts = df_matched['month_year'].value_counts().sort_index()
        result = {str(k): int(v) for k, v in counts.items()}
    else:
        result = {}

    print("__RESULT__:")
    print(json.dumps(result))"""

env_args = {'var_function-call-2501921911844964614': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-2501921911844962647': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-455465860512101407': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-2577931855183809706': 'file_storage/function-call-2577931855183809706.json', 'var_function-call-8123939596398534791': {'2020-09': 1, '2020-11': 2, '2021-01': 1, '2021-03': 1}, 'var_function-call-7821128947417071662': [{'Name': 'SecureAnalytics Pro'}], 'var_function-call-14362444106178238778': 'file_storage/function-call-14362444106178238778.json'}

exec(code, env_args)
