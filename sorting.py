def sort(arr):
    #print(arr)
    new_list = sorted(arr)
    if(arr == new_list):
        print("yes")
    if len(arr) == 2:
        print("yes")
        print("swap 1 2")
    else:
        count_greater = 0
        count_lower = 0
        greater_flag = False
        lower_flag = False
        start_idx = 0
        end_idx = 0
        for i in range(1, len(arr) - 1):
            # print(i, arr[i])
            if (arr[i] < arr[i + 1] and not lower_flag):
                # print(arr[i], arr[i+1], "lower")
                count_lower += 1
                start_idx = i
                lower_flag = True
                greater_flag = False
            elif (arr[i] > arr[i + 1] and not greater_flag):
                # print(arr[i], arr[i+1], "greater")
                count_greater += 1
                if (end_idx == 0):
                    end_idx = i
                greater_flag = True
                lower_flag = False
        count_lower -= 1
        print(count_lower, count_greater)
        if (count_lower == count_greater and count_lower<=2):
            if (count_greater == 2):
                arr[start_idx], arr[end_idx] = arr[end_idx], arr[start_idx]
                #print(arr[end_idx: start_idx + 1])
                new_list = sorted(arr[end_idx:start_idx+1])
                if(arr[end_idx:start_idx+1] == new_list):
                    print("yes")
                    print("swap", end_idx + 1, start_idx + 1)
                else:
                    print("no")
            elif (count_greater == 1):
                print("yes")
                print("reverse", end_idx + 1, start_idx + 1)
        else:
            print(count_lower, count_greater)
            print("no")


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    sort(arr)
