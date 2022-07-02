if __name__ == "__main__":
    sa = list(input())
    sb = list(input())
    sc = list(input())

    dic = {
        "a": sa,
        "b": sb,
        "c": sc,
    }
    pop = dic["a"].pop(0)
    while dic[pop]:
        pop = dic[pop].pop(0)

    print(pop.upper())
