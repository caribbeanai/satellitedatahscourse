# Teaching the satellite physics labs

Prepared by Adrian Dunkley, Physicist, Climate Studies Group, Mona.

Run each lab before class. Ask students to predict the direction of a change before editing the input values. They should record what the instrument receives, what the code calculates and what further evidence the Jamaican team would need. The labs use synthetic data and run with NumPy and Matplotlib. Allow 60–90 minutes per lab, depending on how much algebra students work through by hand.

## Infrared and temperature

Use [Notebook 09](../notebooks/09_infrared_physics.ipynb) after the measurement lecture. Ask students what emits the infrared energy in each example.

- **Kingston roof and canopy.** The default brightness temperatures are 312.15 K and 298.65 K. The half-roof pixel gives 305.58 K, while the area mean of the input surface temperatures is 310.00 K. Emissivity and the nonlinear Planck relation both affect the difference. Setting both surfaces to 300 K yields brightness temperatures of 293.06 K and 298.65 K. With emissivities set to one and the original temperatures restored, the half-roof pixel yields 310.38 K. This run isolates the nonlinear radiance conversion.
- **Portland cloud.** Both 235 K pixels trigger the same cold-pixel flag, while their assigned rainfall rates differ. A time-matched gauge or radar estimate, where available, could help test the rule. Ask students to compare the reference's location or footprint with the infrared pixel and to specify the interval.

Credit students who distinguish a clear-sky surface-temperature product from an air-temperature measurement taken at the height and time relevant to the school. Use the calibration and retrieval references in the [source register](../SOURCES.md#physics-labs).

## Rainfall and runoff

Use [Notebook 10](../notebooks/10_rainfall_and_runoff.ipynb) before the public decision lecture. Draw the three cell portions at different widths. Ask students which contributes the most water and why.

- **Two ground conditions.** Depths of 20, 14 and 12 mm over 2, 3 and 5 km² give a basin mean of 14.2 mm. The unweighted mean of 15.33 mm gives the smallest, wettest portion too much weight. The runoff assumptions give 35,500 m³ and 78,100 m³ from the same 142,000 m³ of rain. Outlet flow observations and the travel time from each part of the basin could help establish when a peak reaches a crossing.
- **Missing interval.** Losing half an hour over 2 km² removes 1 km²·h of support from 20 km²·h. Coverage is 95%, with 122,000 m³ represented by valid samples. The gap assumptions yield totals of 132,000 and 152,000 m³. Moving the missing sample to a 5 km² cell lowers coverage to 87.5%. Ask students to put the available-sample total and the conditional estimates in separate columns.

## Transport and forecast error

Use [Notebook 11](../notebooks/11_advection_and_forecast_limits.ipynb) after the forecast lecture. Draw a band across three cells and demonstrate one upwind update before showing the code.

- **Correct wind.** The reference moves 18 km in 30 minutes. Persistence scores 8.87 mm/h RMSE and upwind scores 0.45 mm/h on the same grid. The exact peak is 20.00 mm/h and the upwind peak is 18.48 mm/h. The periodic update redistributes the values and preserves the integral. Averaging across cells smooths the peak.
- **Wrong wind and grid refinement.** The 5 m/s eastward run scores 5.68 mm/h. The 10 m/s westward run scores 9.41 mm/h, higher than persistence in this example. Halving the grid spacing and the time step gives 0.24 mm/h against the fine-grid reference. The routine rejects a 120-second step on the coarse grid because its Courant number is 1.2.

For a classroom extension, add a synthetic shower to the later reference. Keep the initial frame fixed. Students can repeat the comparison and identify the extra input or process the model would need to represent that change.

## Marking the investigations

| Criterion | Points | Evidence |
|---|---:|---|
| Physics and units | 3 | Correct quantity, conversion and units |
| Reproducibility | 2 | Changed inputs and results from a fresh run |
| Comparison | 3 | Controlled change and explanation of its effect |
| Field evidence | 2 | Names a missing observation and explains how it would test the claim |

Use the ten-point rubric for each optional investigation. For students who finish early, ask them to take one uncertainty into their capstone and explain how it changes their choice of field measurement.
