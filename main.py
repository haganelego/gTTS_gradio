import os
from gtts import gTTS
import gradio as gr

def text_to_speech(text, file_name):
    tts = gTTS(text=text, lang='en', tld='co.uk')
    save_path = os.path.join('./saved_audio', f"{file_name}.mp3")

    # ディレクトリが存在しない場合は作成
    if not os.path.exists('./saved_audio'):
        os.makedirs('./saved_audio')
    tts.save(save_path)
    return save_path

iface = gr.Interface(
    fn=text_to_speech,
    inputs=[
        gr.Textbox(lines=2, placeholder="読み上げるテキストをここに入力"),
        gr.Textbox(placeholder="保存するファイル名 (拡張子不要)")
    ],
    outputs=gr.Audio(type="filepath", label="生成された音声"),
    title="テキストを音声に変換",
    description="テキストを入力して音声ファイルとして保存し、再生します。"
)

if __name__ == "__main__":
    iface.launch()
