code = """import json, re
# Load data from previous tool calls
transcripts = var_call_ODGYUt9koYO7Vl7PNzPWoR6Z
knowledge_path = var_call_fZKECSywC9N1ZiuAN1XuQJ4f
with open(knowledge_path, 'r') as f:
    knowledge_articles = json.load(f)

# Combine transcript bodies
transcript_text = '\n'.join([t.get('Body__c','') for t in transcripts])
transcript_lower = transcript_text.lower()

failed = []

# --- Budget ---
budget_ok = False
# Look for explicit budget like 'budget is $2,261' or phrases indicating budget fits
m = re.search(r'budget is \$?([0-9,]+(?:\.[0-9]{2})?)', transcript_lower)
budget_val = None
if m:
    try:
        budget_val = float(m.group(1).replace(',',''))
    except:
        budget_val = None

# Find quantity
qty = None
m_qty = re.search(r'(\b\d+\b)\s+units', transcript_lower)
if m_qty:
    qty = int(m_qty.group(1))
else:
    words = {'one':1,'two':2,'three':3,'four':4,'five':5,'fifteen':15,'twenty-five':25}
    for w,n in words.items():
        if f"{w} unit" in transcript_lower or f"{w} units" in transcript_lower:
            qty = n
            break

# Find unit price or total price
unit_price = None
m_up = re.search(r'priced at \$([0-9,]+(?:\.[0-9]{2})?)', transcript_text)
if m_up:
    unit_price = float(m_up.group(1).replace(',',''))
else:
    m_total = re.search(r'for (?:\w+ )?units, it will come to \$([0-9,]+(?:\.[0-9]{2})?)', transcript_text, re.IGNORECASE)
    if m_total and qty:
        total = float(m_total.group(1).replace(',',''))
        unit_price = total/qty

# Check textual budget acceptance
if 'below your budget' in transcript_lower or 'that fits really well' in transcript_lower or 'fits really well' in transcript_lower:
    budget_ok = True
elif budget_val is not None and unit_price is not None and qty is not None:
    total_cost = unit_price * qty
    if total_cost <= budget_val:
        budget_ok = True

if not budget_ok:
    failed.append('Budget')

# --- Authority ---
authority_issue = False
if "i don't have the final say" in transcript_lower or 'i will need to consult' in transcript_lower or 'consult with the finance team' in transcript_lower or 'need to consult with the finance team' in transcript_lower:
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
# Lead mentions tight timeline; check knowledge article for volume-based installation times
timeline_issue = False
if 'tight timeline' in transcript_lower or 'tight timeline for installation' in transcript_lower or 'tight timeline for' in transcript_lower:
    # try to find relevant policy days for the quantity
    policy_days = None
    faqs = '\n'.join([(a.get('faq_answer__c') or '').lower() for a in knowledge_articles])
    # Look for 'small batch purchase (volume: 5)' and associated days
    m_policy = re.search(r'small batch purchase \(volume:\s*5\).*?(\d+) days', faqs)
    if m_policy:
        policy_days = int(m_policy.group(1))
    # If qty exists and policy_days exists and policy_days > 1, and lead expects faster, mark issue
    if qty is not None and policy_days is not None:
        # sales rep claimed installations within a day earlier
        if policy_days > 1:
            timeline_issue = True
    else:
        # If we can't determine exact policy but lead explicitly mentioned tight timeline, mark as potential issue
        timeline_issue = True

if timeline_issue:
    failed.append('Timeline')

# Order results as requested
order = ['Budget','Authority','Need','Timeline']
failed_ordered = [f for f in order if f in failed]

print('__RESULT__:')
print(json.dumps(failed_ordered))"""

env_args = {'var_call_ODGYUt9koYO7Vl7PNzPWoR6Z': [{'Id': 'a05Wt000003SukEIAS', 'OpportunityId__c': 'None', 'LeadId__c': '00QWt0000089AekMAE', 'Body__c': "[2023-10-21T10:02:00] Ava Sullivan: Hi Ali, this is Ava Sullivan from TechSolutions. How are you today?\n[2023-10-21T10:02:10] Ali Hussein: Hi Ava, I'm doing well, thank you. How about you?\n[2023-10-21T10:02:20] Ava Sullivan: I'm great, thank you for asking! I'm glad we could connect. I was looking over the details you provided about your interest in the PulseSim Pro. Is now a good time to discuss?\n[2023-10-21T10:02:30] Ali Hussein: Yes, now works for me. I'm interested to learn more and see how it fits with what we need.\n[2023-10-21T10:02:40] Ava Sullivan: Fantastic! From what you’ve mentioned, you’re interested in four units of the PulseSim Pro, correct?\n[2023-10-21T10:02:50] Ali Hussein: That's right. We want to enhance our simulation capabilities, and the PulseSim Pro seems like a great fit.\n[2023-10-21T10:03:05] Ava Sullivan: Absolutely. The PulseSim Pro is one of our top products for high precision simulation. It offers advanced analytics and seamless integration with existing systems, which is great for boosting efficiency.\n[2023-10-21T10:03:15] Ali Hussein: Those features sound beneficial. We do have a tight timeline for installation, though. Could you tell me more about that?\n[2023-10-21T10:03:30] Ava Sullivan: Certainly. We understand the importance of meeting tight schedules. We usually aim to complete installations within a day and ensure everything runs smoothly. Our technical team is very efficient.\n[2023-10-21T10:03:40] Ali Hussein: That’s reassuring. And as for the budget, how does it look for four units?\n[2023-10-21T10:03:55] Ava Sullivan: Considering your budget is $2,261, I think we can work something out. Each PulseSim Pro unit is priced at $500. For four units, it will come to $2,000. This is below your budget, leaving room for additional services if you wish.\n[2023-10-21T10:04:10] Ali Hussein: That fits really well. I'd like to move forward, but I'll need to consult with the finance team here since I don’t have the final say.\n[2023-10-21T10:04:20] Ava Sullivan: I completely understand, Ali. Would you like me to send over a detailed proposal and pricing information so you can present it to your team?\n[2023-10-21T10:04:25] Ali Hussein: Yes, please. That would be very helpful.\n[2023-10-21T10:04:35] Ava Sullivan: Great! I'll have that to you by the end of the day. Is there anything else you would need from my side?\n[2023-10-21T10:04:40] Ali Hussein: No, that sounds good for now. Thank you, Ava.\n[2023-10-21T10:04:50] Ava Sullivan: You're welcome, Ali. If any questions come up, feel free to reach out. Have a wonderful day!\n[2023-10-21T10:04:55] Ali Hussein: Thanks, Ava. You too!", 'CreatedDate': '2023-10-21T10:02:00.000+0000', 'EndTime__c': '2023-10-21'}], 'var_call_fZKECSywC9N1ZiuAN1XuQJ4f': 'file_storage/call_fZKECSywC9N1ZiuAN1XuQJ4f.json'}

exec(code, env_args)
