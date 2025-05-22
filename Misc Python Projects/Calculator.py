
print("========================")
print("= Samuel's  Calculator =")
print("========================")

while 1:

    calc_cmd = input("Enter the operation (+|-|*|/):")
    
    first_num = int(input("Enter the first number:"))
    second_num = int(input("Enter the second number:"))

    calc_result = 0

    if calc_cmd == "+":
        calc_result = first_num + second_num
    elif calc_cmd == "-":
        calc_result = first_num - second_num
    elif calc_cmd == "*":
        calc_result = first_num * second_num
    elif calc_cmd == "/":
        calc_result = first_num / second_num
    else:
        print("Unknown operation\n\n")
        continue
        
    print("\n", first_num, calc_cmd, second_num, "=", calc_result, "\n\n")
