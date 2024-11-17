from pydub import AudioSegment
import simpleaudio as sa
import random as ran

class VoicePlayer:
    def __init__(self, audio_folder):
        """Initialize the VoicePlayer with the path to the m4a file."""
        self.audio_folder = audio_folder if audio_folder[-1] == '/' else f'{audio_folder}/'
        self.audio = None

    def load_intro(self):
        self.load_audio(self.generate_file_path('intro', 2, '.m4a'))

    def load_never_wrong(self):
        self.load_audio(self.generate_file_path('first_guess_right', 1, '.m4a'))

    def load_wrong(self):
        self.load_audio(self.generate_file_path('wrong', 1, '.m4a'))
    
    def load_right_after_wrong(self):
        self.load_audio(self.generate_file_path('right_after_wrong', 3, '.m4a'))
    
    def load_game_over(self):
        self.load_audio(self.generate_file_path('game_over', 1, '.m4a'))

    def load_audio(self, file):
        """Load the audio file into memory using pydub."""
        try:
            # Load the audio file (support for m4a is provided by ffmpeg)
            self.audio = AudioSegment.from_file(file, format="m4a")
        except Exception as e:
            print(f"Error loading audio file: {e}")

    def play(self):
        """Play the loaded audio file."""
        if self.audio is None:
            print("Audio file is not loaded. Please load the audio first.")
            return

        try:
            # Convert audio to raw data and play using simpleaudio
            raw_data = self.audio.raw_data
            play_obj = sa.play_buffer(raw_data, num_channels=self.audio.channels,
                                      bytes_per_sample=self.audio.sample_width, sample_rate=self.audio.frame_rate)
            play_obj.wait_done()  # Wait until playback is finished
        except Exception as e:
            print(f"Error playing audio: {e}")

    def generate_file_path(self, file_name, num_files, extension):
        extension = extension[1:] if extension[0] == '.' else extension
        return f'{self.audio_folder}{file_name}{ran.randint(1, num_files)}.{extension}'
# Example usage
if __name__ == "__main__":
    voice_player = VoicePlayer("")  # Replace with your .m4a file path
    voice_player.load_audio("/home/aidan/projects/robot/audio/right_after_wrong1.m4a")
    voice_player.play()
