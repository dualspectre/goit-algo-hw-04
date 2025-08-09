#task 1
import shutil
#function of solving total and average salary from file
def total_salary(path:str)->tuple:
    '''
    function of calculating total and average salary
    from input text file

    Input:
    path:str - relative or full file name with text data

    Return: tuple
    (total:float, average:float) - total and average
    '''
    total, average = (0.0, 0.0)
    counter = 0
    try:
        with open(path, 'r', encoding='utf-8') as data_file:
            for elem in data_file.readlines():
                counter+=1
                _, salary = elem.split(',')
                total += float(salary)
        average = total / counter
    except FileNotFoundError:
        print(f'File {path} not found.\
        \nPlease enter correct file name.')
        return (None, None)
    except PermissionError:
        print(f'Can`t read file {path}')
        return (None, None)
    except Exception:
        print(f'Incorrect input data in {path}')
        return (None, None)
    
    return (total, average)

# test_file = 'salary.txt'
# # test_file = './'
# total, average = total_salary(test_file)
# print(total, average)

#task2 - cats info func

#function of getting cats info from file
def get_cats_info(path:str)->list[dict]:
    """
    Function to get cats information from a file.
    Input:
    path:str - relative or full file name with text data

    Return: list[dict] - list of dictionaries with cat information
    """
    result = []    
    try:
        with open(path) as data_file:
            for elem in data_file.readlines():
                id, name, age = elem.split(',')
                result.append({'id':id.strip(), 'name':name.strip(), 'age':age.strip()})
    except FileNotFoundError:
        print(f'File {path} not found')
    except PermissionError:
        print(f"Access denied to {path}")
    except Exception as e:
        print(f'Error reading file {path}: {e}')
    return result

test_path = 'cats.txt'
print(get_cats_info(test_path))