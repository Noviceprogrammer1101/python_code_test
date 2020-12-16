# 统计一个文件中单词出现的次数，并输出出现次数最多的前3个单词
def countword(file):
    fb = open(file, 'r')
    word1 = {}
    for line in fb:
        sword = line.strip().split()
        for word in sword:
            if word in word1:
                word1[word] += 1
            else:
                word1[word] = 1
    word2 = []
    for wd, fy in word1.items():
        word2.append((fy, wd))
    word2.sort(reverse=True)
    for wd in word2[:3]:
        print(wd)
    fb.close()


file = input()
countword(file)