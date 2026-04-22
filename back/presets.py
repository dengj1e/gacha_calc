"""
constants

"""
from app.schemas import BannerPreset


PRESETS: list[BannerPreset] = [
    BannerPreset(
        id="genshin",
        name="Character Event Banner",
        game="Genshin Impact",
        base_rate=0.006,
        soft_pity=74,
        hard_pity=90,
        rate_increase=0.06,
        use_pity=True,
    ),
    BannerPreset(
        id="hsr",
        name="Character Event Warp",
        game="Honkai: Star Rail",
        base_rate=0.006,
        soft_pity=74,
        hard_pity=90,
        rate_increase=0.06,
        use_pity=True,
    ),
    BannerPreset(
        id="wuwa",
        name="Featured Resonator Convene",
        game="Wuthering Waves",
        base_rate=0.008,
        soft_pity=66,
        hard_pity=80,
        rate_increase=0.06,
        use_pity=True,
    ),
    BannerPreset(
        id="zzz",
        name="Exclusive Channel",
        game="Zenless Zone Zero",
        base_rate=0.006,
        soft_pity=74,
        hard_pity=90,
        rate_increase=0.06,
        use_pity=True,
    ),
    BannerPreset(
        id="no-pity",
        name="Pure RNG (no pity)",
        game="Generic",
        base_rate=0.006,
        soft_pity=90,
        hard_pity=90,
        rate_increase=0.0,
        use_pity=False,
    ),
]


PRESETS_BY_ID = {p.id: p for p in PRESETS}