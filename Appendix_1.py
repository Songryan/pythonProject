# a = 1e9
# print(a)
#
# a = 0.3 + 0.6
# print(a)
#
# if a == 0.9:
#     print(True)
# else:
#     print(False)

# a = 0.3 + 0.6
# print(round(a, 4))
#
# if round(a,4) == 0.9:
#     print(True)
# else:
#     print(False)

# n = 10
# a = [0] * n
# print(a)

# array = [i for i in range(20) if i%2 == 1]
# print(array)
#
# array = [i*i for i in range(1,10)]
# print(array)

# n = 3
# m = 4
# array = [[0]*m for i in range(n)]
# print(array)

# a = [1,4,3]
# print("기본 리스트 : ", a)
#
# #리스트에 원소 삽입
# a.append(2)
# print("삽입 : ",a)
#
# #오름차순 정렬
# a.sort()
# print("오름차순 정렬 : ",a)
#
# #내림차순 정렬
# a.sort(reverse=True)
# print("내림차순 정렬 : ", a)
#
# #리스트 원소 뒤집기
# a.reverse()
# print("원소 뒤집기 : ",a)
#
# # 특정 인덱스에 데이터 추가
# a.insert(2,3)
# print("인덱스 2에 3추가 ",a)
#
# # 특정 값인 데이터 개수 세기
# print("값이 3인 데이터 개수 : ", a.count(3))
#
# a.remove(1)
# print("값이 1인 데이터 삭제 : ", a)

# #특정 값 제거
# a = [1,2,3,4,5,5,5]
# remove_set = {3,5}
#
# #remove_set에 포함되지 않은 값만을 저장
# result = [i for i in a if i not in remove_set]
# print(result)

# data = "Don't you know \"Python\"?"
# print(data)

# a = "String"
# print((a + " ") *3)

# a = "ABCDEF"
# print(a[0:2])

# data = dict()
# data['사과'] = 'Apple'
# data['바나나'] = 'Banana'
# data['코코넛'] = 'Coconut'
#
# print(data)
#
# if '사과' in data:
#     print("사과있음")
#
# data = dict()
# data['사과'] = 'Apple'
# data['바나나'] = 'Banana'
# data['코코넛'] = 'Coconut'
#
# #키 데이터만 담은 리스트
# key_list = data.keys()
#
# #값 데이터만 담은 리스트
# value_list = data.values()
#
# print(key_list)
# print(value_list)
#
# # 각 ㅋ에 따른 값을 하나씩 출력\
# for key in key_list:
#     print(data[key])

# # 집합 자료형 초기화 방법 1
# data = set([1,2,3,4,5])
# print(data)
#
# # 집합 자료형 초기화 방법
# data = {1,1,2,3,4,4,5}
# print(data)
#
# a = set([1,2,3,4,5])
# b = set([3,4,5,6,7])
#
# print(a|b) # 합집합
# print(a&b) # 교집합
# print(a-b) # 차집합

data = set([1,2,3])
print(data)

# 새로운 원소 추가
data.add(4)
print(data)

# 새로운 원소 여러 개 추가
data.update([5,6])
print(data)

# 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)
















