# Exercise 02: Study of Network cables

**[Open this exercise record PDF](CN_Exercise_02.pdf)**

## Aim

To understand network cable types and make straight-through and cross-wired cables using a crimping tool.

## Requirements

UTP Cat5e cable, two RJ45 connectors, stripper/cutter, crimping tool, optional plug boots and cable tester.

## Procedure / algorithm

1. Identify UTP, STP/SSTP, coaxial and fibre-optic cables. UTP is low cost; shielding reduces EMI; coaxial is used in cable networks; fibre offers high bandwidth and long reach.
2. Cut the required cable length, slide on boots and strip about 1.5 cm of jacket without cutting the conductors.
3. Arrange all eight wires in T568A or T568B order using pinout.csv. View pins 1-8 with contacts facing you and clip facing away.
4. Trim conductors evenly and insert them fully into the RJ45 plug. The jacket must enter the strain relief.
5. Crimp both ends. Use A-A or B-B for straight-through, and A-B for a crossover.
6. Test continuity and pin mapping. Connect appropriate devices and check the link indicator. Record the actual cable category and any faulty crimps.

## Complete source / configuration files

### [pinout.csv](pinout.csv)

```text

pin,T568A,T568B
1,White/Green,White/Orange
2,Green,Orange
3,White/Orange,White/Green
4,Blue,Blue
5,White/Blue,White/Blue
6,Orange,Green
7,White/Brown,White/Brown
8,Brown,Brown

```

### [wiring.txt](wiring.txt)

```text

Straight-through: T568A-T568A or T568B-T568B.
Crossover: T568A-T568B. Pin mappings: 1-3, 2-6, 3-1, 6-2, 4-4, 5-5, 7-7, 8-8.
PC-switch: straight-through. Legacy PC-PC: crossover. Auto-MDI/MDIX ports may accept either.
Read pins 1-8 with contacts facing you and clip facing away.

```

## Actual output / verification

Not executed in the required lab/tool environment. No actual operational output is claimed.

## Expected output

Straight-through tester maps pins 1-8 identically. Crossover maps 1-3, 2-6, 3-1, 6-2; other pins match. A correctly terminated cable gives a working link.

## Observations

Straight-through cables conventionally connect PC-to-switch. Crossover swaps pairs 1/2 with 3/6 for older like-device links. Auto-MDI/MDIX may accept either. Fibre distance and speed depend on the fibre/transceiver; the manual's blanket 100 m limit is not used.

## Result

Cable types, standards, pinouts and testing procedure are documented. Physical crimping and tester observations have not been performed here.
