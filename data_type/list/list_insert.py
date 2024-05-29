'''
* 리스트에 데이터를 추가하는 메서드
1. append(): 요소를 리스트의 맨 마지막에 추가.
2. insert(): 요소를 리스트의 특정 위치에 삽입.
'''

nums = [1, 3, 5, 7]
nums.append('안녕')
print(nums) # [1, 3, 5, 7, '안녕']

# insert(특정 위치 인덱스, 넣을 값)
nums.insert(3, 4)
print(nums) # [1, 3, 5, 4, 7, '안녕']
