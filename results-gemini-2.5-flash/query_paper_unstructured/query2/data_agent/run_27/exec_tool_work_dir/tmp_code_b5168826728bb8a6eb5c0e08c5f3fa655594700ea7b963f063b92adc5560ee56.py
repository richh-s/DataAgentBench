code = """import json
import re

citation_data_path = locals()['var_function-call-7645638154055651717']
with open(citation_data_path, 'r') as f:
    citation_data = json.load(f)

# Extract unique titles from citation data
titles = [record['title'] for record in citation_data]

# Prepare to query paper_docs_database for each title
# Since I cannot make multiple tool calls in one step, I'll need to make a
# single query for all documents that match the titles.
# This might be tricky because MongoDB queries typically work on document content directly,
# not by matching a derived field like 'filename' to 'title'.
# However, the problem description states: "title: The title of the paper (matches the filename without .txt extension)"
# and "The paper title in the Citations SQLite table matches the filename (without .txt extension) of documents in MongoDB."
# So I can use the filename to match the title.

# I need to create a list of filenames from the titles.
filenames = [title + ".txt" for title in titles]

# Since the list of filenames can be very long, I'll query for a subset first
# to see the structure of the paper_docs documents.
# Then I'll refine the query to get all required documents.

# For now, I'll just select all documents, and then filter in python.
# This is a less efficient approach but avoids making too many specific Mongo queries.
# If the number of documents is extremely large, this approach may fail due to memory limits.
# Let's assume the total number of papers isn't excessively large for this problem.
# If I had the ability to iterate on tool calls, I would query for each title.
# For now, I will perform one query for all documents whose filenames match the titles.
# Since the problem statement says "Each document represents a single paper with its complete text",
# and "filename (str): Name of the source file (e.g., "A Lived Informatics Model of Personal Informatics.txt")",
# I can filter by filename.
# The `filename` field can be used in the filter.
# The filter would be {"filename": {"$in": filenames}}

# To avoid potential issues with very large numbers of filenames in a single query,
# let's try to query for a few first, and see if it works.
# Or, even better, if I can pass a list of titles as a filter to the MongoDB query.
# The tool description for query_db says:
# "For MongoDB, provide a JSON string representing the query, including `collection` field,
# and optional `filter`, `projection`, and `limit` fields."
# So I can use a filter like {"filename": {"$in": filenames}}.

# The problem states: "Each document contains the full text of an academic paper. For each paper, you may need to extract:
#     - title: The title of the paper (matches the filename without .txt extension)
#     - year: Publication year
#     - venue: Conference or journal venue (e.g., "CHI", "Ubicomp", "CSCW")
#     - source: Publisher (e.g., "ACM", "IEEE")"

# I need to get the 'text' field to extract the 'source'.
# Let's construct the MongoDB query.

# I'll query for all papers that have a filename matching one of the titles, and project only the filename and text.
# For now, to keep the query manageable, I will query for a subset of the filenames,
# and then extend it if this works.
# For simplicity, let's query all paper_docs and then filter in Python for now as suggested above.
# This assumes the total number of documents in paper_docs is not extremely large.

print("__RESULT__:")
print(json.dumps({"filenames_to_query_count": len(filenames)}))"""

env_args = {'var_function-call-7645638154055651717': 'file_storage/function-call-7645638154055651717.json', 'var_function-call-9199339358258958210': ['paper_docs']}

exec(code, env_args)
