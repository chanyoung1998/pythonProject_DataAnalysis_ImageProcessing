import numpy as np



#NUmpy 기본연산
array = np.random.randint(0,10,size = 4).reshape(2,2)
print(array)

result_array = array +2
print(result_array)

result_array = array*2
print(result_array)


#브로드 캐스트

array1 = np.arange(4).reshape(2,2)
array2 = np.arange(2).reshape(1,2)

result_array = array1+array2
print(array1)
print(array2)
print(result_array)

#마스킹 연산

array3 = np.arange(16).reshape(4,4)
array4 = array3 < 10
print(array4)

array3[array4] = 100 #10보다 작은 값을 100으로 바꾸는 작업
print(array3)

#집계함수

array5 = np.arange(16).reshape(4,4)
print("최대값",np.max(array5))
print("최소값",np.min(array5))
print("평균값",np.mean(array5))
print("합계",np.sum(array5))

#축기준으로 집계
print(array5)
print("합계(세로축)",np.sum(array5,axis=0))
print("합계(가로축)",np.sum(array5,axis=1))