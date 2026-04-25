test_str= str(input("Enter a string: "))
print("Original String: " + test_str)
print("\nReversed String: " + test_str[::-1])
print("\nGapped String: " + test_str[::2])

print("\nWord Letter Reversal: ")
for i  in range(len(test_str.split())):
    print(test_str.split()[i][::-1], end=" ")

print("\nWord Order Reversal: ")
cursor_end = len(test_str)-1
for cursor_start in range(len(test_str)-1,-1,-1):
    #cursor_start will store WORD index
    #cursor_end will store SPACE index
    

    if(test_str[cursor_start]==" " or cursor_start==0): 
        print(test_str[cursor_start:cursor_end+1],end=" ")
        cursor_end=cursor_start
        
