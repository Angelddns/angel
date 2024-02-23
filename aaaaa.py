import jieba
from gensim.models import Word2Vec
def f(a,b):
    raw_sentence = [jieba.lcut("番茄非常好吃"), jieba.lcut("西红柿熟了"), jieba.lcut("我喜欢吃西红柿")]
    model = Word2Vec(raw_sentence,vector_size=192,min_count=1)
    return float(model.wv.similarity("西红柿", "番茄"))

if __name__=="__main__":
    print(f("番茄","西红柿"))