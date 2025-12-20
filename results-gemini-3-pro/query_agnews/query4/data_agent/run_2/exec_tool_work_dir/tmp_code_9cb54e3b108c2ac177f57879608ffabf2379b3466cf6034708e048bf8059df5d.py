code = """import json
import collections
import re

# Load data (files are already there)
path_meta = locals()['var_function-call-4524539130792533253']
path_articles = locals()['var_function-call-8766970931896504381']

with open(path_meta, 'r') as f:
    meta_list = json.load(f)
meta_map = {str(item['article_id']): item['region'] for item in meta_list}

with open(path_articles, 'r') as f:
    articles_list = json.load(f)

# Join
articles_2015 = []
for art in articles_list:
    aid = str(art['article_id'])
    if aid in meta_map:
        articles_2015.append({
            'article_id': aid,
            'title': art.get('title', ''),
            'description': art.get('description', ''),
            'region': meta_map[aid]
        })

# Classification with Regex
categories = {
    'Sports': ["sport", "sports", "soccer", "football", "baseball", "basketball", "tennis", "golf", "hockey", "olympics", "olympic", "tournament", "championship", "league", "team", "teams", "athlete", "coach", "game", "games", "match", "score", "cup", "medal", "nfl", "nba", "mlb", "fifa", "racing", "driver"],
    'Business': ["business", "market", "markets", "economy", "economic", "financial", "finance", "stock", "stocks", "share", "shares", "invest", "investor", "investment", "bank", "banks", "profit", "profits", "loss", "trade", "deal", "merger", "acquisition", "company", "companies", "corp", "corporation", "sales", "revenue", "oil", "price", "prices", "wall st", "nasdaq", "dow", "dollar", "currency", "ceo", "earnings", "imf", "fed", "deficit", "inflation", "tax", "debt"],
    'Sci/Tech': ["science", "technology", "tech", "computer", "computers", "software", "hardware", "internet", "web", "online", "google", "microsoft", "apple", "iphone", "space", "nasa", "mars", "robot", "gadget", "device", "mobile", "wireless", "network", "silicon", "biology", "physics", "chemistry", "study", "research", "data", "cyber", "hacker", "virus", "browser", "server"],
    'World': ["world", "international", "politics", "political", "war", "wars", "conflict", "iraq", "iran", "syria", "afghanistan", "gaza", "israel", "palestine", "ukraine", "russia", "china", "eu", "european union", "un", "united nations", "government", "president", "prime minister", "minister", "official", "officials", "military", "army", "troops", "bomb", "attack", "attacks", "blast", "kill", "killed", "death", "dead", "disaster", "storm", "hurricane", "earthquake", "tsunami", "treaty", "diplomacy", "election", "vote", "poll", "parliament", "foreign", "refugee", "crisis", "terrorism", "terror", "nuclear", "protest", "police", "court", "judge", "law", "legal", "ban", "rights", "human rights", "security", "treaty", "senate", "congress", "parliament"]
}

# Compile regexes for performance and correctness
cat_regexes = {}
for cat, kws in categories.items():
    # Sort by length desc to match longer words first (though with \b it doesn't matter much)
    # Escape keywords just in case
    pattern = r'\b(' + '|'.join(re.escape(kw) for kw in kws) + r')\b'
    cat_regexes[cat] = re.compile(pattern)

def classify(title, desc):
    text = (title + " " + desc).lower()
    scores = {cat: 0 for cat in categories}
    for cat, regex in cat_regexes.items():
        # Count all non-overlapping matches
        matches = regex.findall(text)
        scores[cat] = len(matches)
    
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return "Unknown"
    
    # Tie breaking
    if scores['World'] == scores['Business'] and scores['World'] > 0:
        # Prioritize World if "war" or "politics" context
        if re.search(r'\b(war|military|attack|gov|president)\b', text):
            return "World"
        return "Business"
    
    # Tie breaking between Sci/Tech and Business (e.g. "Apple stocks")
    if scores['Sci/Tech'] == scores['Business'] and scores['Sci/Tech'] > 0:
        return "Business" # Usually stock news
        
    return best_cat

world_counts = collections.defaultdict(int)
debug_list = []

for art in articles_2015:
    cat = classify(art['title'], art['description'])
    if cat == 'World':
        world_counts[art['region']] += 1
        if len(debug_list) < 5:
            debug_list.append(art)

if world_counts:
    top_region = max(world_counts, key=world_counts.get)
    count = world_counts[top_region]
else:
    top_region = "None"
    count = 0

print("__RESULT__:")
print(json.dumps({
    "top_region": top_region, 
    "count": count, 
    "all_counts": world_counts,
    "sample_world_articles": [a['title'] for a in debug_list]
}))"""

env_args = {'var_function-call-4524539130792533253': 'file_storage/function-call-4524539130792533253.json', 'var_function-call-12841960327215520545': 'file_storage/function-call-12841960327215520545.json', 'var_function-call-17275925162365337320': [{'_id': '6944ea9ed4512ac83e64878c', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944ea9ed4512ac83e64878d', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944ea9ed4512ac83e64878e', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944ea9ed4512ac83e64878f', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944ea9ed4512ac83e648790', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-845048519728556146': {'top_region': 'None', 'count': 0, 'all_counts': {}}, 'var_function-call-15108040845174692452': {'count_2015': 0, 'sample_titles': [], 'sample_descriptions': []}, 'var_function-call-16784580192302694402': {'len_articles': 5, 'first_ids': ['0', '1', '2', '3', '4']}, 'var_function-call-8766970931896504381': 'file_storage/function-call-8766970931896504381.json', 'var_function-call-10866169233379572562': {'top_region': 'Europe', 'count': 452, 'all_counts': {'Asia': 434, 'North America': 449, 'South America': 430, 'Europe': 452, 'Africa': 448}, 'total_2015_classified_world': 2213, 'total_2015_articles': 5226, 'sample_world_articles': ['Oracle Sales Data Seen Being Released (Reuters)', "What's in a Name? Well, Matt Is Sexier Than Paul (Reuters)", 'Indictments Using DNA on Rise Nationally (AP)', "News: Climate Change Could Doom Alaska's Tundra", 'News: Warmer Weather, Human Disturbances Interact to Change Forests']}}

exec(code, env_args)
