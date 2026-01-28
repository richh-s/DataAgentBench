code = """import json, re
# Accessing previous tool results
lead = var_call_kowvVNelk985hMJPEwr2c9AV[0] if isinstance(var_call_kowvVNelk985hMJPEwr2c9AV, list) and len(var_call_kowvVNelk985hMJPEwr2c9AV)>0 else {}
transcripts = var_call_BBy7hTIn9Cjqlc0xP4U8xLju
# Load knowledge articles from the provided JSON file path
import os
articles = []
if isinstance(var_call_wSDOTDK2lf0vtqgMrn6w0Cle, str) and os.path.exists(var_call_wSDOTDK2lf0vtqgMrn6w0Cle):
    with open(var_call_wSDOTDK2lf0vtqgMrn6w0Cle, 'r', encoding='utf-8') as f:
        articles = json.load(f)

# Combine transcript bodies for the lead
body = ''
if isinstance(transcripts, list) and len(transcripts)>0:
    # take the latest by CreatedDate if available
    try:
        transcripts_sorted = sorted(transcripts, key=lambda x: x.get('CreatedDate',''))
    except Exception:
        transcripts_sorted = transcripts
    body = '\n'.join([t.get('Body__c','') for t in transcripts_sorted])
else:
    body = ''

text = body.lower()

# Initialize BANT flags as unknown
budget_ok = None
authority_ok = None
need_ok = None
timeline_ok = None

# Budget: look for 'budget' mentions and dollar amounts and positive confirmation
if 'budget' in text:
    budget_ok = False
    # find sentences around 'budget'
    sents = re.split(r'[\n\.]', body)
    for s in sents:
        if 'budget' in s.lower():
            if any(word in s.lower() for word in ['fits', 'fit', 'works', 'ok', 'okay', 'i\'d like to move forward', 'that fits really well', 'that fits']):
                budget_ok = True
                break
    # also check for explicit pricing below budget
    dollar_vals = re.findall(r'\$[\d,]+', body)
    if dollar_vals:
        # parse amounts
        amounts = [int(re.sub(r'[\$,]', '', d)) for d in dollar_vals]
        # if two amounts present and one labeled budget, assume budget >= price
        if len(amounts) >= 2 and 'budget' in text:
            # crude heuristic: if any amount equals 2261 or higher than others
            if max(amounts) >= min(amounts):
                budget_ok = True

# If no mention of budget, set unknown->False (fail)
if budget_ok is None:
    budget_ok = False

# Authority: look for phrases indicating lack of decision power
if any(kw in text for kw in ['i don\'t have the final say', 'i don\'t have the final', 'need to consult', 'consult with', 'get approval', 'finance team', 'approve']):
    authority_ok = False
else:
    # look for affirmative authority statements
    if any(kw in text for kw in ['i will approve', 'i can approve', 'i have authority', 'i have the final say', 'i am the decision maker']):
        authority_ok = True
    else:
        authority_ok = True  # default to true if no negative phrasing

# Need: check for explicit interest and fit
if any(kw in text for kw in ['interested', 'want', 'need', 'fits with', 'fit with', 'great fit', 'enhance our simulation', 'enhance our simulation capabilities']):
    need_ok = True
else:
    need_ok = False

# Timeline: check for 'timeline' and installation statements
if 'timeline' in text or 'installation' in text or 'install' in text:
    # if vendor offers quick install and lead doesn't object, timeline ok
    if any(kw in text for kw in ['complete installations within a day', 'installations within a day', 'within a day', 'we usually aim to complete installations within a day', 'we can complete']):
        timeline_ok = True
    else:
        # if lead says 'tight timeline' but vendor didn't confirm, mark unclear->False
        if 'tight timeline' in text or 'tight timeline for installation' in text:
            # but in transcript vendor did confirm next line, so conservatively set True if both present
            if any(kw in text for kw in ['complete installations within a day','within a day']):
                timeline_ok = True
            else:
                timeline_ok = False
        else:
            timeline_ok = True
else:
    timeline_ok = True

# Based on extracted flags, determine which BANT factors fail
failures = []
if not budget_ok:
    failures.append('Budget')
if not authority_ok:
    failures.append('Authority')
if not need_ok:
    failures.append('Need')
if not timeline_ok:
    failures.append('Timeline')

# However, override based on strong evidence in transcript: specifically detect exact phrases
# Recompute authority accurately from transcript
if 'i don\'t have the final say' in text or 'i will need to consult with the finance team' in text or 'consult with the finance team' in text:
    # ensure Authority is marked failed
    if 'Authority' not in failures:
        failures.append('Authority')
    # If budget was explicitly confirmed in the transcript, remove it from failures
    if 'budget is' in text or 'that fits really well' in text:
        if 'Budget' in failures:
            failures.remove('Budget')

# Final cleanup: if no failures, return empty list
result = failures

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_kowvVNelk985hMJPEwr2c9AV': [{'Id': '00QWt0000089AekMAE', 'FirstName': 'Ali', 'LastName': 'Hussein', 'Email': 'ali.hussein@baghdadhtechhub.com', 'Phone': '555-452-7654', 'Company': 'Baghdad Tech Hub', 'Status': 'Converted', 'ConvertedContactId': 'None', 'ConvertedAccountId': 'None', 'Title': 'Head of Emerging Technologies', 'CreatedDate': '2023-08-18T15:35:50.000+0000', 'ConvertedDate': 'None', 'IsConverted': '0', 'OwnerId': '005Wt000003NErnIAG'}], 'var_call_BBy7hTIn9Cjqlc0xP4U8xLju': [{'Id': 'a05Wt000003SukEIAS', 'OpportunityId__c': 'None', 'LeadId__c': '00QWt0000089AekMAE', 'Body__c': "[2023-10-21T10:02:00] Ava Sullivan: Hi Ali, this is Ava Sullivan from TechSolutions. How are you today?\n[2023-10-21T10:02:10] Ali Hussein: Hi Ava, I'm doing well, thank you. How about you?\n[2023-10-21T10:02:20] Ava Sullivan: I'm great, thank you for asking! I'm glad we could connect. I was looking over the details you provided about your interest in the PulseSim Pro. Is now a good time to discuss?\n[2023-10-21T10:02:30] Ali Hussein: Yes, now works for me. I'm interested to learn more and see how it fits with what we need.\n[2023-10-21T10:02:40] Ava Sullivan: Fantastic! From what you’ve mentioned, you’re interested in four units of the PulseSim Pro, correct?\n[2023-10-21T10:02:50] Ali Hussein: That's right. We want to enhance our simulation capabilities, and the PulseSim Pro seems like a great fit.\n[2023-10-21T10:03:05] Ava Sullivan: Absolutely. The PulseSim Pro is one of our top products for high precision simulation. It offers advanced analytics and seamless integration with existing systems, which is great for boosting efficiency.\n[2023-10-21T10:03:15] Ali Hussein: Those features sound beneficial. We do have a tight timeline for installation, though. Could you tell me more about that?\n[2023-10-21T10:03:30] Ava Sullivan: Certainly. We understand the importance of meeting tight schedules. We usually aim to complete installations within a day and ensure everything runs smoothly. Our technical team is very efficient.\n[2023-10-21T10:03:40] Ali Hussein: That’s reassuring. And as for the budget, how does it look for four units?\n[2023-10-21T10:03:55] Ava Sullivan: Considering your budget is $2,261, I think we can work something out. Each PulseSim Pro unit is priced at $500. For four units, it will come to $2,000. This is below your budget, leaving room for additional services if you wish.\n[2023-10-21T10:04:10] Ali Hussein: That fits really well. I'd like to move forward, but I'll need to consult with the finance team here since I don’t have the final say.\n[2023-10-21T10:04:20] Ava Sullivan: I completely understand, Ali. Would you like me to send over a detailed proposal and pricing information so you can present it to your team?\n[2023-10-21T10:04:25] Ali Hussein: Yes, please. That would be very helpful.\n[2023-10-21T10:04:35] Ava Sullivan: Great! I'll have that to you by the end of the day. Is there anything else you would need from my side?\n[2023-10-21T10:04:40] Ali Hussein: No, that sounds good for now. Thank you, Ava.\n[2023-10-21T10:04:50] Ava Sullivan: You're welcome, Ali. If any questions come up, feel free to reach out. Have a wonderful day!\n[2023-10-21T10:04:55] Ali Hussein: Thanks, Ava. You too!", 'CreatedDate': '2023-10-21T10:02:00.000+0000', 'EndTime__c': '2023-10-21'}], 'var_call_wSDOTDK2lf0vtqgMrn6w0Cle': 'file_storage/call_wSDOTDK2lf0vtqgMrn6w0Cle.json'}

exec(code, env_args)
