# -*- coding:utf-8 -*-

"""
    desc:用gensim提取文章主题测试
"""
from gensim import corpora, models, similarities
from base.svmtrain import cutwords, init_stopwords

html_content = """<p>点击上面蓝字“脉脉养生”关注，疾病搜索、经典养生知识不再只看朋友圈.</p>
<p>美国转基因推手把地点选中了阿根廷，阿根廷的人民也因此成为转基因作物的第一批活体实验品。到2004年，阿根廷的转基因作物种 植面积为3400万英亩，转基因农业的历史和阿根廷的“大豆革命”，是一个国家在“进步”的名义下全面失去粮食自给能力的典型案例。</p>
<img src="http://mmbiz.qpic.cn/mmbiz/Q7Dy5s5ibWGsaYbzbv3jvFYOE5hhC0WUKEjfD7XRjtp8VoicYVIic7xSXQWX3spZHrgURdMI4WKvK5rL9uInQlxgQ/0?wxfmt=jpeg" />
<p>孟山都转基因 //完全改变了阿根廷</p>
<p>阿根廷转基因大豆革命，在不到10年的时间里，这个国家的农业经济被彻底改造了。</p>
<p>20世纪70年代，在债务危机之前，大豆在这个国家的农业经济中所占地微不足道，种植面积有9500公顷。</p>
<p>在那些年月里，一个典型的家庭农场种植多种蔬菜和粮食作物，还养些鸡，有的还养有少量的牛，来生产牛奶、奶酪和牛肉。</p>
<p>阿根廷用转基因的结果</p>
<img src="http://mmbiz.qpic.cn/mmbiz/SwsiadjW9rKBo1gnJic2Gvk4dKQsPZPlm0wEnO09WsapGGckoVoqrkxgmIbmNs3ZIcVbs8XXafzbloCnuvpBYvgw/0?wxfmt=jpeg&wxfrom=5" />
<p>因转基因阿根廷的贫困率从5%上升到了51%</p>
<p>20世纪70年代，阿根廷的生活水平是拉丁美洲最高的国家之一。官方公布的生活在贫困线之下的人口比例1970年仅为5%，到1998年， 这个数字陡升至 30%。</p>
<p>而到了2002年，又激增至51%。以前在阿根廷闻所未闻的营养不良现象，到2003年上升到约占3700万总人口的11%～17%。</p>
<p>在因国家拖欠债务而引发的全国性严重经济危机当中，阿根廷人发现，他们已经不能再依靠小块土地生存。</p>
<p>这些土地已经被大片的转基因大豆所占据，堵死了种植能维持生存的一般作物的出路。</p>
<img src="http://mmbiz.qpic.cn/mmbiz/SwsiadjW9rKBo1gnJic2Gvk4dKQsPZPlm0Mvty2o1B3PiaDia2mwwgVYcfR9APAgAW3luxicv1WiacLT7q0as5V91vLQ/0?wxfmt=jpeg&wxfrom=5" />
<p>血淋淋的案例 //
你们还想吃转基因吗？</p>
<p>在阿根廷，农作物农药喷洒量从1990年的9百万加仑至今天的8千4百万加仑已增加了九倍，然而，在这个南美洲国家存在着各种无视法规现象，使人暴露在危险中。</p>
<p>这些滥用的化学品污染了家园、教室以及饮用水，医生和科学家均提出警告说，不受控制的喷涂将会在全国范围内引起严重的健康问 题。</p>
<p>那些被转基因害苦的阿根廷人民</p>
<p>加油工巴萨维尔瓦素在巴萨维尔瓦索，47岁的前雇农FabianTomasi站在家里展示他瘦弱的身体。Tomasi的工作是为快速飞行的作物喷 粉飞机加油，但他说从来没有人训练他如何处理农药，现在他已经濒临死亡。</p>
<p>在巴萨维尔瓦索，47岁的前雇农FabianTomasi站在家里展示他瘦弱的身体。</p>
<p>Tomasi的工作是为快速飞行的作物喷粉飞机加油，但他说从来没有人训练他如何处理农药，现在他已经濒临死亡。</p>
<img src="http://mmbiz.qpic.cn/mmbiz/SwsiadjW9rKBo1gnJic2Gvk4dKQsPZPlm0SDzOlz5Vz7SIO6YF6nUpAhY8WzIzglbpmiaqCCYKH2Gdos6Hz8JJ8ow/0?wxfmt=jpeg&wxfrom=5" />
<p>5岁的AixaCano5岁的AixaCano身上长满了连医生也无法解释的痣毛，她正坐在自家门口的台阶上。虽然无法证明，但医生说，Cano的 身体缺陷可能与农药有关。在Chaco，由于阿根廷急剧扩大农业生物技术，儿童的先天缺陷比起其他地方高出四倍。</p>
<p>5岁的AixaCano身上长满了连医生也无法解释的痣毛，她正坐在自家门口的台阶上。</p>
<p>虽然无法证明，但医生说，Cano的身体缺陷可能与农药有关。在Chaco，由于阿根廷急剧扩大农业生物技术，儿童的先天缺陷比起其他地方高出四倍。</p>
<img src="http://mmbiz.qpic.cn/mmbiz/SwsiadjW9rKBo1gnJic2Gvk4dKQsPZPlm0cBPalpFdf6pAbNiaZy5Yl2JeeRnKqRgjTBiaiaiaMhBibCNmbF5aibC6MyjA/0?wxfmt=jpeg&wxfrom=5" />
<p>阿根廷孟山都回收中心去年5月2日，位于阿根廷圣地亚哥埃斯特罗省Quimili的孟山都公司回收中心，废弃的空农药容器。农药喷洒已经增加了九倍，从1990年的9百万加仑至今天的8千4百万加仑。草甘膦是孟山都公司农药产品的主要成分，每亩比在美国多用了大概八至 十倍，然而，阿根廷没有正规的农用化学品国家标准，也没有制定的规则供各省市执行。</p>
<p>去年5月2日，位于阿根廷圣地亚哥埃斯特罗省Quimili的孟山都公司回收中心，废弃的空农药容器。</p>
<p>农药喷洒已经增加了九倍，从1990年的9百万加仑至今天的8千4百万加仑。</p>
<p>草甘膦是孟山都公司农药产品的主要成分，每亩比在美国多用了大概八至十倍，然而，阿根廷没有正规的农用化学品国家标准，也没 有制定的规则供各省市执行。</p>
<img src="http://mmbiz.qpic.cn/mmbiz/SwsiadjW9rKBo1gnJic2Gvk4dKQsPZPlm0dDV0PKo0W7l89fFubHF2Gv3N1SIwWFD2J6UE6kqAv4EvhuqF0zmjiaQ/0?wxfmt=jpeg&wxfrom=5" />
<p>两岁的CamilaVeron两岁的小女孩CamilaVeron，患有天生的多器官问题和严重残疾。医生告诉Camila的母亲，罪魁祸首应该是农药， 过多的化学物品能引起癌症或其他先天缺陷。</p>
<p>两岁的小女孩CamilaVeron，患有天生的多器官问题和严重残疾。</p>
<p>医生告诉Camila的母亲，罪魁祸首应该是农药，过多的化学物品能引起癌症或其他先天缺陷。</p>
<img src="http://mmbiz.qpic.cn/mmbiz/SwsiadjW9rKBo1gnJic2Gvk4dKQsPZPlm0497WqTDqrGqLjtZmXoOCoaClnXJ0eBC7oFmbZMWJib96Xp4uqCrSVbQ/0?wxfmt=jpeg&wxfrom=5" />
<p>阿维亚特莱生物技术大豆种植基地去年5月31日，在阿维亚特莱生物技术大豆种植基地，女孩们在玩弹弓。在这17年里，阿根廷整个国家的大豆作物和几乎所有的玉米棉花已成为转基因，圣路易斯孟山都公司承诺转基因是一种使用较少杀虫剂和化学物是就能获得巨大产量的专利种子。但情况却正相反，据该国农业部说，从1990年的9百万加仑至今天的8千4百万加仑，农药喷洒已经增加了九倍。</p>
<p>去年5月31日，在阿维亚特莱生物技术大豆种植基地，女孩们在玩弹弓。在这17年里，阿根廷整个国家的大豆作物和几乎所有的玉米棉花已成为转基因，圣路易斯孟山都公司承诺转基因是一种使用较少杀虫剂和化学物是就能获得巨大产量的专利种子。</p>
<p>但情况却正相反，据该国农业部说，从1990年的9百万加仑至今天的8千4百万加仑，农药喷洒已经增加了九倍。</p>
<img src="http://mmbiz.qpic.cn/mmbiz/SwsiadjW9rKBo1gnJic2Gvk4dKQsPZPlm0Xv5TYPPGhA22ZEkYnmg2Hud9g6dicEqzpKBrMDd6LTf4jrd3Bzb5wyQ/0?wxfmt=jpeg&wxfrom=5" />
<p>患了慢性呼吸系统疾病的儿童Erika（左）和她的孪生妹妹Macarena患有慢性呼吸系统疾病。她们在家中后院附近用回收的农药容器装水，用于冲洗厕所、养鸡和洗衣服。</p>
<p>Erika（左）和她的孪生妹妹Macarena患有慢性呼吸系统疾病。</p>
<p>她们在家中后院附近用回收的农药容器装水，用于冲洗厕所、养鸡和洗衣服。</p>
<img src="http://mmbiz.qpic.cn/mmbiz/SwsiadjW9rKBo1gnJic2Gvk4dKQsPZPlm0v9bEe7PlNOIpFqReAYic6Gpc4DBNjCSNCmNw6icOjXeddra9Qu0ib9R6w/0?wxfmt=jpeg&wxfrom=5" />
<p>化学品导致他患了脊椎病去年4月6日，阿根廷布宜诺斯艾利斯省的罗森，FelixSanRoman走在这片属于他的田地里，Roman向当地政府 抱怨化学品渗透到他家院子里，导致他的脊椎疾病并使他的牙齿脱落，但Roman说跟政府反应这些也于事无补。</p>
<p>去年4月6日，阿根廷布宜诺斯艾利斯省的罗森，FelixSanRoman走在这片属于他的田地里，Roman向当地政府抱怨化学品渗透到他家院 子里，导致他的脊椎疾病并使他的牙齿脱落，但Roman说跟政府反应这些也于事无补。</p>
<img src="http://mmbiz.qpic.cn/mmbiz/SwsiadjW9rKBo1gnJic2Gvk4dKQsPZPlm0RZIYKEMS7DvrN4FWw7SWIcX4Y2QiaUkjugkg2LuSIWNFkXHoCPtqs5Q/0?wxfmt=jpeg&wxfrom=5" />
<p>农药导致她两次流产4月1日，在阿根廷查科省的甘塞多，SilviaAlvarez靠着她家红色的砖上照看儿子EzequielMoreno，他患有先天性积水。Alvarez指责喷洒农药导致她两次流产，并对她儿子的健康造成影响。</p>
<p>4月1日，在阿根廷查科省的甘塞多，SilviaAlvarez靠着她家红色的砖上照看儿子EzequielMoreno，他患有先天性积水。Alvarez指责 喷洒农药导致她两次流产，并对她儿子的健康造成影响。</p>
<img src="http://mmbiz.qpic.cn/mmbiz/SwsiadjW9rKBo1gnJic2Gvk4dKQsPZPlm0As0HkicsdJnMuS0BHAiblW6NCRkia8tBlAEWrzkZ0m4FjzrZcichO8PSjg/0?wxfmt=jpeg&wxfrom=5" />
<p>美国生物科技已使阿根廷成为了世界第三大大豆生产国，但化学物质的滥用并未被限于大豆、棉花和玉米领域，他们已经污染家庭、 教室和饮用水。</p>
<p>越来越多的医生和科学家们提出警告，南美洲国家滥用化学物质使民众的健康问题日趋恶化。阿根廷，欲哭无泪！！！</p>
<img src="http://mmbiz.qpic.cn/mmbiz/SwsiadjW9rKBo1gnJic2Gvk4dKQsPZPlm0UQ8HOZcsCkZGHoQdaYmvibYeJB5SXeiciaEpe33UwYNpMYmf3CCU2iammw/0?wxfmt=jpeg&wxfrom=5" />
<p>观点中国到现在为止，还没有真正重视转基因的危害，并且还在大量进口美国，阿根廷的大豆和玉米等转基因作物。农业部可以不为 国人及后代的健康负责，因为他们有特供，可我们自己应该为自己的健康负责，阿根廷的今天，就是我们的明天，每一个中国人，为了龙的传人世世代代繁衍不息地传下去，我们有责任，有义务把阿根廷的现实公展在世人的面前。</p>
<p>来源：时代日刊</p>
<img src="http://mmbiz.qpic.cn/mmbiz/uc2hFtP7ZxMZj95udlyXeVgMv8MfJ0ng7GibswB7ZytQyt0Rdo1NyB5LNZUPeJC2jibw7rYmGKCN57Rqb2jRDiccQ/640?wxfrom=5" />
<p>请点击文章标题下面：“脉脉养生”关注</p>
<p>小儿发烧、小儿腹泻、夜啼、小儿推拿、小儿常识、腰痛、男科、补肾食疗、强腰锻炼、腰间盘突出、背痛、腿痛、颈椎病、肝病、 养肝、解酒、胃病、便秘、小腹突出、妇科、经期保养、乳腺增生、乳腺癌、坐月子、痘痘、白发、脱发、丰胸、美容、皮肤病、胆结石、咽炎、痛风、牙痛、打呼噜、口腔溃疡、鼻炎、眼病、手脚、感冒、咳嗽、失眠、痔疮、脑出血、高血压、糖尿病、心脏病、心血管、癌症、食物属性、补血、瘦弱、肥胖、瘦腿、瘦腰、湿气、打嗝...更多</p>
<img src="http://mmbiz.qpic.cn/mmbiz/uc2hFtP7ZxOPYnHVoeayoLaY1MILVwFDlbOs2u3CTeiahTtLhhJfibYA5lSqFciarLG3nvmsMPfaCRY3BIMnUicEew/0?wxfmt=gif&wxfrom=5" />
"""
init_stopwords()
html_content_list = []

lines = html_content.split("\n")
for l in lines:
    words, length = cutwords(l.strip())
    if len(words) == 0 and words == '':
        continue
    html_content_list.append(words.split(","))


# 得到的分词结果构造词典
dic = corpora.Dictionary(html_content_list)
# 词典生成好之后，就开始生成语料库了
corpus = [dic.doc2bow(text) for text in html_content_list]

# 做一个TF-IDF变换
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]

for doc in corpus_tfidf:
    print 'corpus_tfidf:', doc

# 训练LSI模型中的1个主题
# 基于SVD建立的主题模型内容
lsi = models.LsiModel(corpus_tfidf, id2word=dic, num_topics=1)
"""
lsiout = lsi.print_topics(1)
print '==========lsi============='
for i in range(0, len(lsiout)):
    print 'lsa:', lsiout[i]
"""
lsiout = lsi.show_topics(num_topics=1, formatted=False)
print '==========lsi============='
res_list = []

# print 'lsiout:', lsiout
for i in lsiout:
    print 'i=', i

#for i in lsiout[0]:
#    print i[1].encode("utf-8"), i[0]

"""
for i in range(0, len(lsiout)):
    res_list = [(r[1].encode("utf-8"), r[0]) for r in lsiout[i]]
    res_list.append(())
    print 'lsa:', lsiout[i]
print 'res_list:', res_list
"""


"""
print '==========lda============='
# LDA模型
lda = models.LdaModel(corpus_tfidf, passes=20, id2word=dic, num_topics=1)
ldaout = lda.print_topics(1)
for i in ldaout:
    print 'lda:', i
"""


"""
num_topics=1时，输出主题结果
区分词性结果
==========lsi=============
lsa: 1.000*"" + 0.000*"转基因" + 0.000*"阿根廷" + 0.000*"孟山都" + 0.000*"大豆" + 0.000*"加仑" + 0.000*"作物" + 0.000*"国家" + 0.000*"人民" + 0.000*"农业"
==========lda=============
lda: 0.049* + 0.018*转基因 + 0.014*阿根廷 + 0.011*加仑 + 0.011*农药 + 0.009*医生 + 0.009*大豆 + 0.009*孟山都 + 0.008*疾病 + 0.008*国家

未区分词性结果
==========lsi=============
lsa: -1.000*"" + 0.000*"转基因" + 0.000*"阿根廷" + 0.000*"百万" + 0.000*"加仑" + 0.000*"孟山都" + 0.000*"大豆" + 0.000*"农药" + 0.000*"增加" + 0.000*"九倍"
==========lda=============
lda: 0.030* + 0.010*转基因 + 0.007*阿根廷 + 0.005*百万 + 0.005*加仑 + 0.005*农药 + 0.005*大豆 + 0.005*医生 + 0.005*孟山都 + 0.004*缺陷


##############################################################################################
num_topics=3时，输出主题结果
==========lsi=============
lsa: 1.000*"" + 0.000*"转基因" + 0.000*"阿根廷" + 0.000*"加仑" + 0.000*"百万" + 0.000*"大豆" + 0.000*"孟山都" + 0.000*"公司" + 0.000*"农药" + 0.000*"不再"
lsa: 0.636*"转基因" + 0.281*"阿根廷" + 0.225*"加仑" + 0.225*"百万" + 0.167*"孟山都" + 0.157*"大豆" + 0.122*"农药" + 0.113*"九倍" + 0.113*"增加" + 0.107*"喷洒"
lsa: 0.537*"转基因" + -0.383*"加仑" + -0.383*"百万" + -0.192*"增加" + -0.192*"九倍" + -0.187*"农药" + -0.182*"喷洒" + 0.118*"阿根廷" + 0.109*"贫困率" + -0.094*"回收"
==========lda=============
lda: 0.023*转基因 + 0.012*阿根廷 + 0.007*患有 + 0.007*贫困率 + 0.007*医生 + 0.007*儿子 + 0.006*缺陷 + 0.006*改变 + 0.006*人民 + 0.006*农业
lda: 0.007*血淋淋 + 0.006*加油 + 0.006*化学品 + 0.006*脊椎 + 0.006*案例 + 0.006*过多 + 0.006*罪魁祸首 + 0.006*物品 + 0.006*母亲 + 0.006*告诉
lda: 0.080* + 0.011*百万 + 0.011*加仑 + 0.007*农药 + 0.007*孟山都 + 0.007*回收 + 0.007*九倍 + 0.007*增加 + 0.006*公司 + 0.006*容器

##############################################################################################
num_topics=100时，输出主题结果
lsa: 1.000*"" + 0.000*"转基因" + 0.000*"阿根廷" + 0.000*"加仑" + 0.000*"百万" + 0.000*"孟山都" + 0.000*"喷洒" + 0.000*"大豆" + 0.000*"增加" + 0.000*"九倍"
lsa: -0.636*"转基因" + -0.281*"阿根廷" + -0.225*"加仑" + -0.225*"百万" + -0.167*"孟山都" + -0.157*"大豆" + -0.122*"农药" + -0.113*"九倍" + -0.113*"增加" + -0.107*"喷洒"
lsa: -0.537*"转基因" + 0.383*"加仑" + 0.383*"百万" + 0.192*"增加" + 0.192*"九倍" + 0.187*"农药" + 0.182*"喷洒" + -0.118*"阿根廷" + -0.109*"贫困率" + 0.094*"回收"
lsa: -0.349*"缺陷" + -0.285*"医生" + -0.235*"先天" + -0.195*"两岁" + 0.180*"百万" + 0.180*"加仑" + -0.151*"告诉" + -0.151*"过多" + -0.151*"母亲" + -0.151*"物品"
lsa: 0.249*"导致" + 0.235*"疾病" + 0.197*"儿子" + 0.195*"呼吸系统" + 0.195*"慢性" + 0.168*"脊椎" + 0.165*"患有" + 0.148*"化学品" + 0.144*"两次" + 0.144*"流产"
lsa: 0.296*"儿子" + 0.218*"导致" + 0.215*"流产" + 0.215*"两次" + -0.207*"慢性" + -0.207*"呼吸系统" + -0.192*"回收" + -0.174*"容器" + 0.148*"她家" + 0.148*"甘塞多"
lsa: 0.326*"萨维尔" + 0.302*"加油" + 0.229*"瓦索" + 0.229*"雇农" + 0.229*"展示" + 0.229*"家里" + 0.205*"飞行" + 0.205*"死亡" + 0.205*"飞机" + 0.205*"训练"
lsa: 0.225*"脊椎" + 0.214*"化学品" + -0.189*"患有" + 0.155*"布宜诺斯艾利斯省" + 0.155*"田地" + 0.155*"脱落" + 0.155*"这片" + 0.155*"他家" + 0.155*"牙齿" + 0.155*"渗透到"
lsa: 0.221*"孟山都" + -0.180*"疾病" + -0.177*"呼吸系统" + -0.177*"慢性" + 0.174*"中心" + 0.157*"两岁" + 0.148*"公司" + -0.132*"妹妹" + -0.132*"孪生" + 0.127*"位于"
lsa: 0.278*"两岁" + 0.200*"小女孩" + 0.200*"天生" + 0.200*"器官" + 0.200*"残疾" + -0.162*"儿子" + 0.144*"脊椎" + 0.134*"过多" + 0.134*"告诉" + 0.134*"母亲"
lsa: 0.308*"大豆" + -0.236*"转基因" + 0.207*"种植" + -0.182*"加仑" + -0.182*"百万" + 0.162*"基地" + 0.162*"特莱" + 0.162*"维亚" + 0.151*"棉花" + 0.141*"玉米"
lsa: 0.505*"养生" + 0.363*"关注" + 0.363*"点击" + 0.363*"脉脉" + 0.266*"文章" + 0.266*"标题" + 0.171*"朋友圈" + 0.171*"经典" + 0.171*"搜索" + 0.171*"不再"
lsa: 0.280*"滥用" + 0.253*"提出" + 0.253*"科学家" + 0.253*"警告" + 0.192*"饮用水" + 0.192*"教室" + 0.192*"污染" + 0.190*"化学物质" + 0.183*"健康" + 0.154*"南美洲"
lsa: 0.249*"经济" + 0.234*"债务" + 0.209*"农业" + 0.204*"国家" + 0.196*"年代" + 0.196*"世纪" + 0.164*"面积" + 0.162*"公顷" + 0.162*"占地" + 0.162*"危机"
lsa: -0.337*"土地" + -0.337*"生存" + -0.211*"出路" + -0.211*"占据" + -0.211*"堵死" + -0.211*"大片" + -0.194*"全国性" + -0.194*"经济危机" + -0.194*"发现" + -0.194*"当中"
lsa: 0.231*"血淋淋" + 0.220*"案例" + 0.192*"患有" + 0.162*"呼吸系统" + 0.162*"慢性" + 0.162*"妹妹" + 0.162*"孪生" + -0.141*"容器" + 0.139*"台阶" + 0.139*"坐在"
lsa: -0.486*"血淋淋" + -0.454*"案例" + 0.144*"生活" + 0.117*"患有" + 0.110*"改变" + 0.104*"慢性" + 0.104*"呼吸系统" + 0.104*"孪生" + 0.104*"妹妹" + -0.103*"典型"
lsa: 0.259*"小儿" + 0.204*"瘦弱" + 0.177*"瓦索" + 0.177*"展示" + 0.177*"雇农" + 0.177*"家里" + 0.173*"萨维尔" + 0.165*"身体" + -0.162*"喷粉" + -0.143*"加油"
lsa: 0.438*"闻所未闻" + 0.438*"营养不良" + 0.438*"激增" + 0.438*"总人口" + 0.394*"现象" + 0.105*"阿根廷" + -0.064*"转基因" + -0.047*"加仑" + -0.047*"百万" + -0.042*"小儿"
lsa: 0.325*"血淋淋" + 0.274*"案例" + -0.231*"少量" + -0.231*"养有" + -0.231*"蔬菜" + -0.231*"粮食作物" + -0.231*"生产" + -0.231*"牛肉" + -0.231*"牛奶" + -0.231*"养些"
==========lda=============
lda: 0.026*养生 + 0.017*不再 + 0.017*蓝字 + 0.017*搜索 + 0.017*朋友圈 + 0.017*知识 + 0.017*经典 + 0.014*关注 + 0.014*点击 + 0.014*脉脉
lda: 0.003*阿根廷 + 0.003*农药 + 0.003*儿童 + 0.003*癌症 + 0.003*瘦弱 + 0.003*国家 + 0.003*去年 + 0.003*大豆 + 0.003*美国 + 0.003*医生
lda: 0.032*加油 + 0.024*从来 + 0.024*工作 + 0.024*训练 + 0.024*飞机 + 0.024*飞行 + 0.024*濒临 + 0.024*死亡 + 0.024*快速 + 0.018*喷粉
lda: 0.019*总人口 + 0.019*激增 + 0.019*营养不良 + 0.019*闻所未闻 + 0.017*脊椎 + 0.016*现象 + 0.014*当中 + 0.014*全国性 + 0.014*引发 + 0.014*发现
lda: 0.017*孟山都 + 0.017*化学品 + 0.015*公司 + 0.014*每亩 + 0.014*产品 + 0.014*八至 + 0.014*农用 + 0.014*十倍 + 0.014*各省市 + 0.014*国家标准
lda: 0.024*生活 + 0.014*危险 + 0.014*法规 + 0.014*暴露 + 0.014*无视 + 0.014*使人 + 0.014*农作物 + 0.013*升至 + 0.013*水平 + 0.013*拉丁美洲
lda: 0.035*儿子 + 0.026*流产 + 0.026*两次 + 0.021*导致 + 0.018*先天性 + 0.018*她家 + 0.018*影响 + 0.018*指责 + 0.018*查科省 + 0.018*照看
lda: 0.037*两岁 + 0.028*残疾 + 0.028*小女孩 + 0.028*天生 + 0.028*器官 + 0.019*患有 + 0.012*第三 + 0.012*并未 + 0.012*世界 + 0.012*生产国
lda: 0.101*转基因 + 0.038*阿根廷 + 0.028*贫困率 + 0.025*改变 + 0.022*孟山都 + 0.019*大豆 + 0.016*特莱 + 0.016*维亚 + 0.016*基地 + 0.013*玉米
lda: 0.003*阿根廷 + 0.003*农药 + 0.003*儿童 + 0.003*癌症 + 0.003*瘦弱 + 0.003*国家 + 0.003*去年 + 0.003*大豆 + 0.003*美国 + 0.003*医生
lda: 0.036*案例 + 0.034*血淋淋 + 0.017*转基因 + 0.012*作物 + 0.011*名义 + 0.011*地点 + 0.011*实验品 + 0.011*推手 + 0.011*历史 + 0.011*活体
lda: 0.028*萨维尔 + 0.022*家里 + 0.022*展示 + 0.022*瓦索 + 0.022*雇农 + 0.019*瘦弱 + 0.018*身体 + 0.013*占地 + 0.013*危机 + 0.013*微不足道
lda: 0.347* + 0.044*百万 + 0.044*加仑 + 0.023*九倍 + 0.023*增加 + 0.020*喷洒 + 0.015*农药 + 0.014*来源 + 0.014*时代 + 0.014*日刊
lda: 0.023*时间 + 0.023*不到 + 0.023*改造 + 0.020*革命 + 0.020*经济 + 0.015*农业 + 0.013*大豆 + 0.012*国家 + 0.011*转基因 + 0.007*阿根廷
lda: 0.003*阿根廷 + 0.003*农药 + 0.003*儿童 + 0.003*癌症 + 0.003*瘦弱 + 0.003*国家 + 0.003*去年 + 0.003*大豆 + 0.003*美国 + 0.003*医生
lda: 0.028*害苦 + 0.023*人民 + 0.021*冲洗 + 0.021*装水 + 0.021*用于 + 0.021*洗衣服 + 0.021*家中 + 0.021*养鸡 + 0.021*后院 + 0.021*厕所
lda: 0.018*中国 + 0.018*负责 + 0.012*健康 + 0.010*国人 + 0.010*为止 + 0.010*义务 + 0.010*传下去 + 0.010*公展 + 0.010*龙的传人 + 0.010*后代
lda: 0.022*呼吸系统 + 0.022*慢性 + 0.021*疾病 + 0.017*孪生 + 0.017*妹妹 + 0.016*无法解释 + 0.016*身上 + 0.016*长满 + 0.016*家门口 + 0.016*坐在
lda: 0.043*缺陷 + 0.030*先天 + 0.029*医生 + 0.022*儿童 + 0.021*过多 + 0.021*告诉 + 0.021*母亲 + 0.021*物品 + 0.021*罪魁祸首 + 0.019*癌症
lda: 0.022*标题 + 0.022*文章 + 0.019*出路 + 0.019*占据 + 0.019*堵死 + 0.019*大片 + 0.019*点击 + 0.019*关注 + 0.019*脉脉 + 0.019*养生
##############################################################################################
num_topics=100时，输出主题结果
==========lsi=============
lsa: 1.000*"" + 0.000*"转基因" + 0.000*"阿根廷" + 0.000*"百万" + 0.000*"加仑" + 0.000*"大豆" + 0.000*"孟山都" + 0.000*"贫困率" + 0.000*"改变" + 0.000*"农药"
lsa: -0.636*"转基因" + -0.281*"阿根廷" + -0.225*"加仑" + -0.225*"百万" + -0.167*"孟山都" + -0.157*"大豆" + -0.122*"农药" + -0.113*"九倍" + -0.113*"增加" + -0.107*"喷洒"
lsa: -0.537*"转基因" + 0.383*"加仑" + 0.383*"百万" + 0.192*"九倍" + 0.192*"增加" + 0.187*"农药" + 0.182*"喷洒" + -0.118*"阿根廷" + -0.109*"贫困率" + 0.094*"回收"
lsa: -0.349*"缺陷" + -0.285*"医生" + -0.235*"先天" + -0.195*"两岁" + 0.180*"百万" + 0.180*"加仑" + -0.151*"告诉" + -0.151*"过多" + -0.151*"母亲" + -0.151*"物品"
lsa: 0.249*"导致" + 0.235*"疾病" + 0.197*"儿子" + 0.195*"慢性" + 0.195*"呼吸系统" + 0.168*"脊椎" + 0.165*"患有" + 0.148*"化学品" + 0.144*"流产" + 0.144*"两次"
lsa: 0.296*"儿子" + 0.218*"导致" + 0.215*"流产" + 0.215*"两次" + -0.207*"呼吸系统" + -0.207*"慢性" + -0.192*"回收" + -0.174*"容器" + 0.148*"她家" + 0.148*"甘塞多"
lsa: 0.326*"萨维尔" + 0.302*"加油" + 0.229*"雇农" + 0.229*"展示" + 0.229*"家里" + 0.229*"瓦索" + 0.205*"训练" + 0.205*"飞行" + 0.205*"飞机" + 0.205*"从来"
lsa: 0.225*"脊椎" + 0.214*"化学品" + -0.189*"患有" + 0.155*"布宜诺斯艾利斯省" + 0.155*"政府" + 0.155*"渗透到" + 0.155*"牙齿" + 0.155*"田地" + 0.155*"罗森" + 0.155*"脱落"
lsa: 0.221*"孟山都" + -0.180*"疾病" + -0.177*"呼吸系统" + -0.177*"慢性" + 0.174*"中心" + 0.157*"两岁" + 0.148*"公司" + -0.132*"妹妹" + -0.132*"孪生" + 0.127*"罗省"
lsa: 0.278*"两岁" + 0.200*"器官" + 0.200*"天生" + 0.200*"小女孩" + 0.200*"残疾" + -0.162*"儿子" + 0.144*"脊椎" + 0.134*"过多" + 0.134*"告诉" + 0.134*"罪魁祸首"
lsa: 0.308*"大豆" + -0.236*"转基因" + 0.207*"种植" + -0.182*"百万" + -0.182*"加仑" + 0.162*"特莱" + 0.162*"基地" + 0.162*"维亚" + 0.151*"棉花" + 0.141*"玉米"
lsa: 0.505*"养生" + 0.363*"点击" + 0.363*"脉脉" + 0.363*"关注" + 0.266*"文章" + 0.266*"标题" + 0.171*"不再" + 0.171*"搜索" + 0.171*"知识" + 0.171*"经典"
lsa: 0.280*"滥用" + 0.253*"警告" + 0.253*"提出" + 0.253*"科学家" + 0.192*"饮用水" + 0.192*"教室" + 0.192*"污染" + 0.190*"化学物质" + 0.183*"健康" + 0.154*"南美洲"
lsa: 0.249*"经济" + 0.234*"债务" + 0.209*"农业" + 0.204*"国家" + 0.196*"年代" + 0.196*"世纪" + 0.164*"面积" + 0.162*"微不足道" + 0.162*"占地" + 0.162*"危机"
lsa: -0.337*"生存" + -0.337*"土地" + -0.211*"大片" + -0.211*"堵死" + -0.211*"出路" + -0.211*"占据" + -0.194*"当中" + -0.194*"全国性" + -0.194*"经济危机" + -0.194*"拖欠"
lsa: 0.231*"血淋淋" + 0.220*"案例" + 0.192*"患有" + 0.162*"慢性" + 0.162*"呼吸系统" + 0.162*"妹妹" + 0.162*"孪生" + -0.141*"容器" + 0.139*"家门口" + 0.139*"无法解释"
lsa: -0.486*"血淋淋" + -0.454*"案例" + 0.144*"生活" + 0.117*"患有" + 0.110*"改变" + 0.104*"呼吸系统" + 0.104*"慢性" + 0.104*"孪生" + 0.104*"妹妹" + -0.103*"典型"
lsa: 0.259*"小儿" + 0.204*"瘦弱" + 0.177*"展示" + 0.177*"瓦索" + 0.177*"家里" + 0.177*"雇农" + 0.173*"萨维尔" + 0.165*"身体" + -0.162*"喷粉" + -0.143*"加油"
lsa: 0.438*"闻所未闻" + 0.438*"营养不良" + 0.438*"总人口" + 0.438*"激增" + 0.394*"现象" + 0.105*"阿根廷" + -0.064*"转基因" + -0.047*"百万" + -0.047*"加仑" + -0.042*"小儿"
lsa: 0.325*"血淋淋" + 0.274*"案例" + -0.231*"牛奶" + -0.231*"牛肉" + -0.231*"养些" + -0.231*"多种" + -0.231*"少量" + -0.231*"奶酪" + -0.231*"农场" + -0.231*"蔬菜"
lsa: 0.577*"来源" + 0.577*"时代" + 0.577*"日刊" + -0.000*"血淋淋" + -0.000*"案例" + 0.000*"生产" + 0.000*"家庭" + 0.000*"农场" + 0.000*"少量" + 0.000*"牛肉"
lsa: 0.258*"小儿" + 0.189*"身上" + 0.189*"长满" + 0.189*"台阶" + 0.189*"家门口" + 0.189*"无法解释" + 0.189*"坐在" + -0.168*"缺陷" + 0.147*"生活" + 0.137*"血淋淋"
lsa: -0.245*"小儿" + 0.185*"萨维尔" + 0.181*"展示" + 0.181*"雇农" + 0.181*"瓦索" + 0.181*"家里" + 0.166*"血淋淋" + -0.144*"喷粉" + 0.140*"身体" + 0.133*"案例"
lsa: 0.320*"生活" + -0.195*"不到" + -0.195*"改造" + -0.195*"时间" + 0.194*"血淋淋" + -0.186*"经济" + -0.175*"革命" + 0.160*"之下" + 0.160*"官方" + 0.160*"拉丁美洲"
lsa: -0.310*"负责" + -0.310*"中国" + -0.155*"现实" + -0.155*"特供" + -0.155*"不息" + -0.155*"世世代代" + -0.155*"世人" + -0.155*"为止" + -0.155*"义务" + -0.155*"传下去"
lsa: -0.533*"害苦" + -0.475*"人民" + 0.282*"改变" + 0.205*"贫困率" + 0.154*"孟山都" + 0.144*"血淋淋" + 0.090*"经济" + 0.087*"案例" + -0.083*"生活" + 0.079*"改造"
lsa: -0.361*"贫困率" + 0.302*"害苦" + 0.271*"人民" + -0.129*"领域" + -0.129*"世界" + -0.129*"并未" + -0.129*"生产国" + -0.129*"生物科技" + -0.129*"第三" + -0.129*"限于"
lsa: 0.183*"过多" + 0.183*"告诉" + 0.183*"母亲" + 0.183*"物品" + 0.183*"罪魁祸首" + -0.168*"高出" + -0.168*"地方" + -0.168*"四倍" + -0.168*"急剧" + -0.168*"比起"
lsa: 0.268*"改变" + -0.204*"贫困率" + 0.148*"孟山都" + 0.145*"第三" + 0.145*"世界" + 0.145*"已使" + 0.145*"并未" + 0.145*"生产国" + 0.145*"限于" + 0.145*"领域"
lsa: -0.587*"贫困率" + 0.558*"改变" + 0.225*"孟山都" + -0.153*"中心" + -0.143*"废弃" + -0.143*"位于" + -0.143*"圣地亚哥" + -0.143*"埃斯特" + -0.143*"罗省" + -0.100*"去年"
lsa: -0.301*"占据" + -0.301*"堵死" + -0.301*"大片" + -0.301*"出路" + 0.219*"债务" + 0.213*"当中" + 0.213*"经济危机" + 0.213*"发现" + 0.213*"拖欠" + 0.213*"全国性"
lsa: -0.273*"危机" + -0.273*"占地" + -0.273*"公顷" + -0.273*"微不足道" + 0.232*"不到" + 0.232*"改造" + 0.232*"时间" + 0.221*"革命" + -0.198*"面积" + -0.176*"种植"
lsa: -0.242*"家园" + -0.242*"全国" + -0.242*"控制" + -0.242*"将会" + -0.242*"喷涂" + 0.236*"南美洲" + 0.230*"化学物质" + 0.187*"欲哭无泪" + 0.187*"民众" + 0.187*"越来越"
lsa: -0.382*"害苦" + -0.229*"贫困率" + -0.207*"血淋淋" + -0.200*"改造" + -0.200*"不到" + -0.200*"时间" + -0.175*"人民" + -0.173*"改变" + 0.172*"面积" + 0.171*"地点"
lsa: -0.490*"贫困率" + -0.381*"改变" + 0.361*"转基因" + -0.180*"孟山都" + -0.173*"人民" + -0.158*"作物" + -0.135*"革命" + 0.129*"血淋淋" + -0.128*"活体" + -0.128*"推手"
lsa: 0.301*"使人" + 0.301*"无视" + 0.301*"农作物" + 0.301*"法规" + 0.301*"危险" + 0.301*"暴露" + -0.210*"正相反" + -0.210*"情况" + -0.210*"该国" + -0.176*"农业部"
lsa: -0.445*"文章" + -0.445*"标题" + 0.292*"搜索" + 0.292*"经典" + 0.292*"知识" + 0.292*"不再" + 0.292*"朋友圈" + 0.292*"蓝字" + 0.136*"疾病" + -0.127*"点击"
lsa: -0.433*"情况" + -0.433*"该国" + -0.433*"正相反" + -0.374*"农业部" + 0.206*"百万" + 0.206*"加仑" + -0.143*"无视" + -0.143*"暴露" + -0.143*"法规" + -0.143*"使人"
lsa: 0.518*"喷粉" + -0.468*"工巴" + -0.468*"瓦素" + -0.347*"加油" + -0.258*"萨维尔" + 0.131*"瓦索" + 0.131*"家里" + 0.131*"雇农" + 0.131*"展示" + 0.114*"瘦弱"
lsa: -0.558*"子里" + 0.478*"院子" + -0.353*"阿根廷" + 0.331*"脊椎" + 0.283*"导致" + 0.224*"化学品" + 0.085*"转基因" + -0.067*"渗透到" + -0.067*"脱落" + -0.067*"这片"
lsa: -0.838*"阿根廷" + 0.247*"子里" + 0.202*"转基因" + -0.197*"院子" + 0.122*"贫困率" + -0.122*"脊椎" + 0.085*"改变" + -0.081*"化学品" + -0.081*"导致" + 0.070*"人民"
lsa: 0.482*"儿童" + -0.330*"妹妹" + -0.330*"孪生" + 0.291*"两次" + 0.291*"流产" + 0.254*"呼吸系统" + 0.254*"慢性" + -0.254*"患有" + 0.179*"导致" + 0.166*"疾病"
lsa: 0.434*"流产" + 0.434*"两次" + -0.320*"儿童" + 0.277*"导致" + -0.232*"儿子" + 0.230*"妹妹" + 0.230*"孪生" + 0.164*"农药" + -0.150*"呼吸系统" + -0.150*"慢性"
lsa: 0.358*"特莱" + 0.358*"基地" + 0.358*"维亚" + 0.248*"生物" + 0.248*"技术" + 0.223*"种植" + -0.159*"弹弓" + -0.159*"承诺" + -0.159*"一种" + -0.159*"专利"
lsa: -0.858*"两岁" + 0.240*"器官" + 0.240*"残疾" + 0.240*"小女孩" + 0.240*"天生" + 0.117*"患有" + -0.061*"孪生" + -0.061*"妹妹" + 0.053*"儿童" + 0.031*"告诉"
lsa: 0.611*"中心" + 0.466*"回收" + 0.303*"孟山都" + -0.195*"废弃" + -0.195*"埃斯特" + -0.195*"罗省" + -0.195*"位于" + -0.195*"圣地亚哥" + -0.176*"容器" + -0.173*"改变"
==========lda=============
lda: 0.067*告诉 + 0.067*罪魁祸首 + 0.067*物品 + 0.067*母亲 + 0.067*过多 + 0.059*癌症 + 0.053*化学 + 0.053*先天 + 0.053*缺陷 + 0.043*医生
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.062*瓦素 + 0.062*工巴 + 0.002*鼻炎 + 0.002*从来 + 0.002*提出 + 0.002*教室 + 0.002*污染 + 0.002*滥用 + 0.002*科学家 + 0.002*警告
lda: 0.075*养生 + 0.046*不再 + 0.046*知识 + 0.046*蓝字 + 0.046*搜索 + 0.046*朋友圈 + 0.046*经典 + 0.038*脉脉 + 0.038*点击 + 0.038*关注
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.041*中国 + 0.041*负责 + 0.025*健康 + 0.021*繁衍 + 0.021*传下去 + 0.021*义务 + 0.021*为止 + 0.021*后代 + 0.021*世人 + 0.021*世世代代
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.057*脊椎 + 0.046*导致 + 0.042*化学品 + 0.039*罗森 + 0.039*脱落 + 0.039*田地 + 0.039*牙齿 + 0.039*渗透到 + 0.039*政府 + 0.039*抱怨
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.178*百万 + 0.178*加仑 + 0.089*九倍 + 0.089*增加 + 0.077*喷洒 + 0.057*农药 + 0.001*鼻炎 + 0.001*滥用 + 0.001*科学家 + 0.001*警告
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.067*不到 + 0.067*时间 + 0.067*改造 + 0.056*革命 + 0.056*经济 + 0.042*农业 + 0.034*大豆 + 0.032*国家 + 0.029*转基因 + 0.016*阿根廷
lda: 0.181*贫困率 + 0.077*转基因 + 0.043*阿根廷 + 0.002*鼻炎 + 0.002*加油 + 0.002*滥用 + 0.002*科学家 + 0.002*警告 + 0.002*饮用水 + 0.002*害苦
lda: 0.038*每亩 + 0.038*正规 + 0.038*成分 + 0.038*草甘膦 + 0.038*规则 + 0.038*大概 + 0.038*多用 + 0.038*国家标准 + 0.038*各省市 + 0.038*十倍
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.045*日趋 + 0.045*恶化 + 0.045*欲哭无泪 + 0.045*民众 + 0.045*越来越 + 0.038*南美洲 + 0.038*提出 + 0.038*警告 + 0.038*化学物质 + 0.038*科学家
lda: 0.073*儿子 + 0.053*两次 + 0.053*流产 + 0.043*导致 + 0.037*她家 + 0.037*甘塞多 + 0.037*影响 + 0.037*指责 + 0.037*查科省 + 0.037*照看
lda: 0.071*中心 + 0.059*孟山都 + 0.057*回收 + 0.054*罗省 + 0.054*埃斯特 + 0.054*位于 + 0.054*圣地亚哥 + 0.054*废弃 + 0.051*公司 + 0.043*容器
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.074*加油 + 0.053*工作 + 0.053*飞机 + 0.053*快速 + 0.053*从来 + 0.053*飞行 + 0.053*死亡 + 0.053*濒临 + 0.053*训练 + 0.051*阿根廷
lda: 0.061*家中 + 0.061*冲洗 + 0.061*洗衣服 + 0.061*用于 + 0.061*装水 + 0.061*后院 + 0.061*厕所 + 0.061*养鸡 + 0.049*容器 + 0.049*回收
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.080*总人口 + 0.080*激增 + 0.080*营养不良 + 0.080*闻所未闻 + 0.067*现象 + 0.019*阿根廷 + 0.002*鼻炎 + 0.002*污染 + 0.002*滥用 + 0.002*科学家
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.092*血淋淋 + 0.077*案例 + 0.041*公顷 + 0.041*危机 + 0.041*占地 + 0.041*微不足道 + 0.034*经济 + 0.034*年代 + 0.034*面积 + 0.034*债务
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.061*堵死 + 0.061*大片 + 0.061*占据 + 0.061*出路 + 0.051*生存 + 0.051*土地 + 0.038*种植 + 0.033*作物 + 0.031*大豆 + 0.026*转基因
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.077*缺陷 + 0.061*儿童 + 0.049*证明 + 0.049*高出 + 0.049*急剧 + 0.049*地方 + 0.049*四倍 + 0.049*比起 + 0.039*身体 + 0.039*技术
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.035*领域 + 0.035*第三 + 0.035*并未 + 0.035*世界 + 0.035*已使 + 0.035*生物科技 + 0.035*生产国 + 0.035*限于 + 0.035*大豆 + 0.029*化学物质
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.043*将会 + 0.043*控制 + 0.043*家园 + 0.043*喷涂 + 0.043*全国 + 0.036*饮用水 + 0.036*教室 + 0.036*提出 + 0.036*科学家 + 0.036*警告
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.347*转基因 + 0.002*鼻炎 + 0.002*提出 + 0.002*污染 + 0.002*滥用 + 0.002*科学家 + 0.002*警告 + 0.002*饮用水 + 0.002*害苦 + 0.002*从来
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.070*萨维尔 + 0.053*瓦索 + 0.053*展示 + 0.053*雇农 + 0.053*家里 + 0.047*瘦弱 + 0.042*身体 + 0.025*多种 + 0.025*农场 + 0.025*奶酪
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.089*情况 + 0.089*该国 + 0.089*正相反 + 0.078*农业部 + 0.002*鼻炎 + 0.002*从来 + 0.002*污染 + 0.002*滥用 + 0.002*科学家 + 0.002*警告
lda: 0.053*发现 + 0.053*经济危机 + 0.053*全国性 + 0.053*引发 + 0.053*当中 + 0.053*拖欠 + 0.044*土地 + 0.044*生存 + 0.044*债务 + 0.025*国家
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.114*呼吸系统 + 0.114*慢性 + 0.087*妹妹 + 0.087*孪生 + 0.084*疾病 + 0.059*患有 + 0.001*农药 + 0.001*工巴 + 0.001*警告 + 0.001*饮用水
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.137*害苦 + 0.114*人民 + 0.058*转基因 + 0.033*阿根廷 + 0.002*鼻炎 + 0.002*滥用 + 0.002*科学家 + 0.002*警告 + 0.002*饮用水 + 0.002*从来
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.099*两岁 + 0.087*改变 + 0.073*残疾 + 0.073*器官 + 0.073*天生 + 0.073*小女孩 + 0.050*患有 + 0.049*孟山都 + 0.037*转基因 + 0.020*阿根廷
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.078*文章 + 0.078*标题 + 0.065*关注 + 0.065*养生 + 0.065*点击 + 0.065*脉脉 + 0.002*鼻炎 + 0.002*加油 + 0.002*污染 + 0.002*滥用
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.111*日刊 + 0.111*时代 + 0.111*来源 + 0.002*鼻炎 + 0.002*将会 + 0.002*提出 + 0.002*教室 + 0.002*污染 + 0.002*滥用 + 0.002*科学家
lda: 0.076*生活 + 0.038*贫困线 + 0.038*之下 + 0.038*人口比例 + 0.038*公布 + 0.038*升至 + 0.038*官方 + 0.038*拉丁美洲 + 0.038*数字 + 0.038*水平
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.039*大豆 + 0.039*基地 + 0.039*维亚 + 0.039*特莱 + 0.031*生物 + 0.031*技术 + 0.029*种植 + 0.028*转基因 + 0.028*一种 + 0.028*专利
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.034*转基因 + 0.028*法规 + 0.028*暴露 + 0.028*无视 + 0.028*使人 + 0.028*危险 + 0.028*农作物 + 0.025*阿根廷 + 0.024*现象 + 0.024*南美洲
lda: 0.809* + 0.001*鼻炎 + 0.001*家里 + 0.001*污染 + 0.001*滥用 + 0.001*科学家 + 0.001*警告 + 0.001*饮用水 + 0.001*害苦 + 0.001*从来
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.081*长满 + 0.081*无法解释 + 0.081*家门口 + 0.081*坐在 + 0.081*台阶 + 0.081*身上 + 0.068*医生 + 0.001*警告 + 0.001*提出 + 0.001*教室
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.003*鼻炎 + 0.003*萨维尔 + 0.003*提出 + 0.003*教室 + 0.003*污染 + 0.003*滥用 + 0.003*科学家 + 0.003*警告 + 0.003*饮用水 + 0.003*害苦
lda: 0.043*小儿 + 0.011*鼻炎 + 0.011*牙痛 + 0.011*推拿 + 0.011*打嗝 + 0.011*打呼噜 + 0.011*手脚 + 0.011*感冒 + 0.011*心血管 + 0.011*心脏病
"""
