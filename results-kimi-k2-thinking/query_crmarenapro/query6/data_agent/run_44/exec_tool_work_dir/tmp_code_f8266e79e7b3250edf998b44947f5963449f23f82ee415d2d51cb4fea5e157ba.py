code = """# Load the quote IDs to check for corruption patterns
quote_ids = var_functions.query_db:2

# Analyze leading # patterns
with_leading_hash = sum(1 for row in quote_ids if row['Id'].startswith('#'))
without_leading_hash = len(quote_ids) - with_leading_hash

print('__RESULT__:')
print({
    'total': len(quote_ids),
    'with_leading_hash': with_leading_hash,
    'without_leading_hash': without_leading_hash,
    'sample_ids': [row['Id'] for row in quote_ids[:5]]
})"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'Id': '#0Q0Wt000001WLjvKAG'}, {'Id': '0Q0Wt000001WRJ3KAO'}, {'Id': '0Q0Wt000001WKEPKA4'}, {'Id': '0Q0Wt000001WREDKA4'}, {'Id': '0Q0Wt000001WRHRKA4'}, {'Id': '0Q0Wt000001WRCbKAO'}, {'Id': '0Q0Wt000001WRFpKAO'}, {'Id': '0Q0Wt000001WMHpKAO'}, {'Id': '0Q0Wt000001WNnKKAW'}, {'Id': '#0Q0Wt000001WS5RKAW'}, {'Id': '0Q0Wt000001WMpjKAG'}, {'Id': '#0Q0Wt000001WRpKKAW'}, {'Id': '0Q0Wt000001WKW7KAO'}, {'Id': '#0Q0Wt000001WQRqKAO'}, {'Id': '0Q0Wt000001WMcnKAG'}, {'Id': '0Q0Wt000001WO54KAG'}, {'Id': '0Q0Wt000001WSLZKA4'}, {'Id': '0Q0Wt000001WP5zKAG'}, {'Id': '0Q0Wt000001WS5SKAW'}, {'Id': '0Q0Wt000001WMzMKAW'}]}

exec(code, env_args)
