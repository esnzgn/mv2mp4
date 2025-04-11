import subprocess
import os

def convert_mov_to_mp4(input_path, output_path=None):
    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"Input file '{input_path}' not found.")

    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + ".mp4"

    cmd = [
        "ffmpeg",
        "-i", input_path,
        "-vcodec", "libx264",
        "-acodec", "aac",
        output_path
    ]

    print(f"Running command: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        print(f"Conversion successful: {output_path}")
    else:
        print("Error occurred during conversion:")
        print(result.stderr)

# Example usage:
convert_mov_to_mp4("example.mov")
