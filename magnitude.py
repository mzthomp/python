def feet_to_steps(user_feet):
    steps = float(user_feet) // 2.5
    return int(steps)


if __name__ == '__main__':
    user_feet = float(input())

    your_value = feet_to_steps(user_feet)
    print(your_value)


