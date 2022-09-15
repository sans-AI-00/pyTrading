import MetaTrader5 as mt5

mt5.market_book_release(
   'SYMBOL'      # financial instrument name
)

"""
symbol

[in]  Financial instrument name. Required unnamed parameter.

Return Value

True if successful, otherwise – False.

Note

The function is similar to MarketBookRelease.
"""