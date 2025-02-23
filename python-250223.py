sub_num = int(input())
org_score = list(map(float, input().split()))
print(sum(org_score) / max(org_score) * 100 / sub_num)