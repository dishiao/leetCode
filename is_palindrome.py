def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp = temp // 10
    if total == num:
        return True
    else:
        return False
