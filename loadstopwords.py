

stop_words = [unicode(x.strip(), 'utf-8') for x in open('stopword.txt','r').read().split('\n')]
vectorizer = TfidfVectorizer(analyzer='word', stop_words = stop_words)




