def main(arr):
    schet = 0
    result = 0
    stroka = ''
    for i1 in range(0,len(arr)):
        if arr[i1] not in stroka:
            stroka+=arr[i1]
            schet+=1
            continue
        if schet > result:
            result = schet
        stroka = ''
        schet = 0
    return result
    



if __name__ == '__main__':
    with open('input.txt', 'r') as file_in:
        arr = str(file_in.readline().rstrip('\n').split(' '))
        #n = int(file_in.readline())
    result = main(arr)

    with open('output.txt', 'w') as file_out:
        file_out.write(str(result))
