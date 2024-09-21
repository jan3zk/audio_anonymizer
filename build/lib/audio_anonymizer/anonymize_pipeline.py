import os
import shutil
import subprocess
import sys
import argparse
import glob
from audio_anonymizer.anonymize_audio import anonymize_audio

# Define predefined paths and parameters
LEXICON_PATH = "./data/dictionary_optilex.txt"
ACOUSTIC_MODEL_PATH = "./data/acoustic_model_optilex.zip"
G2P_MODEL_PATH = "./data/OPTILEX_v3_g2p.zip"
BEAM = 300
RETRY_BEAM = 3000
TMP_DIR = "./data/tmp"

def run_alignment(in_wav_file, txt_file):
    """Runs MFA alignment based on the provided files."""
    if not os.path.exists(TMP_DIR):
        os.makedirs(TMP_DIR)
    shutil.copy(in_wav_file, TMP_DIR)
    shutil.copy(txt_file, TMP_DIR)

    # MFA alignment command
    mfa_command = [
        "mfa", "align", "--clean", "--single_speaker", TMP_DIR,
        LEXICON_PATH, ACOUSTIC_MODEL_PATH, TMP_DIR,
        "--beam", str(BEAM), "--retry_beam", str(RETRY_BEAM),
        "--g2p_model_path", G2P_MODEL_PATH
    ]
    
    print(f"Running MFA alignment for {in_wav_file}...")
    subprocess.run(mfa_command, check=True)

def main():
    parser = argparse.ArgumentParser(description="Audio Anonymization Pipeline")
    parser.add_argument("in_wav_file", help="Input WAV file")
    parser.add_argument("txt_file", help="Transcription TXT file")
    parser.add_argument("out_wav_file", help="Output WAV file")
    parser.add_argument("--keywords", nargs="*", help="Optional keywords for anonymization", default=[])
    args = parser.parse_args()

    # Run alignment
    run_alignment(args.in_wav_file, args.txt_file)
    
    # Run anonymization
    textgrid_file = f"./data/tmp/{os.path.basename(args.in_wav_file).replace('.wav', '.TextGrid')}"   
    print(f"Anonymizing audio {args.in_wav_file}...")
    anonymize_audio(args.in_wav_file, textgrid_file, args.out_wav_file, args.keywords)

    files = glob.glob(os.path.join(TMP_DIR,'*'))
    for f in files:
        os.remove(f)

if __name__ == "__main__":
    main()
