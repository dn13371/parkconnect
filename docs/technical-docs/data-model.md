---
title: Data Model
parent: Technical Docs
nav_order: 3
---

{: .label }
He Wang

# Data Model

User (#UserID, #mail, password)
Vehicle(#UserID, PlateNR)
Role(#UserID, role)
ParkingLot(#ParkinLotID, ParkingLotName)
ParkingSpace(#ParkingLotID, #ParkingSpaceID, width, length, restrictions)
Booking(#UserID, #ParkingLotID, timeStart, timeEnd)

