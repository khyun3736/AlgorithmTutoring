# 1개단위부터 짜르기 시작하여 총 길이의 절반만큼의 길이단위까지 짤라보고 제일 작은값을 리턴해준다

s = input()

length = len(s)

for cut in range (1, len(s)//2):
    count = 1
    frame = s[0:cut]
    for i in range(cut, len(s), cut):

        if frame == s[j:j+cut]:
            count += 1