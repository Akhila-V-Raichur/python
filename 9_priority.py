class Process:
    def __init__(s, name, arrival_time, burst_time, priority):
        s.name = name
        s.arrival_time = arrival_time
        s.burst_time = burst_time
        s.priority = priority

def preemptive_priority_scheduling(processes):
    total_time = 0
    remaining_time = [process.burst_time for process in processes]
    waiting_time = [0] * len(processes)
    turnaround_time = [0] * len(processes)
    completed = 0
    n=len(processes)
    while completed < len(processes):
        current_process = None
        highest_priority = float('inf')

        for i in range(len(processes)):
            if processes[i].arrival_time <= total_time and remaining_time[i] > 0 and processes[i].priority < highest_priority:
                current_process = i
                highest_priority = processes[i].priority

        if current_process is None:
            total_time += 1
        else:
            remaining_time[current_process] -= 1
            total_time += 1

            if remaining_time[current_process] == 0:
                completed += 1
                turnaround_time[current_process] = total_time - processes[current_process].arrival_time
                waiting_time[current_process] = turnaround_time[current_process] - processes[current_process].burst_time

    print("Process\tWaiting Time\tTurnaround Time")
    for i in range(len(processes)):
        print(f"{processes[i].name}\t{waiting_time[i]}\t\t{turnaround_time[i]}")
    
    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)

    average_waiting_time = total_waiting_time/ n
    average_turnaround_time = total_turnaround_time / n

    print("Average Waiting Time: {:.2f}".format(average_waiting_time))
    print("Average Turnaround Time: {:.2f}".format(average_turnaround_time))
    

n = int(input("Enter the number of processes: "))
processes = []
    
for i in range(n):
    name = input(f"Enter the name of process {i+1}: ")
    arrival_time = int(input(f"Enter arrival time of process {i+1}: "))
    burst_time = int(input(f"Enter burst time of process {i+1}: "))
    priority = int(input(f"Enter priority of process {i+1}: "))
    processes.append(Process(name, arrival_time, burst_time, priority))

processes.sort(key=lambda x: x.arrival_time)

preemptive_priority_scheduling(processes)
