# Dice Class

`Dice` クラスは、乱数生成を行うユーティリティクラスです。

## 概要

*   **名前空間**: `utils`
*   **ヘッダファイル**: `include/utils/Dice.h`
*   **ソースファイル**: `src/utils/Dice.cpp`

## 責務

*   乱数生成器（メルセンヌ・ツイスタ）の初期化と管理
*   指定された範囲の整数の乱数生成

## メンバ変数

### `private`

*   `static std::mt19937 mt`: メルセンヌ・ツイスタ乱数生成器

## メンバ関数

### `public`

#### `static void init()`
*   **説明**: 乱数生成器を初期化します。プログラム開始時に一度だけ呼び出す必要があります。

#### `static int get(int min, int max)`
*   **説明**: 指定された範囲（min以上max以下）のランダムな整数を返します。
