import os
import argparse
import pretty_midi

def clean_midi_files(input_dir, output_dir):
    """
    Performs the following operations on MIDI files in the given directory:
    1. Removes any empty MIDI files
    2. Sets the program for all instruments to Electric Bass (program 33)
    3. Saves the cleaned-up MIDI files to the output directory
    """
    for filename in os.listdir(input_dir):
        if filename.endswith(".mid") or filename.endswith(".midi"):
            input_path = os.path.join(input_dir, filename)
            midi = pretty_midi.PrettyMIDI(input_path)

            # Check if the MIDI file is empty
            if len(midi.instruments) == 0:
                os.remove(input_path)
                print(f"Removed empty MIDI file: {filename}")
                continue

            # Set the program for all instruments to Electric Bass (program 33)
            for instrument in midi.instruments:
                instrument.program = 33

            # Save the cleaned-up MIDI file
            cleaned_filename = os.path.splitext(filename)[0] + ".mid"
            output_path = os.path.join(output_dir, cleaned_filename)
            midi.write(output_path)
            print(f"Saved cleaned MIDI file: {cleaned_filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean up MIDI files")
    parser.add_argument("input_dir", help="Path to the directory containing MIDI files")
    parser.add_argument("output_dir", help="Path to the directory to save the cleaned-up MIDI files")
    args = parser.parse_args()

    clean_midi_files(args.input_dir, args.output_dir)