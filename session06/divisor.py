def gcd(a, b):
    if b > a:
        small = a
        large = b
    else:
        small = b
        large = a
    for i in range(1, small, 1):
        result = large%(i*small)
        if result < small:
            result = large%(i*small)
        else:
            x = large%(i*small)
            return i
                    
                
        

print(gcd(1071, 462))

