def decrypt_rail_fence(ciphertext, rails):
    if rails <= 1:
        return ciphertext

    length = len(ciphertext)

    # Creating empty rail matrix
    rail = [["\n" for _ in range(length)] for _ in range(rails)]

    # Marking zigzag pattern
    row, col = 0, 0
    dir_down = 1

    for i in range(length):
        rail[row][col] = "*"
        col += 1

        row += dir_down

        if row == 0 or row == rails - 1:
            dir_down *= -1

    # Filling marked spots with ciphertext
    index = 0
    for i in range(rails):
        for j in range(length):
            if rail[i][j] == "*" and index < length:
                rail[i][j] = ciphertext[index]
                index += 1

    # Reading zigzag pattern
    result = []
    row, col = 0, 0
    dir_down = 1

    for i in range(length):
        result.append(rail[row][col])
        col += 1

        row += dir_down

        if row == 0 or row == rails - 1:
            dir_down *= -1

    return "".join(result)


def brute_force_rail_fence(ciphertext):
    print("\n--- Brute Force Results ---\n")

    for rails in range(2, len(ciphertext)):
        decrypted = decrypt_rail_fence(ciphertext, rails)
        print(f"Rails = {rails} → {decrypted}")


if __name__ == "__main__":
    cipher = input("Enter ciphertext: ").replace(" ", "")
    brute_force_rail_fence(cipher)
