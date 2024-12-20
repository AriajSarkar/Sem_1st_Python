from colorama import Fore, Style, init

# Initialize colorama for Windows support
init(autoreset=True)

def main():
    
    full_marks = int(input(Fore.CYAN + "Enter Full Marks of 3 Subjects: " + Fore.GREEN))
    physics = float(input(Fore.CYAN + "Enter Physics marks: " + Fore.GREEN))
    chemistry = float(input(Fore.CYAN + "Enter Chemistry marks: " + Fore.GREEN))
    maths = float(input(Fore.CYAN + "Enter Maths marks: " + Fore.GREEN))
    
    total = physics + chemistry + maths
    percentage = (total / full_marks) * 100
    
    print("\n" + Style.BRIGHT + Fore.BLUE + "Total Marks: ", total, "out of", full_marks)
    print(Style.BRIGHT + Fore.MAGENTA + "Percentage: ", percentage)
    
    if percentage >= 80:
        print(Style.BRIGHT + Fore.GREEN + "Grade: A")
    elif 70 <= percentage < 80:
        print(Style.BRIGHT + Fore.CYAN + "Grade: B")
    elif 60 <= percentage < 70:
        print(Style.BRIGHT + Fore.YELLOW + "Grade: C")
    elif 40 <= percentage < 60:
        print(Style.BRIGHT + Fore.RED + "Grade: D")
    elif percentage < 40:
        print(Style.BRIGHT + Fore.RED + "Grade: F")
    else:
        print(Fore.RED + "Invalid Input")
    
if __name__ == "__main__":
    main()