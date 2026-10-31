"""Split a total safely between a non-negative number of people."""

def calculate_share(total: float, people: float) -> float:
    if people < 0:
        raise ValueError("people must be zero or greater")
    if people == 0:
        return 0.0
    return total / people


if __name__ == "__main__":
    print(f"Each person pays: {calculate_share(120, 0):.2f}")
