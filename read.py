data = []
with open ('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)

sum_len = 0
for d in data: # 每筆資料當作d
	sum_len += len(d)
	# sum_len = sum_len + len(d)
print('留言的平均長度是', sum_len / len(data))
