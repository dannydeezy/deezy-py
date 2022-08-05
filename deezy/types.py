# -*- coding: utf-8 -*-
# @Author: lnorb.com
# @Date:   2022-08-05 12:57:18
# @Last Modified by:   lnorb.com
# @Last Modified time: 2022-08-05 13:22:38


class Network:
    testnet = 0
    mainnet = 1


class SwapResponse:
    def __init__(self, bolt11_invoice: str, fee_sats: int):
        self.bolt11_invoice: str = bolt11_invoice
        self.fee_sats: int = fee_sats


class SwapInfo:
    def __init__(
        self,
        liquidity_fee_ppm: int,
        on_chain_bytes_estimate: int,
        max_swap_amount_sats: int,
        min_swap_amount_sats: int,
        available: bool,
    ):
        self.liquidity_fee_ppm: int = liquidity_fee_ppm
        self.on_chain_bytes_estimate: int = on_chain_bytes_estimate
        self.max_swap_amount_sats: int = max_swap_amount_sats
        self.min_swap_amount_sats: int = min_swap_amount_sats
        self.available: bool = available
