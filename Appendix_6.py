# result = sum([1,2,3,4,5])
# print(result)

# result = min([1,2,3,4,1,2])
#
# print(result)

# result = max(7,5,3,2)
# print(result)

# result = eval("(3+5)*7")
# print(result)

# result = sorted([9,1,8,5,4])
# print(result)
# result = sorted([9,1,8,5,4], reverse = True)
# print(result)

# list = ([(35,'홍길동'),(25,'이순신'),(75,'아무개'),])
# result = sorted(list, key = lambda x: x[0], reverse = True)
# print(result)
#
# data = [9,1,8,5,4]
# data.sort()
# print(data)

#Permutations, Combinations

# from itertools import permutations
#
# data = ['A','B','C'] # 데이터 준비
#
# result = list(permutations(data,3)) # 모든 순열 구하기
#
# print(result)

# from itertools import combinations
#
# data = ['A','B','C'] # 데이터 준비
#
# result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합 구하기
#
# print(result)

# from itertools import product
#
# data = ['A','B','C'] # 데이터 준비
# result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기(중복 허용)
#
# print(result)

# from itertools import combinations_with_replacement
#
# # 데이터 준비
# data = ['A','B','C']
#
# # 2개를 뽑는 모든 조합 구하기(중복 허용)
# result = list(combinations_with_replacement(data,2))
# print(result)

# import heapq
#
# def heapsort(iterable):
#     h = []
#     result = []
#     # 모든 원소를 차례대로 힙에 삽입
#     for value in iterable:
#         heapq.heappush(h, value)
#     # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
#     for i in range(len(h)):
#         result.append(heapq.heappop(h))
#     return result
#
# result = heapsort([1,3,5,7,9,2,4,6,8,0])
# print(result)

# import heapq
# def heapsort(iterable):
#     h = []
#     result = []
#     # 모든 원소를 차례대로 힙에 삽입
#     for value in iterable:
#         heapq.heappush(h, -value)
#     # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
#     for i in range(len(h)):
#         result.append(-heapq.heappop(h))
#     return result
#
# result = heapsort([1,3,5,7,9,2,4,6,8,0])
#
# print(result)
#
# from bisect import bisect_left, bisect_right
# a = [1,2,4,4,8]
# x = 4
#
# print(bisect_left(a,x))
# print(bisect_right(a,x))









































