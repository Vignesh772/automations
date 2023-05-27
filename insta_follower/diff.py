import collections
with open('followers.txt') as f:
    pre_followers = f.read().splitlines()
print(len(pre_followers))


pre_followers = set(pre_followers)



with open('followers_1.txt') as f:
    followers = f.read().splitlines()
print(len(followers))
followers = set(followers)

total = followers.union(pre_followers)
print(len(total))
print(len(followers), len(pre_followers))
print(followers-pre_followers)





