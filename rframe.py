import av
import argparse
import os

def save_frames(video_path, frame_numbers):
    container = av.open(video_path)
    frames_to_save = set(frame_numbers)
    saved_frames = 0

    # Создаем папку assets, если она не существует
    os.makedirs('assets', exist_ok=True)

    for frame in container.decode(video=0):
        if frame.pts in frames_to_save:
            img = frame.to_image()
            img.save(f'assets/frame_{frame.pts}.jpg')
            saved_frames += 1
            if saved_frames == len(frames_to_save):
                break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract specific frames from a video.")
    parser.add_argument('-i', '--input', type=str, required=True, help="Path to the input video file.")
    parser.add_argument('-f', '--frames', type=str, required=True, help="Comma-separated list of frame numbers to extract.")
    
    args = parser.parse_args()
    frame_numbers = list(map(int, args.frames.split(',')))
    
    save_frames(args.input, frame_numbers)
