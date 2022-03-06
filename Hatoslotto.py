def my_function():
    nums=[]
    for num in range(1,45):
        if 996300%num==0:
            nums.append(num)


    for n1 in nums:
        for n2 in nums:
            for n3 in nums:
                for n4 in nums:
                    for n5 in nums:
                        for n6 in nums:
                            if n1<n2<n3<n4<n5<n6:
                                if n1+n2+n3+n4+n5+n6==90:
                                    if n1*n2*n3*n4*n5*n6==996300:
                                        print(n1, n2, n3, n4, n5, n6)

def main():
    my_function()


if __name__ == "__main__":
    import time
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))