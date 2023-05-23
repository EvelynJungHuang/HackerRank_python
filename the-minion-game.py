def minion_game(string):
    score_vowel=0
    score_consonant=0
    for i in range(len(string)):
        name = string[i]
        if name in ('A', 'E', 'I', 'O', 'U'):
            score_vowel += len(string)-i
        else:
             score_consonant += len(string)-i
            # your code goes here
    if score_consonant > score_vowel:
        print("Stuart " + str(score_consonant))
    elif score_consonant < score_vowel:
        print("Kevin " + str(score_vowel))
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)