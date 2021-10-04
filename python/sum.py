def sum(l, N):
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i] + l[j] == N and (i != j):
                return True
                
    return False

def test():
    assert sum([-1, 1], 0)
    assert not sum([0,2,3], 4)
    assert sum([0,2,2], 4)
    print("Success!")

if __name__ == "__main__":
    test()
