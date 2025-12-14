# GameManager Class

{cpp:class}`GameManager` クラスは、ゲーム全体の進行を管理するクラスです。

## 概要

*   **名前空間**: `core` (ディレクトリ構成上)
*   **ヘッダファイル**: `include/core/GameManager.h`
*   **ソースファイル**: `src/core/GameManager.cpp`

## 責務

*   ゲームの初期化（`Dice`の初期化など）
*   プレイヤー（`Hero`）と敵（`Monster`）の生成
*   バトルループの制御（ターン管理）
*   勝敗判定と結果表示

## メンバ関数

### `public`

#### {cpp:func}`GameManager::GameManager`
*   **説明**: コンストラクタ。乱数生成器の初期化を行います。

#### {cpp:func}`GameManager::start`
*   **説明**: ゲームを開始します。
*   **処理内容**:
    1.  ユーザーにヒーローの名前を入力させます。
    2.  ヒーローとモンスターのインスタンスを生成します。
    3.  `battle()` メソッドを呼び出してバトルを開始します。

### `private`

#### {cpp:func}`GameManager::battle`
*   **説明**: バトルのメインループを実行します。
*   **処理内容**:
    *   どちらかのHPが0になるまでターンを繰り返します。
    *   各ターンで `heroTurn()` と `monsterTurn()` を交互に呼び出します。
    *   勝敗が決まったら結果を表示します。

#### {cpp:func}`GameManager::heroTurn`
*   **説明**: ヒーローの行動処理を行います。
*   **処理内容**:
    *   ユーザーからの入力を受け付け、攻撃またはスキル使用を実行します。

#### {cpp:func}`GameManager::monsterTurn`
*   **説明**: モンスターの行動処理を行います。
*   **処理内容**:
    *   モンスターのAIロジック（`performAction`）を呼び出します。

#### {cpp:func}`GameManager::showStatus`
*   **説明**: 現在のステータス（HP/MP）を表示します。
