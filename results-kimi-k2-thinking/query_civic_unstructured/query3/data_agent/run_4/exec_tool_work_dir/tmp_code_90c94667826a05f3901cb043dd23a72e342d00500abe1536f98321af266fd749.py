code = """import json

# FEMA/Emergency projects from funding database with extracted status information
projects = [
    {
        "Project_Name": "Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)",
        "Funding_Source": "Private Sponsor",
        "Amount": 94000,
        "Status": "design",
        "Type": "disaster"
    },
    {
        "Project_Name": "Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)",
        "Funding_Source": "Infrastructure Bond",
        "Amount": 92000,
        "Status": "Unknown",
        "Type": "disaster"
    },
    {
        "Project_Name": "Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)",
        "Funding_Source": "Municipal Fund",
        "Amount": 91000,
        "Status": "Unknown",
        "Type": "disaster"
    },
    {
        "Project_Name": "Outdoor Warningn Sirens - Design (FEMA Project)",
        "Funding_Source": "Technology Innovation Fund",
        "Amount": 84000,
        "Status": "design",
        "Type": "disaster"
    },
    {
        "Project_Name": "Outdoor Warning Sirens (FEMA)",
        "Funding_Source": "State Development Grant",
        "Amount": 81000,
        "Status": "Unknown",
        "Type": "disaster"
    },
    {
        "Project_Name": "Storm Drain Master Plan (FEMA Project)",
        "Funding_Source": "Environmental Grant",
        "Amount": 80000,
        "Status": "design",
        "Type": "disaster"
    },
    {
        "Project_Name": "Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)",
        "Funding_Source": "Community Fund",
        "Amount": 78000,
        "Status": "Unknown",
        "Type": "disaster"
    },
    {
        "Project_Name": "Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)",
        "Funding_Source": "Cultural Heritage Grant",
        "Amount": 58000,
        "Status": "Unknown",
        "Type": "disaster"
    },
    {
        "Project_Name": "Guardrail Replacement Citywide (FEMA/CalOES Project)",
        "Funding_Source": "Development Bank Loan",
        "Amount": 45000,
        "Status": "Unknown",
        "Type": "disaster"
    },
    {
        "Project_Name": "Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)",
        "Funding_Source": "National Foundation Fund",
        "Amount": 44000,
        "Status": "Unknown",
        "Type": "disaster"
    },
    {
        "Project_Name": "Corral Canyon Culvert Repairs (FEMA Project)",
        "Funding_Source": "Municipal Fund",
        "Amount": 43000,
        "Status": "Unknown",
        "Type": "disaster"
    },
    {
        "Project_Name": "Outdoor Warning Sirens - Design (FEMA Project)",
        "Funding_Source": "Local Business Support",
        "Amount": 43000,
        "Status": "design",
        "Type": "disaster"
    },
    {
        "Project_Name": "Latigo Canyon Road Culvert Repairs (FEMA Project)",
        "Funding_Source": "Federal Assistance",
        "Amount": 36000,
        "Status": "Unknown",
        "Type": "disaster"
    },
    {
        "Project_Name": "Outdoor Warning Sirens (FEMA Project)",
        "Funding_Source": "Environmental Grant",
        "Amount": 27000,
        "Status": "Unknown",
        "Type": "disaster"
    },
    {
        "Project_Name": "Corral Canyon Road Bridge Repairs (FEMA Project)",
        "Funding_Source": "Local Business Support",
        "Amount": 25000,
        "Status": "Unknown",
        "Type": "disaster"
    },
    {
        "Project_Name": "Guardrail Replacement Citywide (FEMA Project)",
        "Funding_Source": "Impact Investment Fund",
        "Amount": 22000,
        "Status": "Unknown",
        "Type": "disaster"
    },
    {
        "Project_Name": "Clover Heights Storm Drain (FEMA Project)",
        "Funding_Source": "Local NGO Fund",
        "Amount": 21000,
        "Status": "Unknown",
        "Type": "disaster"
    },
    {
        "Project_Name": "Corral Canyon Culvert Repairs (FEMA/CalOES Project)",
        "Funding_Source": "Taxpayer Contribution",
        "Amount": 15000,
        "Status": "Unknown",
        "Type": "disaster"
    },
    {
        "Project_Name": "Birdview Avenue Improvements (FEMA/CalOES Project)",
        "Funding_Source": "Research Institution Funding",
        "Amount": 14000,
        "Status": "Unknown",
        "Type": "disaster"
    },
    {
        "Project_Name": "Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)",
        "Funding_Source": "Infrastructure Bond",
        "Amount": 44000,
        "Status": "Unknown",
        "Type": "disaster"
    }
]

# Sort by amount descending
projects.sort(key=lambda x: x['Amount'], reverse=True)

# Convert to final format
final_results = []
for proj in projects:
    final_results.append({
        "Project_Name": proj["Project_Name"],
        "Funding_Source": proj["Funding_Source"],
        "Amount": proj["Amount"],
        "Status": proj["Status"],
        "Type": proj["Type"]
    })

print('__RESULT__:')
print(json.dumps(final_results))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:16': [{'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 91000}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': 78000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': 44000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000}, {'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': 37000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': 36000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:19': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_functions.execute_python:22': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:28': [{'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000, 'Status': 'design', 'Type': 'disaster'}, {'Project_Name': 'Outdoor Warning Signs', 'Funding_Source': 'Urban Renewal Fund', 'Amount': 92000, 'Status': 'design', 'Type': 'capital'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Funding_Source': 'Urban Renewal Fund', 'Amount': 92000, 'Status': 'design', 'Type': 'capital'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 91000, 'Status': 'Unknown', 'Type': 'disaster'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000, 'Status': 'design', 'Type': 'disaster'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000, 'Status': 'Unknown', 'Type': 'disaster'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 80000, 'Status': 'design', 'Type': 'disaster'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': 78000, 'Status': 'Unknown', 'Type': 'disaster'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000, 'Status': 'Unknown', 'Type': 'disaster'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000, 'Status': 'Unknown', 'Type': 'disaster'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 44000, 'Status': 'Unknown', 'Type': 'disaster'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 44000, 'Status': 'Unknown', 'Type': 'disaster'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': 44000, 'Status': 'Unknown', 'Type': 'disaster'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000, 'Status': 'Unknown', 'Type': 'disaster'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000, 'Status': 'design', 'Type': 'disaster'}, {'Project_Name': 'Storm Drain Master Plan', 'Funding_Source': 'Environmental Grant', 'Amount': 42000, 'Status': 'design', 'Type': 'capital'}, {'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': 37000, 'Status': 'construction', 'Type': 'disaster'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': 36000, 'Status': 'Unknown', 'Type': 'disaster'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000, 'Status': 'Unknown', 'Type': 'disaster'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000, 'Status': 'Unknown', 'Type': 'disaster'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000, 'Status': 'Unknown', 'Type': 'disaster'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000, 'Status': 'Unknown', 'Type': 'disaster'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000, 'Status': 'Unknown', 'Type': 'disaster'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000, 'Status': 'Unknown', 'Type': 'disaster'}]}

exec(code, env_args)
