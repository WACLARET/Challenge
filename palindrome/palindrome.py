# Question 5.
# Context:A palindrome is a word or phrase that is spelt the same way forward and backwords.
# Task: Create a simple program that identifies a palindrome.It should take a word or a phrase from user via input and determines wether palindrome or not and gives the results. Recors 5 entries by user.
def palindrome():
    palindromes = []
    inputs = []
    count = 0
    
    while count < 5:
        string = input("please input a word ")
        reversed_string = string[::-1]
        print("The reversed stirng is:  ", reversed_string)
        if string == reversed_string:
            print("This is a palindrome\n")
            palindromes.append(string)
        else:
            print("This is not a palindrome\n")

        inputs.append(string)
        count+=1

    print (f"user inputs {inputs}")
    return (palindromes)
