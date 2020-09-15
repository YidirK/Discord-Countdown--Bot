import time


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Time is up!')


def test():
    t = int(input("Enter the time in seconds: "))  # todo: error handling
    countdown(int(t))


if __name__ == "__main__":
    test()
