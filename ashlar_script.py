import os
import subprocess



input_dir = r'R:\Aidan\ULA_timecourse_ARC_006_temp'
output_dir = r'R:\Aidan\ULA_timecourse_ARC_006_temp'
os.makedirs(output_dir, exist_ok=True)
label = '0944S'
time_points = 28


# Construct the file series arguments for all rounds
fileseries_args = [f"fileseries|{input_dir}|pattern={label}_ch_{{channel:2}}_m_{{series:2}}_t_{str(round_num).zfill(3)}.tif|overlap=0.105|width=5|height=5|layout=snake|pixel_size=0.325" for round_num in range(time_points)]

# Create the full command as a list of arguments
command = [
    'ashlar',
    *fileseries_args,
    '--output', f"{output_dir}\\{label}_ashlar_{{cycle:3}}_{{channel:2}}.tif",
    '--maximum-shift', '200',
    '--align-channel', '1',
]

# Execute the command using subprocess
subprocess.run(command)
