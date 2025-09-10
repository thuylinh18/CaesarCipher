def caesar_encrypt(plaintext, k):
    result = ""
    shift = k % 26  # để chắc chắn không bị vượt bảng chữ cái
    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

if __name__ == "__main__":
    k = 31
    plaintext = "NguyenThuyLinh"
    ciphertext = caesar_encrypt(plaintext, k)
    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)
