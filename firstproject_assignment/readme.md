# Wordcounter Assignment

## 개요
1. 소개
2. 스크린 샷
3. 기능

* * *
   
## 소개

멋쟁이 사자처럼 7기 django 강의에서 나온 Wordcounter를 만들어 보았습니다.
첫 home 페이지에서 글을 입력하고 버튼을 누르면 문자별로 count 하는 기능을 가지고 있습니다.


* * *
   
## 스크린샷

![wordcounter_screenshot1](/screenshot/screenshot1.png “wordcounter1”)
![wordcounter_screenshot2](/screenshot/screenshot2.png “wordcounter2”)
![wordcounter_screenshot3](/screenshot/screenshot3.png “wordcounter3”)
![wordcounter_screenshot4](/screenshot/screenshot4.png “wordcounter4”)
![wordcounter_screenshot5](/screenshot/screenshot5.png “wordcounter5”)


* * *
   
## 기능

####1. (기본)사용자가 입력한 문장 출력
‘full_text = request.GET[‘fulltext’]’와 같이 home.html에서 사용자가 textarea에 작성한 내용을 받아서 출력


####2. (기본)문장을 구성하는 단어 수 출력
위에서 입력받은 ‘full_text’를 ‘word_list = full_text.split()’ 처럼 공백으로 나누어 단어 리스트를 ‘word_list’에 저장한 다음 ‘len(word_list)’를 보내어 단어 수 출력


####3. (기본)사용된 단어와 단어가 사용된 수 출력
위에서 구한 ‘word_list’를 사용하여 ‘word_dictionary’라는 딕셔너리에 사용된 단어를 key값 그리고 사용된 횟수를 value로 하여 구함
for문을 사용하여 word가 word_dictionary에 존재하면 += 1, 없으면 = 1 을 하는 방식으로 구현
![wordcounter_screenshot6](/screenshot/screenshot6.png “wordcounter6”)

count.html에서는 탬플릿을 사용하여 출력
![wordcounter_screenshot7](/screenshot/screenshot7.png “wordcounter7”)


####4. (추가)문장 수 출력
“. “(온점과 공백)을 기준으로 문장수를 카운트 하여 문장 수 출력. !나 ?로 끝나는 문장은 카운트 안됨.
그리고 맨 마지막 문장은 .(온점) 이후에 공백이 없어서 += 1 함

![wordcounter_screenshot13](/screenshot/screenshot13.png “wordcounter13”)



####5. (추가)가장 긴 단어 출력
가장 긴 단어를 구하기 위해 먼저 가장 긴 단어의 길이를 저장할 변수 ‘longest_word_len’과 가장 긴 단어들을 저장할 문자열 변수 ‘longest_word’를 초기화
![wordcounter_screenshot8](/screenshot/screenshot8.png “wordcounter8”)

그리고 위 3번 기능에서 사용했던 for 문에서 추가로 문자의 길이를 비교하는 코드 추가
![wordcounter_screenshot9](/screenshot/screenshot9.png “wordcounter9”)

새 단어가 기존 단어보다 길면 새 단어를 저장하고, 기존 단어와 길이가 동일하면 추가로 이어 붙임


####6. (추가)Count 기준으로 내림차순 정렬

위에서 ‘word_dictionary’ 딕셔너리를 사용하여 보여준 값은 정렬이 되어 있지 않은 값이다. 그래서 사용자가 많이 사용한 단어 순으로 정렬을 해보았다.

완성된 ‘word_dictionary’ 딕셔너리를 value값을 기준으로 내림차순으로 정렬한 다음 첫번째 값을 value 값을(즉 가장 많이 나온 단어가 나온 횟수) ‘toppest_n’이라는 변수에 저장
![wordcounter_screenshot10](/screenshot/screenshot10.png “wordcounter10”)

그 다음 공동우승이 있을 수 있기때문에 for 문을 돌며 value 값이 toppest_n인 경우(가장 많이 나온 단어인 경우) key 값을 문자열에 추가하였다.
![wordcounter_screenshot11](/screenshot/screenshot11.png “wordcounter11”)

그리고 마지막으로 문자열의 처음부터 “, “으로 시작하기 때문에 앞 부분을 날려주였다.
![wordcounter_screenshot12](/screenshot/screenshot12.png “wordcounter12”)


####7. (추가)공백 포함 단어 출력

단어가 N개 이면 공백을 포함한 단어는 2*N-1 이므로 ‘len(word_list)*2-1’ 값을 return 하여 공백 포함 단어수를 출력하였다.
