#!/bin/bash

# 必要なパッケージのインストール
apt-get update && apt-get install -y \
    git \
    less \
    tree \
    curl \
    jq \
    zsh \
    && rm -rf /var/lib/apt/lists/*

# タイムゾーンの設定
ln -snf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
echo 'Asia/Tokyo' > /etc/timezone

# Oh My Zshのインストール
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" --unattended

# Gitのコマンド補完を有効にする
echo "autoload -Uz compinit && compinit" >> /root/.zshrc

# Gitの設定
git config --global user.name "0413ttanida"
git config --global user.email "electric.guitarou@outlook.com"
