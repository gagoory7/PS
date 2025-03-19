def solution(s):
    alph = ['zero','one','two','three','four','five','six','seven','eight','nine']
    alpha_dict = { alph[i]:i for i in range(len(alph))}
    answer = ''
    s__ = ''
    for i in range(len(s)) :
        s_ = s[i]
        if s_.isdigit() :
            answer += s_
        else :
            s__ += s_

        if s__ in alpha_dict.keys() :
            
            answer += str(alpha_dict[s__])
            s__ = ''
    return int(answer)



# num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

# def solution(s):
#     answer = s
#     for key, value in num_dic.items():
#         answer = answer.replace(key, value)
#     return int(answer)