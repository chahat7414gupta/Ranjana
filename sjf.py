def sjf(processes, burst_times):
    # Number of processes
    n = len(processes)

    # Initialize waiting time and turnaround time lists
    wait_times = [0] * n
    turnaround_times = [0] * n

    # Pair processes with their burst times and sort by burst time
    process_burst = list(zip(processes, burst_times))
    process_burst.sort(key=lambda x: x[1])  # Sort by burst time (ascending)

    # Extract sorted process IDs and burst times
    sorted_processes, sorted_burst_times = zip(*process_burst)
    print(sorted_burst_times,sorted_processes)

    # Calculate waiting time for each process
    for i in range(1, n):
        wait_times[i] = wait_times[i - 1] + sorted_burst_times[i - 1]

    # Calculate turnaround time for each process
    for i in range(n):
        turnaround_times[i] = wait_times[i] + sorted_burst_times[i]

    # Calculate average waiting and turnaround times
    avg_wait_time = sum(wait_times) / n
    avg_turnaround_time = sum(turnaround_times) / n

    # Display the results
    print("Process\tBurst Time\tWait Time\tTurnaround Time")
    for i in range(n):
        print(f"{sorted_processes[i]}\t\t{sorted_burst_times[i]}\t\t\t{wait_times[i]}\t\t\t{turnaround_times[i]}")

    print(f"\nAverage Wait Time: {avg_wait_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")


# Example usage
if __name__ == "__main__":
    # Process IDs and corresponding burst times
    processes = [1, 2, 3, 4]
    burst_times = [6, 8, 7, 3]  # Burst times of each process

    sjf(processes, burst_times)
