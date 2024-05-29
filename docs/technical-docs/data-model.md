---
title: Data Model
parent: Technical Docs
nav_order: 3
---

{: .label }
He Wang

# Data Model

User (#UserID, #mail, password)<br>
Vehicle(#UserID, PlateNR)<br>
Role(#UserID, role)<br>
ParkingLot(#ParkinLotID, ParkingLotName)<br>
ParkingSpace(#ParkingLotID, #ParkingSpaceID, width, length, restrictions)<br>
Booking(#UserID, #ParkingLotID, timeStart, timeEnd)<br>

