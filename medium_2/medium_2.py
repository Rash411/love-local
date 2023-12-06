def maj_elements(nums):
    if not nums:
        return []

    cand1, cand2, count1, count2 = None, None, 0, 0

    for num in nums:
        if num == cand1:
            count1 += 1
        elif num == cand2:
            count2 += 1
        elif count1 == 0:
            cand1, count1 = num, 1
        elif count2 == 0:
            cand2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    count1 = count2 = 0
    for num in nums:
        if num == cand1:
            count1 += 1
        elif num == cand2:
            count2 += 1

    result = []
    if count1 > len(nums) // 3:
        result.append(cand1)
    if count2 > len(nums) // 3:
        result.append(cand2)

    return result

a = input("Enter the integer array separated by spaces: ")
nums = list(map(int, a.split()))

result = maj_elements(nums)
print(f"Elements that appeared more than n/3 times: ",result)
