# JpnSpacyTextSplliterExample

Examples of Japanese sentence segmentation using SpacyTextSpllitter.

## Preparation

Build a virtual environment which you like.<br>
In this example, a virtual environment is built with pyenv and Python 3.10 is used.

```bash
python -m venv .env
source .env/bin/activate
```

After creating a virtual environment, try to install the libraries.

```bash
pip install -U pip
pip install -r requirements.txt
```

## Creating and applying user defined dictionary

In sudachipy, users can prepare user-defined dictionaries. Using this dictionary, users will be able to consider technical terms when dividing sentences into word-for-word segments, or part of speach taggings.

```
mkdir .sudacy_dict
# put your technical terms in .sudachi_dict/user_terms.csv
touch .sudachi_dict/user_terms.csv
# create the user dictionary with sudachipy
sudachipy ubuild -s .env/lib/python3.10/site-packages/sudachidict_core/resources/system.dic \
    .sudachi_dict/user_terms.csv \
    -o .sudachi_dict/user.dict
```

After creating user dictionary, we need to modify the config in sudachipy.

## Executing scirpts

To apply the generated user dictionary to part of speach tagging processes, please update the config file, first. The name of the config file is `sudachi.json` and it is `sudachipy` directory in the  virtual environment's `site-packages` direcotory.<br>
In that file, add the `userDict` key and the user dictionary path as that value. Following is an example input.

```json
{
    "systemDict" : null,
    "characterDefinitionFile" : "char.def",
    "userDict": [".sudachi_dict/user.dict"],
    "inputTextPlugin" : [
        ...
}
```

## Executing POS with Spacy

Enjoy the output with and without the user dictionary settings.

```bash
python pos_tagging.py
```

## Executing RecursiveCharacterTextSplitter

```bash
python text_split_character.py
```

## Executing SpacyTextSplitter with Ginza

Enjoy the output with and without the user dictionary settings.

```bash
python text_split_spacy.py
```
