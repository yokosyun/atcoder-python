def get_indexer(an):
    return dict((a, idx) for idx, a in enumerate(an))


n = int(input())
an = list(map(int, input().split()))
indexer = get_indexer(an)
an = sorted(an)[::-1]

for a in an:
    print(indexer[a] + 1)
