def can_win(s, t):
    for s_letter, t_letter in zip(s, t):
        if (
            s_letter == t_letter
            or (s_letter == "@" and t_letter in atcoder)
            or (t_letter == "@" and s_letter in atcoder)
        ):
            continue
        else:
            return "You will lose"
    return "You can win"


s = list(input())
t = list(input())

atcoder = list("atcoder")


print(can_win(s, t))
