def main(arr):

    return None

if __name__ == '__main__':
    with open('input.txt', 'r') as file_in:
        arr = tuple(file_in.readline().split())
        #n = int(file_in.readline())
    result = main(arr)

    with open('output.txt', 'w') as file_out:
        file_out.write(str(result))
