#!/bin/bash

set -e

INSTALL_DIR="$HOME/.local/bin"
BIN_NAME="aschii"
FILE_NAME="aschii.py"

echo "Installing ASCHII..."

REPO_URL="${ASCHII_REPO_URL:-https://raw.githubusercontent.com/73LIX/ASCHII-ASCII_GENERATOR/refs/heads/main/aschii/aschii.py}"

mkdir -p "$INSTALL_DIR"

curl -sL "$REPO_URL" -o "$INSTALL_DIR/$FILE_NAME"

chmod +x "$INSTALL_DIR/$FILE_NAME"

if [ -L "$INSTALL_DIR/$BIN_NAME" ]; then
    rm "$INSTALL_DIR/$BIN_NAME"
fi
ln -s "$INSTALL_DIR/$FILE_NAME" "$INSTALL_DIR/$BIN_NAME"

if ! echo "$PATH" | grep -q "$INSTALL_DIR"; then
    SHELL_RC=""
    SHELL_NAME="$(basename "$SHELL")"
    if [ "$SHELL_NAME" = "zsh" ]; then
        SHELL_RC="$HOME/.zshrc"
    elif [ "$SHELL_NAME" = "bash" ]; then
        SHELL_RC="$HOME/.bashrc"
    else
        SHELL_RC="$HOME/.profile"
    fi

    if [ -n "$SHELL_RC" ] && [ -f "$SHELL_RC" ]; then
        if ! grep -q "$INSTALL_DIR" "$SHELL_RC" 2>/dev/null; then
            echo "" >> "$SHELL_RC"
            echo "# ASCHII" >> "$SHELL_RC"
            echo "export PATH=\"\$HOME/.local/bin:\$PATH\"" >> "$SHELL_RC"
            echo "Added $INSTALL_DIR to PATH in $SHELL_RC"
            echo "Run: source $SHELL_RC to update PATH"
        fi
    else
        echo "NOTE: Add '$INSTALL_DIR' to your PATH"
    fi
fi

echo ""
echo "ASCHII installed successfully!"
echo "Run 'aschii -m \"hello\"'"
echo "Run 'aschii' to start the TUI mode."