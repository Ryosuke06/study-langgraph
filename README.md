# Study LangGraph

このプロジェクトは、LangGraph（LangChain のグラフベースワークフロー拡張）の学習と実験のためのリポジトリです。

## プロジェクト概要

このプロジェクトでは、LangGraph を使用して、複数のエージェントが協調して動作する対話システムを実装しています。主な機能は以下の通りです：

- OpenAI GPT-4 を使用したチャットベースの対話システム
- ツールを使用した機能拡張
- グラフベースのワークフローによる複雑な対話の管理

## 技術スタック

- Python 3.13
- LangGraph 0.4.0
- LangChain OpenAI 0.3.8
- その他の依存関係（requirements.txt を参照）

## プロジェクト構造

```
study-langgraph/
├── langgraph.json       # プロジェクト設定ファイル
├── main.py             # メインのワークフロー定義
├── requirements.txt    # 依存パッケージリスト
└── src/
    └── utils/
        ├── nodes.py    # ノード定義（モデル呼び出し、ツール実行など）
        ├── state.py    # 状態管理の定義
        └── tools.py    # 使用可能なツールの定義
```

## セットアップ方法

1. リポジトリのクローン

```bash
git clone https://github.com/Ryosuke06/study-langgraph.git
cd study-langgraph
```

2. Python 仮想環境の作成と有効化

```bash
python -m venv venv
source venv/bin/activate  # Windowsの場合: venv\Scripts\activate
```

3. 依存パッケージのインストール

```bash
pip install -r requirements.txt
```

4. 環境変数の設定
   `.env`ファイルを作成し、以下の環境変数を設定してください：

```
# OpenAI API設定
OPENAI_API_KEY=<your_api_key_here>

# ログ設定
LOG_LEVEL=INFO

# LangSmith設定（オプション：デバッグやモニタリング用）
LANGSMITH_API_KEY=<your_langsmith_api_key>
LANGCHAIN_TRACING_V2=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_PROJECT=study-langgraph

# Google API設定（オプション：追加機能用）
GOOGLE_API_KEY=<your_google_api_key>
GOOGLE_CSE_ID=<your_google_cse_id>
```


## 使用方法

メインのワークフローを実行するには：

```bash
python main.py
```

## ワークフローの説明

このプロジェクトでは、LangGraph を使用して以下のような対話フローを実装しています：

1. ユーザーからの入力を受け取る
2. GPT-4 モデルが入力を処理
3. 必要に応じてツールを使用
4. 結果を返却
5. 必要に応じてステップ 2 に戻る

## ライセンス

MIT ライセンス

## 注意事項

- このプロジェクトは学習目的で作成されています
- OpenAI API キーが必要です
- 実験的な実装を含む可能性があります

## 参考にしたもの（てか全くほぼ一緒）

https://zenn.dev/dely_jp/articles/5034db4f729638
