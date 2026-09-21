# Layover pilot: data dictionary and reproducibility

[Back to Part I](../../final-project-part-one.md)

## Provenance and permission to reuse

Source: Dillon Wong (2022), [Flight Prices](https://www.kaggle.com/datasets/dilwong/flightprices), version 1, licensed CC BY 4.0 according to the Kaggle listing. Original observations are Expedia listings. [Creator’s documentation](https://github.com/dilwong/FlightPrices). Modifications: a route/search-block extract, exact-endpoint and one-stop filters, a schedule identity rule, calculated duration/night fields, and summary tables. The analysis and diagrams are new work; attribution does not imply endorsement by the source creator or Expedia.

The source archive is about 5.9 GB compressed. The extraction read the first ZIP member sequentially, retained rows for BOS–LAX or LAX–BOS in its initial contiguous 2022-04-16 search-date block, and stopped at the first row for 2022-04-17. It scanned 87,657 rows in that first block and retained 1,392. Only about 6.3 MB of compressed input had to be read. The resulting departures span April 17–26. No claim is made that the initial block contains every April 16 listing in the entire archive. No random sampling or representativeness claim is made.

`source_bos_lax.csv` retains the original columns and selected source values; its own CSV line references are not full-archive line numbers. `source_csv_rows` counts the header as line 1. The extract is the working copy for this scoped project, not a preview that depends on unavailable full data.

## File inventory and grain

| File | Grain / purpose |
|---|---|
| source_bos_lax.csv | 1,392 selected raw flight-search listings; includes nonstops, multistops, and nearby-airport offers. |
| layovers_clean.csv | 828 unique two-leg schedule-and-carrier combinations with exact BOS/LAX endpoints. This is the recommended Tableau source. |
| hub_summary.csv | One row per direction group and connection airport. “All” overlaps BOS-LAX and LAX-BOS; never add these three groups together. |
| layover_histogram.csv | Nonoverlapping 60-minute bins; lower bound inclusive, upper bound exclusive. Counts sum to 828. |
| quality_checks.json | Filtering counts, invalid-for-scope source rows, date/size checks, and source checksum. |
| independent_checks.json | Recomputed durations, aggregate checks, and quantile reconciliation. |
| layover_analysis.ipynb | Portable standard-library notebook: read the extract, reproduce derived files, and independently verify key claims. |
| extraction.json | Download endpoint, archive member, stopping boundary, and row counts. |
| download_extract.py | Reproduce the bounded source extract from the public original archive. |

## Clean CSV fields

| Field | Type | Meaning |
|---|---|---|
| itinerary_id | String | First 16 hex characters of SHA-256 of date, requested endpoints, both segment epoch arrays, actual airport arrays, carrier codes, and cabin codes. Checked unique within this extract. |
| search_date | Date | Date the source captured the offer: 2022-04-16. |
| flight_date | Date | Starting departure date; April 17–26, 2022. |
| origin, destination | String | Actual and requested endpoint airport codes agree after filtering. |
| direction | String | BOS-LAX or LAX-BOS. |
| hub | String | Shared arrival airport of leg 1 / departure airport of leg 2. “Hub” here means connection airport in the itinerary. |
| inbound_carrier, outbound_carrier, carrier_pair | String | Reported airline codes by leg; carrier_pair preserves both rather than inventing one airline for a mixed itinerary. |
| cabin_pair | String | Reported cabin on both legs. All retained entries are coach / coach. |
| hub_arrival_local, hub_departure_local | ISO datetime string | Offset-aware local timestamps, including dates; retain the original offsets when displaying local clocks. |
| hub_arrival_epoch, hub_departure_epoch | Integer | Unix seconds for the two timestamps bounding the wait. |
| layover_minutes | Number | (hub_departure_epoch − hub_arrival_epoch) / 60. |
| night_overlap_minutes | Number | Duration overlapping 22:00–06:00 at the connection airport; a declared project convention, not a legal or medical definition. |
| crosses_local_midnight | Integer, 0/1 | Departure’s local date is later than arrival’s local date. |
| long_layover_6h | Integer, 0/1 | layover_minutes ≥ 360; editorial discussion threshold. |
| source_offer_count | Integer | Number of raw retained offers sharing this schedule signature; all equal 1 in the pilot. |
| source_csv_rows | String | Semicolon-separated line numbers in source_bos_lax.csv, including the header. |

Summary percentiles use linear interpolation between sorted observations at position (n−1)×q; p90 is descriptive spread, not a confidence interval. Means weight each retained schedule equally; do not average airport means to recover the overall mean. Use a count-weighted mean or calculate directly from the clean table. Night counts and six-hour counts can overlap and must not be added as exclusive categories.

## Scope and validation

Filtering: 1,392 raw = 372 nonstops + 15 multistops + 177 one-stop nearby-endpoint listings + 828 retained. The 177 endpoint exclusions reflect search-area expansion, not corrupt timestamps. All other relevant validation checks pass on the retained rows. No duplicate schedule signatures remain; there were none to remove after the scope filters. The earliest and latest layovers are 31 and 551 minutes, so no long-tail truncation was applied.

Epoch and local-offset values agree for every retained segment. Each arrival airport equals the next departure airport. Both physical legs have positive elapsed time, and their advertised segment durations reconcile to their timestamps. All retained hub arrival/departure offsets agree, so the local-clock overlap calculation does not cross an offset change in this extract. A future sample covering daylight-saving changes must use named airport timezones rather than assume a fixed offset.

The source does not include flight numbers, passenger counts, actual arrivals, hotel use, or guaranteed ticket/connection protection. Codeshares or distinct carrier combinations can describe similar physical schedules; the unit is therefore a listed schedule-and-carrier combination. A descriptive sensitivity view can group by time-and-airport signature alone, but cannot resolve physical-flight identity. This is not a random sample; inferential confidence intervals would not solve its selection bias. Date, direction, search lead time, and carrier composition can affect airport means.

## Reproduce

Open layover_analysis.ipynb from this folder and run it with Python 3. It uses only the standard library and the accompanying source CSV. Generated copies go into a new `reproduced` folder. The notebook verifies the published clean data and summaries against independently reconstructed values. To reacquire the original extract, run download_extract.py from a directory of your choice; it writes into `downloaded_extract/` and stops at the documented date boundary. Internet access is required only for that optional reacquisition step.

## Airport codes shown in the main sketch

DFW: Dallas/Fort Worth; ORD: Chicago O’Hare; IAD: Washington Dulles; JFK: New York John F. Kennedy; EWR: Newark Liberty; MSP: Minneapolis–Saint Paul; DEN: Denver; SLC: Salt Lake City; SFO: San Francisco. BOS: Boston Logan; LAX: Los Angeles International.
