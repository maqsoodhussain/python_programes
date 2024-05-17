
def main():
    l = [1,2,3,4,5]
    avg = average(l)
    print(f"Average : {avg}")



def average(li):
    sum = 0
    for i in li:
        sum += i
    return sum/len(li)


if __name__ == "__main__":
    main()