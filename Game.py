
def game_topdown(N):
    return helper_game_topdown(N)


def helper_game_topdown(n, turn="a", string = "", list=None):
    if list is None:
        list =[]
    if n <= 1:
        if turn == "b":
            list.append(string+f"a win")
        else:
            list.append(string+f"a lost")
    for i in range(1, n):
        if n % i == 0:
            if turn == "a":
                helper_game_topdown(n-i, "b", string+f"a{i}+", list)
            else:
                helper_game_topdown(n-i, "a", string+f"b{i}+", list)
    return list

# def game_bottomup(N):
#
#
# def helper_game_bottomup(n, turn="a"):


if __name__ == '__main__':
    print(game_topdown(3))
    print(game_topdown(8))

