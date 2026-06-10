from rich.console import Console
from rich.panel import Panel

console = Console()


def decrypt_rail_fence(ciphertext, rails):
    if rails <= 1:
        return ciphertext

    length = len(ciphertext)
    rail = [["\n" for _ in range(length)] for _ in range(rails)]
    row, col = 0, 0
    dir_down = 1

    for i in range(length):
        rail[row][col] = "*"
        col += 1
        row += dir_down

        if row == 0 or row == rails - 1:
            dir_down *= -1

    index = 0
    for i in range(rails):
        for j in range(length):
            if rail[i][j] == "*" and index < length:
                rail[i][j] = ciphertext[index]
                index += 1

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
    console.print("\n[bold green]--- Brute Force Results ---[/bold green]\n")
    for rails in range(2, len(ciphertext)):
        decrypted = decrypt_rail_fence(ciphertext, rails)
        console.print(f"Rails = {rails} → {decrypted}")


if __name__ == "__main__":
    console.print(
        Panel.fit(
            "[bold cyan]🚆 Rail Fence Cipher Brute Force[/bold cyan]",
            border_style="cyan",
        )
    )
    cipher = console.input("\n[bold yellow]Enter ciphertext:[/bold yellow] ").replace(
        " ", ""
    )
    brute_force_rail_fence(cipher)
