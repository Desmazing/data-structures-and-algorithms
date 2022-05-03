# get memory in bytes
# convert to GB

byt_mem = float(input("Enter memory in bytes: "))
gb_mem = byt_mem / 1073741824

print(f'{byt_mem} bytes = {gb_mem} GB')