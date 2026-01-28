code = """import json
# Load previous results
transcripts = var_call_ODGYUt9koYO7Vl7PNzPWoR6Z
knowledge_path = var_call_fZKECSywC9N1ZiuAN1XuQJ4f
with open(knowledge_path, 'r') as f:
    knowledge_articles = json.load(f)

# Combine transcript
transcript_text = '\n'.join([t.get('Body__c','') for t in transcripts])
transcript_lower = transcript_text.lower()

failed = []

# --- Budget ---
budget_ok = False
budget_val = None
if 'budget is $' in transcript_lower:
    idx = transcript_lower.find('budget is $') + len('budget is $')
    # capture numbers following
    num_chars = ''
    for ch in transcript_lower[idx:idx+20]:
        if ch.isdigit() or ch==',' or ch=='.':
            num_chars += ch
        else:
            break
    try:
        budget_val = float(num_chars.replace(',',''))
    except:
        budget_val = None

# find quantity
qty = None
# look for digits like '4 units'
parts = transcript_lower.split()
for i,p in enumerate(parts[:-1]):
    if parts[i+1].startswith('unit') or parts[i+1].startswith('units'):
        # try parse p
        try:
            qty = int(p)
            break
        except:
            # word numbers
            words = {'one':1,'two':2,'three':3,'four':4,'five':5,'fifteen':15,'twenty-five':25}
            if p in words:
                qty = words[p]
                break

# find unit price by looking for '$' followed by numbers and context 'priced at' or 'each'
unit_price = None
if 'priced at $' in transcript_text:
    i = transcript_text.find('priced at $') + len('priced at $')
    s=''
    for ch in transcript_text[i:i+20]:
        if ch.isdigit() or ch==',' or ch=='.':
            s+=ch
        else:
            break
    try:
        unit_price = float(s.replace(',',''))
    except:
        unit_price = None
else:
    # look for patterns like '$500' and 'each' nearby
    idx = transcript_text.find('$')
    if idx!=-1:
        # take first $ number
        s=''
        for ch in transcript_text[idx+1:idx+10]:
            if ch.isdigit() or ch==',' or ch=='.':
                s+=ch
            else:
                break
        try:
            unit_price = float(s.replace(',',''))
        except:
            unit_price = None

# textual acceptance
if 'below your budget' in transcript_lower or 'fits really well' in transcript_lower or "that fits really well" in transcript_lower:
    budget_ok = True
elif budget_val is not None and unit_price is not None and qty is not None:
    total_cost = unit_price * qty
    if total_cost <= budget_val:
        budget_ok = True

if not budget_ok:
    failed.append('Budget')

# --- Authority ---
authority_issue = False
if "i don't have the final say" in transcript_lower or 'consult with the finance team' in transcript_lower or 'i will need to consult' in transcript_lower or 'need to consult with the finance team' in transcript_lower:
    authority_issue = True
if authority_issue:
    failed.append('Authority')

# --- Need ---
need_issue = False
if "i'm interested" in transcript_lower or 'we want to enhance' in transcript_lower or "i'd like to move forward" in transcript_lower or 'we want to' in transcript_lower:
    need_issue = False
else:
    need_issue = True
if need_issue:
    failed.append('Need')

# --- Timeline ---
# If lead mentions tight timeline, and knowledge articles indicate installation for qty may take >1 day, mark issue
timeline_issue = False
if 'tight timeline' in transcript_lower or 'tight timeline for installation' in transcript_lower or 'tight timeline for' in transcript_lower:
    # search knowledge articles text for small batch days
    faqs = '\n'.join([(a.get('faq_answer__c') or '').lower() for a in knowledge_articles])
    # look for 'small batch purchase' and number of days
    policy_days = None
    if 'small batch purchase' in faqs and '3 days' in faqs:
        policy_days = 3
    # salesperson claimed 1 day installation earlier in transcript
    # if policy_days >1 and lead needs tight timeline, it's an issue
    if qty is not None and policy_days is not None and policy_days>1:
        timeline_issue = True
    else:
        # can't confirm policy but lead said tight timeline -> mark as issue to be safe
        timeline_issue = True

if timeline_issue:
    failed.append('Timeline')

# order
order = ['Budget','Authority','Need','Timeline']
failed_ordered = [f for f in order if f in failed]

print('__RESULT__:')
print(json.dumps(failed_ordered))"""

env_args = {'var_call_ODGYUt9koYO7Vl7PNzPWoR6Z': [{'Id': 'a05Wt000003SukEIAS', 'OpportunityId__c': 'None', 'LeadId__c': '00QWt0000089AekMAE', 'Body__c': "[2023-10-21T10:02:00] Ava Sullivan: Hi Ali, this is Ava Sullivan from TechSolutions. How are you today?\n[2023-10-21T10:02:10] Ali Hussein: Hi Ava, I'm doing well, thank you. How about you?\n[2023-10-21T10:02:20] Ava Sullivan: I'm great, thank you for asking! I'm glad we could connect. I was looking over the details you provided about your interest in the PulseSim Pro. Is now a good time to discuss?\n[2023-10-21T10:02:30] Ali Hussein: Yes, now works for me. I'm interested to learn more and see how it fits with what we need.\n[2023-10-21T10:02:40] Ava Sullivan: Fantastic! From what you’ve mentioned, you’re interested in four units of the PulseSim Pro, correct?\n[2023-10-21T10:02:50] Ali Hussein: That's right. We want to enhance our simulation capabilities, and the PulseSim Pro seems like a great fit.\n[2023-10-21T10:03:05] Ava Sullivan: Absolutely. The PulseSim Pro is one of our top products for high precision simulation. It offers advanced analytics and seamless integration with existing systems, which is great for boosting efficiency.\n[2023-10-21T10:03:15] Ali Hussein: Those features sound beneficial. We do have a tight timeline for installation, though. Could you tell me more about that?\n[2023-10-21T10:03:30] Ava Sullivan: Certainly. We understand the importance of meeting tight schedules. We usually aim to complete installations within a day and ensure everything runs smoothly. Our technical team is very efficient.\n[2023-10-21T10:03:40] Ali Hussein: That’s reassuring. And as for the budget, how does it look for four units?\n[2023-10-21T10:03:55] Ava Sullivan: Considering your budget is $2,261, I think we can work something out. Each PulseSim Pro unit is priced at $500. For four units, it will come to $2,000. This is below your budget, leaving room for additional services if you wish.\n[2023-10-21T10:04:10] Ali Hussein: That fits really well. I'd like to move forward, but I'll need to consult with the finance team here since I don’t have the final say.\n[2023-10-21T10:04:20] Ava Sullivan: I completely understand, Ali. Would you like me to send over a detailed proposal and pricing information so you can present it to your team?\n[2023-10-21T10:04:25] Ali Hussein: Yes, please. That would be very helpful.\n[2023-10-21T10:04:35] Ava Sullivan: Great! I'll have that to you by the end of the day. Is there anything else you would need from my side?\n[2023-10-21T10:04:40] Ali Hussein: No, that sounds good for now. Thank you, Ava.\n[2023-10-21T10:04:50] Ava Sullivan: You're welcome, Ali. If any questions come up, feel free to reach out. Have a wonderful day!\n[2023-10-21T10:04:55] Ali Hussein: Thanks, Ava. You too!", 'CreatedDate': '2023-10-21T10:02:00.000+0000', 'EndTime__c': '2023-10-21'}], 'var_call_fZKECSywC9N1ZiuAN1XuQJ4f': 'file_storage/call_fZKECSywC9N1ZiuAN1XuQJ4f.json'}

exec(code, env_args)
