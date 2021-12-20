import time

def main():
    print("""
     ██████╗   █████╗   ██╗     ██╗   ██╗
    ██╔════╝  ██╔══██╗  ██║     ██║   ██║
    ╚█████╗   ██║  ██║  ██║     ╚██╗ ██╔╝
     ╚═══██╗  ██║  ██║  ██║      ╚████╔╝
    ██████╔╝  ╚█████╔╝  ███████╗  ╚██╔╝
  _ ╚═════╝    ╚════╝   ╚══════╝   ╚═╝    
 |_                                                              
   | """)
    time.sleep(2)
    value1 = int(input("  [$]>>#~:Enter First Integer: "))
    value2 = int(input("  [$]>>#~:Enter Second Integer: "))
    value3 = 0
    print("   |")
    op = str(input("   [$]>>#~:SpecifyOperator Add-[A] Subtract-[S] Multiply-[M] Divide-[D]: "))
    if op == 'A':
        value3 = value1 + value2
        print("   >>: ADDITION :<<")
        print("   The Sum of Your Inputs Are: " + str(value3))
        time.sleep(2)
    if op == 'S':
        value3 = value1 - value2
        print("   >>: SUBTRACTION :<<")
        print("   The Difference of Your Inputs Are: " + str(value3))
        time.sleep(2)
    if op == 'M':
        value3 = value1 * value2
        print("   >>: MULTIPLICATION :<<")
        print("   The Product of Your Inputs Are: " + str(value3))
        time.sleep(2)
    if op == 'D':
        value3 = value1 / value2
        float = (value3)
        value4 = value1 % value2
        float = (value4)
        print("   >>: DIVISION :<<")
        print("   The Quotient of Your Inputs Are: " + str(value3))
        time.sleep(2)
        print("   The Remainder of Two Inputs Are " + str(value4))
        time.sleep(2)

    repeat = input("   >>: Would you like to Calculate Another Integer Value [y]/[n]: ").lower()
    if repeat == "y":
        main()
    else:
        print("   >>: Thank you User")
        exit()
main()