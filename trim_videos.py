from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

original_video = "video1.mp4"
target_name = "test.mp4"
start_time = 0
end_time = 180 #in seconds

ffmpeg_extract_subclip(original_video, start_time, end_time, targetname=target_name)
