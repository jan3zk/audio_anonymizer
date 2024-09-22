import os
import shutil
import subprocess
import sys
import argparse
import glob
from audio_anonymizer.anonymize_audio import anonymize_audio
from onedrivedownloader import download
from platformdirs import user_cache_dir

# Define predefined paths and parameters
cachedir = user_cache_dir("anonymize-audio")
LEXICON_PATH = os.path.join(cachedir, "dictionary_optilex.txt")
LEXICON_LINK = "https://unilj-my.sharepoint.com/:t:/g/personal/janezkrfe_fe1_uni-lj_si/EdNmItci4dlAhvpaoptW0aABitMviYo4K-Lb6HvSw_jS9w"
ACOUSTIC_MODEL_PATH = os.path.join(cachedir, "acoustic_model_optilex.zip")
ACOUSTIC_MODEL_LINK = "https://unilj-my.sharepoint.com/:u:/g/personal/janezkrfe_fe1_uni-lj_si/EVA5yuhNNTxMqx_ofe2vI0oB3IMGD5sNcsacn-6IXFQzTg"
G2P_MODEL_PATH = os.path.join(cachedir, "OPTILEX_v3_g2p.zip")
G2P_MODEL_LINK = "https://unilj-my.sharepoint.com/:u:/g/personal/janezkrfe_fe1_uni-lj_si/EQm-NH1vxMNOtG70O6TjSnMByE7UM4xwnIQnWIcuJzMaXA"
if not os.path.isfile(LEXICON_PATH):
    print("Downloading pronunciation dictionary ...")
    download(LEXICON_LINK, filename=LEXICON_PATH, unzip=False)
if not os.path.isfile(ACOUSTIC_MODEL_PATH):
    print("Downloading acoustic model ...")
    download(ACOUSTIC_MODEL_LINK, filename=ACOUSTIC_MODEL_PATH, unzip=False)
if not os.path.isfile(G2P_MODEL_PATH):
    print("Downloading G2P model ...")
    download(G2P_MODEL_LINK, filename=G2P_MODEL_PATH, unzip=False)

BEAM = 300
RETRY_BEAM = 3000
TMP_DIR = os.path.join(cachedir, "tmp")

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
    
    print(f"Running MFA alignment for {in_wav_file}. This may take several minutes ...")
    subprocess.run(mfa_command, check=True)

def main():
    parser = argparse.ArgumentParser(description="Audio Anonymization Pipeline")
    parser.add_argument("in_wav_file", help="Input WAV file")
    parser.add_argument("txt_file", help="Transcription TXT file")
    parser.add_argument("out_wav_file", nargs="?", help="Optional output WAV file", default=None)
    parser.add_argument("--keywords", nargs="*", help="Optional keywords for anonymization", default=[])
    args = parser.parse_args()

    # If out_wav_file is not provided, set it as in_wav_file appended with "anonymized"
    if args.out_wav_file is None:
        base, ext = os.path.splitext(args.in_wav_file)
        args.out_wav_file = f"{os.path.basename(base)}_anonymized{ext}"

    # Run alignment
    run_alignment(args.in_wav_file, args.txt_file)
    
    # Run anonymization
    textgrid_file = os.path.join(TMP_DIR, os.path.basename(args.in_wav_file).replace(".wav", ".TextGrid"))
    print(f"Anonymizing audio {args.in_wav_file}:")
    anonymize_audio(args.in_wav_file, textgrid_file, args.out_wav_file, args.keywords)

    files = glob.glob(os.path.join(TMP_DIR,'*'))
    for f in files:
        os.remove(f)

if __name__ == "__main__":
    main()
