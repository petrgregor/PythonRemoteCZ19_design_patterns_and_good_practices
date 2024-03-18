# Single responsibility

# BAD solution
def math_operations(list_):
    print(f"Mean is {sum(list_) / len(list_)}")
    print(f"Max value is {max(list_)}")


math_operations(list_=[1, 2, 3, 4, 5])


# GOOD solution (with Single responsibility principle
def get_mean(list_):
    return sum(list_) / len(list_)


def get_max(list_):
    return max(list_)


def print_mean_and_max(list_):
    print(f"Mean is {get_mean(list_)}")
    print(f"Max is {get_max(list_)}")


def main():
    my_list = [1, 2, 3, 4, 5, 6]
    print_mean_and_max(my_list)


if __name__ == "__main__":
    main()
