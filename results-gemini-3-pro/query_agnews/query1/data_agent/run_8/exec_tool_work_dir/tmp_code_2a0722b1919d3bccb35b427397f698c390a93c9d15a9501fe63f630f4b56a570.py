code = """import json
import re

with open(locals()['var_function-call-8284316981365420739'], 'r') as f:
    articles = json.load(f)

strong_sports = set([
    "football", "basketball", "baseball", "soccer", "tennis", "hockey", "golf", "rugby", "cricket", 
    "boxing", "wrestling", "olympic", "olympics", "medal", "medals", "tournament", "championship", 
    "championships", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "nascar", "wimbledon", 
    "quarterback", "touchdown", "goalkeeper", "pitcher", "homerun", "inning", "puck", "athlete", 
    "athletes", "gymnastics", "swimming", "davis cup", "ryder cup", "world cup", "super bowl",
    "grand prix", "cup", "league" 
    # Added "cup", "league", "grand prix"
])

disq = set([
    "market", "stock", "price", "company", "profit", "revenue", "election", "president", "minister", 
    "iraq", "war", "police", "court", "judge", "senate", "congress", "bush", "kerry", "dollar", 
    "economy", "bank", "software", "microsoft", "google", "internet", "business", "merger", 
    "acquisition", "corp", "inc", "ceo", "executive", "sales", "ad", "advertisement", "linux", 
    "solaris", "intel", "amd"
])

def is_sports(text):
    text = text.lower()
    words = re.findall(r'\w+', text)
    strong_count = 0
    disq_count = 0
    for w in words:
        if w in strong_sports: strong_count += 1
        if w in disq: disq_count += 1
    
    if strong_count > 0 and strong_count > disq_count:
        return True
    return False

articles.sort(key=lambda x: len(x['description']), reverse=True)

matches = []
for art in articles:
    ft = art['title'] + " " + art['description']
    if is_sports(ft):
        matches.append(art)
        if len(matches) >= 3:
            break

print("__RESULT__:")
print(json.dumps(matches))"""

env_args = {'var_function-call-5600887256776046897': [{'_id': '694468d48f62606ef06538a3', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-6243788860290969808': ['authors', 'article_metadata'], 'var_function-call-621124544545937450': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-14125888797793058960': [{'_id': '694468d48f62606ef06538a3', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694468d48f62606ef06538a4', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694468d48f62606ef06538a5', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694468d48f62606ef06538a6', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694468d48f62606ef06538a7', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-371116049882488257': [{'author_id': '0', 'name': 'Felicia Miles'}, {'author_id': '1', 'name': 'Stacy Hunt'}, {'author_id': '2', 'name': 'Carol Reed'}, {'author_id': '3', 'name': 'Dr. Daniel Brown'}, {'author_id': '4', 'name': 'Andre Lam MD'}], 'var_function-call-16428439284826624530': [{'_id': '694468d48f62606ef06538a3', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694468d48f62606ef06538a4', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694468d48f62606ef06538a5', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694468d48f62606ef06538a6', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694468d48f62606ef06538a7', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7895339117705645390': {'count': 5, 'sample_titles': ['Wall St. Bears Claw Back Into the Black (Reuters)', 'Carlyle Looks Toward Commercial Aerospace (Reuters)', "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'Oil prices soar to all-time record, posing new menace to US economy (AFP)']}, 'var_function-call-15665066354817605845': 'file_storage/function-call-15665066354817605845.json', 'var_function-call-4236206756542118061': {'count': 10000}, 'var_function-call-8284316981365420739': 'file_storage/function-call-8284316981365420739.json', 'var_function-call-1559858938885482885': {'_id': '694468d48f62606ef0664643', 'title': '2004 US Senate Outlook', 'description': "With all the hoopla over Bush and Kerry, some of you may not have been paying close attention to the other races going on in this loaded US political season. I've read a good dozen or so Senate outlooks, and my blurry eyes and spinning brain kept getting lost in all the numbers and losing track of who, ultimately, was likely to control the Senate on November third. So I made my very own Senate outlook to figure it out (or add further confusion, depending on what you think of my predictions). The bad news is, we probably won't know who controls the Senate on November third. The good news, if you're a Democrat (or a person who loves one), is that my best guess at this point is that when the dust settles, Democrats will probably be in control by the very slimmest possible margin. Shock! But everyone knows the Dems have no chance of taking either house of Congress. I think everyone hasn't been paying attention. Read on for my rundown."}, 'var_function-call-7699471574982602287': {'_id': '694468d48f62606ef06562b4', 'title': "Baltimore's  quot;Free Books! quot; Charity in Dire Straits", 'description': 'I spend anywhere from three to eight hours every week sweating along with a motley crew of local misfits, shelving, sorting, and hauling ton after ton of written matter in a rowhouse basement in Baltimore. We have no heat nor air conditioning, but still, every week, we come and work. Volunteer night is Wednesday, but many of us also work on the weekends, when we\'re open to the public. There are times when we\'re freezing and we have to wear coats and gloves inside, making handling books somewhat tricky; other times, we\'re all soaked with sweat, since it\'s 90 degrees out and the basement is thick with bodies. One learns to forget about personal space when working at The Book Thing, since you can scarcely breathe without bumping into someone, and we are all so accustomed to having to scrape by each other that most of us no longer bother to say "excuse me" unless some particularly dramatic brushing occurs. '}, 'var_function-call-1516796857255561872': {'_id': '694468d58f62606ef066eca5', 'title': 'Sprint: No comment on reported Nextel merger talks', 'description': 'WASHINGTON - Rumored merger talks between Sprint and Nextel Communications Thursday were met with a "no comment" from Sprint.&lt;p&gt;ADVERTISEMENT&lt;/p&gt;&lt;p&gt;&lt;img src="http://ad.doubleclick.net/ad/idg.us.ifw.general/solaris;sz=1x1;ord=200301151450?" width="1" height="1" border="0"/&gt;&lt;a href="http://ad.doubleclick.net/clk;12204780;10550054;n?http://ad.doubleclick.net/clk;12165994;10522295;g?http://www.sun.com/solaris10"&gt;Solaris 10(TM) OS: Position your business ten moves ahead.&lt;/a&gt;&lt;br/&gt;Solaris 10 OS has arrived and provides even more\\reasons for the world\'s most demanding businesses\\to operate on this, the leading UNIX platform.\\Like the fact you can run Linux and Solaris applications\\side-by-side and run the same OS on SPARC(R),\\AMD Opteron(TM), and Intel processor-based systems.\\Discover more reasons and how Solaris 10 OS can move\\your business ahead today.&lt;/p&gt;'}, 'var_function-call-8082170655389975928': {'_id': '694468d48f62606ef065b3b9', 'title': 'Cavaliers, Hokies Play Host', 'description': "Akron at No. 12 Virginia &lt;br&gt;   Where:  Scott Stadium, Charlottesville&lt;br&gt;   When:  3 p.m.    Radio:  WTNT-570    Tickets:  Sold out &lt;br&gt;   Another Top QB:  Like North Carolina's Darian Durant last week, Akron quarterback Charlie Frye is the key to his team's slim chances of upsetting the Cavaliers. The 6-foot-4 senior, likened by Virginia Coach Al Groh to recent ACC stars Matt Schaub and Philip Rivers, ranks fourth among active NCAA quarterbacks with 9,048 career passing yards. In losses the past two weeks to Penn State and Middle Tennessee, Frye completed 60 of 80 passes for 622 yards. Weather permitting, he will present a challenge for an inexperienced Virginia secondary that made a few too many errors in deep coverage in its first two games."}}

exec(code, env_args)
