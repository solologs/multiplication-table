def format_1():
    print("=== 完整格式 ===")
    for i in range(1, 10):
        for j in range(1, 10):
            print(f"{i}x{j}={i*j:2d}", end=" ")
        print()

def format_2():
    print("=== 三角形格式 ===")
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f"{j}x{i}={i*j:2d}", end=" ")
        print()

def main():
    print("九九乘法表")
    print("1 - 完整格式")
    print("2 - 三角形格式")
    
    choice = input("选一个: ")
    
    if choice == "1":
        format_1()
    elif choice == "2":
        format_2()
    else:
        print("只能选1或2")

if __name__ == "__main__":
    main()
