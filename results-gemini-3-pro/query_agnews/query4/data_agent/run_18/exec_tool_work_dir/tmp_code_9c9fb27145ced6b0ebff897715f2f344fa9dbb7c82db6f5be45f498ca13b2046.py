code = """import json
import collections

# Load metadata (2015 articles)
var_meta = locals()['var_function-call-4607361516680581530']
if isinstance(var_meta, str):
    with open(var_meta, 'r') as f:
        meta_list = json.load(f)
else:
    meta_list = var_meta

meta_map = {str(item['article_id']): item['region'] for item in meta_list}

# Load articles content
var_articles = locals()['var_function-call-12750341033928949967']
if isinstance(var_articles, str):
    with open(var_articles, 'r') as f:
        articles_list = json.load(f)
else:
    articles_list = var_articles

debug_info = {}
debug_info['meta_count'] = len(meta_map)
debug_info['articles_count'] = len(articles_list)

intersection_count = 0
sample_matches = []
# Check intersection
for article in articles_list:
    aid = str(article['article_id'])
    if aid in meta_map:
        intersection_count += 1
        if len(sample_matches) < 5:
            sample_matches.append(article['title'])

debug_info['intersection_count'] = intersection_count
debug_info['sample_matches'] = sample_matches

# Classification logic check
categories = {
    "Sports": ["sport", "game", "match", "score", "team", "league", "cup", "olympic", "football", "soccer", "baseball", "basketball", "cricket", "tennis", "hockey", "golf", "nascar", "champion", "medal", "athlete", "coach", "stadium", "nba", "nfl", "mlb", "nhl", "fifa", "uefa", "racing", "rugby", "boxing", "wrestling"],
    "Business": ["business", "market", "stock", "economy", "economic", "trade", "money", "bank", "financial", "finance", "company", "profit", "loss", "dollar", "euro", "oil", "price", "deal", "merger", "acquisition", "sales", "revenue", "ceo", "wall st", "nasdaq", "dow", "investor", "shares", "inflation", "rate"],
    "Sci/Tech": ["science", "technology", "tech", "computer", "software", "internet", "web", "online", "mobile", "phone", "apple", "google", "microsoft", "intel", "nasa", "space", "orbit", "planet", "study", "research", "medical", "virus", "robot", "digital", "wireless", "broadband", "chip", "satellite", "astronomy", "biology"],
    "World": ["world", "international", "war", "peace", "conflict", "military", "army", "government", "president", "minister", "election", "vote", "parliament", "congress", "treaty", "un", "united nations", "nato", "eu", "china", "russia", "iraq", "iran", "korea", "israel", "palestine", "syria", "afghanistan", "terrorist", "attack", "bomb", "crisis", "refugee", "diplomat", "foreign", "official", "leader", "state", "nuclear", "troops", "rebels", "protest", "police", "kill", "dead", "baghdad", "kabul", "beijing", "moscow", "gaza", "prime minister"]
}

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in categories}
    for cat, keywords in categories.items():
        for kw in keywords:
            if kw in text:
                scores[cat] += 1
    max_cat = max(scores, key=scores.get)
    if scores[max_cat] == 0:
        return "None", scores
    return max_cat, scores

classification_samples = []
# Check classification on first 10 articles (regardless of year)
for article in articles_list[:10]:
    text = article.get('title', "") + " " + article.get('description', "")
    cat, scores = classify(text)
    classification_samples.append({"text": text[:100], "cat": cat, "scores": scores})

debug_info['classification_samples'] = classification_samples

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-4607361516680581530': 'file_storage/function-call-4607361516680581530.json', 'var_function-call-4668912077434412794': 6696, 'var_function-call-12275785215919282874': [{'_id': '6944fef5545aa6729352eb7e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944fef5545aa6729352eb7f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944fef5545aa6729352eb80', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944fef5545aa6729352eb81', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944fef5545aa6729352eb82', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-5711343954142234108': 'file_storage/function-call-5711343954142234108.json', 'var_function-call-12750341033928949967': [{'_id': '6944fef5545aa6729352eb7e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944fef5545aa6729352eb7f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944fef5545aa6729352eb80', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944fef5545aa6729352eb81', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944fef5545aa6729352eb82', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-11979918585808351593': {'region': None, 'count': 0}, 'var_function-call-9255679222197522584': 'Done'}

exec(code, env_args)
