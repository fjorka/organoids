import os
import subprocess



input_dir = r'R:\Aidan\test'
output_dir = r'R:\Aidan\test_output'
os.makedirs(output_dir, exist_ok=True)
label = 'B2_Region1'


# Construct the file series arguments for all rounds
fileseries_args = [f"fileseries|{input_dir}|pattern={label}_ch_{{channel:2}}_m_{{series:2}}_t_{str(round_num).zfill(3)}.tif|overlap=0.105|width=5|height=5|layout=snake|pixel_size=0.325" for round_num in range(11)]

# Create the full command as a list of arguments
command = [
    'ashlar',
    *fileseries_args,
    '--output', f"{output_dir}\\{label}_ashlar_{{cycle:3}}_{{channel:2}}.tif",
    '--maximum-shift', '200',
    '--align-channel', '0'
]

# Execute the command using subprocess
subprocess.run(command)
