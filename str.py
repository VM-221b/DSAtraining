# s="suhani is a good girl"
# print(s[::-1]) #reverse
# print(s.find("is", 0, 10)) #default from left to right
# print(s.rfind("r"))

# f="ababbbcabab"
# print(f.count('a',3,10))

# st="It is difficult to learn java"
# s1=st.replace("difficult","easy")
# print(s1)

# s="22-04-2034"
# ls=s.split("-")
# print(ls)
# print(len(ls))

# l=['Nagpur','Pune','Mumbai']
# s='_'.join(l)
# print(s)

# s='Veda is a student'
# print(s.startswith('Veda')) TRUE
# print(s.endswith('girl')) FALSE

# s='Learning Python from Ashish sir is very easy'
# ls=s.split()
# ans=""
# for i in ls:
#     ans=ans+i[::-1]+" "
# print(ans)

# s='ABCDABBCDABBBCCCDDEEEF'
# result="".join(dict.fromkeys(s))
# print(result)

# num = input("Enter your mobile number: ")
# if num.isdigit() and len(num) == 10 and num[0] in ['6', '7', '8', '9']:
#     print("Valid number")
# else:
#     print("Invalid number")