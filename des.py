
s0 = [[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
s1 = [[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]

def permute(bits, permutation):
    perm = [(p - len(bits))*-1 for p in permutation]
    reorder = [bits[x] for x in perm]
    return ''.join(reorder)

def substitute(b, s):
    return format(s[int(b[0])*2 + int(b[3])][int(b[1])*2 + int(b[2])], '02b')

def round(left, right, key):
    new_left = right

    # Now go to F funciton
    exp = permute(right, [4,1,2,3,2,3,4,1])
    wkey = format(int(exp, 2) ^ int(key, 2), '08b')
    l = wkey[0:4]
    r = wkey[4:8]
    l = substitute(l, s0)
    r = substitute(r, s1)
    c = l + r
    cp = permute(c, [2,4,3,1])
    new_right = format(int(cp, 2) ^ int(left, 2), '04b')
    return(new_left, new_right)

def round_runner(i_text, keys):
    """
    Args:
        i_text: the initial text
        keys : array of keys to be used
    return
    """
    i_perm = permute(i_text, [2,6,3,1,4,8,5,7])
    rd_end = (i_perm[0:4], i_perm[4:8])
    for i in range(2):
        rd_end = round(rd_end[0], rd_end[1], keys[i])
    end_i_perm = permute(rd_end[0] + rd_end[1], [4,1,3,5,7,2,8,6])
    return end_i_perm

def create_keys(key):
    key = permute(key, [3,5,2,7,4,10,1,9,8,6])
    key_left = key[0:5]
    key_right = key[5:10]
    keys = []
    for i in range(2):
        key_left = key_left[1:5] + '0'
        key_right = key_right[1:5] + '0'
        key_c = key_left + key_right
        keys.append(permute(key_c, [6,3,7,4,8,5,10,9]))
    return keys

def str_to_bits(s):
    singles = [format(int(x, 16), '04b') for x in s]
    doubles = [singles[i] + singles[i+1] for i in range(len(singles)//2)]
    if len(singles) % 2 == 1:
        doubles.append(singles[-1] + '0000')
    return doubles

def bits_to_str(b):
    print(b)
    return ''.join(format(int(o[0:4], 2), 'x') + format(int(o[4:8], 2), 'x') for o in b)
