def caesarCipher(s, k):
    # Write your code here
    # Get actual rotation
    k %= 26
    # Store alphabets
    alpha_lower = [chr(i) for i in range(97,123)]
    alpha_upper = [chr(i) for i in range(65,91)]
    # Alphabet rotation
    r_alpha  = alpha_lower[k:] + alpha_lower[:k] + alpha_upper[k:] + alpha_upper[:k]
    # Combination of the upper and lower cases
    alpha = alpha_lower + alpha_upper
    # Createing an hash map for the alphabets and the corresponding rotation
    cipher = dict(zip(alpha,r_alpha))
    temp = []
    # Perform encryption of the data
    for i in s:
        if i in cipher:
            i = cipher[i]
        temp.append(i)
               
    return "".join(temp)