#python program for checking string Pallindrome
s1="Madam"
s1=s1.lower()
s2=reversed(s1)

if list(s2)==list(s1):
    print("Palindrome")
else:
    print("Not Pallindrome")
