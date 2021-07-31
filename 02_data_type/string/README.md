## 목차

- [문자열](#문자열)
    - [문자열 (string)](#문자열-string)
  - [문자열 표현 방식](#문자열-표현-방식)
    - [큰따옴표](#큰따옴표)
    - [작은따옴표](#작은따옴표)
    - [문자열 내부 따옴표](#문자열-내부-따옴표)
    - [이스케이프 문자](#이스케이프-문자)
    - [여러줄](#여러줄)
  - [문자열 연산자](#문자열-연산자)
    - [문자열 연결 연산자](#문자열-연결-연산자)
    - [문자열 반복 연사자](#문자열-반복-연사자)
    - [문자열 선택 연산자(인덱싱)](#문자열-선택-연산자인덱싱)
    - [문자열 범위 선택 연산자(슬라이싱)](#문자열-범위-선택-연산자슬라이싱)
    - [문자열 길이](#문자열-길이)

# 문자열

### 문자열 (string)

- 문자열은 말 그대로 글자를 나열된 것을 뜻하고 영어로는 `string` 이라고 한다.

## 문자열 표현 방식

### 큰따옴표

**`""`**

- 큰따옴표로 감싸진 문자열

```python
print("문자열입니다.")
# 결과 : 
# 문자열입니다.
```

### 작은따옴표 

**`''`**

- 작은따옴표로 감싸진 문자열

```python
print('문자열입니다.')
# 결과 : 
# 문자열입니다.
```

### 문자열 내부 따옴표

**`'"'`**, **`"'"`**, **`"\""`**, **`'\''`**

- 다른 따옴표로 감싸거나 이스케이프 문자를 사용한 문자열
- 이스케이프 문자 (excape character) : 역슬래시(`\`) 기호와 함께 조합해서 사용하는 특수문자를 의미

```python
print('"문자열"입니다.')
# 결과 : 
# "문자열"입니다.
print("'문'자열입니다.")
# 결과 : 
# '문'자열입니다.
print("\"문자열입니다.\"")
# 결과 : 
# "문자열입니다."
print('\'문자열입니다.\'')
# 결과 : 
# '문자열입니다.'
```

### 이스케이프 문자

- `\"` : 큰따옴표
- `\'` : 작은따옴표
- `\\` : 역슬래시
- `\n` : 줄바꿈
- `\t` : 탭

```python
print("줄바꿈\n입니다.")
print("탭\t입니다.")
print("역슬래시 \\")
```

### 여러줄

- 세번 반복 큰따옴표 또는 작은따옴표 기호를 사용

```python
print("""
여러줄1
여러줄2
여러줄3
""")
# 결과 :
#
# 여러줄1
# 여러줄2
# 여러줄3
#

# 첫줄과 마지막줄에 빈줄이 생김
```

```python
print("""\
여러줄1
여러줄2
여러줄3\
""")
# 결과 : 
# 여러줄1
# 여러줄2
# 여러줄3

# 역슬래시 '\'를 활용해서 빈줄제거
```

## 문자열 연산자

- 문자열 연산자는 문자열끼리의 연산을 뜻하며 숫자 연산과 다르다.
- 그러기 때문에 일부 연산자에서 숫자 타입과의 연산을 주의해서 사용해야한다.

### 문자열 연결 연산자 

**`+`**

- `+` 기호를 통해 문자열을 연결

```python
print("문자" + "연결")
# 결과 : 
# 문자연결
print("안녕" + "하세요" + " !")
# 결과 : 
# 안녕하세요 !

print("안녕하세요" + 1)
# 결과(Err) : TypeError: can only concatenate str (not "int") to str
```

### 문자열 반복 연사자 

**`*`**

- `*` 기호를 사용하면 숫자만큼 문자열을 반복시킬 수 있습니다.
- `문자열 * 숫자`와 `숫자 * 문자열`의 실행결과는 똑같다.

```python
print("문자열반복" * 3)
# 결과 :
# 문자열반복문자열반복문자열반복
```

### 문자열 선택 연산자(인덱싱) 

**`[]`**

- 문자열 옆에 `[]`기호를 사용해서 해당 인덱스의 문자를 선택할 수 있다.
- `"문자열"[index]`
  - 인덱스(index)는 숫자로 표기하며 0부터 시작한다.

```python
print("문자열선택하기")
print("문자열선택"[0])
print("문자열선택"[1])
print("문자열선택"[2])
print("문자열선택"[3])
print("문자열선택"[4])
# 결과 : 
# 문자열선택하기
# 문
# 자
# 열
# 선
# 택
```

- 인덱스가 음수이면 뒤에서부터 선택한다.

```python
print("문자열선택"[-1])
print("문자열선택"[-2])
print("문자열선택"[-3])
print("문자열선택"[-4])
print("문자열선택"[-5])
# 결과 :
# 택
# 선
# 열
# 자
# 문
```

- IndexError 예외 : 잘못된 범위 안의 인덱스에 접근할시 발생
```python
print("문자열선택"[10])
# 결과(Err) : IndexError: string index out of range
```

### 문자열 범위 선택 연산자(슬라이싱) 

**`[:]`**

- 선택 연산자(인덱싱)에 콜론`:`을 사용해서 범위의 문자열을 선택할 수 있다.
- 문자열 범위 선택 연산자는 대괄호 안의 두 숫자중 하나를 생략 할 수 있다.
  - `[n:]` : n번째에서 끝의 문자까지의 범위
  - `[:n]` : 첫 문자에서 (n-1)번째까지의 범위

```python
print("문자열범위"[1:3])
print("문자열범위"[0:2])
print("문자열범위"[1:])
print("문자열범위"[:3])
# 결과 :
# 자열
# 문자
# 자열범위
# 문자열
```

### 문자열 길이

**`len()`**

- `len()` : 문자열 길이를 구할 때 사용하는 함수

```python
print(len("문자열길이"))
# 결과 : 
# 5
```