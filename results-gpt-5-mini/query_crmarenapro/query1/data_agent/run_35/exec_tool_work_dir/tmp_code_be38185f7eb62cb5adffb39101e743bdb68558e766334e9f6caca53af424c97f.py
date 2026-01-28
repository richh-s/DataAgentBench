code = """import json
# Accessing stored results from previous tool calls
transcripts = var_call_qvzijT3aqrIcr8dTu4tlL98P
# var_call_3m0tSWDDIZhRYJOgYb2nk0Fn contains a filepath to a JSON file with the knowledge articles
with open(var_call_3m0tSWDDIZhRYJOgYb2nk0Fn, 'r', encoding='utf-8') as f:
    knowledge = json.load(f)

# Simple NLP rules to evaluate BANT from transcripts and knowledge
body = transcripts[0].get('Body__c', '').lower()

# Budget: look for budget number and unit price and quantity
budget_met = False
# find budget figure
import re
budget_match = re.search(r"budget is \$?\s*([0-9,]+(?:\.[0-9]+)?)", body)
price_match = re.search(r"each .*unit is priced at \$?\s*([0-9,]+(?:\.[0-9]+)?)", body)
quantity_match = re.search(r"interested in (\w+) units|we want to .* (\d+) units|interested in (\d+) units", transcripts[0].get('Body__c',''))
# more robust quantity search
qty = None
qm = re.search(r"(\d+) units", body)
if qm:
    qty = int(qm.group(1))

if budget_match and price_match and qty:
    budget = float(budget_match.group(1).replace(',',''))
    price = float(price_match.group(1).replace(',',''))
    total = price * qty
    budget_met = total <= budget
else:
    # fallback: transcript indicates budget fits
    if "fits really well" in body or "below your budget" in body:
        budget_met = True

# Authority: check if lead is decision maker
authority_met = True
if "i don't have the final say" in body or "need to consult" in body or "consult with" in body:
    authority_met = False

# Need: check if lead expressed need clearly
need_met = False
if any(kw in body for kw in ["interested to learn", "interested", "we want to", "need to", "enhance our simulation"]):
    need_met = True

# Timeline: check if timeline can be met per knowledge articles and rep assurance
# Lead said tight timeline; rep said installations usually within a day. Knowledge article: 1 unit=1 day, 5 units=3 days
timeline_met = True
if "tight timeline" in body:
    # find rep assurance
    if "aim to complete installations within a day" in body or any("installation timeline" in (k.get('summary','')+k.get('faq_answer__c','')).lower() for k in knowledge):
        timeline_met = True
    else:
        timeline_met = False

# Determine failing factors
failing = []
if not budget_met:
    failing.append('Budget')
if not authority_met:
    failing.append('Authority')
if not need_met:
    failing.append('Need')
if not timeline_met:
    failing.append('Timeline')

# Based on transcript and knowledge articles, we expect Authority to fail only
# Prepare output as JSON string
output = json.dumps(failing)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_qvzijT3aqrIcr8dTu4tlL98P': [{'Id': 'a05Wt000003SukEIAS', 'OpportunityId__c': 'None', 'LeadId__c': '00QWt0000089AekMAE', 'Body__c': "[2023-10-21T10:02:00] Ava Sullivan: Hi Ali, this is Ava Sullivan from TechSolutions. How are you today?\n[2023-10-21T10:02:10] Ali Hussein: Hi Ava, I'm doing well, thank you. How about you?\n[2023-10-21T10:02:20] Ava Sullivan: I'm great, thank you for asking! I'm glad we could connect. I was looking over the details you provided about your interest in the PulseSim Pro. Is now a good time to discuss?\n[2023-10-21T10:02:30] Ali Hussein: Yes, now works for me. I'm interested to learn more and see how it fits with what we need.\n[2023-10-21T10:02:40] Ava Sullivan: Fantastic! From what you’ve mentioned, you’re interested in four units of the PulseSim Pro, correct?\n[2023-10-21T10:02:50] Ali Hussein: That's right. We want to enhance our simulation capabilities, and the PulseSim Pro seems like a great fit.\n[2023-10-21T10:03:05] Ava Sullivan: Absolutely. The PulseSim Pro is one of our top products for high precision simulation. It offers advanced analytics and seamless integration with existing systems, which is great for boosting efficiency.\n[2023-10-21T10:03:15] Ali Hussein: Those features sound beneficial. We do have a tight timeline for installation, though. Could you tell me more about that?\n[2023-10-21T10:03:30] Ava Sullivan: Certainly. We understand the importance of meeting tight schedules. We usually aim to complete installations within a day and ensure everything runs smoothly. Our technical team is very efficient.\n[2023-10-21T10:03:40] Ali Hussein: That’s reassuring. And as for the budget, how does it look for four units?\n[2023-10-21T10:03:55] Ava Sullivan: Considering your budget is $2,261, I think we can work something out. Each PulseSim Pro unit is priced at $500. For four units, it will come to $2,000. This is below your budget, leaving room for additional services if you wish.\n[2023-10-21T10:04:10] Ali Hussein: That fits really well. I'd like to move forward, but I'll need to consult with the finance team here since I don’t have the final say.\n[2023-10-21T10:04:20] Ava Sullivan: I completely understand, Ali. Would you like me to send over a detailed proposal and pricing information so you can present it to your team?\n[2023-10-21T10:04:25] Ali Hussein: Yes, please. That would be very helpful.\n[2023-10-21T10:04:35] Ava Sullivan: Great! I'll have that to you by the end of the day. Is there anything else you would need from my side?\n[2023-10-21T10:04:40] Ali Hussein: No, that sounds good for now. Thank you, Ava.\n[2023-10-21T10:04:50] Ava Sullivan: You're welcome, Ali. If any questions come up, feel free to reach out. Have a wonderful day!\n[2023-10-21T10:04:55] Ali Hussein: Thanks, Ava. You too!", 'CreatedDate': '2023-10-21T10:02:00.000+0000', 'EndTime__c': '2023-10-21'}], 'var_call_3m0tSWDDIZhRYJOgYb2nk0Fn': 'file_storage/call_3m0tSWDDIZhRYJOgYb2nk0Fn.json'}

exec(code, env_args)
