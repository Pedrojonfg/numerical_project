# Demo notebook placeholder (Bhuvi)

Replace this with `demo_load_results.ipynb` that:

1. Loads `results/*.csv` via `quad_project.results_io.load_results` / `plotting.plot_error_vs_nodes`
2. Works with `results/example_fake.csv` until real method CSVs land
3. Stays read-only on other people’s `rules/` code

```python
from pathlib import Path
from quad_project.plotting import plot_error_vs_nodes
import matplotlib.pyplot as plt

plot_error_vs_nodes(Path("results/example_fake.csv"), integrand="constant_one", d=2)
plt.show()
```
