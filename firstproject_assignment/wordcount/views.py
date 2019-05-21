from django.shortcuts import render
import operator

# Create your views here.
def home(request):
    return render(request, 'wordcount/home.html')

def about(request):
    return render(request, 'wordcount/about.html')

def count(request):
    #추가 구현한 내용
    #1.문장 수 카운트
    #2.가장 긴 단어 찾기
    #3.count 기준으로 내림차순 정렬하기
    #4.가장 많이 쓴 단어 찾기
    #5.공백 포함, 미포함 단어수 세기
    
    full_text = request.GET['fulltext']

    word_list = full_text.split()

    word_dictionary = {}
    # sorted_word_dictionary = {}
    toppest_word = ""

    #1.문장 수 카운트
    #온점과 공백을 카운트 하여 문장 수를 센다
    num_of_dot = full_text.count(". ")
    num_of_dot += 1

    #2.가장 긴 단어 찾기
    #가장 긴 단어 찾기 초기화
    longest_word_len = -1
    longest_word = 'none'

    #단어수 딕셔너리에 추가하는 과정 & 가장 긴 단어 찾는 과정
    for word in word_list:

        #add to dictionary
        if word in word_dictionary:
            word_dictionary[word] += 1
        else :
            word_dictionary[word] = 1

        #find longest word
        if len(word) > longest_word_len:
            longest_word_len = len(word)
            longest_word = word

    #3.count 기준으로 내림차순 정렬하기
    #value 값 사용하여 아이템 정렬
    
    #실패작1
    # sorted_word_dictionary = sorted(word_dictionary.items(), key=lambda x: x[1])
    
    #실패작2
    # for i,j in sorted (word_dictionary) :
    #     sorted_word_dictionary[i] = j         

    #실패작3
    # sorted_word_dictionary = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)

    #드디어 성공...
    sorted_word_dictionary=sorted(word_dictionary.items(), key=lambda x:x[1], reverse=True)

    #4.가장 많이 쓴 단어 찾기
    #정렬된 dictionary인 sorted_word_dictionary의 첫번째 아이템의 value 값을 구한다
    toppest_n = sorted_word_dictionary[0][1]
    
    #위에서 구한 value 값이 동일한 key 가 있으면 추가한다
    for key, value in sorted_word_dictionary :

        if value == toppest_n:
            # toppest_word.append(key)
            toppest_word +=", "
            toppest_word += key
        else:
            break
    
    toppest_word = toppest_word[2:]
   


    return render(request, 'wordcount/count.html', 
        {'fulltext': full_text, 
        'total':len(word_list), 
        'dictionary':word_dictionary.items(),
        #추가된 인자
        'numOfDot':num_of_dot,
        'longestWord':longest_word,       
        'sortedDictionary':sorted_word_dictionary[0:-1],
        'toppestWord':toppest_word,
        'totalNblank':len(word_list)*2-1
        })