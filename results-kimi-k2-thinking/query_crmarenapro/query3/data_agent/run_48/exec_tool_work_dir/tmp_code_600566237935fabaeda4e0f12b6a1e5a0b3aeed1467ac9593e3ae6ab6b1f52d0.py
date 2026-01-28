code = """# Analyze the CRM data to determine the correct stage for the opportunity

# Opportunity details from query
opportunity_data = {
    "Id": "006Wt000007BGGjIAO",
    "Name": "DataWave Analytics AI-Driven Enhancement", 
    "StageName": "Discovery",
    "Amount": "61666.225",
    "Probability": "85.0",
    "CloseDate": "2022-02-20",
    "Description": "DataWave Analytics seeks to enhance its data science services with TechPulse's AI-driven tools. By integrating CloudLink Designer, OptiPower Max, and CircuitSync Pro, they aim to boost efficiency and innovation in data processing. TechPulse's SecureFlow Suite offers them state-of-the-art security and compliance capabilities."
}

# Task details
tasks_data = [
    {
        "Subject": "Organize product demo",
        "Status": "Not Started",
        "ActivityDate": "2022-01-15"
    },
    {
        "Subject": "Follow up on proposal", 
        "Status": "Not Started",
        "ActivityDate": "2022-02-15"
    },
    {
        "Subject": "Hold negotiation meeting",
        "Status": "Not Started",
        "ActivityDate": "2022-02-10"
    }
]

# Analysis of stage appropriateness
analysis = {
    "current_stage": opportunity_data["StageName"],
    "data_points": {
        "probability": float(opportunity_data["Probability"]),
        "close_date": opportunity_data["CloseDate"],
        "amount": float(opportunity_data["Amount"])
    },
    "activities": []
}

# Evaluate each task to determine stage indicators
for task in tasks_data:
    analysis["activities"].append({
        "subject": task["Subject"],
        "status": task["Status"],
        "date": task["ActivityDate"]
    })

# Stage definitions for determination:
# - Discovery: Needs assessment, solution design
# - Quote: Proposal presentation, pricing discussion
# - Negotiation: Final terms negotiation

# Evaluate indicators
proposal_followup_found = any("proposal" in task["Subject"].lower() for task in tasks_data)
negotiation_found = any("negotiation" in task["Subject"].lower() for task in tasks_data)
demo_found = any("demo" in task["Subject"].lower() for task in tasks_data)

analysis["indicators"] = {
    "proposal_foullowup": proposal_followup_found,
    "negotiation_scheduled": negotiation_found,
    "demo_scheduled": demo_found,
    "high_probability": float(opportunity_data["Probability"]) >= 85
}

# Determine correct stage
# The presence of "Follow up on proposal" clearly indicates Quote stage
# The "Hold negotiation meeting" suggests movement toward Negotiation, but Proposal is current
# All tasks are "Not Started" which suggests data inconsistency, but logically it's Quote

if proposal_followup_found:
    correct_stage = "Quote"
elif negotiation_found:
    correct_stage = "Negotiation"
elif demo_found and float(opportunity_data["Probability"]) < 50:
    correct_stage = "Discovery"
else:
    correct_stage = opportunity_data["StageName"]

analysis["correct_stage"] = correct_stage
import json
print('__RESULT__:')
print(json.dumps(analysis, indent=2))"""

env_args = {'var_functions.query_db:0': [{'Id': '006Wt000007BGGjIAO', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'StageName': 'Discovery', 'Amount': '61666.225', 'Probability': '85.0', 'CloseDate': '2022-02-20', 'AccountId': '001Wt00000PGRqjIAH', 'ContactId': '#003Wt00000JqczHIAR', 'OwnerId': '005Wt000003NIs9IAG', 'Description': "DataWave Analytics seeks to enhance its data science services with TechPulse's AI-driven tools. By integrating CloudLink Designer, OptiPower Max, and CircuitSync Pro, they aim to boost efficiency and innovation in data processing. TechPulse's SecureFlow Suite offers them state-of-the-art security and compliance capabilities."}], 'var_functions.query_db:2': [{'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIovIAG', 'Status': 'Not Started', 'Subject': 'Organize product demo', 'Description': 'Set up a product demonstration to showcase the relevant solutions', 'ActivityDate': '2022-01-15'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NF9WIAW', 'Status': 'Not Started ', 'Subject': 'Follow up on proposal', 'Description': 'Reach out to the client to address any questions and negotiate terms', 'ActivityDate': '2022-02-15'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Status': 'Not Started', 'Subject': 'Hold negotiation meeting', 'Description': 'Discuss terms and finalize pricing with the client', 'ActivityDate': '2022-02-10'}], 'var_functions.query_db:3': [], 'var_functions.query_db:4': [], 'var_functions.query_db:9': [{'Id': '#0Q0Wt000001WLjvKAG', 'Name': 'TechPulse-NaviCorp EDA Strategic Quote  ', 'OpportunityId': '#006Wt000007BA3HIAW', 'Status': 'Approved', 'CreatedDate': '2024-03-18T14:15:00.000+0000', 'ExpirationDate': '2024-05-17'}, {'Id': '0Q0Wt000001WRJ3KAO', 'Name': 'NaviCorp Tech Advanced Navigation Optimization Quote', 'OpportunityId': '006Wt000007BFEFIA4', 'Status': 'Accepted', 'CreatedDate': '2021-07-01T10:00:00.000+0000', 'ExpirationDate': '2021-08-01'}, {'Id': '0Q0Wt000001WKEPKA4', 'Name': 'NaviCorp Strategic EDA Solutions Quote', 'OpportunityId': '#006Wt000007BFfeIAG', 'Status': 'Approved', 'CreatedDate': '2024-03-12T10:30:00.000+0000', 'ExpirationDate': '2024-04-12'}, {'Id': '0Q0Wt000001WREDKA4', 'Name': 'NaviCorp Expansion Quote', 'OpportunityId': '006Wt000007BFpKIAW', 'Status': 'Draft', 'CreatedDate': '2023-02-10T11:00:00.000+0000', 'ExpirationDate': '2023-03-10'}, {'Id': '0Q0Wt000001WRHRKA4', 'Name': 'NaviCorp Strategic Partnership Quote', 'OpportunityId': '006Wt000007BFxOIAW', 'Status': 'Needs Review   ', 'CreatedDate': '2021-05-12T09:00:00.000+0000', 'ExpirationDate': '2021-06-10'}]}

exec(code, env_args)
