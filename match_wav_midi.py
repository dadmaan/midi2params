import os
import argparse
import shutil

def match_wav_to_midi(wav_dir, midi_dir, output_dir):
    """
    Matches WAV files to their corresponding cleaned MIDI files and copies them to the output directory.
    """
    for filename in os.listdir(midi_dir):
        if filename.endswith(".mid"):
            midi_path = os.path.join(midi_dir, filename)
            wav_filename = os.path.splitext(filename)[0] + ".wav"
            wav_path = os.path.join(wav_dir, wav_filename)
            
            if os.path.exists(wav_path):
                output_path = os.path.join(output_dir, wav_filename)
                os.makedirs(output_dir, exist_ok=True)
                shutil.copy(wav_path, output_path)
                print(f"Copied {wav_filename} to {output_dir}")
            else:
                print(f"No WAV file found for {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Match WAV files to cleaned MIDI files")
    parser.add_argument("wav_dir", help="Path to the directory containing WAV files")
    parser.add_argument("midi_dir", help="Path to the directory containing cleaned MIDI files")
    parser.add_argument("output_dir", help="Path to the directory to save the matched WAV files")
    args = parser.parse_args()

    match_wav_to_midi(args.wav_dir, args.midi_dir, args.output_dir)