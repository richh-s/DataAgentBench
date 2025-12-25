code = """import json

# Load the result from the previous step
with open('var_function-call-2680107260476408076.json', 'r') as f:
    metadata_records = json.load(f)

# Extract article_ids. They seem to be integers in the DB description but strings in the preview ("3").
# The DB description says article_id (int). The preview shows strings. 
# It's safer to treat them as they appear in the articles_database. 
# Let's check the type.
# I'll extract them as is, but also convert to int if they look like digits, just in case the mongo db uses ints.
# Actually, the SQL result returns them as strings probably because of some serialization or the column type in SQLite was text (though desc says int).
# I'll prepare a list of IDs.

ids = [record['article_id'] for record in metadata_records]

# I need to know if I should query with strings or ints.
# The DB description for MongoDB says article_id is (int).
# The SQL DB description says article_id is (int).
# However, the preview output shows "article_id": "3". This implies the SQL driver returned strings.
# I will convert them to integers for the MongoDB query to be safe, as the schema description specifies int.

id_ints = [int(x) for x in ids]

print("__RESULT__:")
print(json.dumps(id_ints))"""

env_args = {'var_function-call-2680107260476408076': 'file_storage/function-call-2680107260476408076.json'}

exec(code, env_args)
