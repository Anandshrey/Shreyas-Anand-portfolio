| [about me](index.md) | [visualizing government debt](dataviz2.md) | [critique by design](critique-by-design.md) | [final project part one](final-project-part-one.md) | [final project part two](final-project-part-two.md) | [final project part three](final-project-part-three.md) |

# The Architecture of a Layover: Part II

Part I asked what a traveler can learn from the average length of a layover. The critique revealed a more useful question: **where does schedule design create long, highly variable, or night-exposed connections, and how does that pattern change by direction?**

This revision therefore treats airline network and route planners as the primary audience. Travelers remain a secondary audience, but the main decision supported by the story is an operational one: which connection banks deserve closer review?

## Shorthand story

The published Shorthand story is titled **“The Architecture of a Layover: What an Average Wait Hides.”** It contains the narrative draft, the route-planning interpretation, and an exported Tableau prototype.

<iframe src="https://carnegiemellon.shorthandstories.com/the-architecture-of-a-layover/index.html" width="100%" height="720" title="The Architecture of a Layover Shorthand story"></iframe>

[Open the Shorthand story preview](https://carnegiemellon.shorthandstories.com/the-architecture-of-a-layover/index.html)

# Wireframes / storyboards

The storyboard moves from a familiar traveler question to a specific planning decision. The geographic view is used analytically—not decoratively—to show where total scheduled waiting and six-hour connections accumulate.

| Frame | Purpose | Planned visual | Main takeaway |
|---|---|---|---|
| 1. Two flights, one wait | Establish the human experience and the planning problem | Title treatment with two connecting flight segments | A connection is part of the journey, not empty time between flights. |
| 2. What the average hides | Explain the distribution before comparing hubs | Histogram of layover minutes with mean and median reference lines | The mean is 138 minutes, but the median is 96; the distribution has a long right tail. |
| 3. Where the wait changes | Compare hubs without hiding sample size | Sorted horizontal bars with exact mean, median, p90, and *n* in the tooltip | A hub ranking is only useful when typical wait, tail risk, and sample size are visible together. |
| 4. Direction changes the picture | Reveal schedule-bank asymmetry | Hub comparison with a BOS–LAX / LAX–BOS direction control | Pooled airport averages can hide large directional differences. |
| 5. The clock matters | Add a passenger-experience metric | Night-exposure view using the local 10 p.m.–6 a.m. window | Duration alone misses connections that overlap the local overnight period. |
| 6. Where burden accumulates | Add geographic context without overstating coverage | U.S. hub map sized by total scheduled layover minutes and colored by six-hour waits, with a direction filter | Geography is useful when it reveals where schedule burden clusters. The domestic scope matches the U.S. dataset. |
| 7. Planning priorities | Turn findings into actions | Short annotated priority list | Review high-volume hubs with poor tail or night metrics before reacting to unstable small groups. |
| 8. Limits and next steps | Prevent overclaiming | Text close with the collection period and missing variables | These are April 17–26, 2022 advertised schedules, not current operational performance. |

## High-fidelity Tableau prototypes

The Tableau workbook contains the four original connected views plus a new Part II geographic burden map. The hub view was revised in Tableau Desktop to sort hubs, label exact averages, and expose route direction as a filter. The map sizes hubs by total scheduled layover minutes and colors them by the count of six-hour waits.

### Average scheduled layover by hub

<iframe src="https://public.tableau.com/views/Projectpart1_17900063502800/AverageLayoverbyHub?:showVizHome=no" width="100%" height="650" title="Average scheduled layover by hub"></iframe>

[Open the hub comparison in Tableau Public](https://public.tableau.com/views/Projectpart1_17900063502800/AverageLayoverbyHub?:showVizHome=no)

### Distribution of layover durations

<iframe src="https://public.tableau.com/views/Projectpart1_17900063502800/DistributionofLayoverDurations?:showVizHome=no" width="100%" height="650" title="Distribution of layover durations"></iframe>

[Open the layover distribution in Tableau Public](https://public.tableau.com/views/Projectpart1_17900063502800/DistributionofLayoverDurations?:showVizHome=no)

### Night exposure by hub

<iframe src="https://public.tableau.com/views/Projectpart1_17900063502800/NightExposurebyHub?:showVizHome=no" width="100%" height="650" title="Night exposure by hub"></iframe>

[Open night exposure by hub in Tableau Public](https://public.tableau.com/views/Projectpart1_17900063502800/NightExposurebyHub?:showVizHome=no)

## What the plots suggest

- The overall mean layover is about **138 minutes**, while the median is **96 minutes**. The 42-minute gap shows why a route planner should not use the mean alone.
- **392 of 828 itineraries** fall between 60 and 120 minutes, but **54 itineraries last at least six hours**. A median-plus-p90 view would keep both the routine experience and the tail visible.
- Direction can change the conclusion. At SFO, the historical sample averaged **360.8 minutes for BOS–LAX** and **113.7 minutes for LAX–BOS**. The BOS–LAX group contains only eight itineraries, so this is a diagnostic signal rather than a universal ranking.
- **144 itineraries overlap 10 p.m.–6 a.m.** and 21 cross local midnight. Among larger hub groups, IAD has 17 night-exposed itineraries out of 34, SLC 10 of 32, SFO 9 of 37, DEN 15 of 64, and ORD 20 of 130.

### Suggestions for an airline planning audience

1. Review high-volume hubs first, then flag combinations of poor p90 and night exposure instead of ranking hubs by mean alone.
2. Separate BOS–LAX from LAX–BOS before changing arrival or departure banks.
3. Display mean, median, p90, and itinerary count together; suppress or flag unstable comparisons with very small *n*.
4. Audit the night-exposed banks highlighted above, then check whether alternative same-day connection windows exist.
5. Keep the traveler-facing view separate: show the actual itinerary and local clock times, because a hub average is context rather than a booking recommendation.

# In-class and Part I critique

| Source | Critique | Change made for Part II |
|---|---|---|
| Course reviewer (CR) | The story logic tied the pieces together into a complete picture. | I retained the progression from overall distribution to hub differences and then to the time-of-day experience. |
| Course reviewer (CG) | The original story had a great deal of detail without a sufficiently clear reason for the audience to need it. The reviewer suggested the perspective of a route planner or airline manager. | I reframed the primary audience as airline network and route planners and converted the ending into schedule-review actions. |
| Johanna Fickel, Julia Clerici, and Trey Tillotson | Sort the major layover bars, clarify airport abbreviations on hover, and show exact averages. | The Tableau hub view is sorted, exact values are labeled, and the final tooltip specification includes the full airport name, mean, median, p90, direction, and *n*. |
| My response to the discussion | A map was initially proposed as another view. | I redesigned the map as an analytic view: size encodes total layover burden, color encodes six-hour waits, and direction is filterable. I use a U.S. map because the data is domestic; a world map would overstate coverage. |

# User research

## Target audience

**Primary audience:** airline network planners, schedule-development analysts, and route managers who decide how arrival and departure banks connect.

**Secondary audience:** frequent connecting travelers who can judge whether the story makes schedule tradeoffs understandable without implying that a historical average is a current booking recommendation.

## Recruitment approach

I will show the same early Shorthand/Tableau draft to at least three real people:

- one person familiar with airline operations, transportation planning, or aviation analytics;
- one analytically experienced reader who regularly works with dashboards or schedules;
- one frequent traveler who has made connections between Boston and the West Coast or on comparable routes.

Participants will be described only by broad role. Names, employers, contact details, and other personally identifying information will not be included on this page.

## Interview script

Each conversation will last approximately 15–20 minutes. I will first ask the participant to read the story without explanation, then use the same core questions so responses can be compared.

| Goal | Questions to ask |
|---|---|
| Check audience fit | What role do you think this story is written for? What decision could that person make after reading it? |
| Test the opening | After the first two frames, what do you think the story is trying to explain? |
| Test the distribution | What do the mean of 138 minutes and median of 96 minutes tell you? Is the difference clear? |
| Test the hub view | Which hub would you inspect first, and what evidence led you there? What additional field would you need before acting? |
| Test direction | Did the BOS–LAX / LAX–BOS split change your interpretation? Why or why not? |
| Test night exposure | Is the 10 p.m.–6 a.m. measure understandable and useful? Would you define it differently? |
| Test trust | What claim feels strongest? Which claim feels unsupported or too broad? |
| Test usability | Were any labels, airport codes, filters, or interactions confusing? |
| Prioritize revision | If I could change only one thing before Part III, what should it be? |

## Interview findings

**Research status:** The protocol and interview materials are ready. This section must be completed with observations and short quotations from at least three real participants; no responses have been invented.

| Question / theme | Interview 1 — broad role | Interview 2 — broad role | Interview 3 — broad role |
|---|---|---|---|
| Perceived audience and decision | *Pending real interview* | *Pending real interview* | *Pending real interview* |
| Most useful visual | *Pending real interview* | *Pending real interview* | *Pending real interview* |
| Confusing label or interaction | *Pending real interview* | *Pending real interview* | *Pending real interview* |
| Reaction to direction split | *Pending real interview* | *Pending real interview* | *Pending real interview* |
| Reaction to night exposure | *Pending real interview* | *Pending real interview* | *Pending real interview* |
| Short, de-identified quotation | *Pending real interview* | *Pending real interview* | *Pending real interview* |

### Synthesis template

After the interviews, I will distinguish:

- **consistent feedback:** an issue or preference raised by at least two participants;
- **conflicting feedback:** places where the planning and traveler audiences want different levels of detail;
- **isolated feedback:** a useful idea raised by one participant that needs validation before becoming a major design change.

# Identified changes for Part III

The plot analysis and critique already support the following revisions. Interview-driven revisions will be added after the three sessions.

- Keep route planners and airline managers as the primary audience and state the operational decision near the opening.
- Use a sorted horizontal hub chart with exact values, full airport names, direction, and sample size.
- Add median and p90 to prevent the long right tail from disappearing behind the mean.
- Make direction an explicit control and call out only differences with adequate sample size.
- Treat night exposure as a separate schedule-quality metric.
- Keep a traveler view focused on actual itinerary times rather than airport rankings.
- Keep the geographic burden map only because its size, color, and direction encodings support the planning question; remove decorative template imagery.
- Add a compact methods and limitations note to every published view.

# Moodboard / persona

The visual tone should feel like an airline operations briefing rather than a travel advertisement: dark navy, off-white, muted blue, and one warm alert color for tail risk or overnight exposure. Labels should be direct, typography restrained, and interactions limited to decisions the audience actually needs to make.

**Primary persona:** a route-planning analyst preparing a schedule review. They have limited time, need to identify which hub-direction combinations deserve investigation, and distrust rankings that omit sample size or variability.

# References

- Project dataset: 828 one-stop BOS–LAX and LAX–BOS advertised itineraries collected for April 17–26, 2022.
- [Final Project Part I](final-project-part-one.md)
- [Tableau Public workbook](https://public.tableau.com/app/profile/shreyas.anand4069/viz/Projectpart1_17900063502800/DailyAverageLayover)
- [Shorthand story preview](https://carnegiemellon.shorthandstories.com/the-architecture-of-a-layover/index.html)
- Part II Tableau workbook and exported map are preserved in the project deliverables.

# AI acknowledgements

I used OpenAI Codex to help interpret the assignment rubric, profile the project dataset, check calculations, draft and edit the narrative structure, and operate Tableau Desktop and Shorthand while I reviewed the work. Codex also helped translate the critique into a route-planner audience and prepare the user-research protocol. I remain responsible for the analytical claims, design choices, participant recruitment, interviews, quotations, and final submission. No interview findings were generated or inferred by AI.

