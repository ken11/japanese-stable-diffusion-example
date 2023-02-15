# これなに
MacとかCPU環境でもりんなのJapaneseStableDiffusion使ってみよう的なサンプル

## 使い方
venvとかで環境切った方がオススメ  
あとりんなのJapaneseStableDiffusionを使うにはHuggingFaceのユーザ登録が事前に必要なのでそれは済ませておく

### 各種ライブラリを入れる
```sh
$ pip install torch torchvision torchaudio
$ pip install transformers diffusers accelerate
$ huggingface-cli login
$ pip install git+https://github.com/rinnakk/japanese-stable-diffusion
```

### 実行する
```sh
$ python run.py --text ねこかわいい --output ./cat.png
```


