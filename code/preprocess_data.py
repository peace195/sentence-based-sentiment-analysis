import csv
import tensorflow as tf
from itertools import izip
from matplotlib import pylab
from itertools import izip
import nltk
from sklearn.manifold import TSNE
from nltk.tokenize import TweetTokenizer
import collections
import re
import pickle

def read_data(trainfile, testfile):
    data = list()
    train =  open(trainfile, 'rb')
    test =  open(testfile, 'rb')
    trainreader = csv.reader(train, delimiter='\t')
    testreader = csv.reader(test, delimiter='\t')
    
    for row in trainreader:
        tknzr = TweetTokenizer(strip_handles=True, reduce_len=True)
        tweet_wordlist = tknzr.tokenize(re.sub(r"http\S+", "", row[3]).lower())
        data.extend(tweet_wordlist)
        
    for row in testreader:
        tknzr = TweetTokenizer(strip_handles=True, reduce_len=True)
        tweet_wordlist = tknzr.tokenize(re.sub(r"http\S+", "", row[3]).lower())
        data.extend(tweet_wordlist)
    
    train.close()
    test.close()
    return data

def convert_data(raw_csv_file, encode_data_file, encode_label_file, embedding_keys):
    raw_csv =  open(raw_csv_file, 'rb')
    data_file = open(encode_data_file, 'w')
    label_file = open(encode_label_file, 'w')
    spamreader = csv.reader(raw_csv, delimiter='\t')

    for row in spamreader:
        tknzr = TweetTokenizer(strip_handles=True, reduce_len=True)
        tweet_wordlist = tknzr.tokenize(row[3].lower())
        cnt_word = 0
        for word in tweet_wordlist:
            if (word in words_dict.keys()) and (word in embedding_keys):
                # print(word)
                cnt_word = cnt_word + 1
                data_file.write(str(words_dict[word]) + '/' + str(sent_words_dict[word]) + ' ')

        if (cnt_word > 0):
            label_file.write(sent_dict[row[2]])
            label_file.write('\n')
            data_file.write('\n')

    raw_csv.close()
    data_file.close()
    label_file.close()

if __name__ == "__main__":
    
    vocabulary_size = 50000
    
    word_set = set()
    stop_words = set()

    sent_words_dict = dict()
    words_dict = dict()
    sent_dict = dict()

    count = list()
    pos_list = list()
    neg_list = list()
    rev_list = list()
    inc_list = list()
    dec_list = list()

    sent_dict['positive'] = '0'
    sent_dict['negative'] = '1'
    sent_dict['neutral'] = '2'
    sent_dict['objective'] = '2'
    sent_dict['objective-OR-neutral'] = '2'

    words = read_data('../data/semeval/2013/b.dist.csv', '../data/semeval/2013/b.test.dist.csv')
    print('Data size %d' % len(words))

    count.extend(collections.Counter(words).most_common(vocabulary_size - 1))
    for word, _ in count:
        if re.search(r'^[a-zA-Z]', word) and len(word) < 20 and len(word) > 1:
            word_set.add(word)

    f_stop = open('../dict/stop-words(copy).txt', 'r')
    fneg = open('../dict/negative-words.txt', 'r')
    fpos = open('../dict/positive-words.txt', 'r')
    frev = open('../dict/reverse-words.txt', 'r')
    fdec = open('../dict/decremental-words.txt', 'r')
    finc = open('../dict/incremental-words.txt', 'r')
    fsentwords = open('../encoder/dictionary-list', 'w')
    embedding = open('../embedding-results/sswe-u.txt')

    embedding_keys = list()
    for line in embedding:
        elements = line.split()
        embedding_keys.append(elements[0])

    for line in f_stop:
        line = line.strip()
        stop_words.add(line.split()[0])

    total_word_count = 1

    for line in fpos:
        if not line.split()[0] in words_dict:
            words_dict[line.split()[0]] = total_word_count
            total_word_count = total_word_count + 1
            sent_words_dict[line.split()[0]] = 0
            fsentwords.write('%s %d\n' %(line.split()[0],
                                         sent_words_dict[line.split()[0]]))
            pos_list.append(line.split()[0])
            
    for line in fneg:
        if not line.split()[0] in words_dict:
            words_dict[line.split()[0]] = total_word_count
            total_word_count = total_word_count + 1
            sent_words_dict[line.split()[0]] = 1
            fsentwords.write('%s %d\n' %(line.split()[0],
                                         sent_words_dict[line.split()[0]]))
            neg_list.append(line.split()[0])

    for line in frev:
        if not line.split()[0] in words_dict:
            words_dict[line.split()[0]] = total_word_count
            total_word_count = total_word_count + 1
            sent_words_dict[line.split()[0]] = 2
            fsentwords.write('%s %d\n' %(line.split()[0],
                                         sent_words_dict[line.split()[0]]))
            rev_list.append(line.split()[0])
        
    for line in finc:
        if not line.split()[0] in words_dict:
            words_dict[line.split()[0]] = total_word_count
            total_word_count = total_word_count + 1
            sent_words_dict[line.split()[0]] = 3
            fsentwords.write('%s %d\n' %(line.split()[0],
                                         sent_words_dict[line.split()[0]]))
            inc_list.append(line.split()[0])
        
    for line in fdec:
        if not line.split()[0] in words_dict:
            words_dict[line.split()[0]] = total_word_count
            total_word_count = total_word_count + 1

            sent_words_dict[line.split()[0]] = 4
            fsentwords.write('%s %d\n' %(line.split()[0],
                                         sent_words_dict[line.split()[0]]))
            dec_list.append(line.split()[0])
        
    word_set = word_set - stop_words
    word_set = word_set - set(pos_list)
    word_set = word_set - set(neg_list)
    word_set = word_set - set(rev_list)
    word_set = word_set - set(inc_list)
    word_set = word_set - set(dec_list)

    for word in word_set:
        try:
            if not word in words_dict:
                sent_words_dict[word] = 5
                fsentwords.write('%s %d\n' %(word, sent_words_dict[word]))
                words_dict[word] = total_word_count
                total_word_count = total_word_count + 1
        except UnicodeEncodeError:
            continue
        
    words_dict['<unk>'] = total_word_count
    fsentwords.write('<unk> 5')
    
    convert_data('../data/semeval/2013/b.dist.csv', '../encoder/train-data', '../encoder/train-label', embedding_keys)
    convert_data('../data/semeval/2013/b.test.dist.csv', '../encoder/test-data', '../encoder/test-label', embedding_keys)

    print('Words_dict size %d' % len(words_dict))
    save = open('../encoder/dictionary-id', 'w')
    pickle.dump(words_dict, save)
    save.close()

    fsentwords.close()
    fneg.close()
    fpos.close()
    frev.close()
    fdec.close()
    finc.close()
    f_stop.close()
    embedding.close()
