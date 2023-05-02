# 计算每个词语的TF-IDF值
tf_idf = {}
N = len(corpus)
# 计算每个文档中每个词语的出现次数
word_counts = [Counter(doc.split()) for doc in corpus]
# 计算每个词语的TF值和IDF值，并相乘得到TF-IDF值
for i, doc in enumerate(corpus):
    for word in set(doc.split()):
        tf = 1 + math.log(word_counts[i][word])
        idf = math.log(N / sum([1 for doc in corpus 
        if word in doc]))
        tf_idf[(word, i)] = tf * idf
