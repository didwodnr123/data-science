# 파이썬을 이용한 웹 스크래핑

> Using Python to Access Web Data
>
> [출처: edwith](https://www.edwith.org/python-network-data/joinLectures/13749)



## Contents

- **정규식**
- **HTTP**
- **웹 서비스**



## Regular Expression

> 정규식은 효율적으로 검색을 할 수 있도록 도와주고 원하는 문자열 패턴을 검색할 수 있습니다.

```
^           라인의 처음을 매칭

$            라인의 끝을 매칭

.             임의의 문자를 매칭 (와일드 카드)

\s          공백 문자를 매칭

\S         공백이 아닌 문자를 매칭

*            바로 앞선 문자에 적용되고 0 혹은 그 이상의 앞선 문자와 매칭을 표기함.

*?          바로 앞선 문자에 적용되고 0 혹은 그 이상의 앞선 문자와 매칭을 탐욕적이지 않은 방식으로 표기함.

+           바로 앞선 문자에 적용되고 1 혹은 그 이상의 앞선 문자와 매칭을 표기함

+?          바로 앞선 문자에 적용되고 1 혹은 그 이상의 앞선 문자와 매칭을 탐욕적이지 않은 방식으로 표기함.

[aeiou]    명세된 집합 문자에 존재하는 단일 문자와 매칭. “a”, “e”, “i”, “o”, “u” 문자만 매칭되는 예제

[a-z0-9]    - 기호로 문자 범위를 명세할 수 있다. 소문자이거나 숫자인 단일 문자만 매칭되는 예제.

( )         괄호가 정규표현식에 추가될 때, 매칭을 무시한다. 하지만 findall()을 사용 할 때 전체 문자열보다 매칭된 문자열의 상세한 부속 문자열을 추출할 수 있게 한다.
```



**텍스트에서 문자 패턴 찾기**

```python
import re # regular expression

hand = open('sample.txt')
for line in hand:
  line = line.rstrip() # 오른쪽 공백을 제거합니다.
  if line.find('From:') >= 0: # 'From:' 이 포함된 문자열을 찾습니다.
    print(line)
```

stratswith을 사용할 수도 있습니다.

```python
import re # regular expression

hand = open('sample.txt')
for line in hand:
  line = line.rstrip() # 오른쪽 공백을 제거합니다.
  if re.startswith('From:'): # 'From:' 으로 시작하는 문자열을 찾습니다.
    print(line)
```

위 코드를 정규 표현식으로 표현하면 `^` 문자를 사용하면 됩니다.

```python
import re # regular expression

hand = open('sample.txt')
for line in hand:
  line = line.rstrip() # 오른쪽 공백을 제거합니다.
  if re.search('^From:', line): # 'From:' 으로 시작하는 문자열을 찾습니다.
    print(line)
```



**특수문자를 사용한 문자 패턴 찾기**

따라서, 다음과 같은 문자열들은 모두 '^X.*:'라는 패턴을 통해 찾을 수 있습니다.

- X-Sieve: CMU Sieve 2.3
- X-DSPAM-Result: Innocent
- X-DSPAM-Confidence: 0.8475
- X-Content-Type-Message-Body: text/plain

그리고 다음과 같은 문자열들은 '^X-\S+:' 패턴으로 찾을 수 있으며,

- X-Sieve: CMU Sieve 2.3
- X-DSPAM-Result: Innocent

다음의 문자열은 'X-'와 ':' 사이에 공백 문자가 아닌 문자가 포함되지 않았기 때문에 '^X-\S+:' 패턴으로 찾을 수 없습니다.

- X-: Very short
- X-Plane is behind schedule: two weeks