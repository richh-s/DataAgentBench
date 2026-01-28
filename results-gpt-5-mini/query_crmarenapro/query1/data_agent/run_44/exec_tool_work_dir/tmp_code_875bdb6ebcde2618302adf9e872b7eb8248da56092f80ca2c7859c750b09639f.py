code = """import json, re
# Access storage variables
lead_records = var_call_E6RnOu9BrpMxXT5wqRyj1mOP
trans_records = var_call_mucc8kQDlXRR7oNYNtsmsLmH
knowledge_path = var_call_3UuGdXAGsgTYgyzx6CPTo8r1

lead = lead_records[0] if lead_records else {}
trans = trans_records[0] if trans_records else {}
body = (trans.get('Body__c', '') or '').lower()

# Helper to find number words
num_words = {
    'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10
}

# Determine Authority
authority_phrases = ["don't have the final say","i don't have the final say","i will need to consult","i'll need to consult","need to consult with","need to consult","consult with the finance","consult with finance","i don't have the final","i do not have the final say","i don't have final say"]
authority_issue = any(p in body for p in authority_phrases)

# Determine Budget
# Find budget number mentioned
nums = re.findall(r'\$?([0-9{1,3},]*(?:\.[0-9]{2})?)', body)
# Clean and convert
clean_nums = []
for n in nums:
    n2 = n.replace(',', '')
    if n2.strip()=='' or n2=='.00':
        continue
    try:
        clean_nums.append(float(n2))
    except:
        pass

budget_value = None
unit_price = None
units_requested = None
# Look for explicit phrases
m = re.search(r'budget is\s*\$?([0-9,]+(?:\.[0-9]{2})?)', body)
if m:
    budget_value = float(m.group(1).replace(',', ''))
# unit price
m2 = re.search(r'priced at\s*\$?([0-9,]+(?:\.[0-9]{2})?)', body)
if m2:
    unit_price = float(m2.group(1).replace(',', ''))
# total price phrase
m3 = re.search(r'for\s*(?:four|\d+)\s*units,? it will come to\s*\$?([0-9,]+(?:\.[0-9]{2})?)', body)
if m3:
    total_price = float(m3.group(1).replace(',', ''))
else:
    total_price = None
# units requested
m4 = re.search(r'(\b\d+\b)\s+units', body)
if m4:
    units_requested = int(m4.group(1))
else:
    # words
    for w, val in num_words.items():
        if f"{w} units" in body:
            units_requested = val
            break

# If unit price and units known compute total
if unit_price is not None and units_requested is not None:
    computed_total = unit_price * units_requested
    if total_price is None:
        total_price = computed_total

# If budget known compare
budget_ok = True
if budget_value is not None and total_price is not None:
    budget_ok = (budget_value >= total_price)

# Determine Need
need_phrases = ['interested to learn more','we want to enhance our simulation capabilities','seems like a great fit','that fits really well','i\'m interested']
need_ok = any(p in body for p in need_phrases)

# Determine Timeline
# Check for tight timeline mention
timeline_concern = 'tight timeline' in body or 'tight timeline for' in body or 'tight timeline' in body
# Parse knowledge articles for installation timelines
expected_install_days = None
try:
    with open(knowledge_path, 'r', encoding='utf-8') as f:
        ka = json.load(f)
    # Combine text
    text = ' '.join([(a.get('faq_answer__c') or '') for a in ka]).lower()
    # Find patterns like 'Single Unit Purchase (Volume: 1) ... within a single day' or 'Volume: 5 ... 3 days'
    vol_days = {}
    for m in re.finditer(r'volume:\s*(\d+)[^\n\d]*(?:.*?)(\d+)\s*day', text):
        vol = int(m.group(1))
        days = int(m.group(2))
        vol_days[vol] = days
    # Fallback: look for 'single unit' -> 1 day
    if 'single unit' in text and '1 day' in text:
        vol_days.setdefault(1,1)
    # small batch 5 -> 3 days etc handled above
    if units_requested is not None and vol_days:
        # find smallest vol >= units_requested
        candidates = [(v,d) for v,d in vol_days.items() if v>=units_requested]
        if candidates:
            expected_install_days = min(candidates, key=lambda x: x[0])[1]
        else:
            # if none >=, take max mapping
            expected_install_days = max(vol_days.values())
except Exception as e:
    expected_install_days = None

# If timeline concern and expected_install_days >1 or no confirmed date in transcript, mark timeline as failing
# Check transcript for explicit seller commitment like 'complete installations within a day' or 'we usually aim to complete installations within a day'
commitment = False
if 'complete installations within a day' in body or 'complete installation within a day' in body or 'complete installations within a day' in body:
    commitment = True

# But knowledge indicates for 5 units -> 3 days; if units_requested is 4, nearest mapping gave 3 days -> conflict with commitment
timeline_ok = True
if timeline_concern:
    # if commitment present and expected_install_days is not None and expected_install_days>1 -> timeline not okay
    if commitment and expected_install_days is not None and expected_install_days>1:
        timeline_ok = False
    else:
        # if no firm commitment in transcript, treat as not confirmed
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

# Prepare output as JSON array string
output = json.dumps(failing)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_E6RnOu9BrpMxXT5wqRyj1mOP': [{'Id': '00QWt0000089AekMAE', 'FirstName': 'Ali', 'LastName': 'Hussein', 'Email': 'ali.hussein@baghdadhtechhub.com', 'Phone': '555-452-7654', 'Company': 'Baghdad Tech Hub', 'Status': 'Converted', 'ConvertedContactId': 'None', 'ConvertedAccountId': 'None', 'Title': 'Head of Emerging Technologies', 'CreatedDate': '2023-08-18T15:35:50.000+0000', 'ConvertedDate': 'None', 'IsConverted': '0', 'OwnerId': '005Wt000003NErnIAG'}], 'var_call_mucc8kQDlXRR7oNYNtsmsLmH': [{'Id': 'a05Wt000003SukEIAS', 'OpportunityId__c': 'None', 'LeadId__c': '00QWt0000089AekMAE', 'Body__c': "[2023-10-21T10:02:00] Ava Sullivan: Hi Ali, this is Ava Sullivan from TechSolutions. How are you today?\n[2023-10-21T10:02:10] Ali Hussein: Hi Ava, I'm doing well, thank you. How about you?\n[2023-10-21T10:02:20] Ava Sullivan: I'm great, thank you for asking! I'm glad we could connect. I was looking over the details you provided about your interest in the PulseSim Pro. Is now a good time to discuss?\n[2023-10-21T10:02:30] Ali Hussein: Yes, now works for me. I'm interested to learn more and see how it fits with what we need.\n[2023-10-21T10:02:40] Ava Sullivan: Fantastic! From what you’ve mentioned, you’re interested in four units of the PulseSim Pro, correct?\n[2023-10-21T10:02:50] Ali Hussein: That's right. We want to enhance our simulation capabilities, and the PulseSim Pro seems like a great fit.\n[2023-10-21T10:03:05] Ava Sullivan: Absolutely. The PulseSim Pro is one of our top products for high precision simulation. It offers advanced analytics and seamless integration with existing systems, which is great for boosting efficiency.\n[2023-10-21T10:03:15] Ali Hussein: Those features sound beneficial. We do have a tight timeline for installation, though. Could you tell me more about that?\n[2023-10-21T10:03:30] Ava Sullivan: Certainly. We understand the importance of meeting tight schedules. We usually aim to complete installations within a day and ensure everything runs smoothly. Our technical team is very efficient.\n[2023-10-21T10:03:40] Ali Hussein: That’s reassuring. And as for the budget, how does it look for four units?\n[2023-10-21T10:03:55] Ava Sullivan: Considering your budget is $2,261, I think we can work something out. Each PulseSim Pro unit is priced at $500. For four units, it will come to $2,000. This is below your budget, leaving room for additional services if you wish.\n[2023-10-21T10:04:10] Ali Hussein: That fits really well. I'd like to move forward, but I'll need to consult with the finance team here since I don’t have the final say.\n[2023-10-21T10:04:20] Ava Sullivan: I completely understand, Ali. Would you like me to send over a detailed proposal and pricing information so you can present it to your team?\n[2023-10-21T10:04:25] Ali Hussein: Yes, please. That would be very helpful.\n[2023-10-21T10:04:35] Ava Sullivan: Great! I'll have that to you by the end of the day. Is there anything else you would need from my side?\n[2023-10-21T10:04:40] Ali Hussein: No, that sounds good for now. Thank you, Ava.\n[2023-10-21T10:04:50] Ava Sullivan: You're welcome, Ali. If any questions come up, feel free to reach out. Have a wonderful day!\n[2023-10-21T10:04:55] Ali Hussein: Thanks, Ava. You too!", 'CreatedDate': '2023-10-21T10:02:00.000+0000', 'EndTime__c': '2023-10-21'}], 'var_call_3UuGdXAGsgTYgyzx6CPTo8r1': 'file_storage/call_3UuGdXAGsgTYgyzx6CPTo8r1.json'}

exec(code, env_args)
