# Instructor guide and worked answers

Prepared by Adrian Dunkley, Physicist, Climate Studies Group, Mona.

Use the original workshop as the prerequisite. Give students the worked examples before assigning an investigation. This public guide supports teaching; it is not a hidden examination answer bank.

## Preparation and pacing

Install the root requirements and run `python scripts/validate_extension.py`. Default lessons require no live data. Test optional services separately on the classroom connection. For outages, use a permitted cached observation with its metadata, or label a synthetic exercise explicitly. Form pairs, swapping the operator and recorder halfway through.

Use 45 minutes for explanation, 75 for the guided lab, 45 for independent investigation and 15 for evidence discussion. For learners needing support, supply the formula and ask them to explain the denominator. For advanced learners, require an additional baseline or independent validation design.

## Week 1. Expected reasoning

The first calibrated pair is red 0.1 and NIR 0.5, giving NDVI 2/3. The raw-number ratio is 0.5. Nodata remains NaN. An additive offset does not cancel in the ratio; a common multiplicative scale does under the appropriate input assumptions.

The never-observed square stays missing. Increasing minimum support cannot increase observed area for the same stack. The selected vegetation fraction need not be monotone because its denominator changes. Median-of-indices can differ from index-of-median-bands because of nonlinearity and observation selection.

A 20 m square pixel is 0.04 projected hectares. Calculate area from the actual grid. Resampling a coarser band does not create finer independent information.

## Week 2. Expected reasoning

A -0.1 threshold selects at least as many candidate pixels as -0.2, which selects at least as many as -0.3 on the same valid data. Reducing the synthetic loss from 0.25 to 0.12 generally lowers recall at -0.2; students must report their computed results.

The constructed treated mean change is near -0.28 and the control near -0.03, giving a contrast near -0.25. These expectations come from the generator. Causal interpretation of an observed contrast needs credible comparison assumptions. Quiet-year detections are not a true false-positive rate without reference labels.

Block intervals depend on both block size and retained coverage. Their width has no universal monotonic rule. The retained-block estimate can represent a different population from the full observed-pixel mean. Reward students who identify that limitation rather than treating the interval as a complete uncertainty budget.

## Week 3. Additional baseline

Fit a monthly climatology only on the training rows:

```python
train = frame.loc[frame.index < '2022-01-01']
monthly = train.target.groupby(train.index.month).mean()
for label, part in [('validation', frame.loc['2022-01-01':'2022-12-31']),
                    ('test', frame.loc['2023-01-01':])]:
    prediction = pd.Series(part.index.month, index=part.index).map(monthly)
    error = prediction - part.target
    print(label, 'MAE_C', error.abs().mean(),
          'RMSE_C', np.sqrt((error**2).mean()), 'n', len(part))
```

For lags 1, 3 and 7, build all frames, intersect their indexes and run every comparison on that intersection. Verify each lag comes from the declared earlier date. Ridge alpha is fixed at 1.0 and scaling uses training data only. Tuning requires ordered validation within development data and a final test left untouched until the choice is frozen.

The model can lose to persistence. Award full marks for a correctly controlled negative result. The example evaluates daily predictions with refreshed inputs, not one multi-year forecast. Live POWER-based scores measure agreement with that product; station validation is separate.

## Week 4. Scenario arithmetic

The central teaching multiplier is 0.5 × 200,000 × 1 = 100,000 JMD per candidate hectare. The low multiplier is 15,000 and the high is 420,000 JMD/ha. Multiply these by the computed synthetic hectares. None is a verified Jamaican price.

All-missing after data yield zero observed hectares and zero candidate hectares: there is no usable measurement. This cannot support a claim of no damage. Hashes confirm saved bytes; they do not establish scientific validity. Manifest timestamps may change on rerun.

Require the presentation to separate observations, assumptions and recommendations. A recommendation to gather evidence can be appropriate. Apply the assessment's track boundaries to solar suitability and public-green-space claims.

## Original workshop

The original notebooks keep intentional learner gaps and place choices, so they are not expected to execute unchanged. Their shared toolkit is checked separately. Historical empirical outputs have not all been rerun against live services. Do not use a desired sign, fixed loss number or unsourced green-space benchmark as an answer key. See the release review for inherited claims needing validation.
