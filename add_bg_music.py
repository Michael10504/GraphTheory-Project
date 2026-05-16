import os
from pydub import AudioSegment
from moviepy import VideoFileClip, AudioFileClip


def mix_with_auto_ducking(video_path, bg_music_path, output_path):
    print("Loading audio files...")

    # Load the rendered Manim video (which currently only has the voiceovers)
    vo = AudioSegment.from_file(video_path)

    # Load the background music
    bg = AudioSegment.from_file(bg_music_path)

    # 1. Loop the background music if it's shorter than the video
    if len(bg) < len(vo):
        bg = bg * (len(vo) // len(bg) + 1)

    # Trim background music to match the exact length of the video
    bg = bg[:len(vo)]

    # Lower the overall starting volume of the background music so it's not overpowering
    bg = bg - 12

    print("Applying dynamic audio ducking...")
    chunk_size = 50     # Process in 50 millisecond chunks
    duck_db = -22       # Drop the music by 22 decibels when voiceover plays

    ducked_bg = AudioSegment.empty()
    current_duck = 0.0
    smoothing = 0.1     # Makes the fade-in and fade-out smooth instead of sudden

    # Loop through both audio files simultaneously
    for i in range(0, len(vo), chunk_size):
        vo_chunk = vo[i:i+chunk_size]
        bg_chunk = bg[i:i+chunk_size]

        # If the voiceover volume is below -40 dBFS, consider it "silent" (wait time)
        if vo_chunk.dBFS < -40:
            target_duck = 0.0
        else:
            # Voiceover detected! Drop the background music volume
            target_duck = duck_db

        # Apply the smoothing factor for cinematic fade transitions
        current_duck += (target_duck - current_duck) * smoothing

        # Apply the calculated volume to this chunk of background music
        ducked_bg += bg_chunk + current_duck

    print("Mixing tracks together...")
    # Overlay the original voiceovers on top of our new dynamically ducking background music
    final_audio = vo.overlay(ducked_bg)

    temp_audio_path = "temp_mix.wav"
    final_audio.export(temp_audio_path, format="wav")

    print("Attaching mixed audio to final video...")
    # Use MoviePy to stitch the new audio back into the Manim video
    video = VideoFileClip(video_path)
    new_audio_clip = AudioFileClip(temp_audio_path)

    final_video = video.with_audio(new_audio_clip)
    final_video.write_videofile(
        output_path, codec="libx264", audio_codec="aac")

    # Clean up the temporary file
    os.remove(temp_audio_path)
    print("Success! Final video saved to:", output_path)


# --- RUN THE CODE ---
if __name__ == "__main__":
    # Corrected your paths here!
    MANIM_OUTPUT = "media/videos/anim/1080p60/CopsAndRobbers.mp4"
    BACKGROUND_MUSIC = "media/audio/euler-s-clock-f-5-jkom_L9sbU6Iy.wav"
    FINAL_OUTPUT = "Final_CopsAndRobbers.mp4"

    mix_with_auto_ducking(MANIM_OUTPUT, BACKGROUND_MUSIC, FINAL_OUTPUT)
