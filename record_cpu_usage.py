import psutil
import time
import csv

def record_cpu_usage(duration=10, interval=1, output_file="cpu_usage.csv"):
    """
    Records CPU usage every 'interval' seconds for a total of 'duration' seconds.
    The readings are printed to the console and saved to a CSV file.
    
    Args:
        duration (int): Total duration in seconds to record CPU usage.
        interval (int): Interval in seconds between each CPU usage measurement.
        output_file (str): The name of the CSV file to write the CPU usage data.
    """
    samples = int(duration / interval)
    cpu_readings = []
    
    print("Recording CPU usage:")
    for _ in range(samples):
        # psutil.cpu_percent blocks for the interval duration and then returns the average CPU usage over that interval.
        cpu_percent = psutil.cpu_percent(interval=interval)
        timestamp = time.time()
        cpu_readings.append((timestamp, cpu_percent))
        print(f"Time: {timestamp:.2f}, CPU usage: {cpu_percent}%")
    
    # Write the recorded CPU usage data to a CSV file.
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "cpu_usage_percent"])
        writer.writerows(cpu_readings)
    
    return cpu_readings

if __name__ == "__main__":
    record_cpu_usage(duration=10, interval=1)
