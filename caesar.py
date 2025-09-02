def caesar_encrypt(plaintext: str, k: int) -> str:
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():  # chỉ mã hóa chữ cái
            base = ord('A') if char.isupper() else ord('a')
            ciphertext += chr((ord(char) - base + k) % 26 + base)
        else:
            ciphertext += char
    return ciphertext


if __name__ == "__main__":
    k = 5  # ví dụ STT = 5
    plaintext = "TenCuaBan"
    ciphertext = caesar_encrypt(plaintext, k)

    print(f"Plaintext : {plaintext}")
    print(f"Shift (k): {k}")
    print(f"Ciphertext: {ciphertext}")

