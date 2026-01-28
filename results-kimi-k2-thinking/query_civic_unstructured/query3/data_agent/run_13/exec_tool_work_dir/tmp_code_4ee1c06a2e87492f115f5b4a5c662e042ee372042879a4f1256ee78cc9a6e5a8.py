code = """import json

# Access the variables directly
civic_docs_var = 'var_functions.query_db:2'
funding_var = 'var_functions.query_db:5'

civic_docs = locals()[civic_docs_var]
funding_data = locals()[funding_var]

print("Type of civic_docs:", type(civic_docs))
print("Type of funding_data:", type(funding_data))

print("\nFirst few civic docs:", len(civic_docs))
print("First civic doc:", civic_docs[0].keys())

print("\nFirst few funding records:", len(funding_data))
print("First funding record:", funding_data[0])

# Now let's find projects relevant to emergency/FEMA
# Filter funding projects that contain emergency/FEMA keywords

relevant_funding = []
for record in funding_data:
    project_name = record.get("Project_Name", "").lower()
    funding_source = record.get("Funding_Source", "").lower()
    if "emergency" in project_name or "fema" in project_name or "emergency" in funding_source:
        relevant_funding.append(record)

print("\nRelevant funding records:", len(relevant_funding))
for rec in relevant_funding[:10]:
    print(rec)"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
