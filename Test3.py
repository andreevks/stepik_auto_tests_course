str = 'aaaaaaa bbbbbbbfbbbbbbbb cc sddiwjefojfjlk  wssdiojwqdlkj wwwwww kjkjlkjlasdsd   s nnnnnnnnnnnn'

counter = 1
max_len = 1
for i in range(1, len(str)):
    if str[i] == str[i-1]:
        counter += 1
        if counter > max_len:
            max_len = counter
    else:
        counter = 1 # str[i] != str[i-1]


print(max_len)