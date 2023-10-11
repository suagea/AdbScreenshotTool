## ADB スクリーンショットツール README.md

### 概要

ADB スクリーンショットツールは、ADB（Android Debug Bridge）を介して Android デバイスからスクリーンショットを取得するユーティリティです。このツールは、接続されたデバイスを対話的に選択し、指定したファイル名でスクリーンショットを取得するための便利なコマンドラインインターフェースを提供しています。

### インストール方法

仮想環境をセットアップし、必要なパッケージをインストールします：

```bash
python -m venv venv
source venv/bin/activate # Windows の場合：venv\Scripts\activate
pip install -r requirements.txt
```

プロジェクトのルートディレクトリに、必要な ADB バイナリを含む `adb_tool` フォルダが存在することを確認してください。

### 使い方

1. スクリプトを実行します：

```bash
python AdbScreenshotTool.py
```

2. プロンプトに従って、接続された Android デバイスを選択し、スクリーンショットのファイル名を指定します。

3. スクリーンショットの取得を停止するには、ファイル名として `?` を入力します。