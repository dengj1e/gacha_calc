import random

GAME_CONFIG = {
    "genshin": {"pull_cost": 160, "soft_pity": 74, "hard_pity": 90, "base_rate": 0.006, "soft_rate_inc": 0.06},
    "hsr":     {"pull_cost": 160, "soft_pity": 74, "hard_pity": 90, "base_rate": 0.006, "soft_rate_inc": 0.06},
    "zzz":     {"pull_cost": 160, "soft_pity": 74, "hard_pity": 90, "base_rate": 0.006, "soft_rate_inc": 0.06},
}

def get_pull_rate(pull_number, cfg):
    if pull_number >= cfg["hard_pity"]: return 1.0
    if pull_number >= cfg["soft_pity"]:
        extra = (pull_number - cfg["soft_pity"] + 1) * cfg["soft_rate_inc"]
        return min(1.0, cfg["base_rate"] + extra)
    return cfg["base_rate"]

def run_simulation(cfg, current_pity, guaranteed, total_pulls, desired_copies, iterations=80_000):
    successes = 0
    for _ in range(iterations):
        pity, is_guaranteed, copies, left = current_pity, guaranteed, 0, total_pulls
        while left > 0 and copies < desired_copies:
            pity += 1
            if random.random() < get_pull_rate(pity, cfg):
                if is_guaranteed or random.random() < 0.5:
                    copies += 1; is_guaranteed = False
                else:
                    is_guaranteed = True
                pity = 0
            left -= 1
        if copies >= desired_copies: successes += 1
    return successes / iterations

def get_expected_pulls(cfg, current_pity, guaranteed, iterations=20_000):
    total = 0
    for _ in range(iterations):
        pity, is_guaranteed, count = current_pity, guaranteed, 0
        while True:
            pity += 1; count += 1
            if random.random() < get_pull_rate(pity, cfg):
                if is_guaranteed or random.random() < 0.5: break
                else: is_guaranteed = True; pity = 0
        total += count
    return round(total / iterations)