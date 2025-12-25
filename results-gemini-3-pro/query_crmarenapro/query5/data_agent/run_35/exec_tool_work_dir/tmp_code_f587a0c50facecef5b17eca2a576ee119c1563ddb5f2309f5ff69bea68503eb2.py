code = """import json
from datetime import datetime

# Load data
order_items = locals()['var_function-call-11808410621545789283']
cases = locals()['var_function-call-224870146621939057']

# Target Product ID (for reference)
product_id = '01tWt000006hV8LIAU'

# Clean Order Item IDs
valid_order_item_ids = set()
for item in order_items:
    oid = item['Id']
    if oid:
        # Remove leading #
        if oid.startswith('#'):
            oid = oid[1:]
        # Remove whitespace
        oid = oid.strip()
        valid_order_item_ids.add(oid)

# Date range
start_date = datetime(2022, 8, 16)
end_date = datetime(2023, 1, 16, 23, 59, 59)

# Filter Cases
filtered_cases = []
for case in cases:
    # Check date
    c_date_str = case['createddate']
    # Parse date. Format: "2023-07-02T11:00:00.000+0000"
    # Python 3.12 can handle isoformat usually, but the timezone +0000 might need handling if not standard ISO.
    # The example shows +0000. datetime.fromisoformat might handle it in newer python versions.
    # Alternatively use string slicing for YYYY-MM-DD
    
    # Let's try parsing
    try:
        # Remove +0000 and parse, assuming UTC
        # Or better, just compare YYYY-MM-DD parts if time doesn't matter much.
        # But let's try to be precise.
        # Simple parsing
        dt_str = c_date_str.split('+')[0]
        dt = datetime.strptime(dt_str, "%Y-%m-%dT%H:%M:%S.%f")
        # Ignore timezone for comparison if we assume everything is consistent (or convert).
        # Assuming database returns UTC or consistent timezone.
        
        if start_date <= dt <= end_date:
            # Check Order Item
            oid = case['orderitemid__c']
            if oid:
                if oid.startswith('#'):
                    oid = oid[1:]
                oid = oid.strip()
                
                if oid in valid_order_item_ids:
                    filtered_cases.append(case)
    except Exception as e:
        # print(f"Error parsing date: {c_date_str} {e}")
        pass

# Count issues
issue_counts = {}
for case in filtered_cases:
    issue_id = case['issueid__c']
    if issue_id:
        issue_counts[issue_id] = issue_counts.get(issue_id, 0) + 1

# Find most frequent
most_frequent_issue = None
max_count = 0

for issue, count in issue_counts.items():
    if count > max_count:
        max_count = count
        most_frequent_issue = issue

print("__RESULT__:")
print(json.dumps(most_frequent_issue))"""

env_args = {'var_function-call-11808410621545791045': [], 'var_function-call-11808410621545790164': [{'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}], 'var_function-call-11808410621545789283': [{'Id': '802Wt0000078wz5IAA'}, {'Id': '802Wt0000078xAAIAY'}, {'Id': '802Wt0000078yXiIAI'}, {'Id': '#802Wt00000790WEIAY'}, {'Id': '802Wt00000792gDIAQ'}, {'Id': '802Wt00000792zTIAQ'}, {'Id': '#802Wt0000079315IAA'}, {'Id': '802Wt00000793sTIAQ'}, {'Id': '802Wt00000794F3IAI'}, {'Id': '802Wt00000794F4IAI'}, {'Id': '#802Wt00000794JmIAI'}, {'Id': '#802Wt00000794YFIAY'}, {'Id': '802Wt00000794YJIAY'}, {'Id': '802Wt000007959OIAQ'}, {'Id': '802Wt00000795akIAA'}, {'Id': '802Wt00000795ywIAA'}, {'Id': '802Wt000007962JIAQ'}, {'Id': '802Wt000007968hIAA'}, {'Id': '802Wt000007968iIAA'}, {'Id': '802Wt00000796F5IAI'}, {'Id': '#802Wt00000796N7IAI'}, {'Id': '802Wt00000796NAIAY'}, {'Id': '802Wt00000796RzIAI'}, {'Id': '802Wt00000796S0IAI'}, {'Id': '802Wt00000796S1IAI'}, {'Id': '802Wt00000796VDIAY'}, {'Id': '802Wt00000796YPIAY'}, {'Id': '802Wt00000796YQIAY'}, {'Id': '802Wt00000796a1IAA'}, {'Id': '802Wt00000796dFIAQ'}, {'Id': '#802Wt00000796dIIAQ'}, {'Id': '#802Wt00000796jiIAA'}, {'Id': '802Wt00000796myIAA'}, {'Id': '802Wt00000796oaIAA'}, {'Id': '802Wt00000796rlIAA'}, {'Id': '802Wt00000796tTIAQ'}, {'Id': '802Wt00000796v0IAA'}, {'Id': '802Wt00000796wbIAA'}, {'Id': '802Wt00000796wcIAA'}, {'Id': '802Wt00000797FxIAI'}, {'Id': '802Wt00000797MQIAY'}, {'Id': '#802Wt00000797O5IAI'}, {'Id': '#802Wt00000797axIAA'}, {'Id': '802Wt00000797e9IAA'}, {'Id': '802Wt00000797hNIAQ'}, {'Id': '802Wt00000797j0IAA'}, {'Id': '#802Wt00000797mDIAQ'}, {'Id': '802Wt00000797nsIAA'}, {'Id': '#802Wt00000797pSIAQ'}, {'Id': '802Wt00000797sfIAA'}, {'Id': '802Wt00000797z8IAA'}, {'Id': '802Wt000007982LIAQ'}, {'Id': '802Wt00000798IUIAY'}, {'Id': '802Wt00000798IVIAY'}, {'Id': '802Wt00000798NKIAY'}, {'Id': '#802Wt00000798S9IAI'}, {'Id': '#802Wt00000798nBIAQ'}, {'Id': '802Wt00000798rxIAA'}, {'Id': '802Wt00000798wpIAA'}, {'Id': '802Wt000007991dIAA'}, {'Id': '802Wt0000079987IAA'}, {'Id': '802Wt00000799EZIAY'}, {'Id': '802Wt00000799HoIAI'}, {'Id': '#802Wt00000799JPIAY'}, {'Id': '802Wt00000799T3IAI'}, {'Id': '802Wt00000799ckIAA'}, {'Id': '#802Wt00000799fxIAA'}, {'Id': '802Wt00000799srIAA'}, {'Id': '802Wt00000799w5IAA'}, {'Id': '#802Wt0000079A0wIAE'}, {'Id': '802Wt0000079A2aIAE'}, {'Id': '802Wt0000079A49IAE'}, {'Id': '802Wt0000079AU1IAM'}, {'Id': '802Wt0000079AgrIAE'}, {'Id': '802Wt0000079AqXIAU'}, {'Id': '802Wt0000079As9IAE'}], 'var_function-call-224870146621939057': [{'issueid__c': 'a03Wt00000JqzSfIAJ', 'orderitemid__c': '802Wt00000797r4IAA', 'createddate': '2023-07-02T11:00:00.000+0000'}, {'issueid__c': 'a03Wt00000JqtOtIAJ', 'orderitemid__c': '802Wt00000792tiIAA', 'createddate': '2023-09-30T11:30:00.000+0000'}, {'issueid__c': 'a03Wt00000JqtOtIAJ', 'orderitemid__c': '802Wt00000792tiIAA', 'createddate': '2023-10-02T14:15:00.000+0000'}, {'issueid__c': 'a03Wt00000JqmX6IAJ', 'orderitemid__c': '802Wt00000794bXIAQ', 'createddate': '2023-04-05T17:51:00.000+0000'}, {'issueid__c': 'a03Wt00000JqxtvIAB', 'orderitemid__c': '802Wt00000796yFIAQ', 'createddate': '2023-03-08T06:49:00.000+0000'}, {'issueid__c': 'a03Wt00000JqzPSIAZ', 'orderitemid__c': '802Wt0000079ATxIAM', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'issueid__c': 'a03Wt00000JqzUHIAZ', 'orderitemid__c': '802Wt00000799EZIAY', 'createddate': '2023-10-15T09:15:47.000+0000'}, {'issueid__c': 'a03Wt00000JqzPSIAZ', 'orderitemid__c': '802Wt0000079ATxIAM', 'createddate': '2023-10-02T09:15:00.000+0000'}, {'issueid__c': 'a03Wt00000JqmX6IAJ', 'orderitemid__c': '802Wt00000790mNIAQ', 'createddate': '2022-09-05T11:15:00.000+0000'}, {'issueid__c': 'a03Wt00000JqzKcIAJ', 'orderitemid__c': '802Wt00000797RHIAY', 'createddate': '2023-10-02T10:15:00.000+0000'}, {'issueid__c': 'a03Wt00000JqzR3IAJ', 'orderitemid__c': '802Wt00000791h9IAA', 'createddate': '2023-01-18T14:45:00.000+0000'}, {'issueid__c': 'a03Wt00000JqzPSIAZ', 'orderitemid__c': '802Wt00000799mPIAQ', 'createddate': '2023-01-04T08:47:00.000+0000'}, {'issueid__c': 'a03Wt00000JqzSfIAJ', 'orderitemid__c': '802Wt000007906kIAA', 'createddate': '2023-07-01T10:30:00.000+0000'}, {'issueid__c': 'a03Wt00000JqvNUIAZ', 'orderitemid__c': '802Wt0000079AU2IAM', 'createddate': '2023-09-22T08:28:00.000+0000'}, {'issueid__c': 'a03Wt00000JqzSfIAJ', 'orderitemid__c': '802Wt000007968iIAA', 'createddate': '2024-05-02T09:30:00.000+0000'}, {'issueid__c': 'a03Wt00000JqzR3IAJ', 'orderitemid__c': '802Wt00000798S9IAI', 'createddate': '2023-06-12T09:45:00.000+0000'}, {'issueid__c': 'a03Wt00000JqvNUIAZ', 'orderitemid__c': '802Wt00000798K5IAI', 'createddate': '2023-01-03T10:15:00.000+0000'}, {'issueid__c': 'a03Wt00000JqhItIAJ', 'orderitemid__c': '802Wt00000793bTIAQ', 'createddate': '2022-12-01T10:00:00.000+0000'}, {'issueid__c': 'a03Wt00000JqnHwIAJ', 'orderitemid__c': '802Wt00000799ckIAA', 'createddate': '2023-11-03T11:30:00.000+0000'}, {'issueid__c': 'a03Wt00000JqzKcIAJ', 'orderitemid__c': '802Wt00000798FGIAY', 'createddate': '2023-10-16T09:00:00.000+0000'}, {'issueid__c': 'a03Wt00000JqzR3IAJ', 'orderitemid__c': '802Wt00000796IHIAY', 'createddate': '2023-10-03T14:34:22.000+0000'}, {'issueid__c': 'a03Wt00000JqzSfIAJ', 'orderitemid__c': '802Wt00000795izIAA', 'createddate': '2023-08-10T14:20:00.000+0000'}, {'issueid__c': 'a03Wt00000JqnHwIAJ', 'orderitemid__c': '802Wt00000790WEIAY', 'createddate': '2022-10-01T14:45:00.000+0000'}, {'issueid__c': 'a03Wt00000JqzSfIAJ', 'orderitemid__c': '802Wt000007968iIAA', 'createddate': '2024-05-15T14:45:00.000+0000'}, {'issueid__c': 'a03Wt00000JqnHwIAJ', 'orderitemid__c': '802Wt00000790WEIAY', 'createddate': '2022-09-16T09:30:00.000+0000'}, {'issueid__c': 'a03Wt00000JqzPSIAZ', 'orderitemid__c': '802Wt00000798OwIAI', 'createddate': '2023-01-23T08:02:00.000+0000'}, {'issueid__c': 'a03Wt00000JqxVjIAJ', 'orderitemid__c': '802Wt00000798iIIAQ', 'createddate': '2023-02-01T14:15:00.000+0000'}, {'issueid__c': 'a03Wt00000JqzKcIAJ', 'orderitemid__c': '802Wt00000799hbIAA', 'createddate': '2023-03-20T14:15:00.000+0000'}, {'issueid__c': 'a03Wt00000JqxtvIAB', 'orderitemid__c': '802Wt00000794v0IAA', 'createddate': '2023-10-16T09:15:00.000+0000'}, {'issueid__c': 'a03Wt00000JqxtvIAB', 'orderitemid__c': '802Wt000007928FIAQ', 'createddate': '2022-09-22T19:28:00.000+0000'}, {'issueid__c': 'a03Wt00000JqxVjIAJ', 'orderitemid__c': '802Wt00000798iIIAQ', 'createddate': '2023-01-18T10:30:00.000+0000'}, {'issueid__c': 'a03Wt00000JqmX6IAJ', 'orderitemid__c': '802Wt00000798NMIAY', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'issueid__c': 'a03Wt00000JqzPSIAZ', 'orderitemid__c': '802Wt00000798dRIAQ', 'createddate': '2023-09-03T10:15:00.000+0000'}, {'issueid__c': 'a03Wt00000JqxVjIAJ', 'orderitemid__c': '802Wt00000792gBIAQ', 'createddate': '2023-03-05T09:30:00.000+0000'}, {'issueid__c': 'a03Wt00000JqmX6IAJ', 'orderitemid__c': '802Wt0000079A4AIAU', 'createddate': '2022-09-03T15:30:00.000+0000'}, {'issueid__c': 'a03Wt00000JqvvOIAR', 'orderitemid__c': '802Wt00000796IJIAY', 'createddate': '2023-03-15T09:30:00.000+0000'}, {'issueid__c': 'a03Wt00000JqxVjIAJ', 'orderitemid__c': '802Wt00000797CjIAI', 'createddate': '2023-04-15T09:30:00.000+0000'}, {'issueid__c': 'a03Wt00000JqzKcIAJ', 'orderitemid__c': '802Wt00000794EyIAI', 'createddate': '2023-03-16T14:45:00.000+0000'}, {'issueid__c': 'a03Wt00000JqxVjIAJ', 'orderitemid__c': '802Wt00000796i5IAA', 'createddate': '2023-03-17T11:20:00.000+0000'}, {'issueid__c': 'a03Wt00000JqzR3IAJ', 'orderitemid__c': '802Wt00000795xLIAQ', 'createddate': '2023-09-20T10:15:00.000+0000'}, {'issueid__c': 'a03Wt00000JqxVjIAJ', 'orderitemid__c': '802Wt00000797CjIAI', 'createddate': '2023-05-10T14:45:00.000+0000'}, {'issueid__c': 'a03Wt00000JqtOtIAJ', 'orderitemid__c': '802Wt00000792tiIAA', 'createddate': '2023-10-05T09:45:00.000+0000'}, {'issueid__c': 'a03Wt00000JqxVjIAJ', 'orderitemid__c': '802Wt00000797CjIAI', 'createddate': '2023-06-22T11:00:00.000+0000'}, {'issueid__c': 'a03Wt00000JqnHwIAJ', 'orderitemid__c': '802Wt00000798olIAA', 'createddate': '2022-09-05T14:45:00.000+0000'}, {'issueid__c': 'a03Wt00000JqnHwIAJ', 'orderitemid__c': '802Wt0000078yseIAA', 'createddate': '2023-09-06T11:15:00.000+0000'}, {'issueid__c': 'a03Wt00000JqmX6IAJ', 'orderitemid__c': '802Wt00000798qLIAQ', 'createddate': '2023-07-02T09:30:00.000+0000'}, {'issueid__c': 'a03Wt00000JqhItIAJ', 'orderitemid__c': '802Wt00000793sQIAQ', 'createddate': '2023-10-20T10:00:00.000+0000'}, {'issueid__c': 'a03Wt00000JqvNUIAZ', 'orderitemid__c': '802Wt00000798K5IAI', 'createddate': '2023-02-15T14:30:00.000+0000'}, {'issueid__c': 'a03Wt00000JqzR3IAJ', 'orderitemid__c': '802Wt00000798S9IAI', 'createddate': '2023-06-05T11:15:00.000+0000'}, {'issueid__c': 'a03Wt00000JqzR3IAJ', 'orderitemid__c': '802Wt00000798S9IAI', 'createddate': '2023-06-19T14:30:00.000+0000'}, {'issueid__c': 'a03Wt00000JqzR3IAJ', 'orderitemid__c': '802Wt0000078ysdIAA', 'createddate': '2023-09-04T14:20:00.000+0000'}, {'issueid__c': 'a03Wt00000JqzPSIAZ', 'orderitemid__c': '802Wt00000798dRIAQ', 'createddate': '2023-09-07T16:30:00.000+0000'}, {'issueid__c': 'a03Wt00000JqzR3IAJ', 'orderitemid__c': '802Wt00000794F3IAI', 'createddate': '2023-01-17T09:30:00.000+0000'}, {'issueid__c': 'a03Wt00000JqmX6IAJ', 'orderitemid__c': '802Wt00000798NMIAY', 'createddate': '2023-08-01T10:00:00.000+0000'}, {'issueid__c': 'a03Wt00000JqxtvIAB', 'orderitemid__c': '802Wt00000798YdIAI', 'createddate': '2023-06-30T13:03:00.000+0000'}, {'issueid__c': 'a03Wt00000JqxtvIAB', 'orderitemid__c': '802Wt00000796qDIAQ', 'createddate': '2023-05-02T23:55:00.000+0000'}, {'issueid__c': 'a03Wt00000JqhItIAJ', 'orderitemid__c': '802Wt00000799UfIAI', 'createddate': '2023-06-02T09:30:00.000+0000'}, {'issueid__c': 'a03Wt00000JqzPSIAZ', 'orderitemid__c': '802Wt00000798SAIAY', 'createddate': '2023-04-10T10:30:00.000+0000'}, {'issueid__c': 'a03Wt00000JqzSfIAJ', 'orderitemid__c': '802Wt00000796jiIAA', 'createddate': '2023-03-01T09:30:00.000+0000'}, {'issueid__c': 'a03Wt00000JqhItIAJ', 'orderitemid__c': '802Wt000007928GIAQ', 'createddate': '2024-05-02T09:00:00.000+0000'}, {'issueid__c': 'a03Wt00000JqxVjIAJ', 'orderitemid__c': '802Wt00000792gCIAQ', 'createddate': '2023-09-05T10:15:00.000+0000'}, {'issueid__c': 'a03Wt00000JqhItIAJ', 'orderitemid__c': '802Wt00000799UfIAI', 'createddate': '2023-06-03T14:45:00.000+0000'}, {'issueid__c': 'a03Wt00000JqmX6IAJ', 'orderitemid__c': '802Wt00000799L2IAI', 'createddate': '2023-12-02T11:30:00.000+0000'}, {'issueid__c': 'a03Wt00000JqtOtIAJ', 'orderitemid__c': '802Wt00000795j3IAA', 'createddate': '2023-09-16T15:30:00.000+0000'}, {'issueid__c': 'a03Wt00000JqhItIAJ', 'orderitemid__c': '802Wt00000796lLIAQ', 'createddate': '2023-11-02T10:00:00.000+0000'}, {'issueid__c': 'a03Wt00000JqmX6IAJ', 'orderitemid__c': '802Wt00000798nBIAQ', 'createddate': '2024-05-05T10:15:30.000+0000'}, {'issueid__c': 'a03Wt00000JqzR3IAJ', 'orderitemid__c': '802Wt00000797j2IAA', 'createddate': '2023-03-22T14:30:00.000+0000'}, {'issueid__c': 'a03Wt00000JqtOtIAJ', 'orderitemid__c': '802Wt00000795j3IAA', 'createddate': '2023-09-18T09:45:00.000+0000'}, {'issueid__c': 'a03Wt00000JqnHwIAJ', 'orderitemid__c': '802Wt00000798olIAA', 'createddate': '2022-10-15T11:00:00.000+0000'}, {'issueid__c': 'a03Wt00000JqzSfIAJ', 'orderitemid__c': '802Wt00000796jiIAA', 'createddate': '2023-02-24T01:11:00.000+0000'}, {'issueid__c': 'a03Wt00000JqvNUIAZ', 'orderitemid__c': '802Wt0000079AU2IAM', 'createddate': '2023-09-25T10:30:00.000+0000'}, {'issueid__c': 'a03Wt00000JqzSfIAJ', 'orderitemid__c': '802Wt0000079AvNIAU', 'createddate': '2023-03-23T09:15:00.000+0000'}]}

exec(code, env_args)
