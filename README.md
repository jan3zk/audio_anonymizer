# Audio Anonymizer

## Overview

The Audio Anonymizer is a tool designed to anonymize speech data by replacing specified words or phrases in an audio file with a beep sound. This can be useful in contexts such as research data anonymization, privacy preservation, or sensitive information removal from audio recordings.

This package uses the Montreal Forced Aligner (MFA) for forced alignment and supports Slovene speech anonymization with a pre-built acoustic model and pronunciation dictionary.

## Installation

### 1. Clone this repository

```bash
git clone https://github.com/jan3zk/audio_anonymizer.git
cd audio_anonymizer
```

### 2. Install Montreal Forced Aligner (MFA)

Montreal Forced Aligner is a critical dependency for forced alignment. Install it via Conda:

```bash
conda install montreal-forced-aligner==2.2.14
```

For detailed instructions, refer to the official [MFA documentation](https://montreal-forced-aligner.readthedocs.io/en/latest/).

### 3. Install the anonymize-audio package

To install the `anonymize-audio` package, run the following command from within the repository directory:

```bash
pip install .
```

### 4. Download the SpaCy model

This project also requires the SpaCy model for Slovene language processing. Install the model using the following command:

```bash
python -m spacy download sl_core_news_trf
```

## Usage

```bash
anonymize-audio <in_wav_file> <txt_file> [out_wav_file] [--keywords keyword1 keyword2 ...]
```

### Arguments

1. **`in_wav_file`** (required):

   - **Description**: The input audio file in `.wav` format.
   - **Example**: `input.wav`
   - This is the file you wish to anonymize.
2. **`txt_file`** (required):

   - **Description**: The transcription file in `.txt` format that corresponds to the `in_wav_file`.
   - **Example**: `transcription.txt`
   - The transcription must align with the audio content for accurate anonymization.
3. **`out_wav_file`** (optional):

   - **Description**: The output audio file to be created. If not specified, the script will create an anonymized file by appending `_anonymized` to the original filename.
   - **Example**: `anonymized_output.wav`
   - **Default**: `input_anonymized.wav` (if `in_wav_file` is `input.wav`).
4. **`--keywords`** (optional):

   - **Description**: A list of specific words or phrases you want to anonymize in the audio file. If not provided, the script will attempt to automatically detect keywords using Named Entity Recognition.
   - **Example**: `--keywords John confidential secret`
   - **Usage**: Any number of keywords can be provided. The script will replace occurrences of these words in the audio with a beeping sound.

### Example Commands

1. **Basic Anonymization**:

   ```bash
   anonymize-audio input.wav transcription.txt
   ```

   This command will create `input_anonymized.wav` as the output, replacing automatically detected keywords.
2. **Custom Output File**:

   ```bash
   anonymize-audio input.wav transcription.txt output.wav
   ```

   This will generate the anonymized file named `output.wav`.
3. **Specifying Keywords**:

   ```bash
   anonymize-audio input.wav transcription.txt --keywords John Doe
   ```

   This will specifically anonymize the words "John," and "Doe" in the audio file.

### Using Pre-aligned TextGrid Files

If you already have a Praat TextGrid file with word-level time intervals, you can bypass the forced alignment step and directly anonymize the corresponding audio file.

```bash
python audio_anonymizer/anonymize_audio.py <in_wav_file> <textgrid_file> <out_wav_file> [--keywords keyword1 keyword2 ...]
```

**Arguments**
- in_wav_file (required)
  Path to the input .wav audio file.
- textgrid_file (required)
  Path to a Praat TextGrid file containing word-level annotations.
  The script will read the "words" tier to determine time intervals for anonymization.
- out_wav_file (optional)
  Path where the anonymized .wav file will be saved.
- --keywords (optional)
  List of keywords or patterns to anonymize.
  Example: --keywords Janez* Novak* confidential

**Example**
```bash
python audio_anonymizer/anonymize_audio.py input.wav input.TextGrid output.wav --keywords Janez* Novak*
```
This command will replace all intervals matching Janez, Novak and their inflected forms in the input.wav file using a 1 kHz beep mask.

**Notes**

The TextGrid must contain a tier named words with properly aligned intervals.
If you don't have a TextGrid, you can still use the classic pipeline with a .txt transcription, which will automatically generate the alignment via MFA.

## License

This project is licensed under the Apache 2.0 license. See the `LICENSE` file for more details.

## How to cite

If you use this tool in your research work, please cite it as follows:

**APA**  
Križaj, J., Dobrišek, S. (2024). *Anonymize-audio-sl 1.0: Automatic anonymization of Slovene speech recordings* [Computer software].  
Faculty of Electrical Engineering, University of Ljubljana. Available at: [https://github.com/jan3zk/audio_anonymizer](https://github.com/jan3zk/audio_anonymizer)

**BibTeX**
```bibtex
@misc{anonymizeaudio_sl_1_0,
  author       = {Križaj, Janez and Dobrišek, Simon},
  title        = {Anonymize-audio-sl 1.0: Automatic anonymization of Slovene speech recordings},
  year         = {2024},
  howpublished = {\url{https://github.com/jan3zk/audio_anonymizer}},
  note         = {Faculty of Electrical Engineering, University of Ljubljana}
}
```
