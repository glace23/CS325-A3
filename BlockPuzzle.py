

def blockpuzzle_dp(N):
    return helper_blockpuzzle_dp(N)


def helper_blockpuzzle_dp(n, i=0, string = "", list=None):
    # top down approach
    if list is None:
        list = []
    if i == n:
        # remove final + sign from string
        list.append(string[:len(string)-1])
    elif i < n:
        helper_blockpuzzle_dp(n, i+1, "1+"+string, list)
        helper_blockpuzzle_dp(n, i+2, "2+"+string, list)
    return list


if __name__ == '__main__':
    print(blockpuzzle_dp(2))
    print(blockpuzzle_dp(3))


