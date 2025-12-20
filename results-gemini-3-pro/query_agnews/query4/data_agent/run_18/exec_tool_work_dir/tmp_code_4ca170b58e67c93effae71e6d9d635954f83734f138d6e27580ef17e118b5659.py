code = """import json
import collections

# Load metadata (2015 articles)
path_meta = locals()['var_function-call-4607361516680581530']
with open(path_meta, 'r') as f:
    meta_list = json.load(f)

meta_map = {str(item['article_id']): item['region'] for item in meta_list}

# Load articles content
path_articles = locals()['var_function-call-481166772783270383']
with open(path_articles, 'r') as f:
    articles_list = json.load(f)

# Define Keywords
categories = {
    "Sports": ["sport", "game", "match", "score", "team", "league", "cup", "olympic", "football", "soccer", "baseball", "basketball", "cricket", "tennis", "hockey", "golf", "nascar", "champion", "medal", "athlete", "coach", "stadium", "nba", "nfl", "mlb", "nhl", "fifa", "uefa", "racing", "rugby", "boxing", "wrestling", "f1", "motor", "driver", "tournament"],
    "Business": ["business", "market", "stock", "economy", "economic", "trade", "money", "bank", "financial", "finance", "company", "profit", "loss", "dollar", "euro", "oil", "price", "deal", "merger", "acquisition", "sales", "revenue", "ceo", "wall st", "nasdaq", "dow", "investor", "shares", "inflation", "rate", "corp", "inc", "ltd", "fed", "reserve", "jobs", "hiring", "earnings"],
    "Sci/Tech": ["science", "technology", "tech", "computer", "software", "internet", "web", "online", "mobile", "phone", "apple", "google", "microsoft", "intel", "nasa", "space", "orbit", "planet", "study", "research", "medical", "virus", "robot", "digital", "wireless", "broadband", "chip", "satellite", "astronomy", "biology", "physics", "device", "app", "facebook", "amazon", "cyber", "hacker", "data", "browser"],
    "World": ["world", "international", "war", "peace", "conflict", "military", "army", "government", "president", "minister", "election", "vote", "parliament", "congress", "treaty", "un", "united nations", "nato", "eu", "china", "russia", "iraq", "iran", "korea", "israel", "palestine", "syria", "afghanistan", "terrorist", "attack", "bomb", "crisis", "refugee", "diplomat", "foreign", "official", "leader", "state", "nuclear", "troops", "rebels", "protest", "police", "kill", "dead", "baghdad", "kabul", "beijing", "moscow", "gaza", "prime minister", "ukraine", "isis", "islamic state", "boko haram", "al qaeda", "yemen", "saudi", "putin", "obama", "merkel", "cameron", "hollande", "xi jinping", "greece", "turkey", "egypt", "libya", "sudan", "somalia", "nigeria", "venezuela", "brazil", "mexico", "argentina", "colombia", "peru", "chile", "pakistan", "india", "bangladesh", "myanmar", "thailand", "indonesia", "philippines", "vietnam", "malaysia", "australia", "zealand", "canada", "britain", "uk", "france", "germany", "italy", "spain", "poland", "sweden", "norway", "finland", "denmark", "netherlands", "belgium", "austria", "switzerland", "ireland", "portugal", "greece", "hungary", "czech", "romania", "bulgaria", "serbia", "croatia", "bosnia", "albania", "macedonia", "montenegro", "kosovo", "slovenia", "slovakia", "estonia", "latvia", "lithuania", "belarus", "ukraine", "moldova", "georgia", "armenia", "azerbaijan", "kazakhstan", "uzbekistan", "turkmenistan", "kyrgyzstan", "tajikistan"]
}

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in categories}
    for cat, keywords in categories.items():
        for kw in keywords:
            if kw in text:
                scores[cat] += 1
    
    # Special handling: "World Cup" is Sports
    if "world cup" in text:
        scores["Sports"] += 5
    
    max_cat = max(scores, key=scores.get)
    if scores[max_cat] == 0:
        return "None"
    return max_cat

region_world_counts = collections.defaultdict(int)
intersection_count = 0

for article in articles_list:
    aid = str(article['article_id'])
    if aid in meta_map:
        intersection_count += 1
        title = article.get('title', "")
        desc = article.get('description', "")
        text = title + " " + desc
        
        category = classify(text)
        
        if category == "World":
            region = meta_map[aid]
            region_world_counts[region] += 1

# Find max region
if region_world_counts:
    max_region = max(region_world_counts, key=region_world_counts.get)
    max_count = region_world_counts[max_region]
    result = {"region": max_region, "count": max_count, "all_counts": region_world_counts, "intersection": intersection_count}
else:
    result = {"region": None, "count": 0, "intersection": intersection_count}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-4607361516680581530': 'file_storage/function-call-4607361516680581530.json', 'var_function-call-4668912077434412794': 6696, 'var_function-call-12275785215919282874': [{'_id': '6944fef5545aa6729352eb7e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944fef5545aa6729352eb7f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944fef5545aa6729352eb80', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944fef5545aa6729352eb81', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944fef5545aa6729352eb82', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-5711343954142234108': 'file_storage/function-call-5711343954142234108.json', 'var_function-call-12750341033928949967': [{'_id': '6944fef5545aa6729352eb7e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944fef5545aa6729352eb7f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944fef5545aa6729352eb80', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944fef5545aa6729352eb81', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944fef5545aa6729352eb82', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-11979918585808351593': {'region': None, 'count': 0}, 'var_function-call-9255679222197522584': 'Done', 'var_function-call-937582430899318814': {'meta_count': 6696, 'articles_count': 5, 'intersection_count': 0, 'sample_matches': [], 'classification_samples': [{'text': "Wall St. Bears Claw Back Into the Black (Reuters) Reuters - Short-sellers, Wall Street's dwindling\\b", 'cat': 'Business', 'scores': {'Sports': 0, 'Business': 1, 'Sci/Tech': 0, 'World': 1}}, {'text': 'Carlyle Looks Toward Commercial Aerospace (Reuters) Reuters - Private investment firm Carlyle Group,', 'cat': 'World', 'scores': {'Sports': 0, 'Business': 1, 'Sci/Tech': 1, 'World': 2}}, {'text': "Oil and Economy Cloud Stocks' Outlook (Reuters) Reuters - Soaring crude prices plus worries\\about th", 'cat': 'Business', 'scores': {'Sports': 0, 'Business': 5, 'Sci/Tech': 0, 'World': 1}}, {'text': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters) Reuters - Authorities have halted oil e', 'cat': 'World', 'scores': {'Sports': 0, 'Business': 1, 'Sci/Tech': 1, 'World': 3}}, {'text': 'Oil prices soar to all-time record, posing new menace to US economy (AFP) AFP - Tearaway world oil p', 'cat': 'Business', 'scores': {'Sports': 0, 'Business': 4, 'Sci/Tech': 0, 'World': 3}}]}, 'var_function-call-481166772783270383': 'file_storage/function-call-481166772783270383.json'}

exec(code, env_args)
