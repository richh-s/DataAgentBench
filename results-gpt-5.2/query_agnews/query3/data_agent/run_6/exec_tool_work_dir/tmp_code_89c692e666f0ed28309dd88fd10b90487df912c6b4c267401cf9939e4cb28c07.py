code = """import json, pandas as pd, re

# Load metadata article_ids and dates for Europe 2010-2020
meta_path = var_call_b7HeGfRV4nk9z9C07TIuGo9Q
with open(meta_path, 'r') as f:
    meta_list = json.load(f)
meta_ids = set(int(r['article_id']) for r in meta_list)

# Articles content
articles = pd.DataFrame(var_call_4OlB5V3gnxAnDPibobVsNMtK)
articles['article_id'] = articles['article_id'].astype(int)
articles = articles[articles['article_id'].isin(meta_ids)].copy()

# Simple keyword-based business classifier
business_kw = re.compile(r"\b(stock|stocks|market|markets|wall st|wall street|nasdaq|dow|s&p|earnings|profit|revenue|bank|banks|banking|loan|loans|bond|bonds|treasury|fed|interest rate|inflation|economy|economic|gdp|trade|tariff|import|export|exports|currency|currencies|dollar|euro|yen|oil|crude|gas|energy|company|companies|firm|firms|ceo|merger|acquisition|ipo|shares|shareholder|dividend|finance|financial|business|industry|corporate|retail|sales)\b",
                       re.IGNORECASE)

def is_business(row):
    text = f"{row.get('title','')} {row.get('description','')}"
    return bool(business_kw.search(text))

articles['is_business'] = articles.apply(is_business, axis=1)

# Need yearly counts: pull publication_date for those ids
# Build a dataframe from metadata with publication_date
meta_df = pd.DataFrame(meta_list)
meta_df['article_id'] = meta_df['article_id'].astype(int)
meta_df['publication_date'] = pd.to_datetime(meta_df['publication_date'], errors='coerce')
meta_df['year'] = meta_df['publication_date'].dt.year

biz_ids = set(articles.loc[articles['is_business'], 'article_id'].astype(int))
biz_meta = meta_df[meta_df['article_id'].isin(biz_ids)].copy()

year_counts = biz_meta.groupby('year')['article_id'].nunique().reindex(range(2010,2021), fill_value=0)
avg_per_year = year_counts.mean()

out = {
    'average_business_articles_per_year_europe_2010_2020': float(avg_per_year),
    'total_business_articles_2010_2020': int(year_counts.sum()),
    'years': {int(y): int(c) for y,c in year_counts.items()}
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_BYEYRTbp8MVVlsKwooJZTNUl': [{'cnt': '14860'}], 'var_call_b7HeGfRV4nk9z9C07TIuGo9Q': 'file_storage/call_b7HeGfRV4nk9z9C07TIuGo9Q.json', 'var_call_4OlB5V3gnxAnDPibobVsNMtK': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
