# Tableau design specification: The Architecture of a Layover

[Back to Part I](../../final-project-part-one.md)

This is an advisory build plan, not a published Tableau workbook. The source schema and pilot rows were inspected locally; no connected Tableau site was queried. The four sketches are original planning artifacts and use real pilot values.

## Brief and priorities

Audience: occasional travelers. Context: embedded charts within a guided Shorthand story. Decision: understand a scheduled average, examine variability, and inspect an individual connection’s local timing. Desktop target: approximately 1,000 px embed width; phone target: 375–430 px with a separately designed Tableau phone layout. Data: layovers_clean.csv, 828 itinerary-grain records.

| Priority / question | Fields and aggregation | View / evidence status |
|---|---|---|
| 1. Where do average waits differ? | hub; AVG(layover_minutes); COUNTD(itinerary_id); direction/date/carrier filters | Zero-based horizontal bars, ordered by mean. Supported for the pilot only. |
| 2. What does the mean hide? | layover_minutes; count per 60-minute bin; MEDIAN(layover_minutes) | Histogram with mean/median narrative. Supported. |
| 3. Which waits reach the night? | hub_arrival_local; hub_departure_local; night_overlap_minutes; crosses_local_midnight | Itinerary timeline and labeled detail table. Supported timing, unverified hotel need. |
| 4. What hotel is needed or included? | Hotel use, personal needs, fare eligibility, entry conditions | No numerical verdict. Required itinerary-level fields are absent. Link to full policy context if used. |

## Metric hierarchy and definitions

Lead with mean scheduled layover (whole minutes), paired with median (whole minutes) and itinerary count. These describe the selected subset and have no target or universally favorable direction: a shorter connection can be harder to make. Secondary measures: count and share at least six hours; count crossing midnight. Always show denominators. Do not label either as a passenger probability or hotel-need rate. The six-hour and 22:00–06:00 definitions are project conventions.

## Layout and controls

Use tiled containers: title and scope (~15% height), comparison (~65%), definitions and data link (~20%). Within the comparison module, use approximately 70% width for the bar chart and 30% for the selected airport’s count, median, and source note. Keep the histogram and timeline in later story sections rather than competing on the first screen.

Direction selector: All (default), BOS-LAX, LAX-BOS; applies to all comparison/distribution sheets. Departure-date range defaults to the ten pilot dates; carrier-pair selector defaults to All. Provide Reset to full pilot and visibly state active filters. Keep controls collapsed under “Explore this sample” on phones; retain a direction control beside the chart. No filters should change the static opening claim without updating its value and scope together; either bind the opening to filters or label it “full pilot.”

Airport action: select a bar → filter the airport detail histogram and itinerary table; clearing → restore all airports within current controls. Timeline action: select an itinerary table row → show that record’s arrival and onward departure; clearing → return to the explicitly labeled initial example. Provide table/select controls for touch and keyboard access; essential facts must remain visible without hover. An empty selection shows “No itineraries match these filters” and a reset action, never a zero-minute average.

The initial static bar sketch shows n ≥ 30. In the interactive comparison, preserve all airports under filtering, add “small group” labels for n < 30, and offer a clearly labeled display toggle rather than silently dropping groups. The threshold is not statistical significance. Tooltip order: airport name/code, direction/date scope, mean, median, n, source date. Do not imply that the combined mean controls for direction or airline mix.

## Sheets and calculation guidance

Connect the clean CSV as an extract for this fixed historical project. Treat itinerary_id, airport codes, and carrier codes as dimensions; parse flight_date as a date. Preserve the offset-aware local timestamps as source strings for display; do not let an automatic conversion replace the hub’s local clock with the computer’s timezone. Use the precomputed layover_minutes for plotting and independently check it against (hub_departure_epoch − hub_arrival_epoch)/60.0.

Suggested sheets: “Airport mean”, “Wait distribution”, “Itinerary detail”, and “Local clock”. At this observed one-row-per-itinerary grain, AVG([layover_minutes]), MEDIAN([layover_minutes]), COUNTD([itinerary_id]), and AVG([long_layover_6h]) have the intended meanings. These are formula specifications to validate in Tableau, not claims of a built workbook. Use the raw clean table for filters and aggregations; do not join hub_summary.csv to it and multiply observations. No table calculation is needed for the core average.

Build the local-clock sheet from date-qualified local timestamps or explicitly prepared wall-clock offsets. Preserve next-day labels and the correct local dates. The night interval is a reference band, not measured sleep. Avoid interpreting the 21 midnight-crossing itineraries as 21 people or 21 hotel stays.

## Visual system and responsive behavior

Use a near-white background (#FAF8F2), dark text (#152F40), blue (#22577A) for general observations, and amber (#A65F00) for long-wait/night emphasis. Pair colors with labels; no red/green eligibility coding. Use Arial or a tested available sans-serif. Target title 24–30 px, body and direct labels at least 16 px in the final embed, and visibly larger lead metrics. Text/background contrast must be checked in the rendered final implementation, including selection and focus states; palette choice alone does not establish accessibility.

On phones, stack summary and chart; show the full airport list vertically rather than shrinking labels; move detailed provenance below the chart. Split the two timelines into stacked cards while retaining local times, next-day labels, and the source row. Keep narrative, counts, and meaning intact. The HTML wireframe is nonfunctional and does not demonstrate these Tableau behaviors.

## Verification and open questions

Before publishing the later final story: reconcile mean 137.927536... and median 96 on all 828 rows; reconcile direction counts 383/445; check all filters update counts and values; test reset and empty states; verify the two example timelines against source rows 1070 and 40; check mobile readability, keyboard/touch access, and live embed loading. Recompute any statistics after changing scope. The pilot cannot verify international averages, actual passenger waits, hotel use, current schedules, or October–November seasonality. If those become core claims, new comparable source data is required; omit those charts until that evidence exists.
