#as exercise implement exception handling and also write perfect number into perfect.txt file 
try:
    import Prime_numbers_58 as p
except ImportError:
    print("Error: Could not import 'Prime_numbers_58'. Check file name.")
    exit()

try:
    import prfect_number_60 as perf
except ImportError:
    print("Error: Could not import 'prfect_number_60'. Check file name.")
    exit()

try:
    read_file = "number2.txt"
    prime_file = "prime.txt"
    perfect_file = "perfect.txt"
    input_file = open(read_file, 'r')         
    prime_output = open(prime_file, 'w')    
    perfect_output = open(perfect_file, 'w')  
    for line in input_file:
        line = line.strip()
        try:
            num = int(line)
            if p.isPrime(num):
                prime_output.write(str(num) + "\n")
            if perf.isPerfect(num):
                perfect_output.write(str(num) + "\n")
        except ValueError:
            print(f"Invalid number: '{line}'")
    input_file.close()
    prime_output.close()
    perfect_output.close()
except FileNotFoundError:
    print("File does not exist. Make sure 'number2.txt' is in the same folder.")
except PermissionError:
    print("Permission error. You might not have access to the file.")
except UnicodeDecodeError:
    print("This is not a text file. Might be binary.")
except Exception as e:
    print("An unexpected error occurred:", e)
finally:
    print("Task Complete.")