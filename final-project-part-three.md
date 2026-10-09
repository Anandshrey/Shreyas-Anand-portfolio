| [Portfolio](https://anandshrey.github.io/Shreyas-Anand-portfolio/) | [Part I](https://anandshrey.github.io/Shreyas-Anand-portfolio/final-project-part-one) | [Part II](https://anandshrey.github.io/Shreyas-Anand-portfolio/final-project-part-two) | [Part III](https://anandshrey.github.io/Shreyas-Anand-portfolio/final-project-part-three) |

# The Architecture of a Layover: Part III

**Shreyas Anand · Telling Stories with Data**

## The story and the decision

The [final public Shorthand story](https://carnegiemellon.shorthandstories.com/layover-architecture-part-two/index.html) is published with the Part III narrative and charts. The existing address is retained so earlier links continue to work. The [Part III Tableau workbook](https://public.tableau.com/app/profile/shreyas.anand4069/viz/Project-Part-III-Layover-Story-REPAIRED/LAX-BOSPlanningReview?publish=yes) contains the updated visual evidence.

The final story asks one question of a route planning analyst: **Which Los Angeles to Boston connection bank should be reviewed first?** It does not ask a traveler to avoid a hub. In this historical sample, Denver's long wait connections are the strongest candidate for investigation. The action is to inspect the relevant arrival and departure banks, then check a broader schedule period and operating data before proposing a change.

## How the project changed

[Part I](final-project-part-one.md) began with the average scheduled layover and showed why a connection is a meaningful part of a journey. [Part II](final-project-part-two.md) added direction, night timing, a geographic view, and three classmate interviews. The Part II feedback identified the main weakness: the visuals supplied evidence, but the reader still lacked a clear narrative and call to action. I changed the structure from a tour of metrics to a planner's decision, using one direction and two hubs as the worked example.

The interview findings shaped that choice. Participants understood the mean versus median histogram, but questioned an airport ranking based on the mean alone, unfamiliar codes, small groups, and a night measure that counted a few minutes the same as several hours. I now spell out airport names, show the number of listings, define the 90th percentile in plain language, and pair night window counts with minutes of overlap. The eye catching San Francisco westbound result is not the lead because that group has only eight listings. The persona is a route-planning analyst preparing a schedule review: they need a defensible shortlist and the evidence needed to test it, not a claim about the best airport.

## What the final comparison shows

The source is a bounded extract of Dillon Wong's 2022 *Flight Prices* listings. After exact-endpoint and one-stop checks, it contains **828 distinct advertised schedule-and-carrier combinations** for Boston Logan and Los Angeles International in both directions, departing **April 17 to 26, 2022**. The overall mean scheduled wait is **138 minutes** and the median is **96 minutes**; **54 listings** have waits of at least six hours. Those figures motivate the direction-specific comparison rather than replacing it.

| Los Angeles → Boston | Denver | Chicago O'Hare |
|---|---:|---:|
| Listed connections | 45 | 55 |
| Median scheduled wait | 99 min | 98 min |
| 90th-percentile scheduled wait | 348 min | 173 min |
| Waits of at least six hours | 5 | 1 |
| Connections touching 10 p.m.–6 a.m. locally | 15 (33%) | 20 (36%) |
| Median night-window overlap among those affected | 64 min | 13 min |

The nearly equal medians conceal different upper tails. O'Hare has more listings that touch the night window, while the affected Denver listings spend longer in it. All five Denver waits of at least six hours in this comparison fall on **April 24 to 26** and are daytime waits. That is why the story ends with a targeted review of the Denver connection bank, not a generic warning about overnight connections.

## Design choices and what I learned

The presentation follows **average → long tail → Los Angeles to Boston comparison → local clock check → review action**. Each view answers the question raised by the previous one. The US burden map remains optional context after the main path; putting it in the one minute presentation would add another metric without changing the recommendation. The visual treatment uses restrained navy and off-white, with amber highlighting the long waits and comparison bars. Four responsive charts make the mean and median, distribution, upper tail comparison, and night overlap duration readable directly in Shorthand. Full airport names, sample sizes, common zero based scales, dates, and source notes are visible without hovering. The interactive eight sheet Tableau workbook follows the main narrative as optional exploration, with a direct link as a fallback. I removed the decorative airport photograph to keep attention on the evidence.

The biggest lesson was that a descriptive chart becomes useful only when its unit and decision are explicit. Here, each row is a listed option, not a passenger or a completed connection. The 90th percentile describes the upper end of this sample, not uncertainty about an airline's performance. The 10 pm to 6 am window and 6 hour threshold are project conventions. These advertised schedules cannot establish delay risk, hotel need, passenger impact, current service, or why an airline arranged its banks this way. A planner would need flight identifiers, passenger volumes, connection protection rules, actual operations, and a wider period before changing a timetable.

## Sources, assets, and reproducibility

- Wong, D. (2022). [*Flight Prices*](https://www.kaggle.com/datasets/dilwong/flightprices), Kaggle dataset, listed as CC BY 4.0. The [creator's field documentation](https://github.com/dilwong/FlightPrices) explains the segment data. The source consists of Expedia search listings; attribution does not imply endorsement by Wong or Expedia.
- [Project data dictionary and limitations](assets/layover/DATA_README.md), [prepared 828-row CSV](assets/layover/layovers_clean.csv), and [reproducible analysis notebook](assets/layover/layover_analysis.ipynb) document extraction, filtering, calculations, and checks.
- [Part III Tableau workbook](https://public.tableau.com/app/profile/shreyas.anand4069/viz/Project-Part-III-Layover-Story-REPAIRED/LAX-BOSPlanningReview?publish=yes) supplies the published visualizations. Story diagrams and chart assets were created for this project; no airline logos or third-party photographs are needed.

The published Shorthand story retains these source links and the historical-sample caveats beside the visuals. I checked the live desktop and 390-pixel phone layouts, confirmed that the embedded workbook opens on the planning review with all eight sheet tabs, and independently recalculated the headline, Denver/O'Hare, and date specific results from the prepared CSV. These checks establish consistency with the project extract, not representativeness of current airline service.

## AI acknowledgement

I used OpenAI Codex to help edit the narrative and Part III writeup, check direction specific calculations against the prepared data, draft the one minute presentation, and repair the Tableau workbook. The three interview findings were documented in Part II and were not generated by AI. I remain responsible for the interpretation, design choices, citations, and final submission.

[Back to portfolio](https://anandshrey.github.io/Shreyas-Anand-portfolio/) · [Part I](https://anandshrey.github.io/Shreyas-Anand-portfolio/final-project-part-one) · [Part II](https://anandshrey.github.io/Shreyas-Anand-portfolio/final-project-part-two)

