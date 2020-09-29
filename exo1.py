for i in range(999):
        a = f'{i:03}'
        if a[0] < a[1] and a[1] < a[2] and a[0] != a[1] and a[1] != a[2] and a[2] != a[0]:
            print(f'{i:03}')
    
        