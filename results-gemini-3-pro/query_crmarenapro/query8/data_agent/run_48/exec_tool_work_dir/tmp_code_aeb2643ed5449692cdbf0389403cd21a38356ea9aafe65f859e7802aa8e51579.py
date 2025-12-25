code = """import json

# Load data (using same variables)
with open(locals()['var_function-call-14770685575047062042'], 'r') as f:
    history_data = json.load(f)
with open(locals()['var_function-call-11360643150858883900'], 'r') as f:
    case_data = json.load(f)

# Dates: Last 4 quarters relative to 2023-04-10
# Usually means full quarters: Q2 22, Q3 22, Q4 22, Q1 23. (2022-04-01 to 2023-03-31)
# I will stick to this standard definition first.
# If I use exact year: 2022-04-10 to 2023-04-10.
# Let's try 2022-04-01 to 2023-03-31 (Standard 4 quarters).

start_date = "2022-04-01"
end_date = "2023-03-31"

def clean_id(i):
    if not i: return None
    i = str(i).strip()
    if i == 'None': return None
    return i.lstrip('#')

def in_range(d):
    if not d: return False
    return start_date <= d[:10] <= end_date

# Filter
hist_filt = [r for r in history_data if in_range(r.get('createddate'))]
case_filt = [r for r in case_data if in_range(r.get('createddate'))]

# Calculate handled cases count and transfer count
# Handled count: Number of times agent appears as 'newvalue' (in history) or 'ownerid' (in created cases).
# Note: A case might be counted multiple times if transferred to same agent?
# "Handled more than 0 cases" -> Just need count > 0.
# Transfer count: Number of times agent appears as 'oldvalue'.

agent_stats = {}

# Process History
for r in hist_filt:
    old = clean_id(r.get('oldvalue__c'))
    new = clean_id(r.get('newvalue__c'))
    
    # Transfer: old -> new
    if old:
        if old not in agent_stats: agent_stats[old] = {'handled': 0, 'transfers': 0}
        agent_stats[old]['transfers'] += 1
        # Being in 'old' implies they handled it previously.
        # But we want to filter by "handled > 0". Being a sender means handled > 0?
        # Yes, you can't transfer what you don't have.
        
    if new:
        if new not in agent_stats: agent_stats[new] = {'handled': 0, 'transfers': 0}
        agent_stats[new]['handled'] += 1

# Process Cases (Initial ownership)
# Note: If a case is in 'case_filt', its owner handled it.
# Check if this assignment is already covered by history?
# If history has (Old=None, New=Owner, Date=CreatedDate), it's covered.
# If history is missing, we add.
# For simplicity, let's just count 'ownerid' towards handled.
# We are only checking handled > 0 condition.
for r in case_filt:
    owner = clean_id(r.get('ownerid'))
    if owner:
        if owner not in agent_stats: agent_stats[owner] = {'handled': 0, 'transfers': 0}
        agent_stats[owner]['handled'] += 1

# Filter: handled > 0
# Logic: An agent handled a case if 'handled' count > 0 OR 'transfers' count > 0 (since they must have handled to transfer).
candidates = []
for agent, stats in agent_stats.items():
    if stats['handled'] > 0 or stats['transfers'] > 0:
        candidates.append((agent, stats['transfers'], stats['handled']))

# Find min transfers
if not candidates:
    print("__RESULT__:")
    print(json.dumps("No candidates"))
else:
    min_trans = min(c[1] for c in candidates)
    best_candidates = [c for c in candidates if c[1] == min_trans]
    
    # Sort by handled count descending? (Just to see)
    best_candidates.sort(key=lambda x: x[2], reverse=True)
    
    print("__RESULT__:")
    print(json.dumps(best_candidates))"""

env_args = {'var_function-call-8945435299677273893': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-4371058042737837782': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_function-call-3765472477778977412': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-10721788631355263215': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-14770685575047062042': 'file_storage/function-call-14770685575047062042.json', 'var_function-call-11360643150858883900': 'file_storage/function-call-11360643150858883900.json', 'var_function-call-13863447851476092692': {'min_transfers': 0, 'candidates': ['005Wt000003NINVIA4', '005Wt000003NJcvIAG', '005Wt000003NJTFIA4', '005Wt000003NIwzIAG', '005Wt000003NJEjIAO', '005Wt000003NJrRIAW', '005Wt000003NDJ1IAO', '005Wt000003NIvNIAW', '005Wt000003NIc2IAG', '005Wt000003NJ8HIAW', '005Wt000003NJ6gIAG', '005Wt000003NInLIAW', '005Wt000003NJoDIAW', '005Wt000003NFr4IAG', '005Wt000003NIVZIA4', '005Wt000003NDsUIAW', '005Wt000003NEGhIAO', '005Wt000003NISLIA4', '005Wt000003NGjuIAG', '005Wt000003NEzqIAG', '005Wt000003NDqFIAW', '005Wt000003NJhlIAG', '005Wt000003NI2XIAW', '005Wt000003NJ0DIAW', '005Wt000003NHsrIAG', '005Wt000003NFKoIAO', '005Wt000003NBcAIAW', '005Wt000003NHpeIAG', '005Wt000003NJD9IAO', '005Wt000003NBykIAG', '005Wt000003NIaQIAW']}}

exec(code, env_args)
