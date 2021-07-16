# 백준 2908 상수 문제
nums = map(lambda s: s[::-1], input().split())
print(nums[0] if eval('>'.join(nums)) else nums[1])
#----#
nums = map(int, map(lambda s: s[::-1], input().split()))
print(max(nums))