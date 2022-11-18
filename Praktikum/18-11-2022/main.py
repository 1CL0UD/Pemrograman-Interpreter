# file = open('data.txt', 'r', encoding='utf-8')
# print(file.read())
# file.close()

with open('data.txt', 'r', encoding='utf-8') as file:
    # file.writelines('helo\n')
    #print(file.readline())
    x = file.readlines()
    #print(x[0])
    x = map(lambda i : i.replace('\n', 'ssss'), x)
    # for i in range(len(x)):
    #     x[i] = x[i].replace('\n','x')
    for kata in x:
        print(kata)
    

