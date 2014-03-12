Jimat-dan-SENang-Kira
=====================

Jimat-dan-SENang-Kira is Python implementation of Malaysia's over-the-counter payment rounding mechanism.

What is "Jimat dan SENang Kira"
-------------------------------

Bank Negara Malaysia(BNM) introduced a Rounding Mechanism to the nearest multiple of 5 sen for the over-the-counter
payments and was fully implemented by 1st April 2008.

The Rounding Mechanism only applies to the total amount of a bill and not on individual items. In the Rounding Mechanism
exercise, the total amount of a bill which ends in 1, 2, 6 and 7 sen will be rounded down while the total bill which
ends in 3, 4, 8 and 9 sen will be rounded up to the nearest multiple of 5 sen.

The implementation of the Rounding Mechanism brings benefits to both businesses and customers. Businesses will be able
to save on handling costs and for customers, it will make payment faster and more convenient.

The table below illustrates how the Rounding Mechanism works:

<table>
  <tr align="center">
    <td rowspan="2">Bill end in sen</td>
    <td rowspan="2">Round off to the nearest 5 sen</td>
    <td colspan="2">Total</td>
  </tr>
  <tr align="center">
    <td>Total amount before rounding</td>
    <td>Total amount after rounding</td>
  </tr>
  <tr align="center">
    <td rowspan="2">1, 2</td>
    <td rowspan="2">Down</td>
    <td>82.01</td>
    <td>82.00</td>
  </tr>
  <tr align="center">
    <td>82.02</td>
    <td>82.00</td>
  </tr>
  <tr align="center">
    <td rowspan="2">3, 4</td>
    <td rowspan="2">Up</td>
    <td>82.03</td>
    <td>82.05</td>
  </tr>
  <tr align="center">
    <td>82.04</td>
    <td>82.05</td>
  </tr>
  <tr align="center">
    <td rowspan="2">6, 7</td>
    <td rowspan="2">Down</td>
    <td>82.06</td>
    <td>82.05</td>
  </tr>
  <tr align="center">
    <td>82.07</td>
    <td>82.05</td>
  </tr>
  <tr align="center">
    <td rowspan="2">8, 9</td>
    <td rowspan="2">Up</td>
    <td>82.08</td>
    <td>82.10</td>
  </tr>
  <tr align="center">
    <td>82.09</td>
    <td>82.10</td>
  </tr>
</table>

Example
=======

    >> from jimat_senang_kira import round

    >> round(89.01)
    Decimal('89.00')

    >> round(89.04)
    Decimal('89.05')

    >> round(89.05)
    Decimal('89.05')

    >> round(89.09)
    Decimal('89.10')
