import psutil

physical_cores= psutil.cpu_count(logical=False)
print(physical_cores)

total_cores = psutil.cpu_count(logical=True)
print(total_cores)

cpu_info = psutil.cpu_times()
print("CPU times Info:", cpu_info)

frequency= psutil.cpu_freq()
print("Max Frequency:",frequency.max)
print("Min Frequcy:",frequency.min)
print("current Frequcy",frequency.current)



