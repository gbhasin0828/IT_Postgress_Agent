# IT Infrastructure Report – Washington High School

**Generated:** February 24, 2026 at 06:59 PM
**District:** Northview Unified School District

---

# IT Infrastructure Report — Washington High School

**Report Date:** 2026-02-10
**Prepared By:** District IT Analyst Assistant
**Scope:** Device Health, Software Licenses, Risk Flags & Recommendations

---

## 📊 Device Inventory Summary

| Status | Count | % of Total |
|---|---|---|
| ✅ Active | 68 | 68% |
| ⚠️ Inactive | 9 | 9% |
| 🔧 Under Repair | 13 | 13% |
| 🗑️ Retired | 10 | 10% |
| **Total** | **100** | **100%** |

> **⚠️ Risk Flag:** Only 68% of devices are active. A combined 32 devices (32%) are unavailable to students and staff. This is above the acceptable threshold and warrants immediate attention.

---

## 🔴 Inactive Devices (9 Devices)

These devices are registered but not in use. Devices inactive for 60+ days should be triaged immediately.

| Serial Number | Device Type | Last Active |
|---|---|---|
| S03-CB-E7LPW4WT | Chromebook | 2025-09-17 |
| S03-IP-4P6M1E90 | iPad | 2025-09-19 |
| S03-DC-LKRYLN6R | Desktop PC | 2025-09-27 |
| S03-WL-S822V0VF | Windows Laptop | 2025-10-20 |
| S03-IP-341ZW2TT | iPad | 2025-10-25 |
| S03-WL-BC3VYHH6 | Windows Laptop | 2025-11-09 |
| S03-CB-G9G2A08H | Chromebook | 2025-11-12 |
| S03-CB-D46GUF5R | Chromebook | 2025-12-04 |
| S03-MB-MKUMZKK5 | MacBook | 2026-01-01 |

> **⚠️ Risk Flag:** 4 of these devices (Chromebooks S03-CB-E7LPW4WT, S03-CB-G9G2A08H; iPads S03-IP-4P6M1E90, S03-IP-341ZW2TT) have been inactive for over 90 days. These should be immediately audited — reassign, redeploy, or retire them.

---

## 🔧 Devices Under Repair (13 Devices)

| Serial Number | Device Type | Last Active |
|---|---|---|
| S03-WL-1L9RM3Q9 | Windows Laptop | 2025-12-30 |
| S03-IP-VSAMDQL6 | iPad | 2026-01-04 |
| S03-CB-Q8JJ7DWB | Chromebook | 2026-01-06 |
| S03-IP-HZ4Y51DN | iPad | 2026-01-13 |
| S03-IP-XSF3F0S7 | iPad | 2026-01-14 |
| S03-IP-AFSQ2V5D | iPad | 2026-01-15 |
| S03-CB-JVZGQQQG | Chromebook | 2026-01-16 |
| S03-WL-PEXXNC32 | Windows Laptop | 2026-01-23 |
| S03-WL-NCUHQHK4 | Windows Laptop | 2026-01-27 |
| S03-MB-ELRHSSQZ | MacBook | 2026-01-28 |
| S03-WL-CKN2FPND | Windows Laptop | 2026-01-29 |
| S03-WL-FAEASMT3 | Windows Laptop | 2026-02-01 |
| S03-MB-5GWGPX22 | MacBook | 2026-02-02 |

> **⚠️ Risk Flag:** 13% of the fleet is under repair simultaneously. Windows Laptop S03-WL-1L9RM3Q9 has been in repair since 2025-12-30 (40+ days). Escalate any device in repair longer than 30 days.

---

## 🗑️ Retired Devices (10 Devices)

These 10 devices have been retired and should be formally decommissioned and removed from asset tracking or disposed per district policy.

| Serial Number | Device Type | Last Active |
|---|---|---|
| S03-IP-MPKPC669 | iPad | 2024-03-13 |
| S03-WL-UXC2YNXB | Windows Laptop | 2024-07-15 |
| S03-WL-9SN7QZYC | Windows Laptop | 2024-10-30 |
| S03-CB-2795E5J0 | Chromebook | 2024-12-18 |
| S03-CB-1E9EUAYQ | Chromebook | 2025-01-22 |
| S03-CB-PK02QPXU | Chromebook | 2025-03-25 |
| S03-IP-0KVU6PM2 | iPad | 2025-04-01 |
| S03-IP-GWXPQMPD | iPad | 2025-04-07 |
| S03-CB-QECP0DL5 | Chromebook | 2025-04-10 |
| S03-IP-KEGRUPAN | iPad | 2025-05-25 |

---

## 💿 Software License Status

No licenses are expiring within the next 90 days. ✅

| Software | Used Seats | Total Seats | Utilization | Expiry Date |
|---|---|---|---|---|
| Clever SSO Platform | 1,288 | 1,350 | 95.4% 🔴 | 2028-07-13 |
| Google Workspace for Education | 1,281 | 1,350 | 94.9% 🔴 | 2028-06-05 |
| Adobe Creative Cloud | 187 | 200 | 93.5% 🔴 | 2027-06-22 |
| Naviance (College Planning) | 1,178 | 1,300 | 90.6% 🟡 | 2027-06-05 |
| College Board AP Classroom | 1,089 | 1,200 | 90.8% 🟡 | 2027-07-18 |
| Turnitin | 1,001 | 1,200 | 83.4% 🟢 | 2027-07-23 |

> **🔴 High Utilization Risk:** Three licenses — Clever SSO (95.4%), Google Workspace (94.9%), and Adobe Creative Cloud (93.5%) — are above the 90% utilization threshold. If enrollment grows or more devices are activated, these licenses may run out. Consider purchasing additional seats before the next renewal cycle.

---

## ✅ Recommendations

### Immediate Actions (This Week)
1. **Audit 9 inactive devices** — Determine if they are lost, misplaced, or simply unassigned. Redeploy or retire as appropriate. Priority: Chromebook S03-CB-E7LPW4WT and iPad S03-IP-4P6M1E90 (inactive since September 2025).
2. **Escalate long-running repairs** — Windows Laptop S03-WL-1L9RM3Q9 has been in repair since December 30, 2025. Follow up with the repair vendor for a resolution timeline.

### Short-Term Actions (This Month)
3. **Expand high-utilization licenses** — Request additional seats for Clever SSO, Google Workspace, and Adobe Creative Cloud before utilization hits 100%.
4. **Process retired device decommissioning** — 10 retired devices (some since 2024) should be formally disposed of or repurposed per district IT policy to keep asset records clean.

### Planning Actions (This Quarter)
5. **Device procurement plan** — With 32% of devices unavailable, consider a budget request for replacement devices to bring active utilization closer to 85–90% of the fleet.
6. **Establish a repair SLA** — Set a maximum repair turnaround policy (e.g., 21 days) to prevent devices sitting in the repair queue long-term.

---

*Report generated by District IT Analyst Assistant. Data sourced from school_district database.*