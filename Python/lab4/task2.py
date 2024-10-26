import argparse
# Importing ImageClip from moviepy.editor
from moviepy.editor import VideoFileClip, ImageClip
from pathlib import Path

"""

Had the same issues.

After digging into the source code (https://github.com/Zulko/moviepy/blob/master/moviepy/video/fx/resize.py)

I found that moviepy will try to use opencv as resizer first, if opencv not installed it will use PIL which leads to the error we are seeing here.

Instead of fixing the deprecated PIL package, simply installing opencv-python works for me.


"""


def extract_frames(input_file, start_time, end_time, step):
    try:
        video_clip = VideoFileClip(input_file)
        resized_clip = video_clip.resize(width=250)
        clip = resized_clip.subclip(start_time, end_time)

        input_path = Path(input_file)
        output_dir = input_path.parent  # Use the same directory as the input file
        output_dir = input_path.parent / "output"
        # Ensure the output directory exists
        output_dir.mkdir(parents=True, exist_ok=True)

        frame_count = 0
        for t in range(0, int(clip.duration), step):
            frame = clip.get_frame(t)
            frame_clip = ImageClip(frame)
            frame_path = output_dir / f"frame_{frame_count:04d}.jpg"
            frame_clip.save_frame(str(frame_path), t=0)  # Save the frame
            print(f"Saved {frame_path}")
            frame_count += 1

        print(f"Extracted {frame_count} frames to {output_dir}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract frames from a video file.")
    parser.add_argument("input_file", type=str,
                        help="Full path to the input video file")
    parser.add_argument("start_time", type=str,
                        help="Start time of the segment (hh:mm:ss)")
    parser.add_argument("end_time", type=str,
                        help="End time of the segment (hh:mm:ss)")
    parser.add_argument("--step", type=int, default=10,
                        help="Step for extracting frames (default: 10 seconds)")

    args = parser.parse_args()

    extract_frames(args.input_file, args.start_time, args.end_time, args.step)

#"c:/Users/turch/Рабочий стол/junk/InstituteProject-course--3-/.venv/Scripts/python.exe" "c:/Users/turch/Рабочий стол/junk/InstituteProject-course--3-/Python/lab4/task2.py" "C:\Users\turch\Рабочий стол\junk\InstituteProject-course--3-\Python\lab4\test_video.mp4"  "00:01:00" "00:02:30" --step 10