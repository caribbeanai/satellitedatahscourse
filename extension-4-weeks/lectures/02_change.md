# Week 2. Change, controls and uncertainty

**Prepared by Adrian Dunkley, Physicist, Climate Studies Group, Mona.**

## Learning outcomes and the investigation

This week you will measure candidate change, compare thresholds, construct a control comparison and explain the limits of a resampling interval. Revisit original notebook 03 and Challenge A. The question is whether a spectral change remains visible when the measurement choices change. A second question follows: how much of that change can reasonably be attributed to an event?

Start by writing the event date, study boundary, comparison windows and quality policy before looking at a change map. This prevents an attractive image from determining your method. For a historical storm case, verify the event chronology against an official event record. The extension's default example is synthetic and makes no claim about the area damaged by Hurricane Melissa.

## Subtraction requires comparable observations

Define change as the after value minus the before value:

$$
\Delta I(x)=I_{after}(x)-I_{before}(x).
$$

Negative NDVI change means the index fell. It does not by itself identify why. Changes in cloud contamination, crop harvest, soil moisture, illumination or registration can change the comparison. Use a common grid and the intersection of valid observations. A missing after pixel must remain missing even if its before value was high. The shared-grid and calibration procedures follow the data-product and raster-processing guidance [S1–S3].

In the laboratory, candidate loss means a previously eligible pixel satisfies \(\Delta I<\tau\), where \(\tau\) is a declared negative threshold. The course explores -0.1, -0.2 and -0.3. These are analyst-selected examples, not validated severity boundaries. Calculate the hectares at every threshold and state how much the answer changes. Calling a threshold severe does not validate it against crop inspections or structural damage.

Here is a useful invented example. Suppose 100 projected hectares can be compared, 20 cannot, and 12 observed hectares cross the selected threshold. The candidate share is 12/100 = 12% of observed eligible area. It is not evidence that the other 108 hectares were unaffected. Preserve the unknown 20 hectares separately and explain any assumption used to extrapolate beyond observed coverage.

## Controls test alternative explanations

A previous-year comparison asks whether a similar seasonal window also produces a change. A nearby comparison area asks whether a contemporaneous change occurs away from the proposed exposure. Neither control is automatically valid. Different rainfall, land use or observation coverage may make the reference inappropriate. Describe why the reference is useful and list at least one way it could fail.

For two areas, a difference-in-differences contrast is

$$
D=(I_{treated,after}-I_{treated,before})
 -(I_{control,after}-I_{control,before}).
$$

If the treated area changes by -0.24 and the control changes by -0.04, the contrast is -0.20. These are teaching values. Interpreting this contrast causally requires assumptions about comparable trends and absence of other differential causes. Here the calculation is a diagnostic, not an automatic estimate of hurricane damage.

A quiet-year map is also not a measured false-positive rate. To estimate that rate, you need reference labels identifying true negatives and a sampling design. Without them, describe the number as background detections under the same algorithm. This distinction stops an algorithm from validating itself.

## Uncertainty follows the data structure

Nearby pixels can resemble one another. Treating every pixel as an independent replicate can produce an unjustifiably narrow interval. Notebook 06 demonstrates resampling spatial block means. The code uses equal-size fully observed blocks so the weighting is explicit. You will repeat the calculation with different block sizes and compare the resulting interval.

The resulting range is a teaching bootstrap interval conditional on the retained blocks and chosen procedure. It omits calibration bias, reference-label error and other systematic effects. Excluding partly observed blocks changes the population represented by the estimate. If block size becomes comparable to the entire image, there may be too few blocks for a useful estimate. Report that failure instead of shrinking the blocks until the result looks precise.

## From spectral area to money

Challenge A multiplies area, farmland share, annual value and recovery duration. This estimates an assumed stream of forgone production under the chosen inputs. It is not the same as insured loss, replacement cost, verified crop loss or a discounted economic appraisal. Correlated assumptions also matter: the crops with the highest value may have longer recovery times.

For homework, prepare low, central and high scenarios, name the source or hypothetical status of each input and identify which assumption moves the answer most. Do not label scenario bounds as a statistical confidence interval. In class, one group plays an analyst and another plays a relief officer deciding whether to request field inspection. A responsible recommendation can be to investigate uncertain locations before allocating money.

## Session close and submission

Submit your sensitivity table, shared-validity mask, block-size comparison and control discussion. Include one plausible counterexample to your interpretation. A successful report allows another student to reconstruct both the candidate hectares and the limits of the claim. Read the calibration and resampling sources [S1–S3](../SOURCES.md); the equations and examples here are course derivations.
