import spacy
import ginza


def normlize_text(text):
    text = text.replace("\n", "").replace("\r", "").replace("\t", " ")
    text = text.lower()
    return text


nlp = spacy.load("ja_ginza")
ginza.set_split_mode(nlp, "A")


text = "『アナと雪の女王』（アナとゆきのじょおう、原題：Frozen）は、ウォルト・ディズニー・アニメーション・スタジオ製作の映画です。"
text = normlize_text(text)
parsed_text = nlp(text)

for sentence in parsed_text.sents:
    for token in sentence:
        print(token.i, token.orth_, token.tag_)
