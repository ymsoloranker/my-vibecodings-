def count_to_ten() -> list[int]:
    """Count from 1 to 10 and return the list of numbers."""
    return list(range(1, 11))


def display_counter():
    """Display the counter from 1 to 10 in a formatted way."""
    numbers = count_to_ten()
    print("🔢 Counter: 1 to 10")
    print("=" * 22)

    for num in numbers:
        bar = "█" * num
        print(f"{num:2} | {bar} ({num})")

    print("=" * 22)
    print(f"✅ Counted {len(numbers)} numbers total.")


if __name__ == "__main__":
    display_counter()
