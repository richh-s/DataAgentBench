code = """import json
import re
transcripts = var_call_VSzYzpGegxtwkhZhYTTzdvqA
articles_path = var_call_NMfSLBRvKsbtG5LezXnCaVLc
with open(articles_path, 'r', encoding='utf-8') as f:
    articles = json.load(f)

full_transcript = '\n'.join([t.get('Body__c','') for t in transcripts])
full_lower = full_transcript.lower()

# Determine Budget
budget_ok = False
m_budget = re.search(r'budget\s+is\s+\$?\s*([0-9][0-9,\.]*)', full_lower)
if m_budget:
    try:
        budget_amount = float(m_budget.group(1).replace(',', ''))
    except:
        budget_amount = None
else:
    budget_amount = None
m_price = re.search(r'priced\s+at\s+\$?\s*([0-9][0-9,\.]*)', full_lower)
if m_price:
    try:
        unit_price = float(m_price.group(1).replace(',', ''))
    except:
        unit_price = None
else:
    unit_price = None
m_qty = re.search(r'\b(\d+)\b\s+units', full_lower)
if m_qty:
    try:
        quantity = int(m_qty.group(1))
    except:
        quantity = None
else:
    quantity = None

if budget_amount is not None and unit_price is not None and quantity is not None:
    total_price = unit_price * quantity
    budget_ok = (budget_amount >= total_price)
else:
    if 'fits really well' in full_lower or 'that fits really well' in full_lower:
        budget_ok = True

# Determine Authority
authority_ok = True
if "don't have the final say" in full_lower or 'dont have the final say' in full_lower or 'need to consult with' in full_lower or 'consult with the finance team' in full_lower or "i'll need to consult" in full_lower or "i\'ll need to consult" in full_lower:
    authority_ok = False

# Determine Need
need_ok = False
if 'interested' in full_lower or 'we want to' in full_lower or 'we want to enhance' in full_lower:
    need_ok = True

# Determine Timeline
timeline_ok = True
if 'tight timeline' in full_lower or 'tight timeline for installation' in full_lower or 'tight timeline for installation' in full_lower:
    timelines = []
    for a in articles:
        txt = (a.get('faq_answer__c') or '') + ' ' + (a.get('summary') or '') + ' ' + (a.get('title') or '')
        for m in re.finditer(r'(\b\d+)\s+days?', txt.lower()):
            try:
                timelines.append(int(m.group(1)))
            except:
                pass
        if 'single day' in txt.lower() or 'within a day' in txt.lower() or 'complete installations within a day' in txt.lower():
            timelines.append(1)
    if len(timelines) == 0:
        if 'we usually aim to complete installations within a day' in full_lower:
            timeline_ok = True
        else:
            timeline_ok = False
    else:
        timeline_ok = any(t <= 3 for t in timelines)

# Compile failing
failing = []
if not budget_ok:
    failing.append('Budget')
if not authority_ok:
    failing.append('Authority')
if not need_ok:
    failing.append('Need')
if not timeline_ok:
    failing.append('Timeline')

print('__RESULT__:')
print(json.dumps(failing))"""

env_args = {'var_call_eVtmQ7d39FBsZN1ngJ9T1l9O': [{'Id': 'a05Wt000003SukEIAS', 'OpportunityId__c': 'None', 'LeadId__c': '00QWt0000089AekMAE', 'Body__c': "[2023-10-21T10:02:00] Ava Sullivan: Hi Ali, this is Ava Sullivan from TechSolutions. How are you today?\n[2023-10-21T10:02:10] Ali Hussein: Hi Ava, I'm doing well, thank you. How about you?\n[2023-10-21T10:02:20] Ava Sullivan: I'm great, thank you for asking! I'm glad we could connect. I was looking over the details you provided about your interest in the PulseSim Pro. Is now a good time to discuss?\n[2023-10-21T10:02:30] Ali Hussein: Yes, now works for me. I'm interested to learn more and see how it fits with what we need.\n[2023-10-21T10:02:40] Ava Sullivan: Fantastic! From what you’ve mentioned, you’re interested in four units of the PulseSim Pro, correct?\n[2023-10-21T10:02:50] Ali Hussein: That's right. We want to enhance our simulation capabilities, and the PulseSim Pro seems like a great fit.\n[2023-10-21T10:03:05] Ava Sullivan: Absolutely. The PulseSim Pro is one of our top products for high precision simulation. It offers advanced analytics and seamless integration with existing systems, which is great for boosting efficiency.\n[2023-10-21T10:03:15] Ali Hussein: Those features sound beneficial. We do have a tight timeline for installation, though. Could you tell me more about that?\n[2023-10-21T10:03:30] Ava Sullivan: Certainly. We understand the importance of meeting tight schedules. We usually aim to complete installations within a day and ensure everything runs smoothly. Our technical team is very efficient.\n[2023-10-21T10:03:40] Ali Hussein: That’s reassuring. And as for the budget, how does it look for four units?\n[2023-10-21T10:03:55] Ava Sullivan: Considering your budget is $2,261, I think we can work something out. Each PulseSim Pro unit is priced at $500. For four units, it will come to $2,000. This is below your budget, leaving room for additional services if you wish.\n[2023-10-21T10:04:10] Ali Hussein: That fits really well. I'd like to move forward, but I'll need to consult with the finance team here since I don’t have the final say.\n[2023-10-21T10:04:20] Ava Sullivan: I completely understand, Ali. Would you like me to send over a detailed proposal and pricing information so you can present it to your team?\n[2023-10-21T10:04:25] Ali Hussein: Yes, please. That would be very helpful.\n[2023-10-21T10:04:35] Ava Sullivan: Great! I'll have that to you by the end of the day. Is there anything else you would need from my side?\n[2023-10-21T10:04:40] Ali Hussein: No, that sounds good for now. Thank you, Ava.\n[2023-10-21T10:04:50] Ava Sullivan: You're welcome, Ali. If any questions come up, feel free to reach out. Have a wonderful day!\n[2023-10-21T10:04:55] Ali Hussein: Thanks, Ava. You too!", 'CreatedDate': '2023-10-21T10:02:00.000+0000', 'EndTime__c': '2023-10-21'}], 'var_call_NMfSLBRvKsbtG5LezXnCaVLc': 'file_storage/call_NMfSLBRvKsbtG5LezXnCaVLc.json', 'var_call_VSzYzpGegxtwkhZhYTTzdvqA': [{'Id': 'a05Wt000003SukEIAS', 'OpportunityId__c': 'None', 'LeadId__c': '00QWt0000089AekMAE', 'Body__c': "[2023-10-21T10:02:00] Ava Sullivan: Hi Ali, this is Ava Sullivan from TechSolutions. How are you today?\n[2023-10-21T10:02:10] Ali Hussein: Hi Ava, I'm doing well, thank you. How about you?\n[2023-10-21T10:02:20] Ava Sullivan: I'm great, thank you for asking! I'm glad we could connect. I was looking over the details you provided about your interest in the PulseSim Pro. Is now a good time to discuss?\n[2023-10-21T10:02:30] Ali Hussein: Yes, now works for me. I'm interested to learn more and see how it fits with what we need.\n[2023-10-21T10:02:40] Ava Sullivan: Fantastic! From what you’ve mentioned, you’re interested in four units of the PulseSim Pro, correct?\n[2023-10-21T10:02:50] Ali Hussein: That's right. We want to enhance our simulation capabilities, and the PulseSim Pro seems like a great fit.\n[2023-10-21T10:03:05] Ava Sullivan: Absolutely. The PulseSim Pro is one of our top products for high precision simulation. It offers advanced analytics and seamless integration with existing systems, which is great for boosting efficiency.\n[2023-10-21T10:03:15] Ali Hussein: Those features sound beneficial. We do have a tight timeline for installation, though. Could you tell me more about that?\n[2023-10-21T10:03:30] Ava Sullivan: Certainly. We understand the importance of meeting tight schedules. We usually aim to complete installations within a day and ensure everything runs smoothly. Our technical team is very efficient.\n[2023-10-21T10:03:40] Ali Hussein: That’s reassuring. And as for the budget, how does it look for four units?\n[2023-10-21T10:03:55] Ava Sullivan: Considering your budget is $2,261, I think we can work something out. Each PulseSim Pro unit is priced at $500. For four units, it will come to $2,000. This is below your budget, leaving room for additional services if you wish.\n[2023-10-21T10:04:10] Ali Hussein: That fits really well. I'd like to move forward, but I'll need to consult with the finance team here since I don’t have the final say.\n[2023-10-21T10:04:20] Ava Sullivan: I completely understand, Ali. Would you like me to send over a detailed proposal and pricing information so you can present it to your team?\n[2023-10-21T10:04:25] Ali Hussein: Yes, please. That would be very helpful.\n[2023-10-21T10:04:35] Ava Sullivan: Great! I'll have that to you by the end of the day. Is there anything else you would need from my side?\n[2023-10-21T10:04:40] Ali Hussein: No, that sounds good for now. Thank you, Ava.\n[2023-10-21T10:04:50] Ava Sullivan: You're welcome, Ali. If any questions come up, feel free to reach out. Have a wonderful day!\n[2023-10-21T10:04:55] Ali Hussein: Thanks, Ava. You too!", 'CreatedDate': '2023-10-21T10:02:00.000+0000', 'EndTime__c': '2023-10-21'}]}

exec(code, env_args)
