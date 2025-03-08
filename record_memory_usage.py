import psutil
import time
import csv
import sys

def record_memory_usage(duration=30, interval=1, output_file="memory_usage.csv"):
    samples = int(duration / interval)
    memory_readings = []
    
    for _ in range(samples):
        mem = psutil.virtual_memory()
        timestamp = time.time()
        # Record total, used, and percentage memory usage
        memory_readings.append((timestamp, mem.total, mem.used, mem.percent))
        print(f"Time: {timestamp:.2f}, Total: {mem.total}, Used: {mem.used}, Percent: {mem.percent}%")
    
    # Write data to CSV
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "total_memory", "used_memory", "memory_usage_percent"])
        writer.writerows(memory_readings)

if __name__ == "__main__":
    # Allow custom duration via command-line argument
    duration = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    record_memory_usage(duration=duration, interval=1, output_file="memory_usage.csv")
