#Native Recursion:
def gallery(ls, k):
    def gallery_h(ls, k, s, left):

        if ls == []:
            if k == 0:
                return s
            return -100

        if k == 0:
            return gallery_h(ls[1:], k, s+ls[0][0]+ls[0][1], not left)

        return max(gallery_h(ls[1:], k-1, s+ls[0][0 if left else 1], left),
            gallery_h(ls[1:], k, s+ls[0][0]+ls[0][1], not left))


    return max(gallery_h(ls, k, 0, True), gallery_h(ls, k, 0, False))

#Dynamic:
#Memoization
def gallery_dp(ls, k):
    table = [[[-1, -1, -1] for __ in ls] for _ in range(k+1)]
    
    def gallery_dp_h(ls, index, k, r):

        if index == len(ls):
            if k == 0:
                return 0
            return -100

        if k == 0:
            if table[k][index][r] < 0:  
                table[k][index][r] = gallery_dp_h(ls, index+1, k, 2)+ls[index][0]+ls[index][1]
            return table[k][index][r]
    
        if table[k][index][r] < 0:
            if r != 2:
                table[k][index][r] = gallery_dp_h(ls, index+1, k-1, r)+ls[index][r]
            else:
                for r in range(2):
                    table[k][index][r] = gallery_dp_h(ls, index+1, k-1, r)+ls[index][r]

            table[k][index][2] = gallery_dp_h(ls, index+1, k, 2)+ls[index][0]+ls[index][1]

        return max(table[k][index])
    
    return gallery_dp_h(ls, 0, k, 2)


def get_input():

    line_1 = input()
    n, k = int(line_1.split()[0]), int(line_1.split()[1])
    rooms = []
    while True:
        line_2 = input().split()
        line_2 = [ int(i) for i in line_2]

        if line_2[0] == 0  and line_2[1] == 0:
            break

        rooms.append(line_2)

    return rooms[:n], k

rooms, k = get_input()

print(gallery_dp(rooms, k))
