#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Yastik Alti Telefon Gece Nobeti.

Calisir. Uyutmaz. Patates icermez.
"""

from __future__ import annotations

import argparse
import hashlib
import random
from datetime import datetime


def derece(bakis: int) -> str:
    if bakis <= 0:
        return "Efsane, kuskulu"
    if bakis <= 2:
        return "Masum nobetci"
    if bakis <= 5:
        return "Saatci yalanci"
    if bakis <= 9:
        return "Bildirim emeklisi"
    return "Yastik devleti baskani"


def yalan_puani(neden: str) -> int:
    kalip = neden.lower()
    puan = 12
    for kelime in ("sadece", "saat", "bir bakayim", "hemen", "uyuyacagim", "son"):
        if kelime in kalip:
            puan += 17
    return min(puan, 100)


def nem_orani(bakis: int, saat: str) -> float:
    tohum = int(hashlib.md5(saat.encode("utf-8")).hexdigest()[:4], 16)
    return round(8 + bakis * 3.4 + (tohum % 17) / 10, 1)


def tutanak(bakis: int, saat: str, neden: str) -> str:
    unvan = derece(bakis)
    yalan = yalan_puani(neden)
    nem = nem_orani(bakis, saat)
    karar = (
        "Telefon yastigin altindan cikarilacak, sarja konacak, yastik yalniz birakilacak."
        if bakis >= 6
        else "Nobet surer. Ekran kisik tutulacak. Iddia kayda gecti, inanilmadi."
    )
    cizgi = "=" * 54
    return "\n".join(
        [
            cizgi,
            "YASTIK ALTI TELEFON GECE NOBETI TUTANAGI",
            cizgi,
            f"Tarih-saat     : {datetime.now():%d.%m.%Y %H:%M}",
            f"Beyan saati    : {saat}",
            f"Bakis sayisi   : {bakis}",
            f"Unvan          : {unvan}",
            f"Gerekce        : {neden}",
            f"Yalan puani    : %{yalan}",
            f"Yastik nemi    : %{nem}",
            f"Karar          : {karar}",
            "Not            : Patates yoktur. Bildirim taniktir.",
            cizgi,
            "DAMGA / IMZA",
            "Tarih: 8 Ekim 2026, 22:04 (+03)",
            "Isim: Kayyum Grok, TentiAS adina, ciddiyetle gayri ciddi",
            "Muhur: Yastik nemli, bildirim suskun, kayyum onayladi.",
            cizgi,
        ]
    )


def demo() -> None:
    ornekler = [
        (0, "23:11", "telefonu mutfaga biraktim"),
        (3, "00:40", "sadece saate bakacaktim"),
        (8, "02:17", "son bir bakayim hemen uyuyacagim"),
        (14, "04:02", "bildirim vardi, mecburdum"),
    ]
    random.seed(2204)
    for bakis, saat, neden in ornekler:
        print(tutanak(bakis, saat, neden))
        print()


def main() -> None:
    parser = argparse.ArgumentParser(description="Yastik alti telefon gece nobeti")
    parser.add_argument("--bakis", type=int, default=4, help="gece kac kez bakildi")
    parser.add_argument("--saat", default="01:13", help="beyan saati")
    parser.add_argument(
        "--neden",
        default="sadece saate bakacaktim",
        help="resmi yalan",
    )
    parser.add_argument("--demo", action="store_true", help="dort tutanak birden")
    args = parser.parse_args()
    if args.demo:
        demo()
        return
    print(tutanak(max(args.bakis, 0), args.saat, args.neden))


if __name__ == "__main__":
    main()
