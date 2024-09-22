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

### 3. Install the Audio Anonymizer package

To install `anonymize-audio` script, run the following command:

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

## License

This project is licensed under the BSD 2-Clause License. See the `LICENSE` file for more details.
