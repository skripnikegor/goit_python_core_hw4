
def total_salary(path: str) -> str:
    """
    Return string with sum of salaries and average salary from inpur file in format Name, Salary.

    Args:
        path - path to the file.

    Returns:
        string with salary data.

    Raises:
        if path/data wrong returns (0, 0).
    """
    if not path:
        return (0, 0)

    try:
        # Open file and read data from it
        with open(path, mode="r", encoding="utf-8") as data:
            # Read all lines from file
            lines = data.readlines()
            # Create array of salaries from data
            try:
                salaries = [float(line.split(",")[-1]) for line in lines]
            except:
                print("Wrong data in the file.")
                return ""
            
            salaries_sum = float(f"{sum(salaries):.0f}")
            try:
                average_salary = float(f"{sum(salaries) / len(salaries):.0f}")
            except ZeroDivisionError:
                print("Can not divide by zero")
                return (0, 0)
            return (salaries_sum, average_salary)
    except FileNotFoundError:
        print("File does not exist in the script directory")
        return (0, 0)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return (0, 0)


# Tests
test1 = total_salary("task_1_1.txt")
print(test1)
test2 = total_salary("task_1_2.txt")
print(test2)