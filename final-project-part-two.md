| [about me](index.md) | [visualizing government debt](dataviz2.md) | [critique by design](critique-by-design.md) | [final project part one](final-project-part-one.md) | [final project part two](final-project-part-two.md) | [final project part three](final-project-part-three.md) |

# The Architecture of a Layover: Part II

Part I asked what a traveler can learn from the average length of a layover. The critique revealed a more useful question: **where does schedule design create long, highly variable, or night exposed connections, and how does that pattern change by direction?**

This revision therefore treats airline network and route planners as the primary audience. Travelers remain a secondary audience, but the main decision supported by the story is an operational one: which connection banks deserve closer review?

## Shorthand story

The published Shorthand story is titled **“The Architecture of a Layover: What an Average Wait Hides.”** It contains the planner focused narrative, the in class critique response, recommendations, user research protocol, and embedded live Tableau views.

<iframe src="https://carnegiemellon.shorthandstories.com/layover-architecture-part-two/index.html" width="100%" height="720" title="The Architecture of a Layover Shorthand story"></iframe>

[Open the Shorthand story preview](https://carnegiemellon.shorthandstories.com/layover-architecture-part-two/index.html)

# Wireframes/storyboards

The storyboard moves from a familiar traveler question to a specific planning decision. The geographic view is used analytically to show where total scheduled waiting and 6 hour connections accumulate.

| Frame | Purpose | Planned visual | Main takeaway |
|---|---|---|---|
| 1. Two flights, one wait | Establish the human experience and the planning problem | Title treatment with two connecting flight segments | A connection is part of the journey, not empty time between flights. |
| 2. What the average hides | Explain the distribution before comparing hubs | Histogram of layover minutes with mean and median reference lines | The mean is 138 minutes, but the median is 96; the distribution has a long right tail. |
| 3. Where the wait changes | Compare hubs without hiding sample size | Sorted horizontal bars with exact mean, median, p90, and *n* in the tooltip | A hub ranking is only useful when typical wait, tail risk, and sample size are visible together. |
| 4. Direction changes the picture | Reveal asymmetry | Hub comparison with a BOS to LAX / LAX to BOS direction control | Pooled airport averages can hide large directional differences. |
| 5. The clock matters | Add a passenger experience metric | Night-exposure view using the local 10 pm to 6 am window | Duration alone misses connections that overlap the local overnight period. |
| 6. Where burden accumulates | Add geographic context without overstating coverage | U.S. hub map sized by total scheduled layover minutes and colored by 6 hour waits, with a direction filter | Geography is useful when it reveals where schedule burden clusters. The domestic scope matches the US dataset |
| 7. Planning priorities | Turn findings into actions | Short annotated priority list | Review high volume hubs with poor tail or night metrics before reacting to unstable small groups. |
| 8. Limits and next steps | Prevent overclaiming | Text close with the collection period and missing variables | These are April 17 to 26, 2022 advertised schedules, not current operational performance. |

## Tableau prototypes

The Tableau workbook contains the four original connected views plus a new Part II geographic burden map. The hub view was revised in Tableau Desktop to sort hubs, label exact averages, and expose route direction as a filter. The map sizes hubs by total scheduled layover minutes and colors them by the count of 6 hour waits.

### Average scheduled layover by hub

<iframe src="https://public.tableau.com/views/Projectpart1_17900063502800/AverageLayoverbyHub?:showVizHome=no" width="100%" height="650" title="Average scheduled layover by hub"></iframe>

[Open the hub comparison in Tableau Public](https://public.tableau.com/views/Projectpart1_17900063502800/AverageLayoverbyHub?:showVizHome=no)

### Distribution of layover durations

<iframe src="https://public.tableau.com/views/Projectpart1_17900063502800/DistributionofLayoverDurations?:showVizHome=no" width="100%" height="650" title="Distribution of layover durations"></iframe>

[Open the layover distribution in Tableau Public](https://public.tableau.com/views/Projectpart1_17900063502800/DistributionofLayoverDurations?:showVizHome=no)

### Night exposure by hub

<iframe src="https://public.tableau.com/views/Projectpart1_17900063502800/NightExposurebyHub?:showVizHome=no" width="100%" height="650" title="Night exposure by hub"></iframe>

[Open night exposure by hub in Tableau Public](https://public.tableau.com/views/Projectpart1_17900063502800/NightExposurebyHub?:showVizHome=no)

### Daily average layover trend

<iframe src="https://public.tableau.com/views/Projectpart1_17900063502800/DailyAverageLayover?:showVizHome=no" width="100%" height="650" title="Daily average scheduled layover"></iframe>

[Open the daily average view in Tableau Public](https://public.tableau.com/views/Projectpart1_17900063502800/DailyAverageLayover?:showVizHome=no)

### Geographic connection-burden map

<iframe src="https://public.tableau.com/views/Projectpart1_17900063502800/Sheet5?:showVizHome=no" width="100%" height="650" title="Where connection burden accumulates"></iframe>

[Open the geographic burden map in Tableau Public](https://public.tableau.com/views/Projectpart1_17900063502800/Sheet5?:showVizHome=no)

The map is intentionally sized by total scheduled layover minutes and colored by 6 hr+ connections. It is an operational diagnostic: large, high intensity hubs should be investigated by direction before schedule changes are made.

### Visualization design evidence

The current prototypes and the Part III specifications explicitly account for the supporting elements required to interpret each view. All views use the same source: 828 advertised one-stop BOS-LAX and LAX-BOS itineraries collected for April 17-26, 2022.

| View | Decision purpose | Titles, encodings, annotations, and context |
|---|---|---|
| Layover distribution | Explain why the mean alone is misleading | Title names the measure; the x-axis is scheduled layover minutes and the y-axis is itinerary count; reference lines identify the 138-minute mean and 96-minute median; the caption states the sample size and collection period. |
| Hub comparison | Identify hub-direction combinations that deserve review | Full airport names, mean, median, p90, direction, and *n* are specified together; p90 will be defined as the value below which 90% of observed layovers fall; low-*n* groups will be visibly flagged rather than treated as stable rankings. |
| Night exposure | Compare schedule-quality risk across hubs | The local 10 pm-6 am window is defined once; the revision will show both count and percentage affected and the duration of overlap, distinguishing a short late-evening overlap from an overnight wait. |
| Daily trend | Show variation across the ten-day collection period | Date is the x-axis and average scheduled layover minutes is the y-axis; the caption limits interpretation to the April 17-26, 2022 collection window. |
| Geographic burden map | Locate where scheduled waiting accumulates | Size represents total scheduled layover minutes, color represents six-hour-plus connections, and direction is filterable; the caption explains that the U.S. extent reflects the domestic dataset rather than global coverage. |

## What the plots suggest

- The overall mean layover is about **138 minutes**, while the median is **96 minutes**. The 42 minute gap shows why a route planner should not use the mean alone.
- **392 of 828 itineraries** fall between 60 and 120 minutes, but **54 itineraries last at least six hours**. 
- Direction can change the conclusion. At SFO, the historical sample averaged **360.8 minutes for BOS to LAX** and **113.7 minutes for LAX to BOS**. The BOS to LAX group contains only eight itineraries, so this is a diagnostic signal rather than a universal ranking.
- **144 itineraries overlap 10 pm to 6 am** and 21 cross local midnight. Among larger hub groups, IAD has 17 night exposed itineraries out of 34, SLC 10 of 32, SFO 9 of 37, DEN 15 of 64, and ORD 20 of 130.

### Suggestions from In class critique for this submission

1. Review high volume hubs first, then flag combinations of poor p90 and night exposure instead of ranking hubs by mean alone.
2. Separate BOS to LAX from LAX to BOS before changing arrival or departure banks.
3. Display mean, median, p90, and itinerary count together and suppress or flag unstable comparisons with very small *n*.
4. Check whether alternative same day connection windows exist.
5. Keep the traveler facing view separate: show the actual itinerary and local clock times, because a hub average is context rather than a booking recommendation.

# In class and Part I critique

| Source | Critique | Change made for Part II |
|---|---|---|
| Course reviewer (CR) | The story logic tied the pieces together into a complete picture. | I retained the progression from overall distribution to hub differences and then to the time of day experience. |
| Course reviewer (CG) | The original story had a great deal of detail without a sufficiently clear reason for the audience to need it. The reviewer suggested the perspective of a route planner or airline manager. | I reframed the primary audience as airline network and route planners and converted the ending into schedule review actions. |
| Johanna Fickel, Julia Clerici, and Trey Tillotson | Sort the major layover bars, clarify airport abbreviations on hover, and show exact averages. | The Tableau hub view is sorted, exact values are labeled, and the final tooltip specification includes the full airport name, mean, median, p90, direction, and *n*. |
| My response to the discussion | A map was initially proposed as another view. | I redesigned the map as an analytic view: size encodes total layover burden, color encodes 6 hour waits, and direction is filterable. I use a US map because the data is domestic; a world map would overstate coverage. |

# User research

## Target audience

**Primary audience:** airline network planners, schedule development analysts, and route managers who decide how arrival and departure banks connect.

**Secondary audience:** frequent connecting travelers who can judge whether the story makes schedule tradeoffs understandable without implying that a historical average is a current booking recommendation.

## Recruitment approach

I will show the same early Shorthand draft to at least three real people:

- one person familiar with airline operations, transportation planning, or aviation analytics
- one analytically experienced reader who regularly works with dashboards or schedules
- one frequent traveler who has had experience of taking connections between Boston and the West Coast or on comparable routes

Participants will be described only by broad role. Names, employers, contact details, and other personally identifying information will not be included on this page.

## Interview script

Each conversation will last approximately 15 to 20 minutes. I will first ask the participant to read the story without explanation, then use the same core questions so responses can be compared.

| Goal | Questions to ask |
|---|---|
| Check audience fit | What role do you think this story is written for? What decision could that person make after reading it? |
| Test the opening | After the first two frames, what do you think the story is trying to explain? |
| Test the distribution | What do the mean of 138 minutes and median of 96 minutes tell you? Is the difference clear? |
| Test the hub view | Which hub would you inspect first, and what evidence led you there? What additional field would you need before acting? |
| Test direction | Did the BOS to LAX / LAX to BOS split change your interpretation? Why or why not? |
| Test night exposure | Is the 10 pm to 6 am measure understandable and useful? Would you define it differently? |
| Test trust | What claim feels strongest? Which claim feels unsupported or too broad? |
| Test usability | Were any labels, airport codes, filters, or interactions confusing? |
| Prioritize revision | If I could change only one thing before Part III, what should it be? |

## Interview findings

**Research status:** Complete. Three classmates reviewed the same early Shorthand draft using the interview script above. To follow the assignment's privacy requirement, they are identified only by the broad role “classmate”; no names, employers, contact details, or other personally identifying information are included.

| Question / theme | Classmate 1 | Classmate 2 | Classmate 3 |
|---|---|---|---|
| Most useful visual | The distribution histogram with mean (138) and median (96) lines. It explains why the average misleads. | Same histogram, plus the direction split. Both show the data's shape rather than a single summary number. | The 10 pm-to-6 am overlap is concrete and relatable. |
| Confusing label or interaction | Night exposure is shown as counts (IAD 17, ORD 20). As rates, IAD is 50%, SLC 31%, SFO 24%, DEN 23%, and ORD 15%, which changes the ranking. | Airport codes (IAD, SLC, SFO) need full names visible, not just on hover. Many readers will not know what p90 means either. | The hub chart is sorted by mean, which undercuts the advice not to rank by mean alone. |
| Reaction to direction split | Show the *n*=8 case visibly, for example with a faded bar, an error band, or a “low *n*” flag. | The two-direction toggle is intuitive, but a traveler may read it as “avoid SFO going west.” | I had the same first reaction: the directional difference is noticeable, but it could be mistaken for booking advice. |
| Reaction to night exposure | Useful as a separate quality metric. Define the window once. | The 10 pm-to-6 am window feels arbitrary unless the story explains why it was chosen. Consider showing the share of each layover that falls inside the window. | Good, but a 20-minute overlap at 10 pm is not the same as a five-hour overnight wait. |

### Representative participant comments

> “The distribution histogram with mean (138) and median (96) lines explains why the average misleads.” — Classmate 1

> “Airport codes need full names visible, not just on hover. Many readers will not know what p90 means either.” — Classmate 2

> “A 20-minute overlap at 10 pm is not the same as a five-hour overnight wait.” — Classmate 3

### Cross-interview synthesis

- **Consistent feedback:** The distribution view was the clearest explanation of why the mean alone is misleading. Participants also agreed that the direction split adds useful information but needs a visible small-sample warning and a clear statement that it is a planning diagnostic, not booking advice.
- **Conflicting or qualified feedback:** Night exposure was considered concrete and useful, but its current binary definition was questioned. One participant wanted a clear definition, another questioned the choice of window, and another emphasized that overlap duration matters.
- **Isolated but actionable feedback:** Showing rates instead of counts and replacing the mean-only hub ordering were each raised directly by one participant. Both are consistent with the story's goal and will be tested in the next revision.
- **Audience tension:** Route planners can use comparative hub metrics to identify schedules for review, while travelers may interpret the same comparisons as recommendations to avoid an airport. The published story therefore needs to state the intended operational decision explicitly.

### Design decisions based on the interviews

The hub view will use full airport names, define p90 in plain language, display sample size beside each mark, and flag or fade low-*n* groups. Mean-only ordering will be replaced by an operational review priority that considers volume, tail risk, and night-exposure rate while retaining mean and median for context. The night-exposure view will show both the percentage of itineraries affected and overlap duration. The story will also state that these historical schedule patterns are diagnostic signals for planners, not current traveler booking recommendations. The revised views will receive a follow-up usability check before Part III is finalized.

# Identified changes for Part III

The plot analysis, in-class critique, and three completed interviews support the following revisions.

- Keep route planners and airline managers as the primary audience and state the operational decision near the opening.
- Use a sorted horizontal hub chart with exact values, full airport names, direction, and sample size.
- Add median and p90 to prevent the long right tail from disappearing behind the mean.
- Make direction an explicit control and call out only differences with adequate sample size.
- Treat night exposure as a separate schedule quality metric.
- Keep a traveler view focused on actual itinerary times rather than airport rankings.
- Keep the geographic burden map only because its size, color, and direction encodings support the planning question; remove decorative template imagery.
- Add a compact methods and limitations note to every published view.

# Moodboard / persona

The visual tone should feel like an airline operations briefing rather than a travel advertisement: dark navy, off white, muted blue, and one warm alert color for tail risk or overnight exposure. Labels should be direct, typography restrained, and interactions limited to decisions the audience actually needs to make.

**Primary persona:** a route planning analyst preparing a schedule review. They have limited time, need to identify which hub direction combinations deserve investigation, and distrust rankings that omit sample size or variability.

# References

- Project dataset: 828 one stop BOS - LAX and LAX - BOS advertised itineraries collected for April 17 to 26, 2022.
- [Final Project Part I](final-project-part-one.md)
- [Tableau Public workbook](https://public.tableau.com/app/profile/shreyas.anand4069/viz/Projectpart1_17900063502800/DailyAverageLayover)
- [Shorthand story preview](https://carnegiemellon.shorthandstories.com/layover-architecture-part-two/index.html)
- Part II Tableau workbook and exported map are preserved in the project deliverables.

# AI acknowledgements

I used OpenAI Codex to compare the final GitHub page against the assignment rubric. It also helped in suggesting write up based on changes made from Part I to Part II. No interview findings were generated or inferred by AI.

