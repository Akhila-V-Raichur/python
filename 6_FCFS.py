class Process:
    def __init__(s, name, arrival_time, burst_time):
        s.name = name
        s.arrival_time = arrival_time
        s.burst_time = burst_time
        s.waiting_time = 0
        s.turnaround_time = 0

def calculate_waiting_time(processes):
    total_waiting_time = 0
    current_time = 0
    for process in processes:
        if process.arrival_time > current_time:
            current_time = process.arrival_time
        else:
            process.waiting_time = current_time - process.arrival_time
            total_waiting_time += process.waiting_time
            current_time += process.burst_time
    return total_waiting_time

def calculate_turnaround_time(processes):
    total_turnaround_time = 0
    for process in processes:
        process.turnaround_time = process.waiting_time + process.burst_time
        total_turnaround_time += process.turnaround_time
    return total_turnaround_time

n = int(input("Enter the number of processes: "))
processes = []
for i in range(n):
    name = input("Enter process name: ")
    arrival_time = int(input("Enter arrival time for process {}: ".format(name)))
    burst_time = int(input("Enter burst time for process {}: ".format(name)))
    processes.append(Process(name, arrival_time, burst_time))

processes.sort(key=lambda x: x.arrival_time) 

total_waiting_time = calculate_waiting_time(processes)
total_turnaround_time = calculate_turnaround_time(processes)
average_waiting_time = total_waiting_time / n
average_turnaround_time = total_turnaround_time / n
print("\nFCFS Scheduling Results:")
print("Average Waiting Time: {:.2f}".format(average_waiting_time))
print("Average Turnaround Time: {:.2f}".format(average_turnaround_time))