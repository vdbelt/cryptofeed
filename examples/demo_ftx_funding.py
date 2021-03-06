'''
Copyright (C) 2017-2020  Bryant Moscon - bmoscon@gmail.com

Please see the LICENSE file for the terms and conditions
associated with this software.
'''

from cryptofeed.callback import FundingCallback
from cryptofeed import FeedHandler
from cryptofeed.exchanges import FTX
from cryptofeed.defines import FUNDING


# Examples of some handlers for different updates. These currently don't do much.
# Handlers should conform to the patterns/signatures in callback.py
# Handlers can be normal methods/functions or async. The feedhandler is paused
# while the callbacks are being handled (unless they in turn await other functions or I/O)
# so they should be as lightweight as possible

async def funding(**kwargs):
    print(f"Funding Update for {kwargs['feed']}")
    print(kwargs)


def main():
    f = FeedHandler()
    f.add_feed(FTX(pairs=['BTC-PERP', 'THETA-PERP'], channels=[FUNDING], callbacks={FUNDING: FundingCallback(funding)}))
    f.run()


if __name__ == '__main__':
    main()
