code = """import json

pricebook_entry_ids_data = locals()['var_function-call-7477208485156344770']['results']
pricebook_entry_ids = [item['PricebookEntryId'] for item in pricebook_entry_ids_data]

# Prepare the list of IDs for the SQL IN clause
if not pricebook_entry_ids:
    pricebook_entry_ids_sql = "('')"
else:
    # Quote each ID and join them with commas, then wrap in parentheses
    quoted_ids = [f"'{id_}'" for id_ in pricebook_entry_ids]
    pricebook_entry_ids_sql = f"({', '.join(quoted_ids)})"

query = (
    "SELECT "
    "REPLACE(TRIM(oi.OrderId), '#', '') AS OrderId, "
    "REPLACE(TRIM(o.OwnerId), '#', '') AS OwnerId, "
    "oi.Quantity, "
    "oi.UnitPrice "
    "FROM OrderItem oi "
    "JOIN \"Order\" o ON REPLACE(TRIM(oi.OrderId), '#', '') = REPLACE(TRIM(o.Id), '#', '') "
    "WHERE REPLACE(TRIM(oi.PriceBookEntryId), '#', '') IN " + pricebook_entry_ids_sql + ";"
)

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-7477208485156344770': [{'PricebookEntryId': '01uWt0000027PDRIA2'}, {'PricebookEntryId': '01uWt0000027P8cIAE'}, {'PricebookEntryId': '01uWt0000027Q34IAE'}, {'PricebookEntryId': '01uWt0000027PjhIAE'}, {'PricebookEntryId': '01uWt0000027PJtIAM'}, {'PricebookEntryId': '01uWt0000027PIIIA2'}, {'PricebookEntryId': '01uWt0000027P5NIAU'}, {'PricebookEntryId': '01uWt0000027PIHIA2'}, {'PricebookEntryId': '01uWt0000027PtOIAU'}, {'PricebookEntryId': '01uWt0000027P8bIAE'}, {'PricebookEntryId': '01uWt0000027PLVIA2'}, {'PricebookEntryId': '01uWt0000027PBpIAM'}, {'PricebookEntryId': '01uWt0000027PGfIAM'}, {'PricebookEntryId': '01uWt0000027P3lIAE'}, {'PricebookEntryId': '01uWt0000027PTZIA2'}, {'PricebookEntryId': '01uWt0000027PVBIA2'}, {'PricebookEntryId': '01uWt0000027PF3IAM'}, {'PricebookEntryId': '01uWt0000027PADIA2'}, {'PricebookEntryId': '01uWt0000027P6zIAE'}, {'PricebookEntryId': '01uWt0000027POjIAM'}]}

exec(code, env_args)
