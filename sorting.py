def sort(arr):
    new_list = sorted(arr)
    if arr == new_list:
        print("yes")
    if len(arr) == 2:
        print("yes")
        print("swap 1 2")
    else:
        count_high = 0
        count_low = 0
        high_flag = False
        low_flag = False
        start_idx = 0
        end_idx = 0
        for i in range(1, len(arr) - 1):
            # count the number of times the value of next element goes up
            if arr[i] < arr[i + 1] and not high_flag:
                count_high += 1
                end_idx = i
                high_flag = True
                low_flag = False
            # count the number of times the value of next element goes down
            elif arr[i] > arr[i + 1] and not low_flag:
                count_low += 1
                if start_idx == 0:
                    start_idx = i
                low_flag = True
                high_flag = False
        # if more than one 'highs' are counted, decrement to remove the extra 'high' counted
        if count_high > 1:
            count_high -= 1
        if count_low == count_high and 2 >= count_high > 0:
            if count_high == 2:
                # if swap sorts the array then print yes
                if swap_works(arr, new_list, start_idx, end_idx):
                    print("yes")
                    print("swap", start_idx + 1, end_idx + 1)
                else:
                    print("no")
            elif count_high == 1:
                print(start_idx, end_idx)
                if abs(start_idx - end_idx) == 1:
                    # if swap and reverse both work (i.e. sort the array), prefer swapping
                    if swap_works(arr, new_list, start_idx, end_idx):
                        print("yes")
                        print("swap", start_idx + 1, end_idx + 1)
                    else:
                        print("no")
                else:
                    print("yes")
                    print("reverse", start_idx + 1, end_idx + 1)
        else:
            print("no")


def swap_works(arr, new_list, start_idx, end_idx):
    arr[start_idx], arr[end_idx] = arr[end_idx], arr[start_idx]
    if arr == new_list:
        return True
    else:
        return False


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    sort(arr)
