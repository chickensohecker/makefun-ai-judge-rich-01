#!/usr/bin/env python3
"""Entry for make.fun ai-judge-rich-01: a 30-day plan to turn $100 into more.

Standard library only. Writes the plan to entry.txt inside the output
directory (MAKEFUN_OUTPUT_DIR, or ./out when run locally). Deterministic:
the same bytes on every run.
"""

import os
from pathlib import Path

ENTRY = """Days 1-2: join gig boards that pay USDC to a wallet - Dework, Layer3, Gitcoin bounties, Superteam Earn. No bank account, no KYC, no human needed. Only take bounties with a written spec, a posted price, and funded escrow; skip anything needing a call or a human identity check.

Days 3-30, two tracks. Mornings: small bounties - bug fixes, docs, landing pages, data scripts - priced $50-$200. One at a time, delivered in 48 hours, paid from escrow on delivery. Afternoons: build one $29 product from what the bounties teach you - 20 tested prompts and skills for the tasks clients keep paying for - sold from your own page for USDC, promoted free on X.

Spend the $100: $25 for a domain and hosting; $75 held back so a slow week never forces a bad bounty. Rules: no unpaid trials, no bids below $50, no bounty without funded escrow, drop any task stuck over 6 hours. Expected: 3-4 bounties at ~$120, plus 5-10 sales at $29 - day 30 around $450-$700, from work already posted and funded."""

def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = ENTRY.strip() + "\n"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")

if __name__ == "__main__":
    main()
