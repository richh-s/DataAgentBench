code = """import json
# Accessing stored results
transcripts = var_call_QeLvMpZRftM2TZZiwrJlig8Z
# var_call_wxV... is a file path string to JSON result
import os
articles_path = var_call_wxVhQkg2fTQ4I6mJIAeYFyTb
# Load articles if path is a file
articles = []
if isinstance(articles_path, str) and os.path.exists(articles_path):
    with open(articles_path, 'r', encoding='utf-8') as f:
        articles = json.load(f)

# Analyze transcript
body = ''
if transcripts:
    body = transcripts[0].get('Body__c','')
    body_low = body.lower()
else:
    body_low = ''

bant_failures = []

# Check Budget: look for explicit budget and price and whether price <= budget
import re
budget_ok = False
# find budget amount
budget_matches = re.findall(r'budget[^\d\$\n\r\,\.]*(?:is|:)?\s*\$?([0-9,]+)', body_low)
# find unit price and quantity
unit_price_matches = re.findall(r'\$([0-9,]+)\s*(?:per unit|each|unit)?', body)
# also capture explicit statement "Each PulseSim Pro unit is priced at $500"
unit_price_matches = unit_price_matches or re.findall(r'priced at \$([0-9,]+)', body)
qty_match = re.search(r'interested in (\d+) units|we(?:'"""|\")re interested in (\d+) units|interested in four units|four units', body_low)
# handle textual 'four' -> 4
if 'four units' in body_low:
    qty = 4
elif qty_match:
    qty = int(qty_match.group(1))
else:
    qty = None

budget_amount = None
if budget_matches:
    try:
        budget_amount = int(budget_matches[0].replace(',',''))
    except:
        budget_amount = None

unit_price = None
if unit_price_matches:
    try:
        unit_price = int(unit_price_matches[0].replace(',',''))
    except:
        unit_price = None

if budget_amount is not None and unit_price is not None and qty is not None:
    total_price = unit_price * qty
    if total_price <= budget_amount:
        budget_ok = True
    else:
        budget_ok = False
elif budget_amount is not None and ('price' in body_low or '$' in body_low):
    # partial evidence that budget likely ok if price mentioned as lower than budget in transcript
    if '$2,000' in body or '2000' in body:
        if budget_amount >= 2000:
            budget_ok = True

# Fallback: transcript explicitly says "That fits really well." after pricing
if 'that fits really well' in body_low or 'that fits really well.' in body:
    budget_ok = True

if not budget_ok:
    bant_failures.append('Budget')

# Check Authority: look for inability to decide / need to consult
authority_phrases = ['i don\'t have the final say', 'i don\'t have final say', 'i don\'t have the final', 'need to consult', 'consult with the finance', 'consult with finance', 'consult with', 'i will need to consult', 'i\'ll need to consult', 'not the final say', 'final say']
authority_flag = False
for p in authority_phrases:
    if p in body_low:
        authority_flag = True
        break
if authority_flag:
    bant_failures.append('Authority')

# Check Need: look for explicit need statements
need_phrases = ['interested', 'want to', 'we want to enhance', 'need', 'fits with what we need', 'want to move forward']
need_flag = any(p in body_low for p in need_phrases)
if not need_flag:
    bant_failures.append('Need')

# Check Timeline: look for tight timeline but vendor can meet
timeline_ok = True
if 'tight timeline' in body_low or 'tight timeline for installation' in body_low or 'tight timeline for' in body_low:
    # check vendor commitment
    if 'complete installations within a day' in body_low or 'installations within a day' in body_low or 'aim to complete installations within a day' in body_low or 'within a day' in body_low:
        timeline_ok = True
    else:
        timeline_ok = False
# if mention of schedule concerns without solution -> fail
if not timeline_ok:
    bant_failures.append('Timeline')

# Also scan knowledge articles for installation lead times that could contradict timeline_ok
installation_warnings = False
for art in articles:
    for field in ['title','faq_answer__c','summary']:
        text = art.get(field,'')
        if text and isinstance(text,str) and 'installation' in text.lower() and ('lead time' in text.lower() or 'delay' in text.lower() or 'long' in text.lower() or 'weeks' in text.lower() or 'months' in text.lower()):
            installation_warnings = True
            break
    if installation_warnings:
        break

if installation_warnings and 'Timeline' not in bant_failures:
    bant_failures.append('Timeline')

# Remove duplicates
bant_failures = list(dict.fromkeys(bant_failures))

# If no failures, return an empty string or 'Qualified'
if not bant_failures:
    result = 'Qualified'
else:
    result = ', '.join(bant_failures)

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_QeLvMpZRftM2TZZiwrJlig8Z': [{'Id': 'a05Wt000003SukEIAS', 'OpportunityId__c': 'None', 'LeadId__c': '00QWt0000089AekMAE', 'Body__c': "[2023-10-21T10:02:00] Ava Sullivan: Hi Ali, this is Ava Sullivan from TechSolutions. How are you today?\n[2023-10-21T10:02:10] Ali Hussein: Hi Ava, I'm doing well, thank you. How about you?\n[2023-10-21T10:02:20] Ava Sullivan: I'm great, thank you for asking! I'm glad we could connect. I was looking over the details you provided about your interest in the PulseSim Pro. Is now a good time to discuss?\n[2023-10-21T10:02:30] Ali Hussein: Yes, now works for me. I'm interested to learn more and see how it fits with what we need.\n[2023-10-21T10:02:40] Ava Sullivan: Fantastic! From what you’ve mentioned, you’re interested in four units of the PulseSim Pro, correct?\n[2023-10-21T10:02:50] Ali Hussein: That's right. We want to enhance our simulation capabilities, and the PulseSim Pro seems like a great fit.\n[2023-10-21T10:03:05] Ava Sullivan: Absolutely. The PulseSim Pro is one of our top products for high precision simulation. It offers advanced analytics and seamless integration with existing systems, which is great for boosting efficiency.\n[2023-10-21T10:03:15] Ali Hussein: Those features sound beneficial. We do have a tight timeline for installation, though. Could you tell me more about that?\n[2023-10-21T10:03:30] Ava Sullivan: Certainly. We understand the importance of meeting tight schedules. We usually aim to complete installations within a day and ensure everything runs smoothly. Our technical team is very efficient.\n[2023-10-21T10:03:40] Ali Hussein: That’s reassuring. And as for the budget, how does it look for four units?\n[2023-10-21T10:03:55] Ava Sullivan: Considering your budget is $2,261, I think we can work something out. Each PulseSim Pro unit is priced at $500. For four units, it will come to $2,000. This is below your budget, leaving room for additional services if you wish.\n[2023-10-21T10:04:10] Ali Hussein: That fits really well. I'd like to move forward, but I'll need to consult with the finance team here since I don’t have the final say.\n[2023-10-21T10:04:20] Ava Sullivan: I completely understand, Ali. Would you like me to send over a detailed proposal and pricing information so you can present it to your team?\n[2023-10-21T10:04:25] Ali Hussein: Yes, please. That would be very helpful.\n[2023-10-21T10:04:35] Ava Sullivan: Great! I'll have that to you by the end of the day. Is there anything else you would need from my side?\n[2023-10-21T10:04:40] Ali Hussein: No, that sounds good for now. Thank you, Ava.\n[2023-10-21T10:04:50] Ava Sullivan: You're welcome, Ali. If any questions come up, feel free to reach out. Have a wonderful day!\n[2023-10-21T10:04:55] Ali Hussein: Thanks, Ava. You too!", 'CreatedDate': '2023-10-21T10:02:00.000+0000', 'EndTime__c': '2023-10-21'}], 'var_call_wxVhQkg2fTQ4I6mJIAeYFyTb': 'file_storage/call_wxVhQkg2fTQ4I6mJIAeYFyTb.json'}

exec(code, env_args)
