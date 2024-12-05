def priority_scheduling(processes, burst_times, priorities):
    """
    Implements non-preemptive priority-based scheduling.
    """
    # Number of processes
    n = len(processes)

    # Combine processes with their burst times and priorities
    process_data = list(zip(processes, burst_times, priorities))

    # Sort processes based on priority (ascending order)
    process_data.sort(key=lambda x: x[2])  # Sort by priority (third element)

    # Initialize waiting time and turnaround time lists
    wait_times = [0] * n
    turnaround_times = [0] * n

    # Calculate waiting times
    for i in range(1, n):
        wait_times[i] = wait_times[i - 1] + process_data[i - 1][1]  # Previous wait time + Previous burst time

    # Calculate turnaround times
    for i in range(n):
        turnaround_times[i] = wait_times[i] + process_data[i][1]  # Wait time + Burst time

    # Calculate averages
    avg_wait_time = sum(wait_times) / n
    avg_turnaround_time = sum(turnaround_times) / n

    # Display process information
    print("Process\tPriority\tBurst Time\tWait Time\tTurnaround Time")
    for i in range(n):
        print(f"{process_data[i][0]}\t{process_data[i][2]}\t\t{process_data[i][1]}\t\t{wait_times[i]}\t\t{turnaround_times[i]}")

    print(f"\nAverage Waiting Time: {avg_wait_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")


# Example usage
if __name__ == "__main__":
    # Input: Process IDs, burst times, and priorities
    processes = [1, 2, 3, 4]
    burst_times = [6, 8, 7, 3]  # Burst times of each process
    priorities = [2, 1, 3, 4]   # Priority of each process (lower number = higher priority)

    priority_scheduling(processes, burst_times, priorities)
