import os

import yaml

from experiment.analysis_utils.aggregations import json_to_flat_df_auto

raw_path = 'fgw_par'
save_path = '.'
df = json_to_flat_df_auto(raw_path)
df.set_index(['name'], inplace=True)
df.sort_index(inplace=True)
df.to_csv(os.path.join(save_path, "fgw_48_analysis.csv"))
