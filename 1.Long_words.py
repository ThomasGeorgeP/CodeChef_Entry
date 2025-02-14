def format_long_word(word : str):
    if len(word)<=10:
        return word
    else:
        return word[0]+str(len(word)-2)+word[-1]


if __name__=="__main__":
    num=int(input())
    words=[]
    for i in range(num):
        words.append(input())
   
    for i in words:
        print(format_long_word(i))