code = """import json
import datetime

# Load data
cases = json.load(open(locals()['var_function-call-13480936882204567300']))
history = json.load(open(locals()['var_function-call-3991008059814266160']))

# Helpers
def clean_id(i):
    if i and i.startswith('#'):
        return i[1:]
    return i

def parse_dt(s):
    # Format: "2023-07-02T11:00:00.000+0000"
    # Python 3.12 handles ISO with timezone
    # But sometimes simple replace is safer for comparison if TZ is consistent
    try:
        return datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%S.%f%z")
    except:
        # Try without micros
        return datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%S%z")

# Period P
p_start = datetime.datetime(2022, 4, 1, tzinfo=datetime.timezone.utc)
p_end = datetime.datetime(2023, 3, 31, 23, 59, 59, tzinfo=datetime.timezone.utc)

# Process History
# Group transfers by case
case_transfers = {}
for h in history:
    cid = clean_id(h['caseid__c'])
    old_v = clean_id(h['oldvalue__c'])
    new_v = clean_id(h['newvalue__c'])
    
    # Handle "None" string
    if old_v == 'None': old_v = None
    if new_v == 'None': new_v = None
    
    dt = parse_dt(h['createddate'])
    
    if cid not in case_transfers:
        case_transfers[cid] = []
    case_transfers[cid].append({
        'old': old_v,
        'new': new_v,
        'date': dt
    })

# Sort transfers
for cid in case_transfers:
    case_transfers[cid].sort(key=lambda x: x['date'])

# Stats
agent_handled_p = set() # Agents who handled a case in P
agent_transfer_counts_p = {} # Transfer counts in P

# Process Cases
for c in cases:
    cid = clean_id(c['id'])
    created_dt = parse_dt(c['createddate'])
    
    # Get transfers
    transfers = case_transfers.get(cid, [])
    
    # Build timeline: List of (Agent, Start, End)
    timeline = []
    
    current_agent = None
    current_start = created_dt
    
    # Determine Initial Agent
    # If first transfer has old=None, that's the setup
    if transfers and transfers[0]['old'] is None:
        current_agent = transfers[0]['new']
        # technically assignment time is transfer date, but we can assume they "handled" from then
        # Or from creation? If old=None is "Creation", then date matches created_dt roughly.
        # Let's use the transfer date for this segment start, to be precise.
        # But wait, if created_dt < transfer_date, who owned it in between?
        # Usually it's milliseconds.
        current_start = transfers[0]['date']
        start_idx = 1 # Skip this transfer as it's not a reassignment
    elif transfers:
        # First transfer has old != None.
        # So old was the initial agent.
        current_agent = transfers[0]['old']
        current_start = created_dt
        start_idx = 0
    else:
        # No transfers. Owner in Case is the only owner.
        current_agent = clean_id(c['ownerid'])
        current_start = created_dt
        start_idx = 0
        
    # Process transfers to build timeline
    # We iterate through transfers that are actual moves (old -> new)
    for i in range(start_idx, len(transfers)):
        t = transfers[i]
        t_date = t['date']
        t_old = t['old']
        t_new = t['new']
        
        # If we skipped the None->X, the next should be X->Y
        # Verify chain continuity
        if current_agent and t_old and t_old != current_agent:
            # Chain broken or mixed up. Log warning?
            # Assume t_old is correct source
            pass
            
        # Add segment for current_agent
        timeline.append((current_agent, current_start, t_date))
        
        # Switch
        current_agent = t_new
        current_start = t_date
        
    # Add final segment
    # Ends at Now (or Closed Date, but we treat handling as up to now if active, or just check overlap)
    # The agent "holds" the case until now or closed.
    # For "Handled" check, we just need overlap with P.
    # We can use a far future date or actual close date.
    # Let's use current time (now) as effective end if open.
    # Or just check if Start <= P_end.
    # If closed, use close date.
    closed_dt = None
    if c['closeddate'] and c['closeddate'] != 'None':
        closed_dt = parse_dt(c['closeddate'])
    
    final_end = closed_dt if closed_dt else datetime.datetime.now(datetime.timezone.utc)
    timeline.append((current_agent, current_start, final_end))
    
    # Analyze Timeline for "Handled > 0"
    for agent, start, end in timeline:
        if not agent: continue
        # Check overlap with P
        # Overlap if Start <= P_end AND End >= P_start
        if start <= p_end and end >= p_start:
            agent_handled_p.add(agent)
            
    # Analyze Transfers for Count
    # We look at the transfers list directly
    for t in transfers:
        if t['old'] is not None:
            # This is a transfer FROM t['old']
            if p_start <= t['date'] <= p_end:
                aid = t['old']
                agent_transfer_counts_p[aid] = agent_transfer_counts_p.get(aid, 0) + 1

# Result
candidates = []
for agent in agent_handled_p:
    # Initialize count to 0 if not present
    tc = agent_transfer_counts_p.get(agent, 0)
    candidates.append({'id': agent, 'count': tc})

# Sort by count ASC
candidates.sort(key=lambda x: x['count'])

print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_function-call-10596123665962995333': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-4624164474270102215': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-15624615594297472901': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_function-call-15061620003663225348': [{'count': '153'}], 'var_function-call-13480936882204567300': 'file_storage/function-call-13480936882204567300.json', 'var_function-call-3991008059814266160': 'file_storage/function-call-3991008059814266160.json'}

exec(code, env_args)
