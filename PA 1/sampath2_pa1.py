class CountInversion:
    def __init__(self):
        self.inversions = 0

    def accept_input(self):
        lines = []
        n = input()
        arr_index = 0
        while arr_index < int(n):
            user_in = input()

            # break out of read loop
            if user_in == '':
                break
            else:
                lines.append(int(user_in))
            arr_index += 1

        return lines

    def count_inversions(self, arr, temp_arr,  length):

        self.merge_sort(arr, temp_arr, 0, length-1)
        return self.inversions

    def merge_sort(self, arr, temp_arr, left, right):

        if left < right:

            mid = (left + right)//2
            # Process left half
            self.merge_sort(arr, temp_arr, left, mid)
            # Process right half
            self.merge_sort(arr, temp_arr, mid + 1, right)
            # Merge
            self.merge(arr, temp_arr, left, mid, right)

    def merge(self, arr, temp_arr, left, mid, right):
        left_pointer = left
        right_pointer = mid + 1
        temp_iterator = left

        while left_pointer <= mid and right_pointer <= right:
            # Retain the order of the elements if left element is less than
            # right element
            if arr[left_pointer] <= arr[right_pointer]:
                temp_arr[temp_iterator] = arr[left_pointer]
                temp_iterator += 1
                left_pointer += 1

            # If right element is less than left element, then there are
            # inversions and the right element is used for constructing
            # the sorted array
            else:
                temp_arr[temp_iterator] = arr[right_pointer]
                self.inversions += (mid-left_pointer + 1)
                temp_iterator += 1
                right_pointer += 1

        while left_pointer <= mid:
            temp_arr[temp_iterator] = arr[left_pointer]
            temp_iterator += 1
            left_pointer += 1

        while right_pointer <= right:
            temp_arr[temp_iterator] = arr[right_pointer]
            temp_iterator += 1
            right_pointer += 1

        for i in range(left, right + 1):
            arr[i] = temp_arr[i]


# Driver Code
obj = CountInversion()
input_arr = obj.accept_input()
n = len(input_arr)
temp_arr = [0]*n
result = obj.count_inversions(input_arr, temp_arr, length=n)
print(result)
