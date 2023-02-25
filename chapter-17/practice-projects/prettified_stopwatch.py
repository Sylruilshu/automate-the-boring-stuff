import time, pyperclip


# Display the program's instructions.
print(
    'Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch.Press Ctrl-C to quit.'
)
input()  # press Enter to begin
print("Started.")
start_time = time.time()  # get the first lap's start time
last_time = start_time
lap_num = 1

stopwatch_output = []

# Start tracking the lap times.
try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)

        padded_total_time = str(total_time).rjust(6)
        padded_lap_time = str(lap_time).rjust(6)

        print(f"Lap # {lap_num}: {padded_total_time} ({padded_lap_time})", end="")
        output = f"Lap # {lap_num}: {padded_total_time} ({padded_lap_time})"
        stopwatch_output.append(output)

        lap_num += 1
        last_time = time.time()  # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    pyperclip.copy("\n".join(stopwatch_output))
    print("\nDone.")
