import numpy as np

#단일 객체 저장 및 불러오기
array = np.arange(0,10)
np.save('saved.npy', array)

result = np.load('saved.npy')
print(result)

#복수 객체 저장 및 불러오기
array1 = np.arange(0,10)
array2 = np.arange(10,20)
np.savez('saved.npz', savedarray1 = array1, savedarray2 = array2)

data = np.load('saved.npz')
result1 = data['savedarray1']
result2 = data['savedarray2']

print(result1)
print(result2)

# 정렬

array3 = np.array([5,9,10,3,1])
array3.sort()
print(array3)#기본 오름차순
print(array3[::-1]) #내림차순

#각 축을 기준으로 정렬
array4 = np.array([[5,9,10,3,1],[8,3,4,2,5]])
print("축 정렬 전\n",array4)

array4.sort(axis= 0)
print("세로(열) 축 정렬 후\n",array4)

array4.sort(axis= 1)
print("가로(행) 축 정렬 휴\n",array4)

#균일한 간격으로 데이터 생성 시작값과 끝값 사이 균일한 간격으로 5개 데이터 생성
array5 = np.linspace(0,10,5)
print(array5)

#난수의 재연(실행마다 결과 동일) seed를 설정해 주는 것
np.random.seed(7)
print(np.random.randint(0,10,(2,3)))

#NUmpy 배열 객체 복사
array6 = np.arange(0,10)
array7 = array6
array7[0] = 99
print(array6) #이 경우에는 array7이 array6의 주소 값을 복사 받기 때문에 array7의 값을 바꾸어도 array6의 값이 바뀐다

array6 = np.arange(0,10)
array8 = array6.copy()
array8[0] = 99
print(array6)

#중복된 원소 제거
array9 = np.array([1,1,2,2,2,3,4])
print(np.unique(array9))