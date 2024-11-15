import os
import argparse
import shutil
import pretty_midi

def copy_long_files(input_dir, output_dir):
    """
    Copies MIDI and WAV files that are at least 3 seconds long to new subdirectories in the output directory.
    """
    length_secs = 5.0
    midi_output_dir = os.path.join(output_dir, "midi")
    wav_output_dir = os.path.join(output_dir, "wav")
    os.makedirs(midi_output_dir, exist_ok=True)
    os.makedirs(wav_output_dir, exist_ok=True)

    for root, dirs, files in os.walk(input_dir):
        for filename in files:
            midi_path = os.path.join(input_dir, filename)
            wav_path = os.path.join(input_dir.replace("midi", "wav"), os.path.splitext(filename)[0] + ".wav")
            midi = pretty_midi.PrettyMIDI(midi_path)
            print(midi.get_end_time())
            if midi.get_end_time() >= length_secs:
                midi_output_path = os.path.join(midi_output_dir, filename)
                wav_output_path = os.path.join(wav_output_dir, os.path.splitext(filename)[0] + ".wav")
                shutil.copy(midi_path, midi_output_path)
                print(f"Copied MIDI file: {filename}")
                shutil.copy(wav_path, wav_output_path)
                print(f"Copied WAV file: {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copy long MIDI and WAV files")
    parser.add_argument("input_dir", help="Path to the directory containing MIDI and WAV files")
    parser.add_argument("output_dir", help="Path to the directory to save the copied files")
    args = parser.parse_args()

    copy_long_files(args.input_dir, args.output_dir)