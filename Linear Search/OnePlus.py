digits = [9]
def plusOne(digits):
        list_len = len(digits)
        last_index = list_len -1
        if digits[list_len-1] != 9:
            digits[list_len-1]+=1
            return digits
        while digits[last_index] == 9:
            digits[last_index] = 0
            print(digits)
            last_index-=1
        if last_index < 0:
            print(last_index)
            digits.insert(0,1)
            return digits
        digits[last_index]+=1
        return digits
a = plusOne(digits)
print(a)