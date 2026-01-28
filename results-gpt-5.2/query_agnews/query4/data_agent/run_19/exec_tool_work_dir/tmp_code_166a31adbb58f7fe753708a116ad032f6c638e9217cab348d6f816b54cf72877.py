code = """import json, pandas as pd

meta_src = var_call_fbhyUopFqnyuaOVMGrrnYK8F
if isinstance(meta_src, str):
    with open(meta_src, 'r') as f:
        meta = json.load(f)
else:
    meta = meta_src

meta_df = pd.DataFrame(meta)
meta_df['article_id'] = meta_df['article_id'].astype(int)

# derive list of ids from 2015 metadata
ids = meta_df['article_id'].dropna().astype(int).unique().tolist()

# chunk query articles for those ids from mongo using $in
# We'll take manageable chunks
chunks = [ids[i:i+800] for i in range(0, len(ids), 800)]

print('__RESULT__:')
print(json.dumps({'n_ids': len(ids), 'n_chunks': len(chunks), 'first_chunk': chunks[0][:10], 'last_chunk_size': len(chunks[-1])}))"""

env_args = {'var_call_fbhyUopFqnyuaOVMGrrnYK8F': 'file_storage/call_fbhyUopFqnyuaOVMGrrnYK8F.json', 'var_call_qgtj10c1qo8C3FJDfGMQM6rm': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_call_eGbIZx2lmVO2Ifn3ehSVE5kc': {'region': None, 'world_article_count_2015': 0}, 'var_call_flgsIvucXY7PHhLQgTfqSk7f': [{'publication_date': '2004-01-01', 'n': '22'}, {'publication_date': '2004-01-02', 'n': '15'}, {'publication_date': '2004-01-03', 'n': '14'}, {'publication_date': '2004-01-04', 'n': '13'}, {'publication_date': '2004-01-05', 'n': '15'}], 'var_call_ZvdoSSETVsofTXsfp0tECSKG': [{'min_date': '2004-01-01', 'max_date': '2022-12-30', 'total': '127600'}], 'var_call_APd1ceK93rafQ8d5Ik7aDbRf': [{'n': '6696'}], 'var_call_pBevDdMHlocSiDEc1PqOFoON': [{'article_id': '13'}, {'article_id': '18'}, {'article_id': '26'}, {'article_id': '51'}, {'article_id': '52'}]}

exec(code, env_args)
