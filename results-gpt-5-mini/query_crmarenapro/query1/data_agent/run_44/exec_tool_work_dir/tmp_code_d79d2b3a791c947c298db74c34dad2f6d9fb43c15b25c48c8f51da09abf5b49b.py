code = """import json
# Load variables from storage
lead_records = var_call_E6RnOu9BrpMxXT5wqRyj1mOP
trans_records = var_call_mucc8kQDlXRR7oNYNtsmsLmH
knowledge_path = var_call_3UuGdXAGsgTYgyzx6CPTo8r1

lead = lead_records[0] if lead_records else {}
trans = trans_records[0] if trans_records else {}
body = (trans.get('Body__c') or '').lower()

# Authority
authority_phrases = ["don't have the final say", "i don't have the final say", "i will need to consult", "i'll need to consult", "need to consult with", "need to consult", "consult with the finance", "consult with finance", "i don't have the final", "i do not have the final say", "i don't have final say"]
authority_issue = any(p in body for p in authority_phrases)

# Budget
import re
budget_value = None
unit_price = None
units_requested = None
# budget
m = re.search(r'budget is\s*\$?([0-9,]+)', body)
if m:
    budget_value = float(m.group(1).replace(',', ''))
# unit price
m = re.search(r'priced at\s*\$?([0-9,]+)', body)
if m:
    unit_price = float(m.group(1).replace(',', ''))
# units requested (look for 'four units' or '4 units')
m = re.search(r'(\b\d+\b)\s+units', body)
if m:
    units_requested = int(m.group(1))
else:
    if 'four units' in body:
        units_requested = 4
    elif 'five units' in body:
        units_requested = 5

# total price phrase
total_price = None
m = re.search(r'for\s*(?:four|\d+)\s*units,?\s*it will come to\s*\$?([0-9,]+)', body)
if m:
    total_price = float(m.group(1).replace(',', ''))

if unit_price is not None and units_requested is not None and total_price is None:
    total_price = unit_price * units_requested

budget_ok = True
if budget_value is not None and total_price is not None:
    budget_ok = (budget_value >= total_price)

# Need
need_phrases = ['interested to learn more', 'we want to enhance our simulation capabilities', 'seems like a great fit', 'that fits really well', "i'm interested", "i am interested"]
need_ok = any(p in body for p in need_phrases)

# Timeline
timeline_concern = 'tight timeline' in body or 'tight timeline for' in body or 'tight timeline' in body
# detect seller commitment
commitment_phrases = ['complete installations within a day', 'complete installation within a day', 'we usually aim to complete installations within a day', 'we usually aim to complete installation within a day']
commitment = any(p in body for p in commitment_phrases)

# read knowledge articles text
expected_install_days = None
try:
    with open(knowledge_path, 'r', encoding='utf-8') as f:
        ka = json.load(f)
    text = ' '.join([(a.get('faq_answer__c') or '') for a in ka]).lower()
    if 'volume-based installation timeline policy' in text:
        mapping = {1:1, 5:3, 15:7, 25:14}
        if units_requested is not None:
            # find smallest mapping key >= units_requested
            keys = sorted(mapping.keys())
            chosen = None
            for k in keys:
                if k >= units_requested:
                    chosen = k
                    break
            if chosen is None:
                # use largest
                expected_install_days = mapping[keys[-1]]
            else:
                expected_install_days = mapping[chosen]
except Exception:
    expected_install_days = None

# Determine timeline_ok
timeline_ok = True
if timeline_concern:
    if commitment and expected_install_days is not None and expected_install_days > 1:
        timeline_ok = False
    else:
        if not commitment:
            timeline_ok = False

# Compile failing factors
failing = []
if not budget_ok:
    failing.append('Budget')
if authority_issue:
    failing.append('Authority')
if not need_ok:
    failing.append('Need')
if not timeline_ok:
    failing.append('Timeline')

print("__RESULT__:")
print(json.dumps(failing))"""

env_args = {'var_call_E6RnOu9BrpMxXT5wqRyj1mOP': [{'Id': '00QWt0000089AekMAE', 'FirstName': 'Ali', 'LastName': 'Hussein', 'Email': 'ali.hussein@baghdadhtechhub.com', 'Phone': '555-452-7654', 'Company': 'Baghdad Tech Hub', 'Status': 'Converted', 'ConvertedContactId': 'None', 'ConvertedAccountId': 'None', 'Title': 'Head of Emerging Technologies', 'CreatedDate': '2023-08-18T15:35:50.000+0000', 'ConvertedDate': 'None', 'IsConverted': '0', 'OwnerId': '005Wt000003NErnIAG'}], 'var_call_mucc8kQDlXRR7oNYNtsmsLmH': [{'Id': 'a05Wt000003SukEIAS', 'OpportunityId__c': 'None', 'LeadId__c': '00QWt0000089AekMAE', 'Body__c': "[2023-10-21T10:02:00] Ava Sullivan: Hi Ali, this is Ava Sullivan from TechSolutions. How are you today?\n[2023-10-21T10:02:10] Ali Hussein: Hi Ava, I'm doing well, thank you. How about you?\n[2023-10-21T10:02:20] Ava Sullivan: I'm great, thank you for asking! I'm glad we could connect. I was looking over the details you provided about your interest in the PulseSim Pro. Is now a good time to discuss?\n[2023-10-21T10:02:30] Ali Hussein: Yes, now works for me. I'm interested to learn more and see how it fits with what we need.\n[2023-10-21T10:02:40] Ava Sullivan: Fantastic! From what you’ve mentioned, you’re interested in four units of the PulseSim Pro, correct?\n[2023-10-21T10:02:50] Ali Hussein: That's right. We want to enhance our simulation capabilities, and the PulseSim Pro seems like a great fit.\n[2023-10-21T10:03:05] Ava Sullivan: Absolutely. The PulseSim Pro is one of our top products for high precision simulation. It offers advanced analytics and seamless integration with existing systems, which is great for boosting efficiency.\n[2023-10-21T10:03:15] Ali Hussein: Those features sound beneficial. We do have a tight timeline for installation, though. Could you tell me more about that?\n[2023-10-21T10:03:30] Ava Sullivan: Certainly. We understand the importance of meeting tight schedules. We usually aim to complete installations within a day and ensure everything runs smoothly. Our technical team is very efficient.\n[2023-10-21T10:03:40] Ali Hussein: That’s reassuring. And as for the budget, how does it look for four units?\n[2023-10-21T10:03:55] Ava Sullivan: Considering your budget is $2,261, I think we can work something out. Each PulseSim Pro unit is priced at $500. For four units, it will come to $2,000. This is below your budget, leaving room for additional services if you wish.\n[2023-10-21T10:04:10] Ali Hussein: That fits really well. I'd like to move forward, but I'll need to consult with the finance team here since I don’t have the final say.\n[2023-10-21T10:04:20] Ava Sullivan: I completely understand, Ali. Would you like me to send over a detailed proposal and pricing information so you can present it to your team?\n[2023-10-21T10:04:25] Ali Hussein: Yes, please. That would be very helpful.\n[2023-10-21T10:04:35] Ava Sullivan: Great! I'll have that to you by the end of the day. Is there anything else you would need from my side?\n[2023-10-21T10:04:40] Ali Hussein: No, that sounds good for now. Thank you, Ava.\n[2023-10-21T10:04:50] Ava Sullivan: You're welcome, Ali. If any questions come up, feel free to reach out. Have a wonderful day!\n[2023-10-21T10:04:55] Ali Hussein: Thanks, Ava. You too!", 'CreatedDate': '2023-10-21T10:02:00.000+0000', 'EndTime__c': '2023-10-21'}], 'var_call_3UuGdXAGsgTYgyzx6CPTo8r1': 'file_storage/call_3UuGdXAGsgTYgyzx6CPTo8r1.json'}

exec(code, env_args)
