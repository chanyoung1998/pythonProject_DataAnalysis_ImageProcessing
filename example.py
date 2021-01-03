import numpy as np

#기본적인 기능

list_data = [1,2,3]
array = np.array(list_data)

print(array)
print(array.size)
print(array.dtype)
print(array[2])

#0 부터 3까지의 배열 만들기

array1 = np.arange(4)
print(array1)

#4x4행렬이면서 0으로 초기화하는 배열을 만들기, 데이터 타입은 실수형

array2 = np.zeros((4,4),dtype=float)
print(array2)

#3x3행렬이면서 1으로 초기화하는 배열을 만들기, 데이터 타입은 문자열형

array3 = np.ones((3,3),dtype= str)
print(array3)


#3x3행렬이면서 무작위로 초기화(0~9)하는 배열을 만들기, 데이터 타입은 정수형

array4 = np.random.randint(0,10,(3,3))
print(array4)

#평균이 0이고 표준편차가 1인 표준 정규를 띄는 배열

array5 = np.random.normal(0,1,(3,3))
print(array5)



#배열 합치기 concatenate 사용

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
array3 = np.concatenate([array1,array2])

print(array3.shape)
print(array3)

#배열의 형태 바꾸기 reshape

array1 = np.array([1,2,3,4,5,6,7,8,])
array2 = array1.reshape((4,2))

print(array2)

#배열의 형태 바꾸기: 세로축 기준으로 합치기
array1 = np.arange(4).reshape(1,4)
array2 = np.arange(8).reshape(2,4)

print(array1)
print(array2)

array3 = np.concatenate([array1,array2], axis=0)
print(array3)

#배열 나누기

array6 = np.arange(8).reshape(2,4)
left,right = np.split(array6,[2],axis= 1)
print(left.shape)
print(right.shape)
print(array6)
print(left)
print(left[1][1])