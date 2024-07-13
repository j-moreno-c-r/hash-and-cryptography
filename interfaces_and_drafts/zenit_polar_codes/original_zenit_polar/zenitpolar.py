def encrypt(text):
    zenit_to_polar = {'z': 'p', 'e': 'o', 'n': 'l', 'i': 'a', 't': 'r'}
    polar_to_zenit = {'p': 'z', 'o': 'e', 'l': 'n', 'a': 'i', 'r': 't'}
    answer = ""
    for c in text:
        if c in zenit_to_polar:
            answer += zenit_to_polar[c]
        elif c in polar_to_zenit:
            answer += polar_to_zenit[c]
        else:
            answer += c
    print(answer)
    return answer

