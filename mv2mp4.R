# linux bash
# sudo apt install ffmpeg


# Define input and output paths
input_mov <- "your_video.mov"
output_mp4 <- "your_video.mp4"

# Construct FFmpeg command
cmd <- sprintf("ffmpeg -i \"%s\" -vcodec libx264 -acodec aac \"%s\"", input_mov, output_mp4)

# Run the command from R
system(cmd)


library(processx)

run("ffmpeg", c("-i", input_mov, "-vcodec", "libx264", "-acodec", "aac", output_mp4))
