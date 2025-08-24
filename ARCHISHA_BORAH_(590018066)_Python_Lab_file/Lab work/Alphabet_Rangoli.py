'''def print_rangoli(size):
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n) '''

''' def print_rangoli(N):
    alphabets='abcdefghijklmnopqrstuvwxyz'
    if N>26 :
        return
    else:
        final_result=' '
        for i in range(N):
            for j in range(N-i-1, N):
                final_result=final_result+'-'+final_result '''

''' def print_rangoli(N):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    if N > 26:
        return
    else:
        final_result = []
        for i in range(N):
            characters = alphabets[N-1:N-i-1:-1]  #for decrement (-1)    
            line='-'.join(characters) 
            final_result+=line+'\n'
            #final_result.append(line.center(4*N-3, '-'))
            final_result+=final_result[-2::-1]
            return final_result
size = int(input("Enter the size of the rangoli (1-26): "))
print(print_rangoli(size)) '''

''' def print_rangoli(N):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    if N > 26:
        return
    else: 
        final_result = []
        for i in range(N):
            left = alphabets[N-1:N-i-1:-1]  
            right = alphabets[N-i-1:N]      
            row = '-'.join(left+ right)  
            final_result.append(row.center(4 * N - 3, '-')) 
        print('\n'.join(final_result + final_result[-2::-1]))
        return final_result
size = int(input("Enter the size of the rangoli (1-26): "))
print_rangoli(size) '''

''' def print_rangoli(N): 
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    final_result = []
    
    # Generate the top half of the rangoli (including the center line)
    for i in range(N):
        characters = alphabets[N-1:N-i-1:-1] + alphabets[N-i-1:N]
        line = '-'.join(characters)
        final_result.append(line.center(4 * N - 3, '-'))
    
    # Add the bottom half by reversing the top half except the last line (center line)
    final_result += final_result[:-1][::-1]
    
    # Join all lines and print
    print('\n'.join(final_result))


# Input for Rangoli size
N = int(input("Enter the size of the Rangoli (1-26): "))
if N>26:
    print_rangoli(N)
else:
    print("Please enter a valid size (1-26).") '''

''' def print_rangoli(N):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    final_results = []

    for i in range(N):
        characters = alphabets[N-1:N-i-1:-1] + alphabets[N-i-1:N]
        line = '-'.join(characters)
        line = '-' * ((4*N-3 - len(line)) // 2) + line + '-' * ((4*N-3 - len(line)) // 2)
        final_results.append(line)

    result = '\n'.join(final_results + final_results[-2::-1])
    print(result)
    return result

N = int(input("Please enter a valid size (1-26):"))
print_rangoli(N)  '''

def print_rangoli(N):
    alphabets='abcdefghijklmnopqrstuvwxyz'
    rangoli=[]
    for i in range(N):
        characters=alphabets[N-1:N-i-1:-1]
        pattern='-'.join(characters)
        filler='-' * ( (4*N-3)-len(pattern))//2
        line=filler+pattern+filler
        rangoli.append(line)
        result='\n'.join(rangoli) 
        print(result)
        return result
       



