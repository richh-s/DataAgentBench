code = """import json
# Load stored tool results
transcripts = var_call_xjq2cIkiXaBPPa2NrlCded7x
knowledge_filepath = var_call_TACd1elz3myK62mTpgn4LmSg
with open(knowledge_filepath, 'r', encoding='utf-8') as f:
    knowledge = json.load(f)

# Combine transcript bodies for the lead
body_text = "\n".join([t.get('Body__c','') for t in transcripts])
body_lower = body_text.lower()

failed = []

# Need: check for keywords
need_keywords = ["interested", "want to", "want", "need", "enhance", "looking to", "interested to"]
need = any(k in body_lower for k in need_keywords)

# Budget: find dollar amounts by scanning for '$'
dollars = []
for i in range(len(body_text)):
    if body_text[i] == '$':
        # capture following characters up to space or punctuation
        j = i+1
        num_str = ''
        while j < len(body_text) and (body_text[j].isdigit() or body_text[j] in ',.'):
            num_str += body_text[j]
            j += 1
        if num_str:
            try:
                dollars.append(float(num_str.replace(',','')))
            except:
                pass

budget = None
unit_price = None
if dollars:
    budget = max(dollars)
    if len(dollars) >= 2:
        # assume the smaller is unit price
        unit_price = min(dollars)

# Quantity: look for digits followed by 'units' or word 'four units'
quantity = None
if '4 units' in body_lower:
    quantity = 4
elif 'four units' in body_lower:
    quantity = 4
else:
    # look for pattern like 'four' or '5 units'
    for token in body_lower.split():
        if token.isdigit():
            # check next token
            parts = body_lower.split()
            for idx, t in enumerate(parts):
                if t.isdigit():
                    if idx+1 < len(parts) and parts[idx+1].startswith('unit'):
                        quantity = int(t)
                        break
            if quantity is not None:
                break

budget_ok = False
if budget is not None and unit_price is not None and quantity is not None:
    total = unit_price * quantity
    budget_ok = (budget >= total)

# Authority: check phrases indicating lack of decision
authority = True
authority_phrases = ["don't have the final say", "dont have the final say", "i don't have the final say", "consult with the finance", "consult with the finance team", "need to consult", "will need to consult", "need approval", "need to consult with"]
for phrase in authority_phrases:
    if phrase in body_lower:
        authority = False
        break

# Timeline: check if lead mentions tight timeline and whether policy can meet it
timeline_issue = False
if 'tight timeline' in body_lower or 'timeline' in body_lower:
    # check for urgency phrases
    urgent_phrases = ['within a day', 'by tomorrow', 'asap', 'urgent', 'end of the day', 'today']
    urgent = any(p in body_lower for p in urgent_phrases)
    # estimate timeline from quantity
    est_timeline = None
    if quantity is not None:
        if quantity == 1:
            est_timeline = 1
        elif quantity <= 5:
            est_timeline = 3
        elif quantity <= 15:
            est_timeline = 7
        else:
            est_timeline = 14
    if urgent and est_timeline is not None and est_timeline > 1:
        timeline_issue = True

# Determine failures
if not need:
    failed.append('Need')
if not budget_ok:
    failed.append('Budget')
if not authority:
    failed.append('Authority')
if timeline_issue:
    failed.append('Timeline')

print("__RESULT__:")
print(json.dumps(failed))"""

env_args = {'var_call_xjq2cIkiXaBPPa2NrlCded7x': [{'Id': 'a05Wt000003SukEIAS', 'OpportunityId__c': 'None', 'LeadId__c': '00QWt0000089AekMAE', 'Body__c': "[2023-10-21T10:02:00] Ava Sullivan: Hi Ali, this is Ava Sullivan from TechSolutions. How are you today?\n[2023-10-21T10:02:10] Ali Hussein: Hi Ava, I'm doing well, thank you. How about you?\n[2023-10-21T10:02:20] Ava Sullivan: I'm great, thank you for asking! I'm glad we could connect. I was looking over the details you provided about your interest in the PulseSim Pro. Is now a good time to discuss?\n[2023-10-21T10:02:30] Ali Hussein: Yes, now works for me. I'm interested to learn more and see how it fits with what we need.\n[2023-10-21T10:02:40] Ava Sullivan: Fantastic! From what you’ve mentioned, you’re interested in four units of the PulseSim Pro, correct?\n[2023-10-21T10:02:50] Ali Hussein: That's right. We want to enhance our simulation capabilities, and the PulseSim Pro seems like a great fit.\n[2023-10-21T10:03:05] Ava Sullivan: Absolutely. The PulseSim Pro is one of our top products for high precision simulation. It offers advanced analytics and seamless integration with existing systems, which is great for boosting efficiency.\n[2023-10-21T10:03:15] Ali Hussein: Those features sound beneficial. We do have a tight timeline for installation, though. Could you tell me more about that?\n[2023-10-21T10:03:30] Ava Sullivan: Certainly. We understand the importance of meeting tight schedules. We usually aim to complete installations within a day and ensure everything runs smoothly. Our technical team is very efficient.\n[2023-10-21T10:03:40] Ali Hussein: That’s reassuring. And as for the budget, how does it look for four units?\n[2023-10-21T10:03:55] Ava Sullivan: Considering your budget is $2,261, I think we can work something out. Each PulseSim Pro unit is priced at $500. For four units, it will come to $2,000. This is below your budget, leaving room for additional services if you wish.\n[2023-10-21T10:04:10] Ali Hussein: That fits really well. I'd like to move forward, but I'll need to consult with the finance team here since I don’t have the final say.\n[2023-10-21T10:04:20] Ava Sullivan: I completely understand, Ali. Would you like me to send over a detailed proposal and pricing information so you can present it to your team?\n[2023-10-21T10:04:25] Ali Hussein: Yes, please. That would be very helpful.\n[2023-10-21T10:04:35] Ava Sullivan: Great! I'll have that to you by the end of the day. Is there anything else you would need from my side?\n[2023-10-21T10:04:40] Ali Hussein: No, that sounds good for now. Thank you, Ava.\n[2023-10-21T10:04:50] Ava Sullivan: You're welcome, Ali. If any questions come up, feel free to reach out. Have a wonderful day!\n[2023-10-21T10:04:55] Ali Hussein: Thanks, Ava. You too!", 'CreatedDate': '2023-10-21T10:02:00.000+0000', 'EndTime__c': '2023-10-21'}], 'var_call_TACd1elz3myK62mTpgn4LmSg': 'file_storage/call_TACd1elz3myK62mTpgn4LmSg.json'}

exec(code, env_args)
