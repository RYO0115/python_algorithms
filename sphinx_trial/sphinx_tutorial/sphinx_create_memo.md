# Sphinxの基本的な使い方

## 完成系

- Markdwonファイルを用いてドキュメントを作成する
- 一般的なフォルダ構成、設定を用いる
- Markdownファイルを最低3つ作成する

## 作成手順

1. **環境構築**
   - 必要なライブラリをインストールする
     ```bash
     uv init
     uv add sphinx myst-parser
     ```

2. **プロジェクト作成**
   - ドキュメント用のディレクトリを作成し、初期化する
     ```bash
     mkdir docs
     cd docs
     uv run sphinx-quickstart
     ```
   - `sphinx-quickstart` の質問には適宜答える（基本的にはデフォルトでOK、言語は `ja` 推奨）

3. **設定変更 (`conf.py`)**
   - Markdownをサポートするために `myst_parser` 拡張を追加する
     ```python
     extensions = [
         'myst_parser',
     ]
     ```

4. **ドキュメント作成**
   - `.md` ファイルを作成する（例: `intro.md`, `usage.md` 等）
   - `index.rst` (または `index.md`) の `toctree` に作成したファイルを追加する

5. **ビルド**
   - HTMLを生成する
     ```bash
     uv run make html
     ```