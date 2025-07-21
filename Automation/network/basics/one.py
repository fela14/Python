from datetime import datetime

log_file = "one.log"

def read_log(log):
    # Open the log file and print contents to the terminal
    with open(log, 'r') as f:
        print(f.read())

def write_log(log, name):
    # Add new log file entry with datestamp
    log_time = str(datetime.now())
    with open(log, 'a') as f:
        f.writelines("Entry logged at: {} by {}\n".format(log_time, name))

# Entry point for program
if __name__ == "__main__":
    # Get username
    name = input("What is your name?")
    # Add enrty to log file
    print("Adding new log entry")
    write_log(log_file, name)
    print()
    # Access starting log file
    print("Log file contents")
    print("-----------------")
    read_log(log_file)






from datetime import datetime

log_file = "two.log"

def read_log(log):
    with open(log, 'r') as f:
        print(f.read())

def write_log(log, name):
    time = str(datetime.now())
    with open(log, 'a') as f:
        f.writelines("Entry was logged by {} at {}\n".format(name, time))

if __name__ == '__main__':
    name = input("What is your name?: ")

    print("Added new entry")
    write_log(log_file, name)
    print()
    print("Log file contents")
    print("-----------------")
    read_log(log_file)







