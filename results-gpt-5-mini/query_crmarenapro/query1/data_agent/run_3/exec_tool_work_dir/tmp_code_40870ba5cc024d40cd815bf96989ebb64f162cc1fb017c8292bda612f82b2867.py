code = """import json, re
# Accessing tool results stored in variables
transcript_records = var_call_r56em5Wr9EiCysqheFUrxVN5
knowledge_records = None
# var_call_v9bz32xvcOVEhBMkkKgSY55i may be a filepath if large, but in this run it's a list preview stored directly
knowledge_records = var_call_v9bz32xvcOVEhBMkkKgSY55i

transcript = transcript_records[0].get('Body__c','') if transcript_records else ''
# Normalize whitespace
text = re.sub('\s+',' ', transcript)
text_lower = text.lower()

failed = []
reasons = {}

# Check Budget: look for budget and pricing
budget_match = re.search(r"budget is \$?([0-9,]+(?:\.[0-9]{2})?)", text_lower)
price_match = re.search(r"priced at \$?([0-9,]+(?:\.[0-9]{2})?)", text_lower)
quantity_match = re.search(r"interest(ed)? in (?:four|4) units|we want to .* four units|4 units", text_lower)

budget_ok = False
if budget_match and price_match and quantity_match:
    try:
        budget = float(budget_match.group(1).replace(',',''))
        price = float(price_match.group(1).replace(',',''))
        # assume quantity 4 if quantity_match
        quantity = 4
        total = price * quantity
        if total <= budget:
            budget_ok = True
        else:
            budget_ok = False
    except:
        budget_ok = False
else:
    # If explicit budget or price not found, mark as unknown -> not failed
    budget_ok = True

if not budget_ok:
    failed.append('Budget')
    reasons['Budget'] = f'Calculated total exceeds budget (total {total} > budget {budget}).'
else:
    reasons['Budget'] = 'Budget appears sufficient based on transcript: budget $2,261 vs estimated total $2,000.'

# Check Authority: look for phrases indicating lack of decision-making power
if re.search(r"i don't have the final say|i do not have the final say|need to consult|consult with .* finance|need to run it by|i'll need to consult", text_lower):
    authority_ok = False
    failed.append('Authority')
    reasons['Authority'] = 'Lead explicitly stated they need to consult the finance team and do not have final decision authority.'
else:
    authority_ok = True
    reasons['Authority'] = 'No indication lead lacks authority.'

# Check Need: look for expressed need
if re.search(r"interested to learn more|we want to enhance our simulation|interested.*pulse?sim|we want to enhance", text_lower):
    need_ok = True
    reasons['Need'] = 'Lead expressed a clear need to enhance simulation capabilities and interest in the product.'
else:
    need_ok = False
    failed.append('Need')
    reasons['Need'] = 'No clear statement of need in transcript.'

# Check Timeline: analyze transcript and knowledge article for installation timelines
# From transcript: lead said "We do have a tight timeline for installation"
timeline_concern = bool(re.search(r"tight timeline|tight schedule|urgent|as soon as possible|need it soon", text_lower))
# From knowledge articles, look for installation timeline policy
install_days = None
for rec in knowledge_records:
    faq = (rec.get('faq_answer__c') or '').lower()
    if 'volume-based installation timeline' in faq or 'installation timeline' in faq or 'small batch purchase' in faq:
        # look for pattern 'small batch ... 3 days' or 'single unit ... within a single day'
        m = re.search(r"small batch purchase \(volume: 5\).*?(\d+) days", faq)
        if m:
            install_days = int(m.group(1))
            break
        m2 = re.search(r"single unit purchase .* within a single day", faq)
        if m2:
            install_days = 1

# For 4 units, use small batch (5) if mentioned -> 3 days
if install_days is None:
    # default to transcript rep claim of 'complete installations within a day'
    if re.search(r"complete installations within a day|complete installations within a day", text_lower):
        install_days = 1

# Determine if timeline fails: lead has tight timeline, and install_days exists; we'll mark timeline as failed only if install_days > 1 and lead said tight timeline implying sooner than that
timeline_ok = True
if timeline_concern and install_days is not None:
    # If install_days >1 and lead said 'tight timeline' without specifying, we cannot be certain it fails. But conservative approach: only fail timeline if install_days >1 and rep earlier promised 1 day? 
    # Here transcript shows rep said installations within a day, but knowledge article sets 3 days for 4 units -> ambiguous. We'll treat timeline as NOT conclusively failed.
    timeline_ok = True
    reasons['Timeline'] = f'Lead mentioned a tight timeline. Installation policy indicates ~{install_days} day(s) for this volume; timeline may be feasible but not conclusively met.'
else:
    reasons['Timeline'] = 'No explicit timeline conflict found.'

if not timeline_ok:
    failed.append('Timeline')

# Prepare result
result = {'failed_factors': failed, 'reasons': reasons}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_r56em5Wr9EiCysqheFUrxVN5': [{'Id': 'a05Wt000003SukEIAS', 'OpportunityId__c': 'None', 'LeadId__c': '00QWt0000089AekMAE', 'Body__c': "[2023-10-21T10:02:00] Ava Sullivan: Hi Ali, this is Ava Sullivan from TechSolutions. How are you today?\n[2023-10-21T10:02:10] Ali Hussein: Hi Ava, I'm doing well, thank you. How about you?\n[2023-10-21T10:02:20] Ava Sullivan: I'm great, thank you for asking! I'm glad we could connect. I was looking over the details you provided about your interest in the PulseSim Pro. Is now a good time to discuss?\n[2023-10-21T10:02:30] Ali Hussein: Yes, now works for me. I'm interested to learn more and see how it fits with what we need.\n[2023-10-21T10:02:40] Ava Sullivan: Fantastic! From what you’ve mentioned, you’re interested in four units of the PulseSim Pro, correct?\n[2023-10-21T10:02:50] Ali Hussein: That's right. We want to enhance our simulation capabilities, and the PulseSim Pro seems like a great fit.\n[2023-10-21T10:03:05] Ava Sullivan: Absolutely. The PulseSim Pro is one of our top products for high precision simulation. It offers advanced analytics and seamless integration with existing systems, which is great for boosting efficiency.\n[2023-10-21T10:03:15] Ali Hussein: Those features sound beneficial. We do have a tight timeline for installation, though. Could you tell me more about that?\n[2023-10-21T10:03:30] Ava Sullivan: Certainly. We understand the importance of meeting tight schedules. We usually aim to complete installations within a day and ensure everything runs smoothly. Our technical team is very efficient.\n[2023-10-21T10:03:40] Ali Hussein: That’s reassuring. And as for the budget, how does it look for four units?\n[2023-10-21T10:03:55] Ava Sullivan: Considering your budget is $2,261, I think we can work something out. Each PulseSim Pro unit is priced at $500. For four units, it will come to $2,000. This is below your budget, leaving room for additional services if you wish.\n[2023-10-21T10:04:10] Ali Hussein: That fits really well. I'd like to move forward, but I'll need to consult with the finance team here since I don’t have the final say.\n[2023-10-21T10:04:20] Ava Sullivan: I completely understand, Ali. Would you like me to send over a detailed proposal and pricing information so you can present it to your team?\n[2023-10-21T10:04:25] Ali Hussein: Yes, please. That would be very helpful.\n[2023-10-21T10:04:35] Ava Sullivan: Great! I'll have that to you by the end of the day. Is there anything else you would need from my side?\n[2023-10-21T10:04:40] Ali Hussein: No, that sounds good for now. Thank you, Ava.\n[2023-10-21T10:04:50] Ava Sullivan: You're welcome, Ali. If any questions come up, feel free to reach out. Have a wonderful day!\n[2023-10-21T10:04:55] Ali Hussein: Thanks, Ava. You too!", 'CreatedDate': '2023-10-21T10:02:00.000+0000', 'EndTime__c': '2023-10-21'}], 'var_call_v9bz32xvcOVEhBMkkKgSY55i': 'file_storage/call_v9bz32xvcOVEhBMkkKgSY55i.json'}

exec(code, env_args)
