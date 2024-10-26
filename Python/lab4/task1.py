import argparse
from moviepy.video.io.VideoFileClip import VideoFileClip
from pathlib import Path

def extract_video_clip(input_file, start_time, end_time, output_file):
    try:
        video = VideoFileClip(str(input_file))  # Convert Path to string
        clip = video.subclip(start_time, end_time)
        
        output_path = input_file.parent / output_file
        clip.write_videofile(str(output_path), codec="libx264", audio_codec="aac", remove_temp=True)
        print(f"Clip successfully saved as {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract a clip from a video file.")
    parser.add_argument("input_file", type=str, help="Full path to the input video file")
    parser.add_argument("start_time", type=str, help="Start time of the clip (hh:mm:ss)")
    parser.add_argument("end_time", type=str, help="End time of the clip (hh:mm:ss)")
    parser.add_argument("output_file", type=str, help="Output video file name (will be saved in the same directory as the input file)")

    args = parser.parse_args()

    input_path = Path(args.input_file)

    if not input_path.is_file():
        print(f"Input file {input_path} does not exist.")
    else:
        extract_video_clip(input_path, args.start_time, args.end_time, args.output_file)

#"c:/Users/turch/Рабочий стол/junk/InstituteProject-course--3-/.venv/Scripts/python.exe" "c:/Users/turch/Рабочий стол/junk/InstituteProject-course--3-/Python/lab4/task1.py" "C:\Users\turch\Рабочий стол\junk\InstituteProject-course--3-\Python\lab4\test_video.mp4"  "00:01:00" "00:02:30" output_clip.mp4