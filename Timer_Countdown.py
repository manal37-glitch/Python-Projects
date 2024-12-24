import time

def countdown():
    # Take input for seconds and ensure it's an integer
    try:
        seconds = int(input("Enter your time in seconds: "))
    except ValueError:
        print("Please enter a valid integer.")
        return  # Exit the function if input is invalid

    while seconds:
        # Divmod takes the number of seconds and divides it by 60, returning minutes and seconds
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02}:{secs:02}"  # Format the timer as MM:SS
        print(timer, end='\r')  # Overwrite the same line instead of printing on a new line
        time.sleep(1)  # Pause for 1 second
        seconds -= 1

    print("Time's Up!")

countdown()
