data = []
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line) # 要加入清單

# 要篩選留言長度小於100的
new = []
for d in data: # for loop是把清單(data)的東西一個一個拿出來(每一個叫做d)
	# d是字串/data是清單
	if len(d) < 100: # 如果留言長度小於一百
		new.append(d) # 就把這留言加入清單 (!!!!)注意不是data
print('一共有', len(new), '筆留言長度小於100') 
# 如果放在for loop框框下就會一直印,但這邊只想印一次