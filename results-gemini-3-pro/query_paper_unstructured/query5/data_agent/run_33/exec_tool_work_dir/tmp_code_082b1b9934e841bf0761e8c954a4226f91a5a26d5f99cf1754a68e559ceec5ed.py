code = """import json
import os

# Load citations
file_path = locals()['var_function-call-4107798492102735370']
with open(file_path, 'r') as f:
    citations_data = json.load(f)

# Map filename -> citation_count
# filename = title + ".txt"
filename_counts = {}
filenames = []
for item in citations_data:
    fname = item['title'] + ".txt"
    filename_counts[fname] = item['citation_count']
    filenames.append(fname)

# Save the map for later use
with open('citation_counts_map.json', 'w') as f:
    json.dump(filename_counts, f)

# Construct the query filter
mongo_filter = {"filename": {"$in": filenames}}
query_str = json.dumps({"collection": "paper_docs", "filter": mongo_filter})

print(f"Query length: {len(query_str)}")

# If length is acceptable, print it. Otherwise print chunks.
if len(query_str) < 10000:
    print("__RESULT__:")
    print(query_str)
else:
    print("Query too long")
    # Print the first batch query
    batch1 = filenames[:50]
    query1 = json.dumps({"collection": "paper_docs", "filter": {"filename": {"$in": batch1}}})
    print("__RESULT__:")
    print(query1)"""

env_args = {'var_function-call-4107798492102735370': 'file_storage/function-call-4107798492102735370.json', 'var_function-call-13958868829656037489': {'sample_filename': 'Sundroid: Solar Radiation Awareness with Smartphones.txt', 'titles_count': 188}, 'var_function-call-16540664085193316271': 'file_storage/function-call-16540664085193316271.json', 'var_function-call-15194230552685176329': 'file_storage/function-call-15194230552685176329.json'}

exec(code, env_args)
