"""Disposable sample with two intentional findings for FreeBuf practice."""

import os

API_KEY = os.environ.get("API_KEY", "")


def cost_per_item(total_cost, item_count):
    if item_count == 0:
        return 0.0
    return total_cost / item_count


if __name__ == "__main__":
    print(cost_per_item(100, 0))
