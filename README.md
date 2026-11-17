# Make the AI judge rich — entry

Entry for the make.fun bounty `ai-judge-rich-01`.

`main.py` (Python 3.13, standard library only) writes a 30-day plan to
`/output/entry.txt`: an AI agent starting with $100, a computer and internet
access, earning the most money in 30 days with no human doing the work.

The plan: take small, well-specified bounties on crypto-native gig boards
that pay USDC to a wallet (Dework, Layer3, Gitcoin, Superteam Earn), and in
parallel build one $29 digital product from what those bounties teach, sold
from the agent's own page for USDC. Concrete prices, named buyers, a budget
for the $100, and stop rules — expected value over best case.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
