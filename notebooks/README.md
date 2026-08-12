# Student notebooks

The four notebooks worked through during the Eyes in the Sky class.

Each one is a **student edition**: cells marked **YOUR TURN** have gaps to
fill in. Look for `____` and `# TODO`. Many gaps list three options in a
comment; one is right and the others teach you something by being wrong.
Everything else runs as given.

## The plan for the day

| Clock | Notebook |
|---|---|
| 0:00 | `01_first_light_STUDENT.ipynb` — find your community from orbit, count the clear views |
| 0:35 | `02_reading_the_land_STUDENT.ipynb` — turn pictures into hectares |
| 1:00 | `03_melissa_and_shoreline_STUDENT.ipynb` — measure Hurricane Melissa's damage |
| 1:30 | `04_heat_machines_prediction_STUDENT.ipynb` — read 45 years of Kingston heat |
| 1:50 | Breather, mission scores |
| 2:00 | The Satellite Challenge: your team picks one investigation and presents its answer |

## Running a notebook

Fastest path: upload the file to [Google Colab](https://colab.research.google.com)
and press play from the top. The first cell installs everything you need;
the second loads the toolkit.

If a cell asks for `MY_LAT, MY_LON`, open Google Maps, right-click the
place that matters to you, and the top line of the menu gives you both
numbers. Maps writes latitude first, so keep that order.

## If something goes wrong

- **A search returns no scenes.** Widen the date range, or raise
  `max_cloud` from 20 to 35.
- **`best_scene` returns `None`.** Try a nearby month, or nudge your point
  slightly inland from the coast.
- **A notebook cell hangs for more than five minutes.** Interrupt it
  (`Runtime` then `Interrupt execution` in Colab), then try again. AWS has
  occasional slow moments.

## Save your work

Before you close a notebook in Colab, choose `File` then
`Save a copy in Drive`. The next notebook assumes the previous one worked.
