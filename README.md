Jimat-dan-SENang-Kira
=====================

Jimat-dan-SENang-Kira is Python implementation of Malaysia's over-the-counter payment rounding mechanism.

What is "Jimat dan SENang Kira"
===============================

Bank Negara Malaysia(BNM) introduced a Rounding Mechanism to the nearest multiple of 5 sen for the over-the-counter
payments and was fully implemented by 1st April 2008.

The Rounding Mechanism only applies to the total amount of a bill and not on individual items. In the Rounding Mechanism
exercise, the total amount of a bill which ends in 1, 2, 6 and 7 sen will be rounded down while the total bill which
ends in 3, 4, 8 and 9 sen will be rounded up to the nearest multiple of 5 sen.

The implementation of the Rounding Mechanism brings benefits to both businesses and customers. Businesses will be able
to save on handling costs and for customers, it will make payment faster and more convenient.

The table below illustrates how the Rounding Mechanism works:

                -----------------------------------------------------------------------------------------
                | Bill end in sen | Round off to the nearest |               Total amount               |
                |                 |           5 sen          |----------------------------------------- |
                |                 |                          | Total amount before | Total amount after |
                |                 |                          |       rounding      |      rounding      |
                -----------------------------------------------------------------------------------------
                |      1, 2       |           Down           |         82.01       |        82.00       |
                |                 |                          |         82.02       |        82.00       |
                |---------------------------------------------------------------------------------------|
                |      3, 4       |            Up            |         82.03       |        82.05       |
                |                 |                          |         82.04       |        82.05       |
                |---------------------------------------------------------------------------------------|
                |      6, 7       |           Down           |         82.06       |        82.05       |
                |                 |                          |         82.07       |        82.05       |
                |---------------------------------------------------------------------------------------|
                |      8, 9       |            Up            |         82.08       |        82.10       |
                |                 |                          |         82.09       |        82.10       |
                -----------------------------------------------------------------------------------------

Example
=======

In [4]: from jimat_senang_kira import round

In [5]: round(89.01)
Out[5]: Decimal('89.00')

In [6]: round(89.04)
Out[6]: Decimal('89.05')

In [7]: round(89.05)
Out[7]: Decimal('89.05')

In [8]: round(89.09)
Out[8]: Decimal('89.10')