def fcfs(processes, burst_times):
    n = len(processes)
    wait_times = [0] * n
    turnaround_times = [0] * n

    # Calculate waiting time for each process
    for i in range(1, n):
        wait_times[i] = wait_times[i - 1] + burst_times[i - 1]

    # Calculate turnaround time for each process
    for i in range(n):
        turnaround_times[i] = wait_times[i] + burst_times[i]

    # Calculate average wait time and turnaround time
    avg_wait_time = sum(wait_times) / n
    avg_turnaround_time = sum(turnaround_times) / n

    # Display process details
    print("Process\tBurst Time\tWait Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i]}\t\t{burst_times[i]}\t\t\t{wait_times[i]}\t\t\t{turnaround_times[i]}")

    print(f"\nAverage Wait Time: {avg_wait_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")


# Example usage
if __name__ == "__main__":
    processes = [1, 2, 3, 4]  # Process IDs
    burst_times = [5, 9, 6, 3]  # Burst times of each process

    fcfs(processes, burst_times)
