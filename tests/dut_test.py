import cocotb
from cocotb.triggers import Timer
from cocotb_coverage.coverage import coverage_db, CoverCross, CoverPoint
import numpy as np

bits = 8


@CoverPoint("top.a", xf=lambda x, y: x, bins=list(range((2**bits - 1))))
@CoverPoint("top.b", xf=lambda x, y: y, bins=list(range((2**bits - 1))))
@CoverCross("top.cross.ab", items=["top.a", "top.b"])
def cover(a, b):
    pass


@cocotb.test()
async def dut_test(dut):
    a = [10, 2, 3]
    b = [21, 1, 3]
    for i, j in zip(a, b):
        dut.a.value = i
        dut.b.value = j
        cover(i, j)
        await Timer(1, "ns")
    coverage_db.report_coverage(cocotb.log.info)
