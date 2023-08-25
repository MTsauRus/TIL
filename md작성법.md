## md 작성법
+ [마크다운 공식 문서](https://www.markdownguide.org/basic-syntax/)
+ [vsc 공식 문서](https://code.visualstudio.com/docs/languages/markdown#_dynamic-previews-and-preview-locking)

## headings  
1개~6개를 사용하여 제목을 작성하자.
### paragraphs
그냥 엔터를 누르자.

이렇게.
## line breaks
줄이 끝날 때 스페이스를 두 번 누르고 엔터를 치면  
이렇게 다음 줄로  
가게  
됩  
니  
다  
<p>html 태그를 써도 됩니다.<br>
이렇게요.

## Bold and italic
**star 두개로 감싸요**
strong 태그를 써도 <strong>된답니다.</strong><br>
*star 하나는 이탤릭*<br>
***star 3개는 bold italic***

## blockquotes
> 부등호를 씁시다.
>
> 이렇게요.
>> 부등호 두 개도
>>> 세 개도 된답니다.

> #### 내부에서 다른 기호 사용가능
> - 이렇게요
> - **bold도 됩니다.**

## ordered list
1. 1번
2. 2번
    1. 2-1번
    2. 2-2번

## unordered list
- 큰 항목
    - 작은 항목
        - 더 작은 항목

## adding elements in lists
1. 리스트<br>
세부 항목은 br 태크를 쓰거나 스페이스 두번.
2. 리스트  
이렇게요.

## nest unordered list in order list

1. 리스트 제목
    - 세부 항목은 tap으로.
2. 리스트 제목  
    - 세부 항목

## code
- `` 안에는 짧은 코드  
`print("hello world!")`
- \`````` 안에는 긴 코드

## 링크
[표시될 것](www.google.com)  
[처음으로](#md-작성법)
- 문서 내부로 갈때에는 #을 붙이자.

## tables
|제목1 |제목2|
|-----|  ----|
|항목1|항목2|
|항목3은길어요|항목4|

## alignment
|왼쪽|가운데|오른쪽|
|:---|:---:|---:|
|아아아아아|아아아아아|아아아아아|

## task lists(vsc에선 지원 안하는듯?)
- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media
## highlight
<mark>mark 태그</mark>는 하이라이트에요.



<!-- ## 목차
## [1. css란?](#css란)
    이런게 css입니다. 
### [1-1](아오아오)
## [2. html이란?](html-이란?)


### css란?
이런이런것을 css라고합니다.
+ 아오아오
+ 이런거네

### html 이란?
이런것도 html입니다.
+ 아오아오
+ 아오아오 -->
