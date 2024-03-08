from langchain.text_splitter import RecursiveCharacterTextSplitter


document = """政治的な虚偽報道や悪意のあるでっち上げを作成するためにも使用される。
選挙運動で対立候補を陥れるネガティブ・キャンペーン、政権政党への批判、戦時下における扇動などの工作にも使われている。
2023年、AI技術を駆使しニュース番組の画面に見せかけた上で当時の日本の内閣総理大臣岸田文雄が卑猥な言葉を発してるように見せたディープフェイク動画がSNSで拡散された。"""

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,  # チャンクの文字数
    chunk_overlap = 10,  # チャンクオーバーラップの文字数
)
docs = text_splitter.split_text(document.replace("\n", ""))

for id, text in enumerate(docs):
    print(f"Chunk {id} (length: {len(text)}): {text}\n\n")
