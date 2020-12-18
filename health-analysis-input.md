# 음주 여부에 따라 건강검진 수치 차이가 있을까?
# 신장과 허리 둘레의 크기는 체중과 상관관계가 있을까?
- 분석을 통해 가설을 검증해보기

# 라이브러리 로드


```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

%matplotlib inline
```

# 한글 폰트 설정


```python
import os
if os.name == 'posix':
    plt.rc("font", family="AppleGothic")  
plt.rc("axes", unicode_minus = False)
%config InlineBackend.figure_format = 'retina'
```

# 데이터 불러오기


```python
df = pd.read_csv('../data/NHIS_OPEN_GJ_2017.csv', encoding='cp949')
print(df.shape)
```

    (1000000, 34)


## 데이터 미리보기


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>기준년도</th>
      <th>가입자일련번호</th>
      <th>성별코드</th>
      <th>연령대코드(5세단위)</th>
      <th>시도코드</th>
      <th>신장(5Cm단위)</th>
      <th>체중(5Kg단위)</th>
      <th>허리둘레</th>
      <th>시력(좌)</th>
      <th>시력(우)</th>
      <th>...</th>
      <th>감마지티피</th>
      <th>흡연상태</th>
      <th>음주여부</th>
      <th>구강검진수검여부</th>
      <th>치아우식증유무</th>
      <th>결손치유무</th>
      <th>치아마모증유무</th>
      <th>제3대구치(사랑니)이상</th>
      <th>치석</th>
      <th>데이터공개일자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2017</td>
      <td>1</td>
      <td>1</td>
      <td>8</td>
      <td>43</td>
      <td>170</td>
      <td>75</td>
      <td>90.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>40.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>20181126</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2017</td>
      <td>2</td>
      <td>1</td>
      <td>7</td>
      <td>11</td>
      <td>180</td>
      <td>80</td>
      <td>89.0</td>
      <td>0.9</td>
      <td>1.2</td>
      <td>...</td>
      <td>27.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.0</td>
      <td>20181126</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2017</td>
      <td>3</td>
      <td>1</td>
      <td>9</td>
      <td>41</td>
      <td>165</td>
      <td>75</td>
      <td>91.0</td>
      <td>1.2</td>
      <td>1.5</td>
      <td>...</td>
      <td>68.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>20181126</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2017</td>
      <td>4</td>
      <td>1</td>
      <td>11</td>
      <td>48</td>
      <td>175</td>
      <td>80</td>
      <td>91.0</td>
      <td>1.5</td>
      <td>1.2</td>
      <td>...</td>
      <td>18.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>20181126</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2017</td>
      <td>5</td>
      <td>1</td>
      <td>11</td>
      <td>30</td>
      <td>165</td>
      <td>60</td>
      <td>80.0</td>
      <td>1.0</td>
      <td>1.2</td>
      <td>...</td>
      <td>25.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>20181126</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 34 columns</p>
</div>




```python
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>기준년도</th>
      <th>가입자일련번호</th>
      <th>성별코드</th>
      <th>연령대코드(5세단위)</th>
      <th>시도코드</th>
      <th>신장(5Cm단위)</th>
      <th>체중(5Kg단위)</th>
      <th>허리둘레</th>
      <th>시력(좌)</th>
      <th>시력(우)</th>
      <th>...</th>
      <th>감마지티피</th>
      <th>흡연상태</th>
      <th>음주여부</th>
      <th>구강검진수검여부</th>
      <th>치아우식증유무</th>
      <th>결손치유무</th>
      <th>치아마모증유무</th>
      <th>제3대구치(사랑니)이상</th>
      <th>치석</th>
      <th>데이터공개일자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>999995</th>
      <td>2017</td>
      <td>999996</td>
      <td>1</td>
      <td>10</td>
      <td>48</td>
      <td>175</td>
      <td>80</td>
      <td>92.1</td>
      <td>1.5</td>
      <td>1.5</td>
      <td>...</td>
      <td>27.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>20181126</td>
    </tr>
    <tr>
      <th>999996</th>
      <td>2017</td>
      <td>999997</td>
      <td>1</td>
      <td>8</td>
      <td>41</td>
      <td>170</td>
      <td>75</td>
      <td>86.0</td>
      <td>1.0</td>
      <td>1.5</td>
      <td>...</td>
      <td>15.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>20181126</td>
    </tr>
    <tr>
      <th>999997</th>
      <td>2017</td>
      <td>999998</td>
      <td>2</td>
      <td>9</td>
      <td>26</td>
      <td>155</td>
      <td>50</td>
      <td>68.0</td>
      <td>1.0</td>
      <td>0.7</td>
      <td>...</td>
      <td>17.0</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>20181126</td>
    </tr>
    <tr>
      <th>999998</th>
      <td>2017</td>
      <td>999999</td>
      <td>1</td>
      <td>6</td>
      <td>29</td>
      <td>175</td>
      <td>60</td>
      <td>72.0</td>
      <td>1.5</td>
      <td>1.0</td>
      <td>...</td>
      <td>17.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>20181126</td>
    </tr>
    <tr>
      <th>999999</th>
      <td>2017</td>
      <td>1000000</td>
      <td>1</td>
      <td>11</td>
      <td>41</td>
      <td>160</td>
      <td>70</td>
      <td>90.5</td>
      <td>1.0</td>
      <td>1.5</td>
      <td>...</td>
      <td>36.0</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>20181126</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 34 columns</p>
</div>




```python
# get random value
df.sample()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>기준년도</th>
      <th>가입자일련번호</th>
      <th>성별코드</th>
      <th>연령대코드(5세단위)</th>
      <th>시도코드</th>
      <th>신장(5Cm단위)</th>
      <th>체중(5Kg단위)</th>
      <th>허리둘레</th>
      <th>시력(좌)</th>
      <th>시력(우)</th>
      <th>...</th>
      <th>감마지티피</th>
      <th>흡연상태</th>
      <th>음주여부</th>
      <th>구강검진수검여부</th>
      <th>치아우식증유무</th>
      <th>결손치유무</th>
      <th>치아마모증유무</th>
      <th>제3대구치(사랑니)이상</th>
      <th>치석</th>
      <th>데이터공개일자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>269190</th>
      <td>2017</td>
      <td>269191</td>
      <td>1</td>
      <td>8</td>
      <td>41</td>
      <td>175</td>
      <td>75</td>
      <td>87.0</td>
      <td>1.2</td>
      <td>1.2</td>
      <td>...</td>
      <td>17.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>20181126</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 34 columns</p>
</div>



# 기본 정보 보기


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 1000000 entries, 0 to 999999
    Data columns (total 34 columns):
     #   Column        Non-Null Count    Dtype  
    ---  ------        --------------    -----  
     0   기준년도          1000000 non-null  int64  
     1   가입자일련번호       1000000 non-null  int64  
     2   성별코드          1000000 non-null  int64  
     3   연령대코드(5세단위)   1000000 non-null  int64  
     4   시도코드          1000000 non-null  int64  
     5   신장(5Cm단위)     1000000 non-null  int64  
     6   체중(5Kg단위)     1000000 non-null  int64  
     7   허리둘레          999734 non-null   float64
     8   시력(좌)         999817 non-null   float64
     9   시력(우)         999811 non-null   float64
     10  청력(좌)         999842 non-null   float64
     11  청력(우)         999844 non-null   float64
     12  수축기혈압         999981 non-null   float64
     13  이완기혈압         999982 non-null   float64
     14  식전혈당(공복혈당)    999958 non-null   float64
     15  총콜레스테롤        999957 non-null   float64
     16  트리글리세라이드      999955 non-null   float64
     17  HDL콜레스테롤      999956 non-null   float64
     18  LDL콜레스테롤      997088 non-null   float64
     19  혈색소           999948 non-null   float64
     20  요단백           995408 non-null   float64
     21  혈청크레아티닌       999957 non-null   float64
     22  (혈청지오티)AST    999959 non-null   float64
     23  (혈청지오티)ALT    999958 non-null   float64
     24  감마지티피         999958 non-null   float64
     25  흡연상태          999856 non-null   float64
     26  음주여부          999464 non-null   float64
     27  구강검진수검여부      1000000 non-null  int64  
     28  치아우식증유무       0 non-null        float64
     29  결손치유무         0 non-null        float64
     30  치아마모증유무       0 non-null        float64
     31  제3대구치(사랑니)이상  0 non-null        float64
     32  치석            400523 non-null   float64
     33  데이터공개일자       1000000 non-null  int64  
    dtypes: float64(25), int64(9)
    memory usage: 259.4 MB



```python
df.columns
```




    Index(['기준년도', '가입자일련번호', '성별코드', '연령대코드(5세단위)', '시도코드', '신장(5Cm단위)',
           '체중(5Kg단위)', '허리둘레', '시력(좌)', '시력(우)', '청력(좌)', '청력(우)', '수축기혈압',
           '이완기혈압', '식전혈당(공복혈당)', '총콜레스테롤', '트리글리세라이드', 'HDL콜레스테롤', 'LDL콜레스테롤',
           '혈색소', '요단백', '혈청크레아티닌', '(혈청지오티)AST', '(혈청지오티)ALT', '감마지티피', '흡연상태',
           '음주여부', '구강검진수검여부', '치아우식증유무', '결손치유무', '치아마모증유무', '제3대구치(사랑니)이상', '치석',
           '데이터공개일자'],
          dtype='object')




```python
df.dtypes
```




    기준년도              int64
    가입자일련번호           int64
    성별코드              int64
    연령대코드(5세단위)       int64
    시도코드              int64
    신장(5Cm단위)         int64
    체중(5Kg단위)         int64
    허리둘레            float64
    시력(좌)           float64
    시력(우)           float64
    청력(좌)           float64
    청력(우)           float64
    수축기혈압           float64
    이완기혈압           float64
    식전혈당(공복혈당)      float64
    총콜레스테롤          float64
    트리글리세라이드        float64
    HDL콜레스테롤        float64
    LDL콜레스테롤        float64
    혈색소             float64
    요단백             float64
    혈청크레아티닌         float64
    (혈청지오티)AST      float64
    (혈청지오티)ALT      float64
    감마지티피           float64
    흡연상태            float64
    음주여부            float64
    구강검진수검여부          int64
    치아우식증유무         float64
    결손치유무           float64
    치아마모증유무         float64
    제3대구치(사랑니)이상    float64
    치석              float64
    데이터공개일자           int64
    dtype: object



# 결측치 보기


```python
# isnull로 null 이면 True(1), null이 아니면 False(0)
# 위 값을 sum()으로 더한다.
df.isnull().sum()
```




    기준년도                  0
    가입자일련번호               0
    성별코드                  0
    연령대코드(5세단위)           0
    시도코드                  0
    신장(5Cm단위)             0
    체중(5Kg단위)             0
    허리둘레                266
    시력(좌)               183
    시력(우)               189
    청력(좌)               158
    청력(우)               156
    수축기혈압                19
    이완기혈압                18
    식전혈당(공복혈당)           42
    총콜레스테롤               43
    트리글리세라이드             45
    HDL콜레스테롤             44
    LDL콜레스테롤           2912
    혈색소                  52
    요단백                4592
    혈청크레아티닌              43
    (혈청지오티)AST           41
    (혈청지오티)ALT           42
    감마지티피                42
    흡연상태                144
    음주여부                536
    구강검진수검여부              0
    치아우식증유무         1000000
    결손치유무           1000000
    치아마모증유무         1000000
    제3대구치(사랑니)이상    1000000
    치석               599477
    데이터공개일자               0
    dtype: int64




```python
df.isna().sum()
```




    기준년도                  0
    가입자일련번호               0
    성별코드                  0
    연령대코드(5세단위)           0
    시도코드                  0
    신장(5Cm단위)             0
    체중(5Kg단위)             0
    허리둘레                266
    시력(좌)               183
    시력(우)               189
    청력(좌)               158
    청력(우)               156
    수축기혈압                19
    이완기혈압                18
    식전혈당(공복혈당)           42
    총콜레스테롤               43
    트리글리세라이드             45
    HDL콜레스테롤             44
    LDL콜레스테롤           2912
    혈색소                  52
    요단백                4592
    혈청크레아티닌              43
    (혈청지오티)AST           41
    (혈청지오티)ALT           42
    감마지티피                42
    흡연상태                144
    음주여부                536
    구강검진수검여부              0
    치아우식증유무         1000000
    결손치유무           1000000
    치아마모증유무         1000000
    제3대구치(사랑니)이상    1000000
    치석               599477
    데이터공개일자               0
    dtype: int64




```python
df.isnull().sum().plot.barh(figsize=(10,9))
```




    <AxesSubplot:>




    
![png](output_18_1.png)
    


# 일부 데이터 요약하기


```python
df.columns
```




    Index(['기준년도', '가입자일련번호', '성별코드', '연령대코드(5세단위)', '시도코드', '신장(5Cm단위)',
           '체중(5Kg단위)', '허리둘레', '시력(좌)', '시력(우)', '청력(좌)', '청력(우)', '수축기혈압',
           '이완기혈압', '식전혈당(공복혈당)', '총콜레스테롤', '트리글리세라이드', 'HDL콜레스테롤', 'LDL콜레스테롤',
           '혈색소', '요단백', '혈청크레아티닌', '(혈청지오티)AST', '(혈청지오티)ALT', '감마지티피', '흡연상태',
           '음주여부', '구강검진수검여부', '치아우식증유무', '결손치유무', '치아마모증유무', '제3대구치(사랑니)이상', '치석',
           '데이터공개일자'],
          dtype='object')




```python
# 두 개 이상의 컬럼을 가져오려면 []로 감싸줘서 리스트 형태를 만들어야한다.
df[['(혈청지오티)ALT', '(혈청지오티)AST']].head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>(혈청지오티)ALT</th>
      <th>(혈청지오티)AST</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>35.0</td>
      <td>21.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>36.0</td>
      <td>20.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>32.0</td>
      <td>47.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>34.0</td>
      <td>29.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>12.0</td>
      <td>19.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[['(혈청지오티)ALT', '(혈청지오티)AST']].info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 1000000 entries, 0 to 999999
    Data columns (total 2 columns):
     #   Column      Non-Null Count   Dtype  
    ---  ------      --------------   -----  
     0   (혈청지오티)ALT  999958 non-null  float64
     1   (혈청지오티)AST  999959 non-null  float64
    dtypes: float64(2)
    memory usage: 15.3 MB



```python
df[['(혈청지오티)ALT', '(혈청지오티)AST']].describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>(혈청지오티)ALT</th>
      <th>(혈청지오티)AST</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>999958.000000</td>
      <td>999959.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>25.749509</td>
      <td>25.994671</td>
    </tr>
    <tr>
      <th>std</th>
      <td>26.294770</td>
      <td>23.587469</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>15.000000</td>
      <td>19.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>20.000000</td>
      <td>23.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>29.000000</td>
      <td>28.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>7210.000000</td>
      <td>9999.000000</td>
    </tr>
  </tbody>
</table>
</div>



# value_counts로 값 집계하기


```python
# 남자: 1, 여자: 2
df['성별코드'].value_counts()
```




    1    530410
    2    469590
    Name: 성별코드, dtype: int64




```python
df['흡연상태'].value_counts()
```




    1.0    607942
    3.0    215702
    2.0    176212
    Name: 흡연상태, dtype: int64



# groupby 와 pivot_table 사용하기
## groupby


```python
df.groupby(["성별코드"])['가입자일련번호'].count()
# Series 형태로 결과가 나온다.
# pivot_table 은 DF 형태로 나온다.
```




    성별코드
    1    530410
    2    469590
    Name: 가입자일련번호, dtype: int64




```python
df.groupby(['성별코드', '음주여부'])['가입자일련번호'].count()
```




    성별코드  음주여부
    1     0.0     173612
          1.0     356587
    2     0.0     326827
          1.0     142438
    Name: 가입자일련번호, dtype: int64




```python
# 음주 여부에 따라 간에 관련된 수치의 평균이 영향이 받는 것을 분석
df.groupby(['성별코드', '음주여부'])['감마지티피'].mean()
```




    성별코드  음주여부
    1     0.0     34.739868
          1.0     56.610981
    2     0.0     22.612408
          1.0     25.001018
    Name: 감마지티피, dtype: float64




```python
df.groupby(['성별코드', '음주여부'])['감마지티피'].describe()
# max 값이 2, 3사분위 수보다 지나치게 높다.
# 다른 의미가 있음을 암시 Or 쓰레기 값
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
    <tr>
      <th>성별코드</th>
      <th>음주여부</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">1</th>
      <th>0.0</th>
      <td>173604.0</td>
      <td>34.739868</td>
      <td>37.606197</td>
      <td>1.0</td>
      <td>18.0</td>
      <td>25.0</td>
      <td>38.0</td>
      <td>999.0</td>
    </tr>
    <tr>
      <th>1.0</th>
      <td>356576.0</td>
      <td>56.610981</td>
      <td>68.851128</td>
      <td>1.0</td>
      <td>24.0</td>
      <td>37.0</td>
      <td>63.0</td>
      <td>999.0</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">2</th>
      <th>0.0</th>
      <td>326813.0</td>
      <td>22.612408</td>
      <td>25.203579</td>
      <td>1.0</td>
      <td>13.0</td>
      <td>17.0</td>
      <td>24.0</td>
      <td>999.0</td>
    </tr>
    <tr>
      <th>1.0</th>
      <td>142429.0</td>
      <td>25.001018</td>
      <td>36.725100</td>
      <td>1.0</td>
      <td>13.0</td>
      <td>17.0</td>
      <td>25.0</td>
      <td>999.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.groupby(['성별코드', '음주여부'])['감마지티피'].agg(['count', 'mean', 'median'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>median</th>
    </tr>
    <tr>
      <th>성별코드</th>
      <th>음주여부</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">1</th>
      <th>0.0</th>
      <td>173604</td>
      <td>34.739868</td>
      <td>25.0</td>
    </tr>
    <tr>
      <th>1.0</th>
      <td>356576</td>
      <td>56.610981</td>
      <td>37.0</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">2</th>
      <th>0.0</th>
      <td>326813</td>
      <td>22.612408</td>
      <td>17.0</td>
    </tr>
    <tr>
      <th>1.0</th>
      <td>142429</td>
      <td>25.001018</td>
      <td>17.0</td>
    </tr>
  </tbody>
</table>
</div>



## pivot_table


```python
# 사용법이 groupby에 비해 직관적이고 효과적이다. 속도는 상대적으로 느리다.
df.pivot_table(index='음주여부', values="가입자일련번호", aggfunc='count')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>가입자일련번호</th>
    </tr>
    <tr>
      <th>음주여부</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0.0</th>
      <td>500439</td>
    </tr>
    <tr>
      <th>1.0</th>
      <td>499025</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.pivot_table(df, index='음주여부', values='감마지티피', 
               aggfunc=['mean', 'median'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>mean</th>
      <th>median</th>
    </tr>
    <tr>
      <th></th>
      <th>감마지티피</th>
      <th>감마지티피</th>
    </tr>
    <tr>
      <th>음주여부</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0.0</th>
      <td>26.819650</td>
      <td>19.0</td>
    </tr>
    <tr>
      <th>1.0</th>
      <td>47.588675</td>
      <td>30.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.pivot_table(df, index=['성별코드', '음주여부'], values='감마지티피', 
               aggfunc='describe')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>count</th>
      <th>max</th>
      <th>mean</th>
      <th>min</th>
      <th>std</th>
    </tr>
    <tr>
      <th>성별코드</th>
      <th>음주여부</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">1</th>
      <th>0.0</th>
      <td>18.0</td>
      <td>25.0</td>
      <td>38.0</td>
      <td>173604.0</td>
      <td>999.0</td>
      <td>34.739868</td>
      <td>1.0</td>
      <td>37.606197</td>
    </tr>
    <tr>
      <th>1.0</th>
      <td>24.0</td>
      <td>37.0</td>
      <td>63.0</td>
      <td>356576.0</td>
      <td>999.0</td>
      <td>56.610981</td>
      <td>1.0</td>
      <td>68.851128</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">2</th>
      <th>0.0</th>
      <td>13.0</td>
      <td>17.0</td>
      <td>24.0</td>
      <td>326813.0</td>
      <td>999.0</td>
      <td>22.612408</td>
      <td>1.0</td>
      <td>25.203579</td>
    </tr>
    <tr>
      <th>1.0</th>
      <td>13.0</td>
      <td>17.0</td>
      <td>25.0</td>
      <td>142429.0</td>
      <td>999.0</td>
      <td>25.001018</td>
      <td>1.0</td>
      <td>36.725100</td>
    </tr>
  </tbody>
</table>
</div>



# 전체 데이터 시각화
- 100만개 이상의 데이터를 시각화할 때는 되도록 groupby or pivot_table로 연산을 하고 시각화를 하는 것을 권장.
- 100만개 이상의 데이터를 seaborn과 같은 고급 통계 연산을 하는 그래프를 사용하게 되면 많이 느리다.

## 히스토그램


```python
h = df.hist(figsize=(12,12))
```


    
![png](output_39_0.png)
    


## 슬라이싱을 사용해 히스토그램 그리기


```python
# 11 컬럼까지만 그리기
h = df.iloc[:, :12].hist(figsize=(12,12))
```


    
![png](output_41_0.png)
    



```python
# 12 ~ 23까지 (12:24)
h = df.iloc[:, 12:24].hist(figsize=(12, 12), bins=100)
```


    
![png](output_42_0.png)
    



```python
# 24 ~ 끝까지 (24:)
h = df.iloc[:, 24:].hist(figsize=(12, 12), bins=10)
```


    
![png](output_43_0.png)
    


# 샘플 데이터 추출하기


```python
# df.sample을 통해 일부 데이터만 샘플 데이터를 추출합니다.
# random_state를 사용해 샘플링되는 값을 고정할 수 있습니다.
# 실험을 통제하기 위해 random_state는 고정하기도 합니다.
# 여기에서는 1을 사용하겠습니다. 이 값은 높든 낮든 상관 없이 값을 고정하는 역할만 합니다.

df_sample = df.sample(1000, random_state=1)
df_sample.shape
```




    (1000, 34)



# 데이터 시각화 도구 seaborn 사용하기
- matplotlib을 사용하기 쉽게 만들어 졌으며, 간단하게 고급 통계 연산을 할 수 있습니다.

# 범주형(카테고리) 데이터 시각화
- countplot은 범주형 데이터의 수를 더한 값을 그래프로 표현한다.
- value_counts로 구한 값을 시각화 한다고 보면 된다.

## countplot - 음주여부


```python
# 음주 여부에 따른 countplot 그리기.
df['음주여부'].value_counts().plot.bar()
```




    <AxesSubplot:>




    
![png](output_49_1.png)
    



```python
sns.countplot(x='음주여부', data=df)
```




    <AxesSubplot:xlabel='음주여부', ylabel='count'>




    
![png](output_50_1.png)
    



```python

```
