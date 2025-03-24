import pandas as pd
import sys

try:
    # Read the CPU usage CSV, assuming it has columns:
    # timestamp, total_memory, used_memory, percent
    df_cpu = pd.read_csv('cpu_usage.csv', header=None, names=['timestamp','total_memory','used_memory','percent'])
    # Remove total_memory
    df_cpu = df_cpu[['timestamp', 'used_memory', 'percent']]
except Exception as e:
    df_cpu = pd.DataFrame()
    print('CPU file error:', e, file=sys.stderr)

try:
    # Read the memory usage CSV similarly
    df_mem = pd.read_csv('memory_usage.csv', header=None, names=['timestamp','total_memory','used_memory','percent'])
    df_mem = df_mem[['timestamp', 'used_memory', 'percent']]
except Exception as e:
    df_mem = pd.DataFrame()
    print('Memory file error:', e, file=sys.stderr)

try:
    # Read the test duration CSV (assumed to have headers)
    df_test = pd.read_csv('test_duration.csv')
except Exception as e:
    df_test = pd.DataFrame()
    print('Test duration file error:', e, file=sys.stderr)

# Write combined CSV: First write CPU, then append memory and test duration data
df_cpu.to_csv('combined_metrics.csv', index=False)
if not df_mem.empty:
    df_mem.to_csv('combined_metrics.csv', mode='a', index=False, header=False)
if not df_test.empty:
    df_test.to_csv('combined_metrics.csv', mode='a', index=False, header=False)

with open('combined_metrics.csv', 'r') as f:
    print(f.read())
