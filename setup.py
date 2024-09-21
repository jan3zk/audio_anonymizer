from setuptools import setup, find_packages

setup(
    name="audio_anonymizer",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    scripts=['audio_anonymizer/anonymize_pipeline.py'],
    install_requires=[
        # Add external dependencies
        "montreal-forced-aligner",
    ],
    entry_points={
        'console_scripts': [
            'anonymize-audio = audio_anonymizer.anonymize_pipeline:main',
        ],
    },
    description="An audio anonymization tool using MFA.",
    author="Janez Krizaj",
    author_email="janez.krizaj@fe.uni-lj.si",
    url="https://github.com/jan3zk/audio_anonymizer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
