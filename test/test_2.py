def find_two_indexes(data, expected_sum):
    # Ваше решение?
    for i1 in range(0,len(data)):
        for i2 in range(0, len(data)):
            if i2==i1:
                i2+=1
                continue
            if data[i2]+data[i1]==expected_sum:
                return (i1, i2)


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 11]
    expected_sum = 10
    print(find_two_indexes(data, expected_sum))