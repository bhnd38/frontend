# 최대 6글자 최소 2글자o
# 숫자는 끝부분에만 와야한다. 첫번째숫자는 0이 올 수 없다.
# 공백,특수문자 불가.

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if 2>len(s) or len(s)>6:
        return False

    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    i=0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] =='0':
                return False
            else:
                break
        i+=1

    if punc_check(s):
        return True

#-----------------------------------
# def len_check(s):
#     if 2>len(s) or len(s)>6:
#         return False


# def num_check(s):
#     i=0
#     while i < len(s):
#         if s[i].isdigit():
#             return False

# def zero_check(s):
#     for i in s:
#         if s[i].isdigit() and s[i]=="0":
#             return False
#         else:
#             return True

def punc_check(s):
    if s.isalnum():
        return True
    else:
        return False





main()
