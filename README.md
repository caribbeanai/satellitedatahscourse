# Eyes in the Sky: Satellite Data Analysis for Jamaica

Course materials for **Eyes in the Sky**, a one-day satellite data science
workshop for Jamaican high school students, prepared by
**Adrian Dunkley**, Climate Studies Group Mona, Faculty of Science and
Technology, University of the West Indies.

Students use free, open satellite data (Sentinel-2 from the European Space
Agency, hosted on Amazon Web Services) and NASA POWER climate records to
measure real things over Jamaica: the vegetation around their community,
the water inside Portmore, the hectares Hurricane Melissa flattened around
New Hope, and 45 years of heat over Kingston. No API keys, no fees, no
permission needed.

## Links

- **Course sign up:** https://adriandunkley.net/courses/eyes-in-the-sky-high-school.html
- **Final assessment:** https://adriandunkley.net/courses/eyes-in-the-sky-high-school-exam.html

## What is in this repository

| Folder | Contents |
|---|---|
| [`notebooks/`](notebooks/) | The four student notebooks worked through during the class |
| [`final-assessment/`](final-assessment/) | The take-home assessment materials |

## The four notebooks

Each notebook takes roughly 20 to 30 minutes in class. Cells marked
**YOUR TURN** have small gaps to fill in; everything else runs as given.

| # | Notebook | Mission |
|---|---|---|
| 1 | [`01_first_light_STUDENT.ipynb`](notebooks/01_first_light_STUDENT.ipynb) | Find your community from space and count the clear satellite views of Treasure Beach in 2025 |
| 2 | [`02_reading_the_land_STUDENT.ipynb`](notebooks/02_reading_the_land_STUDENT.ipynb) | Turn satellite pictures into hectares and measure the open water inside Portmore |
| 3 | [`03_melissa_and_shoreline_STUDENT.ipynb`](notebooks/03_melissa_and_shoreline_STUDENT.ipynb) | Measure the hectares of severe vegetation loss Hurricane Melissa caused around New Hope, Westmoreland |
| 4 | [`04_heat_machines_prediction_STUDENT.ipynb`](notebooks/04_heat_machines_prediction_STUDENT.ipynb) | Read 45 years of Kingston temperature and find the hottest day of July 2026 |

## How to run the notebooks

The easiest path is **Google Colab**, which needs no installation:

1. Open [colab.research.google.com](https://colab.research.google.com).
2. Choose `File` then `Upload notebook`, and pick one of the `.ipynb` files
   from the `notebooks/` folder.
3. Run the cells from the top.

The first two cells install the required packages and load the toolkit;
after that, work through the mission.

Alternatively, run locally with JupyterLab:

```bash
pip install jupyterlab rasterio requests imageio pandas scikit-learn matplotlib pillow
jupyter lab
```

## Data and credits

- **Sentinel-2** imagery: European Space Agency, hosted on the Registry of
  Open Data on AWS by Element 84.
- **NASA POWER** climate records: NASA Langley Research Center, MERRA-2
  reanalysis.

Both are free to use, with no account or key required.

## Licence

Course materials are released under the [MIT Licence](LICENSE).

---

*Prepared by Adrian Dunkley, Climate Studies Group Mona, Faculty of Science
and Technology, University of the West Indies.*
