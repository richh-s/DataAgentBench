code = """import json
from datetime import datetime, timezone

# Load data
with open(locals()['var_function-call-3119883133918778239'], 'r') as f:
    cases_data = json.load(f)

with open(locals()['var_function-call-18131444671333490707'], 'r') as f:
    history_data = json.load(f)

def clean_id(i):
    if i and i.startswith('#'):
        return i[1:]
    return i

def parse_date(d):
    if not d or d == 'None':
        return None
    try:
        return datetime.strptime(d, "%Y-%m-%dT%H:%M:%S.%f%z")
    except ValueError:
        try:
            return datetime.strptime(d, "%Y-%m-%dT%H:%M:%S%z")
        except:
            return None

# Process History
case_history = {}
for h in history_data:
    cid = clean_id(h.get('caseid__c'))
    oid = clean_id(h.get('newvalue__c'))
    cdate = parse_date(h.get('createddate'))
    if cid and oid and cdate:
        if cid not in case_history:
            case_history[cid] = []
        case_history[cid].append({'date': cdate, 'owner': oid})

for cid in case_history:
    case_history[cid].sort(key=lambda x: x['date'])

# Define Window
window_start = datetime(2023, 5, 2, tzinfo=timezone.utc)
window_end = datetime(2023, 9, 2, 23, 59, 59, tzinfo=timezone.utc)

agent_processed_in_window = {}
agent_handle_times = {}

for c in cases_data:
    cid = clean_id(c.get('id'))
    created_date = parse_date(c.get('createddate'))
    closed_date = parse_date(c.get('closeddate'))
    initial_owner = clean_id(c.get('ownerid')) # Fallback or current?
    
    # We need to reconstruct the timeline.
    # Start with created date and first owner?
    # History has "Owner Assignment".
    # Case table has "OwnerId" which is the CURRENT owner.
    # If history is present, the first "Owner Assignment" might be later than creation?
    # Or maybe "Owner Assignment" logs the change?
    # If created with Owner A. Then changed to B.
    # History: "Owner Assignment" -> B.
    # So [Created, Assignment B] is Owner A.
    # [Assignment B, Closed/Now] is Owner B.
    
    timeline = []
    
    # Get history events
    events = case_history.get(cid, [])
    
    # Determine initial owner.
    # If we have history, the previous owner of the first event? 
    # History entries have "oldvalue__c" and "newvalue__c".
    # But in previous tools, `oldvalue__c` was often "None".
    # So we might rely on inference.
    # However, if there are NO history events, the only owner is `c.ownerid`.
    # If there ARE events, `c.ownerid` should match the `newvalue` of the last event.
    
    current_time = created_date
    if not current_time:
        continue # Bad data
        
    # We don't explicitly know the initial owner if oldvalue is None.
    # But we can assume the Case ownerid is the final owner.
    # If events exist:
    # Event 1: New Owner O1 at T1.
    # Who was owner before T1?
    # Maybe we can't know. Or maybe the first event IS the assignment at creation?
    # In the preview: "Owner Assignment", oldvalue "None", newvalue "X". createddate = case createddate.
    # This suggests the first event IS the initial assignment.
    # So we can just iterate events.
    
    # If the first event time > created time, there was an owner before.
    # But for this problem, let's use the events.
    
    # Logic:
    # Sort events by date.
    # If first event is at creation (approx), start there.
    # If first event is later, we have a gap. 
    # But let's assume events cover the changes.
    # And the `ownerid` on Case is the current one.
    
    # Actually, simpler approach for "processed":
    # Identify all owners who held the case during the window.
    # If no history: Owner is `c.ownerid`. Interval [Created, Closed/Now].
    # If history: 
    #   Segments defined by events.
    #   Last segment ends at Closed/Now.
    
    segments = []
    
    if not events:
        # No transfers
        segments.append({'owner': initial_owner, 'start': created_date, 'end': closed_date})
    else:
        # Has history
        # Check if first event matches creation
        # If not, we have an unknown initial owner or the first event is the initial.
        # Let's assume the first event IS the initial assignment if it's close to creation.
        # If not, we miss the first owner.
        # But we can try to guess? No, sticking to data.
        
        # Actually, if `oldvalue` is None, it's likely initial.
        
        last_time = created_date
        current_owner = None 
        
        # If first event has oldvalue=None, it sets the owner starting at event time.
        # If event time == created time, good.
        # If event time > created time, who was owner in between?
        # Maybe the `created by`?
        # Let's ignore the gap for now and process the events.
        
        for e in events:
            time = e['date']
            new_owner = e['owner']
            
            # If we had a current owner, they owned it from last_time to time.
            if current_owner:
                segments.append({'owner': current_owner, 'start': last_time, 'end': time})
            
            # Update
            current_owner = new_owner
            last_time = time
            
        # After last event, current_owner owns it until closed/now
        if current_owner:
            segments.append({'owner': current_owner, 'start': last_time, 'end': closed_date})
    
    # Now check intersection with window
    owners_in_window = set()
    for seg in segments:
        owner = seg['owner']
        start = seg['start']
        end = seg['end'] # None means open
        
        # Interval [start, end]
        # Overlap [w_start, w_end]
        # Logic: Start < w_end AND (End is None OR End > w_start)
        
        is_overlap = False
        if start < window_end:
            if end is None:
                is_overlap = True # Open case starts before window end
            elif end > window_start:
                is_overlap = True
        
        if is_overlap:
            owners_in_window.add(owner)
            
    for o in owners_in_window:
        if o not in agent_processed_in_window:
            agent_processed_in_window[o] = set()
        agent_processed_in_window[o].add(cid)
        
    # Handle Time Calculation
    # Only if Closed in Window
    if closed_date and window_start <= closed_date <= window_end:
        # Final owner
        # If transferred, previous don't get time.
        # Final owner is the one in the last segment (or `c.ownerid`).
        # Check if transferred (more than 1 owner in history? or just > 1 segment?)
        # "do not compute handle time for cases that have been transferred to other agents"
        # If > 1 segment with DIFFERENT owners.
        
        # Get unique owners in segments (lifetime)
        unique_owners = set(s['owner'] for s in segments)
        
        # If multiple owners -> Transferred.
        # Then only final owner gets time?
        # "do not compute handle time for cases that have been transferred to other agents" -> The agents who transferred it don't get time.
        # The final agent (who closed it) didn't transfer it. So they get time.
        # This assumes the rule applies per-agent.
        
        final_owner = clean_id(c.get('ownerid'))
        
        # Time
        duration = (closed_date - created_date).total_seconds()
        
        if final_owner not in agent_handle_times:
            agent_handle_times[final_owner] = []
        agent_handle_times[final_owner].append(duration)

# Results
results = []
for agent in agent_processed_in_window:
    count = len(agent_processed_in_window[agent])
    if count > 1:
        # Check handle time
        times = agent_handle_times.get(agent, [])
        if times:
            avg_time = sum(times) / len(times)
            results.append({'agent': agent, 'avg_time': avg_time, 'count': count})

results.sort(key=lambda x: x['avg_time'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-9942462505138529069': [{'id': '500Wt00000DDepmIAD', 'priority': 'Medium', 'subject': 'Update Alerts Missing', 'description': "I am not receiving consistent notifications about feature updates, which causes us to miss out on the CloudLink Designer's full capabilities.", 'status': 'Closed', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'orderitemid__c': '802Wt000007906kIAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDyzpIAD', 'priority': 'High', 'subject': 'Tailoring Problem', 'description': 'The AI Cirku-Tech tool is not flexible enough for specific customizations required by our unique projects.', 'status': 'Closed', 'contactid': '#003Wt00000Jqt79IAB', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'orderitemid__c': '802Wt00000798NMIAY', 'issueid__c': 'a03Wt00000JqmX6IAJ', 'accountid': '001Wt00000PHViZIAX', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDzUPIA1', 'priority': 'Medium', 'subject': 'AI Features Unreliable', 'description': 'The AI functionalities of the CollabCircuit Hub are not consistently working, leading to decreased productivity and dissatisfaction among our team members.', 'status': 'Closed', 'contactid': '003Wt00000Jquw2IAB', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'orderitemid__c': '802Wt00000797CjIAI', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '001Wt00000PHVfJIAX', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzsbIAD', 'priority': 'High', 'subject': 'Scalability Problem', 'description': 'I am encountering difficulties in scaling TechPulse solutions to meet the increasing demands of our enterprise which is impacting our expansion efforts.', 'status': 'Closed', 'contactid': '003Wt00000JqviSIAR', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'orderitemid__c': '802Wt00000798YdIAI', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '#001Wt00000PGovMIAT', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'priority': 'High', 'subject': 'Scaling Issues with OptiPower', 'description': 'I face challenges in scaling the OptiPower Manager to accommodate increasing demands for our projects.', 'status': 'Closed', 'contactid': '#003Wt00000JqxfNIAR', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'orderitemid__c': '802Wt00000796qDIAQ', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '001Wt00000PFsmcIAD', 'ownerid': '005Wt000003NEtOIAW'}], 'var_function-call-16399685360638173134': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_function-call-1831095406268104650': [{'count': '7'}], 'var_function-call-10695664970778867569': [{'count': '33'}], 'var_function-call-3419309582017879422': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'newvalue__c': '005Wt000003NJufIAG', 'assignment_date': '2023-07-01T10:30:00.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'newvalue__c': '005Wt000003NDqDIAW', 'assignment_date': '2023-05-10T14:45:00.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'newvalue__c': '005Wt000003NJJaIAO', 'assignment_date': '2023-06-02T09:30:00.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'newvalue__c': '005Wt000003NJGLIA4', 'assignment_date': '2023-08-15T14:30:00.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'newvalue__c': '005Wt000003NJD9IAO', 'assignment_date': '2023-06-30T13:03:00.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'newvalue__c': 'None', 'assignment_date': 'None'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'newvalue__c': 'None', 'assignment_date': 'None'}], 'var_function-call-12446716404083854311': [{'id': 'a04Wt00000537msIAA', 'caseid__c': '500Wt00000DE02HIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-03T14:45:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000537zmIAA', 'caseid__c': '500Wt00000DE02HIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-03T15:21:34.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000539BxIAI', 'caseid__c': '500Wt00000DE02HIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-11214778995977530316': [{'id': 'a04Wt00000532s4IAA', 'caseid__c': '500Wt00000DDzscIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000537LUIAY', 'caseid__c': '500Wt00000DDepmIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000537baIAA', 'caseid__c': '500Wt00000DDzUPIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000538hMIAQ', 'caseid__c': '500Wt00000DDzuEIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000538r0IAA', 'caseid__c': '500Wt00000DDyzpIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000538scIAA', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000539BxIAI', 'caseid__c': '500Wt00000DE02HIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-14666509999231107248': [{'caseid__c': '500Wt00000DDz6FIAT', 'cnt': '2'}, {'caseid__c': '500Wt00000DDflsIAD', 'cnt': '2'}, {'caseid__c': '500Wt00000DDDfwIAH', 'cnt': '2'}, {'caseid__c': '500Wt00000DDzW3IAL', 'cnt': '2'}, {'caseid__c': '500Wt00000DDfvXIAT', 'cnt': '2'}, {'caseid__c': '500Wt00000DDYpGIAX', 'cnt': '2'}, {'caseid__c': '500Wt00000DE0YXIA1', 'cnt': '2'}, {'caseid__c': '500Wt00000DDZtLIAX', 'cnt': '2'}, {'caseid__c': '500Wt00000DDzRCIA1', 'cnt': '2'}, {'caseid__c': '500Wt00000DDnt7IAD', 'cnt': '2'}, {'caseid__c': '500Wt00000DDzSnIAL', 'cnt': '2'}, {'caseid__c': '500Wt00000DDTERIA5', 'cnt': '2'}], 'var_function-call-7995095031378652022': [{'count': '153'}], 'var_function-call-3119883133918778239': 'file_storage/function-call-3119883133918778239.json', 'var_function-call-18131444671333490707': 'file_storage/function-call-18131444671333490707.json', 'var_function-call-5642097747574217868': [], 'var_function-call-7420334025887168728': [{'agent': '005Wt000003NDqDIAW', 'avg_time': 882.0, 'count': 3}, {'agent': '005Wt000003NEtOIAW', 'avg_time': 1007.0, 'count': 2}, {'agent': '005Wt000003NJGLIA4', 'avg_time': 1442.0, 'count': 2}, {'agent': '005Wt000003NIddIAG', 'avg_time': 2194.0, 'count': 4}, {'agent': '005Wt000003NJJaIAO', 'avg_time': 14712.0, 'count': 4}, {'agent': '005Wt000003NJD9IAO', 'avg_time': 21608.0, 'count': 2}, {'agent': '005Wt000003NJufIAG', 'avg_time': 33068.0, 'count': 2}]}

exec(code, env_args)
