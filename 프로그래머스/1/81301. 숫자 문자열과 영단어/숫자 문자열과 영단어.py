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