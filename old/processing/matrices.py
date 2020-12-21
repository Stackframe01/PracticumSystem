from gensim.models import Word2Vec
from processing.preprocessing import token_and_stem, get_stopwords
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer


def get_lda(dataset):
    ct = CountVectorizer(tokenizer=token_and_stem, stop_words=get_stopwords(), min_df=0.01,
                         token_pattern=r'[(?u)\b\w\w+\bа-яА-Я]+')
    ct.transform(dataset)

    return ct


def get_tfidf(dataset):
    tfidf_vectorizer = TfidfVectorizer(tokenizer=token_and_stem, stop_words=get_stopwords(), min_df=0.01,
                                       token_pattern=r'[(?u)\b\w\w+\bа-яА-Я]+')
    tfidf_matrix = tfidf_vectorizer.fit_transform(dataset)

    return tfidf_matrix.toarray()


def get_word2vec(dataset):
    preprocessed = []
    for i in dataset:
        temp = token_and_stem(i)
        if temp not in get_stopwords():
            preprocessed.append(temp)

    model = Word2Vec(preprocessed)
    return model[model.wv.vocab]


if __name__ == '__main__':
    pass
