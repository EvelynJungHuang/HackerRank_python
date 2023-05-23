def mutate_string(string, position, character):
    l = list(string)
    l[int(position)] = character
    string_v2=''.join(l)
    return string_v2

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)