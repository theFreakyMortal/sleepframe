import os

def find_modules(directory):
    modules = {}
    i = 1
    for filename in os.listdir(directory):
        if filename.endswith(".py") and filename != "main.py":
            module_name = filename[:-3]
            modules[str(i)] = module_name
            i += 1
    return modules

def main():
    modules = find_modules(os.path.dirname(__file__))
    
    while True:
        print("Select a module to run:")
        for key, module in modules.items():
            print(f"{key}. {module}")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice in modules:
            os.system(f'python -m {modules[choice]}')
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()