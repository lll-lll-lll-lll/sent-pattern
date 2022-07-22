#!/usr/bin/python3
import setuptools
import sent_pattern
with open("README.md", "r") as fh:
    long_description = fh.read()


def get_lines(path):
    with open(path) as f:
        return f.readlines()


factory = [
    "sent_pattern = sent_pattern.pipelines.sent_pattern:create_sentence_pattern",
    "span_noun = sent_pattern.pipelines.span_noun:create_span_noun"
]

setuptools.setup(
    name='sent-pattern',
    version=sent_pattern.__version__,
    author='Shunpei Nakayama',
    license="MIT",
    author_email='hoku804049@gmail.com',
    description='project that interpret English sentences to improve your ability to read English sentences correctly.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/lll-lll-lll-lll/sent-pattern',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.8',
    entry_points={
        "spacy_factories": factory,
    },
    install_requires=get_lines("requirements.txt"),
)
