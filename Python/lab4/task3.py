import cv2
import argparse
from pathlib import Path

def play_video_with_info(video_file):
    # Open the video file
    cap = cv2.VideoCapture(video_file)
    
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_file}")
        return
    
    # Get the FPS and filename
    fps = cap.get(cv2.CAP_PROP_FPS)
    video_path = Path(video_file)
    filename = video_path.name

    # Loop to read and display frames
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Add text to the frame
        text = f"File: {filename} | FPS: {fps:.2f}"
        cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        
        # Display the frame
        cv2.imshow("Video Player", frame)
        
        # Check if 'q' is pressed or window is closed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if cv2.getWindowProperty("Video Player", cv2.WND_PROP_VISIBLE) < 1:
            break
    
    # Release the video capture object and close the display window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Play a video file and display its name and FPS.")
    parser.add_argument("video_file", type=str, help="Path to the video file to play")

    args = parser.parse_args()
    
    play_video_with_info(args.video_file)
